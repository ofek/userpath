import os
import platform
import subprocess

ON_WINDOWS = False
if os.name == 'nt' or platform.system() == 'Windows':
    ON_WINDOWS = True


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

    def put(path, front=True, app_name=None):
        path = normpath(path)

        # PowerShell will always be available on Windows 7 or later.
        try:
            old_path = get_new_path()
            head, tail = (path, old_path) if front else (old_path, path)
            new_path = '{}{}{}'.format(head, os.pathsep, tail)

            subprocess.check_call([
                'powershell',
                '-Command',
                "& {{[Environment]::SetEnvironmentVariable('PATH', '{}', 'User')}}".format(new_path)
            ], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        except subprocess.CalledProcessError:
            try:
                head, tail = (path, '%~a') if front else ('%~a', path)
                new_path = '{}{}{}'.format(head, os.pathsep, tail)

                # https://superuser.com/a/601034/766960
                subprocess.check_call((
                    'for /f "skip=2 tokens=3*" %a in (\'reg query HKCU\Environment '
                    '/v PATH\') do @if [%b]==[] ( @setx PATH "{new_path}" ) else '
                    '( @setx PATH "{new_path} %~b" )'.format(new_path=new_path)
                ), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            except subprocess.CalledProcessError:
                return False

        return location_in_path(path, get_new_path())

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

    def put(path, front=True, app_name=None):
        # This function is probably insufficient even though it works in
        # most situations. Please improve this to succeed more broadly!
        path = normpath(path)

        try:
            head, tail = (path, '$PATH') if front else ('$PATH', path)
            new_path = '{}{}{}'.format(head, os.pathsep, tail)

            for file in INIT_FILES:
                if os.path.exists(file):
                    with open(file, 'r') as f:
                        lines = f.readlines()
                else:
                    lines = []

                lines.extend([
                    '# Created by `{}` on {}\n'.format(
                        app_name or 'addpath', datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
                    ),
                    INIT_FILES[file].format(new_path)
                ])
                with open(file, 'w') as f:
                    f.writelines(lines)
        except (OSError, PermissionError):
            return False

        return location_in_path(path, get_new_path())


def prepend(location, app_name=None):
    return put(location, front=True, app_name=app_name)


def append(location, app_name=None):
    return put(location, front=False, app_name=app_name)


def in_current_path(location):
    return location_in_path(location, os.environ.get('PATH', ''))


def in_new_path(location):
    return location_in_path(location, get_new_path())


def need_shell_restart(location):
    return not in_current_path(location) and in_new_path(location)
