import logging
import sys
import time

logging.Formatter.converter = time.gmtime
_logger = logging.getLogger()
_streamHandler = logging.StreamHandler(sys.stdout)
_formatter = logging.Formatter('%(asctime)s.%(msecs)03d UTC - %(name)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
_streamHandler.setFormatter(_formatter)
_logger.addHandler(_streamHandler)

LOGGER = _logger
