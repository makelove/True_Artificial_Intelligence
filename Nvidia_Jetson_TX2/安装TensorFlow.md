## 安装TensorFlow

- 参考
    - [为Python安装TensorFlow - NVIDIA Jetson TX开发工具包](http://www.jetsonhacks.com/2017/09/22/install-tensorflow-python-nvidia-jetson-tx-dev-kits/)
    - https://github.com/jetsonhacks/installTensorFlowJetsonTX
    
- 安装
    - sudo apt-get install -y python3-pip python3-dev
    - pip3 install ./tensorflow-1.3.0-cp35-cp35m-linux_aarch64.whl
- 测试 ipython
```bash
In [1]: import tensorflow as tf
In [2]: tf
Out[2]: <module 'tensorflow' from '/home/nvidia/.py3/lib/python3.5/site-packages/tensorflow/__init__.py'>
```    