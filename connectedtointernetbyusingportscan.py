"""
1. write data to PLCs that are connected to the internet by using port scanning function
"""

import socket
import time
import sys
import os
import threading
import queue
import struct
import random
import string
import re

# global variables
# the number of threads
thread_num = 10
# the number of ports to be scanned
port_num = 100
# the number of ports that are scanned
port_scanned = 0
# the number of ports that are open
port_open = 0
# the number of ports that are closed
port_closed = 0
# the number of ports that are filtered
port_filtered = 0
# the number of ports that are unfiltered
port_unfiltered = 0
# the number of ports that are open|filtered
port_open_filtered = 0
# the number of ports that are closed|filtered
port_closed_filtered = 0
# the number of ports that are open|unfiltered
port_open_unfiltered = 0
# the number of ports that are closed|unfiltered
port_closed_unfiltered = 0
# the number of ports that are open|filtered|unfiltered
port_open_filtered_unfiltered = 0
# the number of ports that are closed|filtered|unfiltered
port_closed_filtered_unfiltered = 0
# the number of ports that are open|closed
port_open_closed = 0
# the number of ports that are open|closed|filtered
port_open_closed_filtered = 0
# the number of ports that are open|closed|unfiltered
port_open_closed_unfiltered = 0
# the number of ports that are open|closed|filtered|unfiltered
port_open_closed_filtered_unfiltered = 0