## python-vlc-安装-使用
- 参考
    - https://github.com/oaubert/python-vlc
- 安装
```bash
pip install vlc
sudo apt-get install libvlc-dev
sudo apt install vlc-nox
sudo apt-get install vlc browser-plugin-vlc
sudo apt-get install python-qt4
sudo apt-get install python3-pyqt4
```

- 把系统安装的包链接到虚拟环境virtualenv中
    - VLC
        - ln -s /usr/lib/python3/dist-packages/sip.cpython-35m-x86_64-linux-gnu.so  ~/.py3/lib/python3.5/site-packages/sip.cpython-35m-x86_64-linux-gnu.so
    - PyQt4
        - ln -s /usr/lib/python3/dist-packages/PyQt4  ~/.py3/lib/python3.5/site-packages/PyQt4
        
- 测试
    - git clone https://github.com/oaubert/python-vlc.git
    - python examples/tkvlc.py   
    - python examples/qtvlc.py   
    - 弹出一个播放器界面

- 代码
    - [How to Play Audio With VLC In Python](https://linuxconfig.org/how-to-play-audio-with-vlc-in-python)
```python
import vlc
player = vlc.MediaPlayer("奔跑.mp3")
player.play()
player.pause()
player.stop()
player.audio_set_volume(10)
player.audio_set_volume(70)
player.audio_set_volume(20)
player.audio_set_volume(40)
player.audio_set_volume(100)
player.audio_set_volume(200)
```    
- 播放视频
```python
vp=vlc.MediaPlayer("5111.mp4")
vp.play()# 不能弹出视频界面
'''
 [00007ff37544c648] core window error: corrupt module: /Applications/VLC.app/Contents/MacOS/plugins/lib
[00007ff377b0d2f8] macosx vout display error: No drawable-nsobject nor vout_window_t found, passing over.
[00007ff3763bf6b8] core video output error: video output creation failed
[00007ff37582dcb8] core decoder error: failed to create video output
'''
vp.stop()
```