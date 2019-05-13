from os import path, pathsep

DEFAULT_SHELLS = ('bash', 'sh')


class Shell(object):
    comment_starter = '#'

    def __init__(self, home=None):
        self.home = home or path.expanduser('~')


class Sh(Shell):
    def config(self, location, front=True):
        head, tail = (location, '$PATH') if front else ('$PATH', location)
        new_path = '{}{}{}'.format(head, pathsep, tail)

        return {path.join(self.home, '.profile'): 'PATH="{}"'.format(new_path)}

    @classmethod
    def show_path_command(cls):
        return ['sh', '-l', '-c', 'echo $PATH']


class Bash(Shell):
    def config(self, location, front=True):
        head, tail = (location, '$PATH') if front else ('$PATH', location)
        new_path = '{}{}{}'.format(head, pathsep, tail)
        contents = 'export PATH="{}"'.format(new_path)

        return {
            path.join(self.home, '.bashrc'): contents,
            # NOTE: If it is decided in future that we want to make a distinction between
            # login and non-login shells, be aware that macOS will still need this since
            # Terminal.app runs a login shell by default for each new terminal window.
            path.join(self.home, '.bash_profile'): contents,
        }

    @classmethod
    def show_path_command(cls):
        return ['bash', '--login', '-c', 'echo $PATH']


class Fish(Shell):
    def config(self, location, front=True):
        location = ' '.join(location.split(pathsep))
        head, tail = (location, '$PATH') if front else ('$PATH', location)

        # https://github.com/fish-shell/fish-shell/issues/527#issuecomment-12436286
        contents = 'set PATH {} {}'.format(head, tail)

        return {path.join(self.home, '.config', 'fish', 'config.fish'): contents}

    @classmethod
    def show_path_command(cls):
        return ['fish', '--login', '-c', 'for p in $PATH; echo "$p"; end']


class Xonsh(Shell):
    def config(self, location, front=True):
        locations = location.split(pathsep)

        if front:
            contents = '\n'.join('$PATH.insert(0, r"{}")'.format(location) for location in reversed(locations))
        else:
            contents = '\n'.join('$PATH.append(r"{}")'.format(location) for location in locations)

        return {path.join(self.home, '.xonshrc'): contents}

    @classmethod
    def show_path_command(cls):
        return ['xonsh', '--login', '-c', "print('{}'.join($PATH))".format(pathsep)]


class Zsh(Shell):
    def config(self, location, front=True):
        head, tail = (location, '$PATH') if front else ('$PATH', location)
        new_path = '{}{}{}'.format(head, pathsep, tail)
        contents = 'export PATH="{}"'.format(new_path)

        return {path.join(self.home, '.zshrc'): contents, path.join(self.home, '.zprofile'): contents}

    @classmethod
    def show_path_command(cls):
        return ['zsh', '--login', '-c', 'echo $PATH']


SHELLS = {
    'bash': Bash,
    'fish': Fish,
    'sh': Sh,
    'xonsh': Xonsh,
    'zsh': Zsh,
}
