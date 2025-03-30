import os
from dotenv import load_dotenv
from nb_log import get_logger

logger = get_logger(__name__)

def string_to_bool(s: str) -> bool:
    return s.lower() in ["true", "yes", "1", "y"]


load_dotenv()
ACCOUNT = os.getenv("ACCOUNT").strip()
PASSWORD = os.getenv("PASSWORD").strip()
PROXY =  os.getenv("PROXY",None)
DOCKERMODE = string_to_bool(os.getenv("DOCKERMODE", "false"))
if DOCKERMODE:
    from pyvirtualdisplay import Display
    display = Display(visible=False, size=(1920, 1080))
    display.start()
    logger.info("Display started")