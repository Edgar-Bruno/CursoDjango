import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

TPATH = os.path.join(BASE_DIR, 'aula4/templates/index.html')

xPATH = os.path.join(BASE_DIR, 'siteStatics/')

print BASE_DIR
print TPATH
print xPATH
print "----"
print os.path.dirname(os.path.abspath(__file__))
print "-----"
