## Mac SourceTree免登陆方法
- http://www.boyu0.com/mac-sourcetree%E5%85%8D%E7%99%BB%E9%99%86%E6%96%B9%E6%B3%95/

- 而注册Atlassian账号需要谷歌验证码，由于众所周知的原因，我们无法看到验证码，注册不了
- 试着学着Windows的方式在Mac的~/Library/Application Support/SourceTree/目录下新建相应的json文件，无效
- 打开SourceTree -> 点击菜单栏的 窗口 选项 -> 点击显示托管在远端的仓库 -> 点击登录注册页面右上角的关闭按钮 -> 点击Quit -> 点击确定关闭刷新远端仓库失败的窗口 -> 即可正常使用SourceTree了
- 虽然此方法可以绕过登录，但是每次打开SourceTree都需要操作一次，略烦，而且指不定哪个版本此bug就给修复了，有需要的最好还是凭本事翻个墙吧。