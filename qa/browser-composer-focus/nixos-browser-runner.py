import glob
import os
import re
import subprocess
import sys

binary = '/home/andrei/.cache/ms-playwright/chromium_headless_shell-1208/chrome-headless-shell-linux64/chrome-headless-shell'
env = os.environ.copy()
paths = env.get('LD_LIBRARY_PATH', '').split(':') if env.get('LD_LIBRARY_PATH') else []
for _ in range(8):
    env['LD_LIBRARY_PATH'] = ':'.join(paths)
    linked = subprocess.run(['ldd', binary], env=env, capture_output=True, text=True)
    missing = re.findall(r'^\s*(\S+) => not found', linked.stdout, re.M)
    if not missing:
        break
    for name in missing:
        candidates = sorted(glob.glob('/nix/store/*/lib/' + name))
        if not candidates:
            sys.exit('No Nix library found for ' + name)
        directory = os.path.dirname(candidates[-1])
        if directory not in paths:
            paths.append(directory)
else:
    sys.exit('Unresolved Chromium libraries: ' + ', '.join(missing))
os.execvpe(sys.argv[1], sys.argv[1:], env)
