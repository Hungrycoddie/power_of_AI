import sys
import time
import logging
import threading
import queue
import os
import json

from pycomm.ab_comm.clx import Driver as ClxDriver
from pycomm.cip.cip_base import CIPError

from pycomm.utils import get_logger
from pycomm.utils import get_log_level
from pycomm.utils import get_log_file
from pycomm.utils import get_log_format
from pycomm.utils import get_log_date_format
from pycomm.utils import get_log_file_size
from pycomm.utils import get_log_file_count
from pycomm.utils import get_log_file_mode
from pycomm.utils import get_log_file_encoding
from pycomm.utils import get_log_file_backup_count
from pycomm.utils import get_log_file_max_bytes
from pycomm.utils import get_log_file_delay
from pycomm.utils import get_log_file_when
from pycomm.utils import get_log_file_interval
from pycomm.utils import get_log_file_utc
from pycomm.utils import get_log_file_at_time