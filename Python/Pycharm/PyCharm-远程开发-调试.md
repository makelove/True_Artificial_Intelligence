## PyCharm-远程开发-调试

- [使用PyCharm进行远程开发和调试](https://www.xncoding.com/2016/05/26/python/pycharm-remote.html)

- 心得
    - 不需要使用root账户
    - 使用旧工程需要自己上传同步
    - 新建工程，选择远程python，会自动建立同步功能
    - 只支持pycharm pro
    - 解决【自定义PYTHONPATH】的问题
        - 在远程服务器上，有时需要source某个sh文件，引入新的包
            - 例如rospy ： source /opt/ros/kinetic/setup.bash     
        - 解决： 
            - 打开Project Interpreters，选中你的python Interpreters
            - 打开Interpreter Paths，添加/opt/ros/linetic/lib/python2.7/dist-packages
            - 在程序中测试 import rospy
            - 搞定