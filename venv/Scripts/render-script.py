#!"F:\Python projects\weather\venv\Scripts\python.exe"
# EASY-INSTALL-ENTRY-SCRIPT: 'render==1.0.0','console_scripts','render'
__requires__ = 'render==1.0.0'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('render==1.0.0', 'console_scripts', 'render')()
    )
