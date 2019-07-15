import inspect, os
loc = inspect.getfile(inspect.currentframe())
relloc = os.path.abspath(loc)
dirloc = relloc.partition('/install.py')[0]

def spaceantibug(path1):
    """
    formats string for terminal based execution.
    """
    l = path1.split(' ')
    if len(l) == 1: return path1
    else: return '\ '.join(l)

stringinp = '''
[Desktop Entry]
Version=1.0
Encoding=UTF-8
Type=Application
Terminal=false
Name=FilterApp
Exec=python {0}
Icon= {1}
Name[en]=FilterApp
'''.format(spaceantibug(dirloc) + '/run.py',  dirloc + '/Pictures/filter.png')

deskpath = dirloc + '/Filter_app.desktop'
if not os.path.exists(deskpath):
    with open(deskpath, 'w') as var: pass
    with open(deskpath, 'r+') as var:
        var.truncate(0)
        var.write(stringinp)
else:
    with open(deskpath, 'r+') as var:
        var.truncate(0)
        var.write(stringinp)

os.system('chmod +x {}'.format(spaceantibug(deskpath)))

