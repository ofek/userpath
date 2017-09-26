import os
import platform
import subprocess

ON_WINDOWS = os.name == 'nt' or platform.system() == 'Windows'


def normpath(location):
    return os.path.normpath(location.strip(';:'))


def location_in_path(location, path):
    return normpath(location) in (
        os.path.normpath(p) for p in path.split(os.pathsep)
    )


if ON_WINDOWS:
    def get_new_path():
        output = subprocess.check_output([
            'powershell', '-Command', "& {[Environment]::GetEnvironmentVariable('PATH', 'User')}"
        ], shell=True).decode().strip()

        # We do this because the output may contain new lines.
        return ''.join(output.splitlines())

    def put(location, front=True, app_name=None):
        location = normpath(location)

        # PowerShell will always be available on Windows 7 or later.
        try:
            old_path = get_new_path()
            head, tail = (location, old_path) if front else (old_path, location)
            new_path = '{}{}{}'.format(head, os.pathsep, tail)

            subprocess.check_call([
                'powershell',
                '-Command',
                "& {{[Environment]::SetEnvironmentVariable('PATH', '{}', 'User')}}".format(new_path)
            ], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        except subprocess.CalledProcessError:
            try:
                head, tail = (location, '%~a') if front else ('%~a', location)
                new_path = '{}{}{}'.format(head, os.pathsep, tail)

                # https://superuser.com/a/601034/766960
                subprocess.check_call((
                    'for /f "skip=2 tokens=3*" %a in (\'reg query HKCU\Environment '
                    '/v PATH\') do @if [%b]==[] ( @setx PATH "{new_path}" ) else '
                    '( @setx PATH "{new_path} %~b" )'.format(new_path=new_path)
                ), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            except subprocess.CalledProcessError:
                return False

        new_path = get_new_path()
        return all(location_in_path(l, new_path) for l in location.split(os.pathsep))

else:
    from datetime import datetime

    INIT_FILES = {
        os.path.expanduser('~/.profile'): 'PATH="{}"\n',
        os.path.expanduser('~/.bashrc'): 'export PATH="{}"\n',
        # macOS seems to need this.
        os.path.expanduser('~/.bash_profile'): 'export PATH="{}"\n',
    }

    def get_new_path():
        return subprocess.check_output(['bash', '--login', '-c', 'echo $PATH']).decode().strip()

    def put(location, front=True, app_name=None):
        # This function is probably insufficient even though it works in
        # most situations. Please improve this to succeed more broadly!
        location = normpath(location)

        try:
            head, tail = (location, '$PATH') if front else ('$PATH', location)
            new_path = '{}{}{}'.format(head, os.pathsep, tail)

            for file in INIT_FILES:
                if os.path.exists(file):
                    with open(file, 'r') as f:
                        lines = f.readlines()
                else:
                    lines = []

                lines.extend([
                    '# Created by `{}` on {}\n'.format(
                        app_name or 'userpath', datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
                    ),
                    INIT_FILES[file].format(new_path)
                ])
                with open(file, 'w') as f:
                    f.writelines(lines)
        except (OSError, PermissionError):
            return False

        new_path = get_new_path()
        return all(location_in_path(l, new_path) for l in location.split(os.pathsep))


def prepend(location, app_name=None):
    if isinstance(location, list) or isinstance(location, tuple):
        location = os.pathsep.join(normpath(l) for l in location)
    return put(location, front=True, app_name=app_name)


def append(location, app_name=None):
    if isinstance(location, list) or isinstance(location, tuple):
        location = os.pathsep.join(normpath(l) for l in location)
    return put(location, front=False, app_name=app_name)


def in_current_path(location):
    current_path = os.environ.get('PATH', '')
    if isinstance(location, list) or isinstance(location, tuple):
        return all(location_in_path(l, current_path) for l in location)
    else:
        return location_in_path(location, current_path)


def in_new_path(location):
    new_path = get_new_path()
    if isinstance(location, list) or isinstance(location, tuple):
        return all(location_in_path(l, new_path) for l in location)
    else:
        return location_in_path(location, new_path)


def need_shell_restart(location):
    if isinstance(location, list) or isinstance(location, tuple):
        return any(not in_current_path(l) and in_new_path(l) for l in location)
    else:
        return not in_current_path(location) and in_new_path(location)
