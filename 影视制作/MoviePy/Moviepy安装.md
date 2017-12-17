## Moviepy安装
- 参考
    - pypi 安装https://pypi.python.org/pypi/moviepy
    - GitHub：Video editing with Python  
        https://github.com/Zulko/moviepy
    - 文档 https://zulko.github.io/moviepy/
    
- 安装
    - pip install moviepy
    - git clone https://github.com/Zulko/moviepy.git
        - 设置FFmpeg路径
        - python setup.py install
- 测试
    - python setup.py test
- 安装 FFmpeg 
    - 不用下载，export FFMPEG_BINARY='/usr/local/bin/ffmpeg'
```python
import imageio
imageio.plugins.ffmpeg.download()
from moviepy.editor import *
```
- 安装 ImageMagick 
    - brew install imagemagick
    
