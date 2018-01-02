FROM ampervue/ffmpeg

# https://github.com/ampervue/docker-ffmpeg-moviepy
# https://hub.docker.com/r/dkarchmervue/moviepy/

MAINTAINER David Karchmer <dkarchmer@ampervue.com>

#####################################################################
#
# A Docker image with everything needed to run Moviepy scripts
#
# Image based on https://github.com/ampervue/docker-ffmpeg
#
#   with
#     - Latest Python 3.4
#     - Latest FFMPEG (built)
#     - ImageMagick, Numpy, Scipy and other requirements for moviepy
#
#   For more on Moviepy, see http://zulko.github.io/moviepy/
#
#   plus a bunch of build/web essentials
#
#####################################################################

#ENV NUM_CORES 4

#ENV MOVIEPY_VERSION 0.2.2.11 - Building from source due to issue 237
ENV NUMPY_VERSION 1.10.4
# Pillow 3 is not compatible with MoviePy
# https://github.com/Zulko/moviepy/issues/241
ENV PILLOW_VERSION 2.8.1
ENV SCIPY_VERSION 0.17.0

RUN locale-gen en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

# Install moviepy and related packages
# ====================================
RUN pip install -U numpy==$NUMPY_VERSION
RUN pip install -U Pillow==$PILLOW_VERSION
RUN pip install -U scipy==$SCIPY_VERSION
#RUN pip install -U moviepy==$MOVIEPY_VERSION

ENV FFMPEG_BINARY ffmpeg
ENV IMAGEMAGICK_BINARY convert
# Manually build version that allows control of FFMPEG exe
# See https://github.com/Zulko/moviepy/issues/237
# Use PIP when issue fixed. For now, change the defaults
# manually
RUN pip install tqdm

WORKDIR /usr/local/src
RUN git clone -q https://github.com/Zulko/moviepy.git
WORKDIR /usr/local/src/moviepy
#ADD config_defaults.py moviepy/config_defaults.py
RUN sudo python setup.py install

# Remove all tmpfile and cleanup
# =================================
WORKDIR /usr/local/
RUN rm -rf /usr/local/src
# =================================

# Setup a working directory to allow for
# docker run --rm -ti -v ${PWD}:/code ...
# =======================================
WORKDIR /work
