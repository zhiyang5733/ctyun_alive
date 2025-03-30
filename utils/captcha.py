import time
import ddddocr
import requests
from nb_log import get_logger
logger = get_logger(__name__)


def get_captcha_code(account,proxy_server=None):
    url = f'https://desk.ctyun.cn:8810/api/auth/client/captcha?height=36&width=85&userInfo={account}&mode=auto&_t={int(time.time() * 1000)}'
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36"
    }
    if proxy_server:
        proxies = {
            "http": proxy_server,
            "https": proxy_server
        }
    else:
        proxies = None


    response = requests.get(url, headers=headers, proxies=proxies)
    if response.ok:
        img_content = response.content
        # with open("image.png", "wb") as f:
        #     f.write(img_content)
        ocr = ddddocr.DdddOcr()
        result = ocr.classification(img_content)
        logger.debug(f"获取验证码成功: {result}")
        return result
    else:
        logger.error(f"获取验证码失败: {response.status_code}")
        return None
if __name__ == "__main__":
    get_captcha_code("13301000000")