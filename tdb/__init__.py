"""
Debugger for Tensorflow

import tfdebugger as td

"""

from .interface import debug, c, s, get_exe_queue, get_value
from .op_store import *
from .plot_op import plot_op
from . import plot_op
from . import python_op
from .debug_session import INITIALIZED, RUNNING, PAUSED, FINISHED
from .app import connect
#from .app import is_notebook, connect
#import examples
#import tests

connect()
