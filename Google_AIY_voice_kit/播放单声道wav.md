## 播放单声道wav 文件

- 使用FFmpeg
    - 树莓派apt安装的，不行，需要从源代码安装
        - [FFmpeg 在树莓派上的运行](http://blog.csdn.net/applelppa/article/details/25655335)
        - [树莓派安装ffmpeg（主要用于you-get视频的合并）](https://aoenian.github.io/2016/12/01/installFfmpegOnRasp/)
    - 使用
        - ffmpeg -i little_apple.mp3 -acodec pcm_s16le -ar 44100 -ac 1 little_apple2.wav
