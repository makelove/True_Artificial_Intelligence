## style-transfer风格转换
- 参考
    - https://github.com/lengstrom/fast-style-transfer

- 下载mat文件
    - wget http://www.vlfeat.org/matconvnet/models/beta16/imagenet-vgg-verydeep-19.mat


- 运行
```bash
(.py3) nvidia@gpu:~/github/neural-style$ python neural_style.py --styles examples/2-style2.jpg --content ./examples/3-big_bang_3.jpg  --output ./examples/3-big_bang_3out.jpg
2017-12-07 11:42:35.757561: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:857] ARM64 does not support NUMA - returning NUMA node zero
2017-12-07 11:42:35.757770: I tensorflow/core/common_runtime/gpu/gpu_device.cc:955] Found device 0 with properties:
name: NVIDIA Tegra X2
major: 6 minor: 2 memoryClockRate (GHz) 1.3005
pciBusID 0000:00:00.0
Total memory: 7.67GiB
Free memory: 3.78GiB
2017-12-07 11:42:35.757825: I tensorflow/core/common_runtime/gpu/gpu_device.cc:976] DMA: 0
2017-12-07 11:42:35.757856: I tensorflow/core/common_runtime/gpu/gpu_device.cc:986] 0:   Y
2017-12-07 11:42:35.757932: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1045] Creating TensorFlow device (/gpu:0) -> (device: 0, name: NVIDIA Tegra X2, pci bus id: 0000:00:00.0)
2017-12-07 11:42:44.089779: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1045] Creating TensorFlow device (/gpu:0) -> (device: 0, name: NVIDIA Tegra X2, pci bus id: 0000:00:00.0)
2017-12-07 11:42:58.430615: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1045] Creating TensorFlow device (/gpu:0) -> (device: 0, name: NVIDIA Tegra X2, pci bus id: 0000:00:00.0)
Optimization started...
Iteration    1/1000
Iteration    2/1000

Iteration  999/1000
Iteration 1000/1000
  content loss: 3.62553e+06
    style loss: 679985
       tv loss: 105576
    total loss: 4.41109e+06
```