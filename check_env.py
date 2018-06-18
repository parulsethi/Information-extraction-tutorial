# this file is largely based on https://github.com/amueller/scipy-2017-sklearn/blob/master/check_env.ipynb

from distutils.version import LooseVersion as Version
import sys, importlib

try:
    import curses
    curses.setupterm()
    assert curses.tigetnum("colors") > 2
    OK = "\x1b[1;%dm[ OK ]\x1b[0m" % (30 + curses.COLOR_GREEN)
    FAIL = "\x1b[1;%dm[FAIL]\x1b[0m" % (30 + curses.COLOR_RED)
except:
    OK = '[ OK ]'
    FAIL = '[FAIL]'
    
def import_version(pkg, min_ver, fail_msg=""):
    mod = None
    try:
        mod = importlib.import_module(pkg)
        ver = mod.__version__
        if Version(ver) < min_ver:
            print(FAIL, "%s version %s required, but %s installed."
                  % (lib, min_ver, ver))
        else:
            print(OK, '%s version %s' % (pkg, ver))
    except ImportError:
        print(FAIL, '%s not installed. %s' % (pkg, fail_msg))
    return mod

# check python version
print('Using python in', sys.prefix)
print(sys.version)
py_version = Version(sys.version)
if py_version >= "3":
    if py_version < "3.4":
        print(FAIL, "Python version 3.4 or higher is required,"
                    " but %s is installed." % sys.version)
else:
    print(FAIL, "Unknown Python version: %s" % sys.version)

print()
requirements = {'plotly': "2.7.0", 'pyLDAvis': "2.1.2", 'jupyter': "1.0.0", 'scikit-learn': "0.19.1", 'bokeh': "0.12.16", 'numpy': "1.14.4", 'scipy': "1.1.0", 'matplotlib': "2.2.2",'nltk': "3.3", 'pandas': "0.23.0", 'gensim': "3.4.0", 'networkx':"2.1", 'visdom': "0.1.4"}

# check dependencies version
for lib, version in list(requirements.items()):
    import_version(lib, version)