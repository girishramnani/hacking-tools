__author__ = 'girish'

import argparse
import os
import _pfish_tools
import logging
import time
import sys

logging.basicConfig(filemode="ghasher.log",level=logging.DEBUG,format="%(asctime)s %(message)s ")
logging.info("Welcome to ghasher ver 1 New scan started")
logging.info("Welcome to ghasher ver 1.0")
logging.info("System: "+sys.platform)
logging.info("version: "+sys.version)
_pfish_tools.parse_command_line()
start_time = time.time()


fileprocessed = _pfish_tools.Walk_path()

#Record the end time and calculate the duration
endTime = time.time()
duration = endTime-start_time
logging.info("files Processed"+str(fileprocessed))
logging.info("Elapsed time: "+str(duration)+" seconds")
logging.info("Program End")





