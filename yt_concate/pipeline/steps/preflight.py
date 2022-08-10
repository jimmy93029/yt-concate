import logging
from .step import Step


class Preflight(Step):
    def process(self, data, inputs, utils):
        logging.info('in preflight')
        utils.create_dirs()
        logging.warning('just for test')
