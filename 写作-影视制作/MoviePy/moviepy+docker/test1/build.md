- 构建
    - docker build -t play4fun/u1604py36:0.1 -f Dockerfile_ubuntu16.04_py36 .
    - docker build -t play4fun/moviepy_opencv:0.1 -f Dockerfile .
    - docker build -t play4fun/moviepy_opencv_ffmpeg:0.1 -f Dockerfile_ffmpeg .
    
```bash
(.py3) pro:test1 play$ docker build -t play4fun/u1604py36:0.1 -f Dockerfile_ubuntu16.04_py36 .
Sending build context to Docker daemon  17.92kB
Step 1/9 : FROM ubuntu:16.04
 ---> 00fd29ccc6f1
Step 2/9 : RUN apt-get update
 ---> Running in 1585caa98e91
Get:1 http://security.ubuntu.com/ubuntu xenial-security InRelease [102 kB]
Get:2 http://archive.ubuntu.com/ubuntu xenial InRelease [247 kB]
Get:3 http://security.ubuntu.com/ubuntu xenial-security/universe Sources [56.7 kB]


Step 10/10 : RUN apt-get autoremove -y; apt-get clean -y
 ---> Running in f2572ab21b96
Reading package lists...
Building dependency tree...
Reading state information...
0 upgraded, 0 newly installed, 0 to remove and 0 not upgraded.
 ---> 7b444229214e
Removing intermediate container f2572ab21b96
Successfully built 7b444229214e
Successfully tagged play4fun/u1604py36:0.1
(.py3) pro:test1 play$
```    

    
```bash
(.py3) pro:test1 play$ docker build -t play4fun/moviepy_opencv:0.1 -f Dockerfile .
Sending build context to Docker daemon  14.34kB
Step 1/6 : FROM python:3.6
 ---> c1e459c00dc3
Step 2/6 : WORKDIR /usr/src/app
 ---> Using cache
 ---> e778785a89b7
Step 3/6 : COPY requirements.txt ./
 ---> Using cache
 ---> 316bab18e96e
Step 4/6 : RUN pip3 install -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com --no-cache-dir -r requirements.txt
 ---> Running in 29ceb006db52
Collecting Cython (from -r requirements.txt (line 1))


Successfully installed Automat-0.6.0 Cython-0.27.3 Flask-0.12.2 Jinja2-2.10 Keras-2.1.2 MarkupSafe-1.0 Pillow-4.3.0 PyDispatcher-2.0.5 Scrapy-1.4.0 Twisted-17.9.0 Werkzeug-0.13 asn1crypto-0.24.0 attrs-17.3.0 beautifulsoup4-4.6.0 bleach-2.1.2 cffi-1.11.2 chardet-3.0.4 click-6.7 constantly-15.1.0 cryptography-2.1.4 cssselect-1.0.1 cycler-0.10.0 decorator-4.1.2 entrypoints-0.2.3 enum34-1.1.6 h5py-2.7.1 html5lib-0.9999999 hyperlink-17.3.1 idna-2.6 imageio-2.1.2 imutils-0.4.4 incremental-17.5.0 ipykernel-4.7.0 ipython-6.2.1 ipython-genutils-0.2.0 ipywidgets-7.0.5 itsdangerous-0.24 jedi-0.11.1 jsonschema-2.6.0 jupyter-1.0.0 jupyter-client-5.2.0 jupyter-console-5.2.0 jupyter-core-4.4.0 lxml-4.1.1 markdown-2.6.10 matplotlib-2.1.1 mistune-0.8.3 moviepy-0.2.3.2 nbconvert-5.3.1 nbformat-4.4.0 notebook-5.2.2 numpy-1.13.3 olefile-0.44 opencv-contrib-python-3.3.0.10 pandas-0.21.1 pandocfilters-1.4.2 parsel-1.2.0 parso-0.1.1 pexpect-4.3.1 pickleshare-0.7.4 pluggy-0.6.0 prompt-toolkit-1.0.15 protobuf-3.5.0.post1 ptyprocess-0.5.2 py-1.5.2 pyOpenSSL-17.5.0 pyasn1-0.4.2 pyasn1-modules-0.2.1 pycparser-2.18 pygments-2.2.0 pymongo-3.6.0 pyparsing-2.2.0 pysrt-1.1.1 pytest-3.3.1 python-dateutil-2.6.1 pytz-2017.3 pyyaml-3.12 pyzmq-16.0.3 qtconsole-4.3.1 queuelib-1.4.2 scikit-learn-0.19.1 scipy-1.0.0 service-identity-17.0.0 simplegeneric-0.8.1 six-1.11.0 tensorflow-1.4.1 tensorflow-tensorboard-0.4.0rc3 terminado-0.8.1 testpath-0.3.1 tornado-4.5.2 tqdm-4.11.2 traitlets-4.3.2 w3lib-1.18.0 wcwidth-0.1.7 widgetsnbextension-3.0.8 youtube-dl-2017.12.14 zope.interface-4.4.3
 ---> 1ff291b049dc
Removing intermediate container 29ceb006db52
Step 5/6 : RUN mkdir /work
 ---> Running in 389f63b0f720
 ---> 7ac932403fe3
Removing intermediate container 389f63b0f720
Step 6/6 : WORKDIR /work
 ---> 082bc8e6bf71
Removing intermediate container 18f4106fb0a4
Successfully built 082bc8e6bf71
Successfully tagged play4fun/moviepy_opencv:0.1
(.py3) pro:test1 play$
```    

- 测试运行
    - docker run -it play4fun/u1604py36:0.1 bash
    - docker run -it play4fun/moviepy_opencv_ffmpeg:0.1 bash
    - docker run -it play4fun/moviepy_opencv:0.1 env LANG=C.UTF-8 bash
    - env LANG=C.UTF-8
    - 目录映射 
        - docker run -it -v /Users/xxx/Docker_test:/work play4fun/moviepy_opencv:0.1 env LANG=C.UTF-8 bash


- 时区支持
    - RUN  echo "Asia/Shanghai" > /etc/timezone
    - RUN  dpkg-reconfigure -f noninteractive tzdata
    - dpkg-reconfigure --frontend noninteractive tzdata