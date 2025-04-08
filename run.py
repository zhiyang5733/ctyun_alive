import time
from utils.browser import Browser
from utils.captcha import get_captcha_code
from config import ACCOUNT,PASSWORD,PROXY,USER_AGENT
from nb_log import get_logger
logger = get_logger(__name__)

def login(page, account,proxy):
    if page.ele(".code", timeout=10):
        logger.info("检测到验证码！")
        code= get_captcha_code(account,proxy)
        page.ele(".code").input(code)
    page.listen.start('desk.ctyun.cn:8810/api/auth/client/login') 
    page.ele(".:btn-submit").click()
    response = page.listen.wait(timeout=5)
    login_info = response._raw_body
    logger.info(f"登录信息: {response._raw_body}")

    if "云电脑租户" in login_info:
        logger.info("登录成功！")
    elif "验证码错误" in login_info:
        logger.error("验证码错误！")
        return False
    elif "图形验证码错误" in login_info:
        logger.error("图形验证码错误")
        return False
    else:
        logger.error("登录失败！")
        return False
    
    # 默认打开第一台云电脑
    if page.ele(".desktop-main-entry", timeout=10):
        logger.info("打开云电脑界面成功！")
        page.ele(".desktop-main-entry").click()
        page.wait(30)
        logger.info("保活成功！")
        return True
    else:
        logger.error("打开云电脑界面失败！")
        return False


def main():
    account = ACCOUNT
    password = PASSWORD
    proxy = PROXY
    user_agent = USER_AGENT


    browser = Browser(proxy_server=proxy,user_agent=user_agent)
    page = browser.get_page()
    page.get("https://pc.ctyun.cn")

    if page.ele(".account", timeout=10):
        logger.info("页面打开成功！")
        page.ele(".account").click()
        page.ele(".account").input(account)
        page.ele(".password").input(password)
    for i in range(3):
        if login(page, account,proxy):
            break
    browser.quit()


if __name__ == "__main__":
    import schedule
    
    def job():
        try:
            main()
        except Exception as e:
            logger.exception(f"保活任务运行失败: {e}")
    
    # 每50分钟运行一次
    schedule.every(50).minutes.do(job)
    # 立即运行一次
    job()
    while True:
        schedule.run_pending()
        time.sleep(1)
