''' start a language '''
from os import path
import json

DATA = '%s/data/' % path.abspath(path.dirname(__file__))
pos = json.loads(open('%s/pos.json' % DATA).read())
