import inspect
import logging

import pytest


@pytest.mark.usefixtures("setup")
class BaseClass:

    def calllogger(self):

        logger = logging.getLogger(inspect.stack()[1][3])  # created an logger object.

        file_handler = logging.FileHandler('logfile1.log')  # created a file where the logs can be written.

        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")

        file_handler.setFormatter(formatter)

        logger.addHandler(file_handler)  # handler will inform the logger to write the logs in specified location.
        logger.setLevel(logging.INFO)
        return logger


