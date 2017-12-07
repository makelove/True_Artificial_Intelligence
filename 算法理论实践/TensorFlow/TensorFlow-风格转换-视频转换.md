## TensorFlow-风格转换-视频转换
- 参考
    - https://github.com/lengstrom/fast-style-transfer
    - 模型下载https://drive.google.com/drive/folders/0B9jhaT37ydSyRk9UX0wwX3BpMzQ
-  实践
    - 下载模型
    - 转换图片
```bash
(.py3) nvidia@gpu:~/github/fast-style-transfer$ python evaluate.py --checkpoint examples/ckpt/rain_princess.ckpt --in-path examples/11-7/in --out-path examples/11-7/out/ --allow-different-dimensions
Processing images of shape 320x480x3
2017-12-07 18:27:19.624138: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:857] ARM64 does not support NUMA - returning NUMA node zero
2017-12-07 18:27:19.624325: I tensorflow/core/common_runtime/gpu/gpu_device.cc:955] Found device 0 with properties:
name: NVIDIA Tegra X2
major: 6 minor: 2 memoryClockRate (GHz) 1.3005
pciBusID 0000:00:00.0
Total memory: 7.67GiB
Free memory: 4.58GiB
2017-12-07 18:27:19.624388: I tensorflow/core/common_runtime/gpu/gpu_device.cc:976] DMA: 0
2017-12-07 18:27:19.624445: I tensorflow/core/common_runtime/gpu/gpu_device.cc:986] 0:   Y
2017-12-07 18:27:19.624488: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1045] Creating TensorFlow device (/gpu:0) -> (device: 0, name: NVIDIA Tegra X2, pci bus id: 0000:00:00.0)
Processing images of shape 208x370x3
2017-12-07 18:27:28.605136: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1045] Creating TensorFlow device (/gpu:0) -> (device: 0, name: NVIDIA Tegra X2, pci bus id: 0000:00:00.0)

```    


