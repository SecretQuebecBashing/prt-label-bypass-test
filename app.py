# Simple application with logging
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def hello():
    logger.info("hello() called")
    return "Hello, World!"

if __name__ == "__main__":
    print(hello())
