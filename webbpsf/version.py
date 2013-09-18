# Autogenerated by Astropy-affiliated package webbpsf's setup.py on 2013-09-18 00:59:00.509089

from astropy.version_helpers import update_git_devstr, get_git_devstr

_last_generated_version = '0.3.dev108'

version = update_git_devstr(_last_generated_version)
githash = get_git_devstr(sha=True, show_warning=False)

major = 0
minor = 3
bugfix = 0

release = False
debug = False

try:
    from .utils._compiler import compiler
except ImportError:
    compiler = "unknown"

try:
    from .cython_version import cython_version
except ImportError:
    cython_version = "unknown"
