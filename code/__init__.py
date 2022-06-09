import logging

prefix = (
    "%(asctime)s,%(msecs)03d [%(levelname)-7s] [%(filename)s:%(lineno)d %(funcName)s] %(message)s"
)
logging.basicConfig(format=prefix, datefmt='%M:%S', level=logging.INFO)
logger = logging.getLogger(__name__)
