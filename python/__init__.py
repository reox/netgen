import os
from os import environ
from sys import path
from sys import platform as __platform
if __platform.startswith('linux'):
    try:
        path.append(environ['NETGENDIR']+'/../lib')
    except KeyError:
        path.append(os.path.dirname(__file__) + '/../../..')
if __platform.startswith('win'):
    path.append(environ['NETGENDIR'])
if __platform.startswith('darwin'):
    path.append(environ['NETGENDIR'])

 
# from libngpy import *
import libngpy 

from . import csg
from . import meshing

del environ
del path
