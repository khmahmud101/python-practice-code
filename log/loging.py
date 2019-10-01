import logging

logging.basicConfig(format='%(asctime)s %(message)s',datefmt='%m/%d/%Y %I:%M:%S %p',filename='test.log',filemode='w',level=logging.DEBUG)
logging.debug("this is debug log")
logging.info("this is info log")
logging.warning("this is warning log")
logging.error("this is error log")
