## Moviepy使用


- 环境
    - macOS
    - python3.6 虚拟环境
    - 
    
- 添加字幕到视频
```python
from moviepy.editor import *
from moviepy.video.tools.subtitles import SubtitlesClip

#
# font="Liberation-Sans-Bold"
font="ArialUnicode"# 只有这个支持中文
generator = lambda txt: TextClip(txt, font=font, fontsize=16, color='red')
subtitles = SubtitlesClip("earth.srt",generator)
#字幕截图
subtitles.save_frame('jfkd2621.png',t=26)

#
video = VideoFileClip("Earth from Space - Orange County-oR1zHoC1_UQ.mp4")
result = CompositeVideoClip([video, subtitles.set_pos(('center','bottom'))])

result.write_videofile("out2.mp4", fps=video.fps,  remove_temp=True, codec="libx264", audio_codec="aac")

#视频截图，带字幕
result.save_frame('jfkd26.png',t=26)

#找出哪个font字体支持中文
from moviepy import editor
for x in editor.TextClip.list('font'):
    generator = lambda txt: TextClip(txt, font=x, fontsize=16, color='red')
    subtitles = SubtitlesClip("earth.srt",generator)
    subtitles.save_frame(x+'.png',t=26)
#列举所有支持的颜色
editor.TextClip.list('color')    

#根据字幕时间轴来截图
from datetime import timedelta
import pysrt
subs=pysrt.open("/Users/play/big3.srt")
#
for i, sub in enumerate(subs[160:170]):
    start=sub.start.to_time()
    t=sub.end.to_time()
    dt=timedelta(hours=t.hour,minutes=t.minute,seconds=t.second)
    dts=timedelta(hours=start.hour,minutes=start.minute,seconds=start.second)
    seconds=int((dt.seconds+dts.seconds)/2)
    result.save_frame(str(seconds)+'.png',t=seconds)
#     print(sub.index,sub.start.ordinal,sub.start.seconds,sub.end.seconds,sub.end.to_time(),sub.text)

```    
- 注意
    - 有些国内字幕是无效的，在moviepy内不能使用，需要ffmpeg进行转换
        - ffmpeg -i big.srt big3.srt