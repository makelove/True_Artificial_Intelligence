## 在virtualenv安装freenect库-python3
- 参考
    - https://github.com/OpenKinect/libfreenect
    - https://github.com/OpenKinect/libfreenect/tree/master/wrappers/python

- 安装,支持python3
```bash
cd github/
ls
git clone https://github.com/OpenKinect/libfreenect
cd libfreenect
mkdir build
cd build
cmake -L ..
#
BUILD_AS3_SERVER:BOOL=OFF
BUILD_CPACK_DEB:BOOL=OFF
BUILD_CPACK_RPM:BOOL=OFF
BUILD_CPACK_TGZ:BOOL=OFF
BUILD_CPP:BOOL=ON
BUILD_CV:BOOL=OFF
BUILD_C_SYNC:BOOL=ON
BUILD_EXAMPLES:BOOL=ON
BUILD_FAKENECT:BOOL=ON
BUILD_OPENNI2_DRIVER:BOOL=OFF
BUILD_PYTHON:BOOL=OFF
BUILD_PYTHON2:BOOL=OFF
BUILD_PYTHON3:BOOL=OFF
BUILD_REDIST_PACKAGE:BOOL=ON
CMAKE_BUILD_TYPE:STRING=
CMAKE_INSTALL_PREFIX:PATH=/usr/local
LIBUSB_1_INCLUDE_DIR:PATH=/usr/include/libusb-1.0
LIBUSB_1_LIBRARY:FILEPATH=/usr/lib/x86_64-linux-gnu/libusb-1.0.so
#

cmake .. -DCMAKE_BUILD_PYTHON3=ON
make
sudo make install

#python3
cd ../wrappers/python
python3 setup.py build_ext --inplace
#python3 -m 'import freenect' #不行
cp freenect.cpython-35m-x86_64-linux-gnu.so ~/.py3/lib/python3.5/site-packages/

#ipython
In [1]: import freenect

In [2]: freenect.__doc__

In [3]: freenect.__name__
Out[3]: 'freenect'

In [4]: freenect
Out[4]: <module 'freenect' from '/home/play/.py3/lib/python3.5/site-packages/freenect.cpython-35m-x86_64-linux-gnu.so'>
```