from loguru import logger
logger.add(sink='error.log', diagnose=True)