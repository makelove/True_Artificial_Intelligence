## FFmpeg使用
- 参考
    - [使用FFmpeg将字幕文件集成到视频文件](http://www.yaosansi.com/post/ffmpeg-burn-subtitles-into-video/)

- macOS安装，支持字幕插件
    - brew install ffmpeg --with-fdk-aac --with-ffplay --with-freetype --with-libass --with-libquvi --with-libvorbis --with-libvpx --with-opus --with-x265
- Ubuntu安装
    - sudo apt install ffmpeg
    
- 使用
    - 合并字幕到视频里
        - ffmpeg -i video.avi -vf subtitles=subtitle.srt out.avi
    - 剪切视频
        - ffmpeg -i 1.mp4 -vf subtitles=1.srt -ss 10 -t 30 -acodec copy -vcodec copy  cut1.mp4
    - 合并字幕，同时剪切
        - ffmpeg -i Blue.Planet.II.S01E06.WEBRip.x264-RARBG.mp4 -vf subtitles=/Users/play/Desktop/Blue.Planet.II.S01E06.WEBRip.x264-RARBG.srt -ss 0 -t 120  33.mp4
    - 第二种是将字幕封装到容器中，就是所谓的字幕流，和视频流、音频流同等地位。值得说明的是，并非所有的容器都支持字幕流，先进的 MKV 是支持的，MP4 目前我只知道支持苹果的 MOV text。http://blog.csdn.net/u013699869/article/details/48162417
        - ffmpeg -i input.mkv -i subtitles.srt -c copy output.mkv
        - 查看 output.mkv 的信息，已经包含了字幕流，但不知为何播放视频时仍然不能显示字幕。
        - 从容器中提取字幕流，生成字幕文件（例子中生成的是 srt 格式的，可以任意生成所需的格式，改一下扩展名即可）：
            -ffmpeg -i input.mkv output.srt        