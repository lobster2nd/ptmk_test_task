import os
import sys

sys.path.insert(1, os.path.join(sys.path[0], '..'))

from orm import create_tables

create_tables()