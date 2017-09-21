import sys

import click

import userpath as up


CONTEXT_SETTINGS = {
    'help_option_names': ['-h', '--help'],
}


def echo_success(text, nl=True):
    click.secho(text, fg='cyan', bold=True, nl=nl)


def echo_failure(text, nl=True):
    click.secho(text, fg='red', bold=True, nl=nl)


def echo_warning(text, nl=True):
    click.secho(text, fg='yellow', bold=True, nl=nl)


@click.group(context_settings=CONTEXT_SETTINGS)
@click.version_option()
def userpath():
    pass


@userpath.command(context_settings=CONTEXT_SETTINGS,
                  short_help='Prepends to the user PATH')
@click.argument('path')
@click.option('-f', '--force', is_flag=True,
              help='Update PATH even if it appears to be correct.')
def prepend(path, force):
    """Prepends to the user PATH. The shell must be restarted for the update to
    take effect.
    """
    if not force:
        if up.in_current_path(path):
            echo_warning((
                'The directory `{}` is already in PATH! If you '
                'are sure you want to proceed, try again with '
                'the -f/--force flag.'.format(path)
            ))
            sys.exit(2)
        elif up.in_new_path(path):
            echo_warning((
                'The directory `{}` is already in PATH, pending a shell '
                'restart! If you are sure you want to proceed, try again '
                'with the -f/--force flag.'.format(path)
            ))
            sys.exit(2)

    if up.prepend(path):
        echo_success('Success!')
    else:
        echo_failure('An unexpected failure seems to have occurred.')
        sys.exit(1)


@userpath.command(context_settings=CONTEXT_SETTINGS,
                  short_help='Appends to the user PATH')
@click.argument('path')
@click.option('-f', '--force', is_flag=True,
              help='Update PATH even if it appears to be correct.')
def append(path, force):
    """Appends to the user PATH. The shell must be restarted for the update to
    take effect.
    """
    if not force:
        if up.in_current_path(path):
            echo_warning((
                'The directory `{}` is already in PATH! If you '
                'are sure you want to proceed, try again with '
                'the -f/--force flag.'.format(path)
            ))
            sys.exit(2)
        elif up.in_new_path(path):
            echo_warning((
                'The directory `{}` is already in PATH, pending a shell '
                'restart! If you are sure you want to proceed, try again '
                'with the -f/--force flag.'.format(path)
            ))
            sys.exit(2)

    if up.append(path):
        echo_success('Success!')
    else:
        echo_failure('An unexpected failure seems to have occurred.')
        sys.exit(1)


@userpath.command(context_settings=CONTEXT_SETTINGS,
                  short_help='Checks if a location is in the user PATH')
@click.argument('path')
def verify(path):
    """Checks if a location is in the user PATH."""
    if up.in_current_path(path):
        echo_success((
            'The directory `{}` is in PATH!'.format(path)
        ))
    elif up.in_new_path(path):
        echo_warning((
            'The directory `{}` is in PATH, pending a shell restart!'.format(path)
        ))
        sys.exit(2)
    else:
        echo_failure((
            'The directory `{}` is not in PATH!'.format(path)
        ))
        sys.exit(1)
