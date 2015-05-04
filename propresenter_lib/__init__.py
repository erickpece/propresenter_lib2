
import logging

FORMAT = '%(asctime)-15s | %(message)s'
logging.basicConfig(format=FORMAT, level=logging.INFO)

logging.info('{} started'.format(__name__))