## 安装TensorFlow

- 参考
    - [为Python安装TensorFlow - NVIDIA Jetson TX开发工具包](http://www.jetsonhacks.com/2017/09/22/install-tensorflow-python-nvidia-jetson-tx-dev-kits/)
    - https://github.com/jetsonhacks/installTensorFlowJetsonTX
- TensorFlow
    - 版本1.3.0
    - 用CUDA支持构建
    - 利用cuDNN    
- 安装
    - sudo apt-get install -y python3-pip python3-dev
    - pip3 install ./tensorflow-1.3.0-cp35-cp35m-linux_aarch64.whl
- 测试 ipython
```bash
In [1]: import tensorflow as tf
In [2]: tf
Out[2]: <module 'tensorflow' from '/home/nvidia/.py3/lib/python3.5/site-packages/tensorflow/__init__.py'>

In [3]: a = tf.constant([1.0, 2.0, 3.0, 4.0, 5.0, 6.0],
   ...:  shape=[2, 3], name='a')
   ...: b = tf.constant([1.0, 2.0, 3.0, 4.0, 5.0, 6.0],
   ...:  shape=[3, 2], name='b')
   ...: c = tf.matmul(a, b)
   ...:

In [4]: sess = tf.Session(config=tf.ConfigProto(log_dev
   ...: ice_placement=True))
2017-11-26 20:03:28.337739: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:857] ARM64 does not support NUMA - returning NUMA node zero
2017-11-26 20:03:28.337868: I tensorflow/core/common_runtime/gpu/gpu_device.cc:955] Found device 0 with properties:
name: NVIDIA Tegra X2
major: 6 minor: 2 memoryClockRate (GHz) 1.3005
pciBusID 0000:00:00.0
Total memory: 7.67GiB
Free memory: 296.00MiB
2017-11-26 20:03:28.337924: I tensorflow/core/common_runtime/gpu/gpu_device.cc:976] DMA: 0
2017-11-26 20:03:28.337952: I tensorflow/core/common_runtime/gpu/gpu_device.cc:986] 0:   Y
2017-11-26 20:03:28.337978: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1045] Creating TensorFlow device (/gpu:0) -> (device: 0, name: NVIDIA Tegra X2, pci bus id: 0000:00:00.0)
Device mapping:
/job:localhost/replica:0/task:0/gpu:0 -> device: 0, name: NVIDIA Tegra X2, pci bus id: 0000:00:00.0
2017-11-26 20:03:28.345344: I tensorflow/core/common_runtime/direct_session.cc:300] Device mapping:
/job:localhost/replica:0/task:0/gpu:0 -> device: 0, name: NVIDIA Tegra X2, pci bus id: 0000:00:00.0


In [5]: print(sess.run(c))
MatMul: (MatMul): /job:localhost/replica:0/task:0/gpu:0
2017-11-26 20:03:42.631569: I tensorflow/core/common_runtime/simple_placer.cc:872] MatMul: (MatMul)/job:localhost/replica:0/task:0/gpu:0
b: (Const): /job:localhost/replica:0/task:0/gpu:0
2017-11-26 20:03:42.631704: I tensorflow/core/common_runtime/simple_placer.cc:872] b: (Const)/job:localhost/replica:0/task:0/gpu:0
a: (Const): /job:localhost/replica:0/task:0/gpu:0
2017-11-26 20:03:42.631773: I tensorflow/core/common_runtime/simple_placer.cc:872] a: (Const)/job:localhost/replica:0/task:0/gpu:0
[[ 22.  28.]
 [ 49.  64.]]
 
```    
- [Tensorflow：验证您的安装](https://www.tensorflow.org/install/install_linux#ValidateYourInstallation)
```python
# Python
import tensorflow as tf
hello = tf.constant('Hello, TensorFlow!')
sess = tf.Session()
print(sess.run(hello))
```