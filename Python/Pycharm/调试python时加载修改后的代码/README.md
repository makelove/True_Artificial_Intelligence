#调试python时加载修改后的代码

- 视频：https://www.bilibili.com/video/av23450263/

- 参考：
    - 文档[Loading Code from Editor into Console](https://www.jetbrains.com/help/pycharm/loading-code-from-editor-into-console.html)
- 问题
    - 在调试python程序时，有时候发现错误，会在代码里直接修改。但是程序需要重启后才能更新到最新代码。
    - pycharm提供了一个解决方案
        - Execute selection in console
    
        
- 案例
    - [PyCharm中是否存在“编辑并继续” ？像在Eclipse / PyDev中一样将代码重新加载到正在运行的程序中？](https://stackoverflow.com/questions/23333815/is-there-edit-and-continue-in-pycharm-reload-code-into-running-program-like-i?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa)
        - 这是一个非常人性化的例子，但希望这可以说明如何在调试时使用Evaluate Expression ...和Execute Line 两种方式来进行调试，而不必在每次发现程序中的错误时重新启动应用程序代码。
        - 在控制台中，如果此调用失败，请输入reload(MyModifiedModule)，并写入import MyModifiedModule并重试。
   - 解决错误：[PyCharm's debugging console fails with KeyError: '_sh'](https://stackoverflow.com/questions/44777057/pycharms-debugging-console-fails-with-keyerror-sh)   
```html
With PyCharm Community Edition 2017.1.3

You need to downgrade, ipython pakage from 6.1.0 to 6.0.0

sudo pip install ipython==6.0.0
```   