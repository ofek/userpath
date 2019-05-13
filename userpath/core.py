from .interface import Interface
from .utils import in_current_path


def prepend(location, app_name=None, shells=None, all_shells=False, home=None):
    interface = Interface(shells=shells, all_shells=all_shells, home=home)
    return interface.put(location, front=True, app_name=app_name)


def append(location, app_name=None, shells=None, all_shells=False, home=None):
    interface = Interface(shells=shells, all_shells=all_shells, home=home)
    return interface.put(location, front=False, app_name=app_name)


def in_new_path(location, shells=None, all_shells=False, home=None):
    interface = Interface(shells=shells, all_shells=all_shells, home=home)
    return interface.location_in_new_path(location)


def need_shell_restart(location, shells=None, all_shells=False, home=None):
    interface = Interface(shells=shells, all_shells=all_shells, home=home)
    return not in_current_path(location) and interface.location_in_new_path(location)
