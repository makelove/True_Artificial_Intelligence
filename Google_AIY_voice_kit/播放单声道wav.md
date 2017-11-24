## 播放单声道wav 文件

- 使用FFmpeg
    - 树莓派apt安装的，不行，需要从源代码安装
        - [FFmpeg 在树莓派上的运行](http://blog.csdn.net/applelppa/article/details/25655335)
        - [树莓派安装ffmpeg（主要用于you-get视频的合并）](https://aoenian.github.io/2016/12/01/installFfmpegOnRasp/)
    - 使用
        - ffmpeg -i little_apple.mp3 -acodec pcm_s16le -ar 44100 -ac 1 little_apple2.wav
        - mono单声道，stereo双声道
```bash
(.py3) pro:wav_files play$ file  little_apple2.wav
little_apple2.wav: RIFF (little-endian) data, WAVE audio, Microsoft PCM, 16 bit, mono 44100 Hz
(.py3) pro:wav_files play$ file  little_apple.wav
little_apple.wav: RIFF (little-endian) data, WAVE audio, Microsoft PCM, 16 bit, stereo 44100 Hz
```

- python代码
```python
import aiy.audio
TEST_SOUND_PATH = '/usr/share/sounds/alsa/Front_Center.wav'
aiy.audio.play_wave(TEST_SOUND_PATH)
#
fl='../wav_files/running.wav'
aiy.audio.play_wave(fl)
#
fl='../wav_files/little_apple2.wav'
aiy.audio.play_wave(fl)
```