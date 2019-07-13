import os
import subprocess

try:
    import psutil
except Exception:
    pass


def normpath(location):
    if isinstance(location, (list, tuple)):
        return os.pathsep.join(normpath(l) for l in location)

    return os.path.abspath(os.path.expanduser(location.strip(';:')))


def location_in_path(location, path):
    return normpath(location) in (os.path.normpath(p) for p in path.split(os.pathsep))


def in_current_path(location):
    return location_in_path(location, os.environ.get('PATH', ''))


def ensure_parent_dir_exists(path):
    parent_dir = os.path.dirname(os.path.abspath(path))
    if not os.path.isdir(parent_dir):
        os.makedirs(parent_dir)


def get_flat_output(command, sep=os.pathsep, **kwargs):
    process = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, **kwargs)
    output = process.communicate()[0].decode('utf-8').strip()

    # We do this because the output may contain new lines.
    lines = [line.strip() for line in output.splitlines()]
    return sep.join(line for line in lines if line)


def get_parent_process_name():
    # We want this to never throw an exception
    try:
        if psutil:
            try:
                pid = os.getpid()
                process = psutil.Process(pid)
                ppid = process.ppid()
                pprocess = psutil.Process(ppid)
                return pprocess.name()
            except Exception:
                pass

        ppid = os.getppid()
        return subprocess.check_output(['ps', '-o', 'cmd=', str(ppid)]).decode('utf-8').strip()
    except Exception:
        pass

    return ''