- 视频转换
```bash
(.py3) nvidia@gpu:~/github/fast-style-transfer$ python transform_video.py --in-path examples/11-7/video/in/banana.mp4  --checkpoint examples/ckpt/rain_princess.ckpt --out-path  examples/11-7/video/out_rain/banana.mp4 --device /gpu:0  --batch-size 10
ffmpeg version 2.8.11-0ubuntu0.16.04.1 Copyright (c) 2000-2017 the FFmpeg developers
  built with gcc 5.4.0 (Ubuntu/Linaro 5.4.0-6ubuntu1~16.04.4) 20160609
  configuration: --prefix=/usr --extra-version=0ubuntu0.16.04.1 --build-suffix=-ffmpeg --toolchain=hardened --libdir=/usr/lib/aarch64-linux-gnu --incdir=/usr/include/aarch64-linux-gnu --cc=cc --cxx=g++ --enable-gpl --enable-shared --disable-stripping --disable-decoder=libopenjpeg --disable-decoder=libschroedinger --enable-avresample --enable-avisynth --enable-gnutls --enable-ladspa --enable-libass --enable-libbluray --enable-libbs2b --enable-libcaca --enable-libcdio --enable-libflite --enable-libfontconfig --enable-libfreetype --enable-libfribidi --enable-libgme --enable-libgsm --enable-libmodplug --enable-libmp3lame --enable-libopenjpeg --enable-libopus --enable-libpulse --enable-librtmp --enable-libschroedinger --enable-libshine --enable-libsnappy --enable-libsoxr --enable-libspeex --enable-libssh --enable-libtheora --enable-libtwolame --enable-libvorbis --enable-libvpx --enable-libwavpack --enable-libwebp --enable-libx265 --enable-libxvid --enable-libzvbi --enable-openal --enable-opengl --enable-x11grab --enable-libdc1394 --enable-libiec61883 --enable-libzmq --enable-frei0r --enable-libx264 --enable-libopencv
  libavutil      54. 31.100 / 54. 31.100
  libavcodec     56. 60.100 / 56. 60.100
  libavformat    56. 40.101 / 56. 40.101
  libavdevice    56.  4.100 / 56.  4.100
  libavfilter     5. 40.101 /  5. 40.101
  libavresample   2.  1.  0 /  2.  1.  0
  libswscale      3.  1.101 /  3.  1.101
  libswresample   1.  2.101 /  1.  2.101
  libpostproc    53.  3.100 / 53.  3.100
Input #0, mov,mp4,m4a,3gp,3g2,mj2, from 'examples/11-7/video/in/banana.mp4':
  Metadata:
    major_brand     : mp42
    minor_version   : 1
    compatible_brands: mp41mp42isom
    creation_time   : 2017-12-07 10:40:08
  Duration: 00:00:10.04, start: 0.000000, bitrate: 1456 kb/s
    Stream #0:0(zho): Audio: aac (LC) (mp4a / 0x6134706D), 48000 Hz, stereo, fltp, 249 kb/s (default)
    Metadata:
      creation_time   : 2017-12-07 10:40:08
      handler_name    : Core Media Audio
    Stream #0:1(und): Video: h264 (High) (avc1 / 0x31637661), yuv420p(tv, bt709), 960x540 [SAR 1:1 DAR 16:9], 1151 kb/s, 25 fps, 25 tbr, 25 tbn, 50 tbc (default)
    Metadata:
      creation_time   : 2017-12-07 10:40:08
      handler_name    : Core Media Video
[swscaler @ 0x5db000] No accelerated colorspace conversion found from yuv420p to rgb24.
Output #0, image2, to '.fns_frames_14212/in/frame_%d.png':
  Metadata:
    major_brand     : mp42
    minor_version   : 1
    compatible_brands: mp41mp42isom
    encoder         : Lavf56.40.101
    Stream #0:0(und): Video: png, rgb24, 960x540 [SAR 1:1 DAR 16:9], q=2-31, 200 kb/s, 25 fps, 25 tbn, 25 tbc (default)
    Metadata:
      creation_time   : 2017-12-07 10:40:08
      handler_name    : Core Media Video
      encoder         : Lavc56.60.100 png
Stream mapping:
  Stream #0:1 -> #0:0 (h264 (native) -> png (native))
Press [q] to stop, [?] for help
frame=  251 fps= 66 q=-0.0 Lsize=N/A time=00:00:10.04 bitrate=N/A
video:114828kB audio:0kB subtitle:0kB other streams:0kB global headers:0kB muxing overhead: unknown
2017-12-07 18:44:11.071928: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:857] ARM64 does not support NUMA - returning NUMA node zero
2017-12-07 18:44:11.072119: I tensorflow/core/common_runtime/gpu/gpu_device.cc:955] Found device 0 with properties:
name: NVIDIA Tegra X2
major: 6 minor: 2 memoryClockRate (GHz) 1.3005
pciBusID 0000:00:00.0
Total memory: 7.67GiB
Free memory: 4.38GiB
2017-12-07 18:44:11.072171: I tensorflow/core/common_runtime/gpu/gpu_device.cc:976] DMA: 0
2017-12-07 18:44:11.072216: I tensorflow/core/common_runtime/gpu/gpu_device.cc:986] 0:   Y
2017-12-07 18:44:11.072263: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1045] Creating TensorFlow device (/gpu:0) -> (device: 0, name: NVIDIA Tegra X2, pci bus id: 0000:00:00.0)
2017-12-07 18:44:21.237245: W tensorflow/core/common_runtime/bfc_allocator.cc:217] Allocator (GPU_0_bfc) ran out of memory trying to allocate 1.39GiB. The caller indicates that this is not a failure, but may mean that there could be performance gains if more memory is available.
2017-12-07 18:48:52.175572: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1045] Creating TensorFlow device (/gpu:0) -> (device: 0, name: NVIDIA Tegra X2, pci bus id: 0000:00:00.0)
ffmpeg version 2.8.11-0ubuntu0.16.04.1 Copyright (c) 2000-2017 the FFmpeg developers
  built with gcc 5.4.0 (Ubuntu/Linaro 5.4.0-6ubuntu1~16.04.4) 20160609
  configuration: --prefix=/usr --extra-version=0ubuntu0.16.04.1 --build-suffix=-ffmpeg --toolchain=hardened --libdir=/usr/lib/aarch64-linux-gnu --incdir=/usr/include/aarch64-linux-gnu --cc=cc --cxx=g++ --enable-gpl --enable-shared --disable-stripping --disable-decoder=libopenjpeg --disable-decoder=libschroedinger --enable-avresample --enable-avisynth --enable-gnutls --enable-ladspa --enable-libass --enable-libbluray --enable-libbs2b --enable-libcaca --enable-libcdio --enable-libflite --enable-libfontconfig --enable-libfreetype --enable-libfribidi --enable-libgme --enable-libgsm --enable-libmodplug --enable-libmp3lame --enable-libopenjpeg --enable-libopus --enable-libpulse --enable-librtmp --enable-libschroedinger --enable-libshine --enable-libsnappy --enable-libsoxr --enable-libspeex --enable-libssh --enable-libtheora --enable-libtwolame --enable-libvorbis --enable-libvpx --enable-libwavpack --enable-libwebp --enable-libx265 --enable-libxvid --enable-libzvbi --enable-openal --enable-opengl --enable-x11grab --enable-libdc1394 --enable-libiec61883 --enable-libzmq --enable-frei0r --enable-libx264 --enable-libopencv
  libavutil      54. 31.100 / 54. 31.100
  libavcodec     56. 60.100 / 56. 60.100
  libavformat    56. 40.101 / 56. 40.101
  libavdevice    56.  4.100 / 56.  4.100
  libavfilter     5. 40.101 /  5. 40.101
  libavresample   2.  1.  0 /  2.  1.  0
  libswscale      3.  1.101 /  3.  1.101
  libswresample   1.  2.101 /  1.  2.101
  libpostproc    53.  3.100 / 53.  3.100
Input #0, image2, from '.fns_frames_14212/out/frame_%d.png':
  Duration: 00:00:10.04, start: 0.000000, bitrate: N/A
    Stream #0:0: Video: png, rgb24(pc), 960x540, 25 fps, 25 tbr, 25 tbn, 25 tbc
Output #0, mp4, to 'examples/11-7/video/out_rain/banana.mp4':
  Metadata:
    encoder         : Lavf56.40.101
    Stream #0:0: Video: mpeg4 ( [0][0][0] / 0x0020), yuv420p, 960x540, q=2-31, 200 kb/s, 30 fps, 15360 tbn, 30 tbc
    Metadata:
      encoder         : Lavc56.60.100 mpeg4
Stream mapping:
  Stream #0:0 -> #0:0 (png (native) -> mpeg4 (native))
Press [q] to stop, [?] for help
frame=  301 fps= 37 q=0.0 Lsize=   29591kB time=00:00:10.03 bitrate=24160.8kbits/s dup=50 drop=0
video:29589kB audio:0kB subtitle:0kB other streams:0kB global headers:0kB muxing overhead: 0.008505%
Video at: examples/11-7/video/out_rain/banana.mp4
```
- 结果
    - [TensorFlow视频+风格转换-小黄人抢香蕉](https://www.bilibili.com/video/av17031324/) ，Youtube:https://www.youtube.com/watch?v=fdaoeybBr5c
    - ![Minions-banana.jpg](Minions-banana.jpg)