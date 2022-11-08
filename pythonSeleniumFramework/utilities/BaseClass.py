import inspect
import logging
import pytest


@pytest.mark.usefixtures("setup")
class BaseClass:
    logger_name = inspect.stack()[1][3]
    log = logging.getLogger(logger_name)
    file_handler = logging.FileHandler("logs.log")
    log.addHandler(file_handler)
    set_format = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
    file_handler.setFormatter(set_format)
    log.setLevel(logging.INFO)
    # log.debug("This is a debug statement")
    # log.info("This is an info statement")
    # log.warning("This is warning statement")
    # log.error("This is an error statement")
    # return log