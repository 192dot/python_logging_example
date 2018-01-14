import os
import getpass
import logging
from logging.config import fileConfig
# setup logging
base_dir = os.path.dirname(os.path.abspath(__file__))
log_dir = base_dir + '/log'
if not os.path.exists(log_dir):
    os.makedirs(log_dir)
os.environ['mylogfile'] = log_dir + '/mylog.log'
log_config = base_dir + '/logging_config.ini'
fileConfig(log_config)
logger = logging.getLogger()

if __name__ == '__main__':
    caller_username = getpass.getuser()
    message = "Script is called on cli by user: {}".format(caller_username)
    logger.info(message)
