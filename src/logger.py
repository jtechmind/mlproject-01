import logging
import os
from datetime import datetime

# Create logs directory
LOG_DIR = "logs"
os.makedirs(LOG_DIR,exist_ok=True)

# Log filename with timestamp
LOG_FILE=f"{datetime.now().strftime('%m_%d_%y_%H_%M_%S')}.log"
LOG_FILE_PATH = os.path.join(LOG_DIR,LOG_FILE)
# log_path=os.path.join(os.getcwd(),"logs",LOG_FILE)

# Congifure logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)


# Console handler
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

console_formatter = logging.Formatter(
    "[%(asctime)s]%(levelname)s - %(message)s"
)
console_handler.setFormatter(console_formatter)

# Add a console handler
logging.getLogger().addHandler(console_handler)