
import asyncio
import json
import logging
import os
import platform
import signal
import subprocess
import time
import platform
import psutil
from DrissionPage import Chromium, ChromiumOptions





logger = logging.getLogger(__name__)


class Browser(object):

    def __init__(self, user_agent=None, proxy_server=None):
        browser_path = "/usr/bin/google-chrome"
        options = ChromiumOptions()
        options.set_paths(browser_path=browser_path)
        ###
        options.auto_port()
        options.set_timeouts(base=1)
        
        arguments = [
            "-no-first-run",
            "-force-color-profile=srgb",
            "-metrics-recording-only",
            "-password-store=basic",
            "-use-mock-keychain",
            "-export-tagged-pdf",
            "-no-default-browser-check",
            "-disable-background-mode",
            "-enable-features=NetworkService,NetworkServiceInProcess,LoadCryptoTokenExtension,PermuteTLSExtensions",
            "-disable-features=FlashDeprecationWarning,EnablePasswordsAccountStorage",
            "-deny-permission-prompts",
            "-disable-gpu",
            "-accept-lang=en-US",
            "-window-size=1920,1080",
        ]

        if platform.system() == "Linux":
            options.headless(True)
            arguments.append("--no-sandbox")
            arguments.append("--headless=new")

        if proxy_server:
            options.set_proxy(proxy_server)

        if user_agent:
            options.set_user_agent(user_agent)
        else:
            options.set_user_agent("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36")

        for argument in arguments:
            options.set_argument(argument)

        self.driver = Chromium(addr_or_opts=options)

    

    def get_page(self):
        page = self.driver.latest_tab
        page.set.load_mode.none()
        return page

    def quit(self):
        if self.driver:
            try:
                self.driver.quit()
            except:
                pass
