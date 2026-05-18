import logging

logger = logging.getLogger(__name__)

def log_message(message: str) -> None:
    logger.info(message)