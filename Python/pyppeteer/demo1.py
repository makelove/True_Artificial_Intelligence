# -*- coding: utf-8 -*-
# @Time    : 2018/5/27 15:15
# @Author  : play4fun
# @File    : demo1.py
# @Software: PyCharm

"""
demo1.py:
"""

import asyncio
from pyppeteer import launch

async def main():
    browser = await launch({'headless':False})
    page = await browser.newPage()
    await page.goto('https://pub.alimama.com/index.htm',{'timeout':0})
    # page.waitFor(3)
    await page.waitFor('#q')
    await page.screenshot({'path': 'pub.alimama.png'})
    await browser.close()

asyncio.get_event_loop().run_until_complete(main())