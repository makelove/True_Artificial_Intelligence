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