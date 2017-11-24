## 测试 GPU NVIDIA_Tegra


- 参考 
    - [如何在Linux上对GPU进行基准测试](https://www.howtoing.com/linux-gpu-benchmark)
    - [Linux下的硬件性能测试工具汇总](http://blog.topspeedsnail.com/archives/9192)
- glxgears
    - sudo apt-get install mesa-utils
    - glxgears
- glmark2
    - sudo apt-get install glmark2
    - glmark2
    
- 硬件信息
    - sudo apt-get install hardinfo
    - hardinfo
    
- NVIDIA_Tegra_Linux_MultimediaAPIReference/nvl4t_docs/nvvid_backend_group.html

```bash
nvidia@gpu:~$ cd tegra_multimedia_api/samples/
nvidia@gpu:~/tegra_multimedia_api/samples$ ls
00_video_decode    04_video_dec_trt  08_video_dec_drm                 12_camera_v4l2_cuda  Rules.mk
01_video_encode    05_jpeg_encode    09_camera_jpeg_capture           backend              v4l2cuda
02_video_dec_cuda  06_jpeg_decode    10_camera_recording              common
03_video_cuda_enc  07_video_convert  11_camera_object_identification  frontend
nvidia@gpu:~/tegra_multimedia_api/samples$ cd backend/
nvidia@gpu:~/tegra_multimedia_api/samples/backend$ ls
backend   trtModel.cache              v4l2_backend_csvparser.o  v4l2_backend_main.o
Makefile  v4l2_backend_csvparser.cpp  v4l2_backend_main.cpp     v4l2_backend_test.h

./backend 1 ../../data/Video/sample_outdoor_car_1080p_10fps.h264 H264 \
    --trt-deployfile ../../data/Model/GoogleNet_one_class/GoogleNet_modified_oneClass_halfHD.prototxt \
    --trt-modelfile ../../data/Model/GoogleNet_one_class/GoogleNet_modified_oneClass_halfHD.caffemodel \
    --trt-forcefp32 0 --trt-proc-interval 1 -fps 10
    
```    