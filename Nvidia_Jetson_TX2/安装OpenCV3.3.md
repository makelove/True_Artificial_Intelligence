## 安装OpenCV3.3

- 参考
    - https://github.com/jetsonhacks/buildOpenCVTX2/blob/master/buildOpenCV.sh
    - https://www.pyimagesearch.com/2015/07/20/install-opencv-3-0-and-python-3-4-on-ubuntu/
    
- 编译，支持python2.7和python3.5
```bash
cmake \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DBUILD_PNG=OFF \
    -DBUILD_TIFF=OFF \
    -DBUILD_TBB=OFF \
    -DBUILD_JPEG=OFF \
    -DBUILD_JASPER=OFF \
    -DBUILD_ZLIB=OFF \
    -DBUILD_EXAMPLES=ON \
    -DBUILD_opencv_java=OFF \
    -DBUILD_opencv_python2=ON \
    -DBUILD_opencv_python3=ON \
    -DENABLE_PRECOMPILED_HEADERS=OFF \
    -DWITH_OPENCL=OFF \
    -DWITH_OPENMP=OFF \
    -DWITH_FFMPEG=ON \
    -DWITH_GSTREAMER=ON \
    -DWITH_GSTREAMER_0_10=OFF \
    -DWITH_CUDA=ON \
    -DWITH_GTK=ON \
    -DWITH_VTK=OFF \
    -DWITH_TBB=ON \
    -DWITH_1394=OFF \
    -DWITH_OPENEXR=OFF \
    -DCUDA_TOOLKIT_ROOT_DIR=/usr/local/cuda-8.0 \
    -DCUDA_ARCH_BIN=6.2 \
    -DCUDA_ARCH_PTX="" \
    -DINSTALL_C_EXAMPLES=ON \
    -DINSTALL_TESTS=ON \
    -DOPENCV_TEST_DATA_PATH=../opencv_extra/testdata \
    ../
    
make -j4
sudo make install
sudo ldconfig    
#
cd .py3/lib/python3.5/site-packages/
ln -s /usr/lib/python3.5/dist-packages/cv2.cpython-35m-aarch64-linux-gnu.so cv2.so
#
#在.bashrc还要取消ros setup.sh,因为ROS也有opencv包
#source /opt/ros/kinetic/setup.bash
然后ipython3
In [1]: import cv2
In [2]: cv2
Out[2]: <module 'cv2' from '/home/nvidia/.py3/lib/python3.5/site-packages/cv2.so'>
```    
- 案例 /usr/share/OpenCV/samples/
- 测试数据 /usr/share/OpenCV/testdata

## 测试 
- https://github.com/jetsonhacks/buildOpenCVTX2/tree/master/Examples
    - cannyDetection.py
    - gstreamer_view.cpp