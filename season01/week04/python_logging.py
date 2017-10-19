"""
# Python Logging
* doc: https://docs.python.org/3/library/logging.html
* video: https://www.youtube.com/watch?v=g8nQ90Hk328
"""
import logging

LOG_FORMAT = '%(levelname)s %(asctime)s - %(message)s'

logging.basicConfig(level=logging.DEBUG,
                    filename='output.log',
                    format=LOG_FORMAT,
                    filemode='w')

logger = logging.getLogger()

logger.debug("Debug Message.")
logger.info("Info Message.")
logger.warning("Warning Message.")
logger.error("Error Message.")
logger.critical("Critical Message.")

print(logger.level)