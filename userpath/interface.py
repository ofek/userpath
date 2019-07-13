import os
import platform
import subprocess
from datetime import datetime
from io import open

from .shells import DEFAULT_SHELLS, SHELLS
from .utils import ensure_parent_dir_exists, get_flat_output, get_parent_process_name, location_in_path, normpath


class WindowsInterface:
    def __init__(self, **kwargs):
        pass

    def location_in_new_path(self, location, check=False):
        locations = normpath(location).split(os.pathsep)
        show_path_command = ['powershell', '-Command', "& {[Environment]::GetEnvironmentVariable('PATH', 'User')}"]
        new_path = get_flat_output(show_path_command, sep='', shell=True)

        for location in locations:
            if not location_in_path(location, new_path):
                if check:
                    raise Exception(
                        'Unable to find `{}` in the output of `{}`:\n{}'.format(location, show_path_command, new_path)
                    )
                else:
                    return False
        else:
            return True

    def put(self, location, front=True, check=False, **kwargs):
        location = normpath(location)

        # PowerShell should always be available on Windows 7 or later.
        try:
            old_path = os.environ.get('PATH', '')
            head, tail = (location, old_path) if front else (old_path, location)
            new_path = '{}{}{}'.format(head, os.pathsep, tail)

            subprocess.check_output(
                [
                    'powershell',
                    '-Command',
                    "& {{[Environment]::SetEnvironmentVariable('PATH', '{}', 'User')}}".format(new_path),
                ],
                shell=True,
            )
        except subprocess.CalledProcessError:  # no cov
            try:
                head, tail = (location, '%~a') if front else ('%~a', location)
                new_path = '{}{}{}'.format(head, os.pathsep, tail)

                # https://superuser.com/a/601034/766960
                subprocess.check_output(
                    (
                        'for /f "skip=2 tokens=3*" %a in (\'reg query HKCU\\Environment '
                        '/v PATH\') do @if [%b]==[] ( @setx PATH "{new_path}" ) else '
                        '( @setx PATH "{new_path} %~b" )'.format(new_path=new_path)
                    ),
                    shell=True,
                )
            except subprocess.CalledProcessError:
                return False

        return self.location_in_new_path(location, check=check)


class UnixInterface:
    def __init__(self, shells=None, all_shells=False, home=None):
        if shells:
            all_shells = False
        else:
            if all_shells:
                shells = sorted(SHELLS)
            else:
                shells = [self.detect_shell()]

        shells = [os.path.basename(shell).lower() for shell in shells if shell]
        shells = [shell for shell in shells if shell in SHELLS]

        if not shells:
            shells = DEFAULT_SHELLS

        # De-dup and retain order
        deduplicated_shells = set()
        selected_shells = []
        for shell in shells:
            if shell not in deduplicated_shells:
                deduplicated_shells.add(shell)
                selected_shells.append(shell)

        self.shells = [SHELLS[shell](home) for shell in selected_shells]
        self.shells_to_verify = [SHELLS[shell](home) for shell in DEFAULT_SHELLS] if all_shells else self.shells

    @classmethod
    def detect_shell(cls):
        # First, try to see what spawned this process
        shell = get_parent_process_name().lower()
        if shell in SHELLS:
            return shell

        # Then, search for environment variables that are known to be set by certain shells
        # NOTE: This likely does not work when not directly in the shell
        if 'BASH_VERSION' in os.environ:
            return 'bash'

        # Finally, try global environment
        shell = os.path.basename(os.environ.get('SHELL', '')).lower()
        if shell in SHELLS:
            return shell

    def location_in_new_path(self, location, check=False):
        locations = normpath(location).split(os.pathsep)

        for shell in self.shells_to_verify:
            for show_path_command in shell.show_path_commands():
                new_path = get_flat_output(show_path_command)
                for location in locations:
                    if not location_in_path(location, new_path):
                        if check:
                            raise Exception(
                                'Unable to find `{}` in the output of `{}`:\n{}'.format(
                                    location, show_path_command, new_path
                                )
                            )
                        else:
                            return False
        else:
            return True

    def put(self, location, front=True, app_name=None, check=False):
        location = normpath(location)
        app_name = app_name or 'userpath'

        for shell in self.shells:
            for file, contents in shell.config(location, front=front).items():
                try:
                    ensure_parent_dir_exists(file)

                    if os.path.exists(file):
                        with open(file, 'r', encoding='utf-8') as f:
                            lines = f.readlines()
                    else:
                        lines = []

                    lines.append(
                        u'\n{} Created by `{}` on {}\n'.format(
                            shell.comment_starter, app_name, datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
                        )
                    )
                    lines.append(u'{}\n'.format(contents))

                    with open(file, 'w', encoding='utf-8') as f:
                        f.writelines(lines)
                except Exception:
                    continue

        return self.location_in_new_path(location, check=check)


__default_interface = WindowsInterface if os.name == 'nt' or platform.system() == 'Windows' else UnixInterface


class Interface(__default_interface):
    pass
