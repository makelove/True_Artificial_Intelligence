## puppeteer建议

- 打开可视窗口调试
    - puppeteer.launch({headless:false})
- 引入sleep
    - let sleep=require('sleep');
    - sleep.sleep(8);
    - 不需要。puppeteer自带等待函数
        - page.waitFor(2000)
        - page.waitFor('.next');//等待某标签出现