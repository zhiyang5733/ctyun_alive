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
USER_AGENT = os.getenv("USER_AGENT",None)
DOCKERMODE = string_to_bool(os.getenv("DOCKERMODE", "false"))
# 间隔执行时间，单位分钟 (不超过60分钟)
INTERVAL_MINUTE = int(os.getenv("INTERVAL_MINUTE", 45))
# 云电脑保活时间，单位秒 (云电脑页面打开时间太短可能无法保活)
ALIVE_SECOND = int(os.getenv("ALIVE_SECOND", 80))

######
logger.info("#"*60)
logger.info(f"ACCOUNT: {ACCOUNT}")
# logger.info(f"PASSWORD: {PASSWORD}")
logger.info(f"PROXY: {PROXY}")
logger.info(f"USER_AGENT: {USER_AGENT}")
# logger.info(f"DOCKERMODE: {DOCKERMODE}")
logger.info(f"INTERVAL_MINUTE: {INTERVAL_MINUTE}")
logger.info(f"ALIVE_SECOND: {ALIVE_SECOND}")
logger.info("#" * 60)
if DOCKERMODE:
    from pyvirtualdisplay import Display
    display = Display(visible=False, size=(1920, 1080))
    display.start()
    logger.info("Display started")