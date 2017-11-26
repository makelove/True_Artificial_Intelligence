```bash


nvidia@gpu:~$ cd opencv/build/

nvidia@gpu:~/opencv/build$ cmake \
>     -DCMAKE_BUILD_TYPE=Release \
>     -DCMAKE_INSTALL_PREFIX=/usr \
>     -DBUILD_PNG=OFF \
>     -DBUILD_TIFF=OFF \
>     -DBUILD_TBB=OFF \
>     -DBUILD_JPEG=OFF \
>     -DBUILD_JASPER=OFF \
>     -DBUILD_ZLIB=OFF \
>     -DBUILD_EXAMPLES=ON \
>     -DBUILD_opencv_java=OFF \
>     -DBUILD_opencv_python2=ON \
>     -DBUILD_opencv_python3=ON \
>     -DENABLE_PRECOMPILED_HEADERS=OFF \
>     -DWITH_OPENCL=OFF \
>     -DWITH_OPENMP=OFF \
>     -DWITH_FFMPEG=ON \
>     -DWITH_GSTREAMER=ON \
>     -DWITH_GSTREAMER_0_10=OFF \
>     -DWITH_CUDA=ON \
>     -DWITH_GTK=ON \
>     -DWITH_VTK=OFF \
>     -DWITH_TBB=ON \
>     -DWITH_1394=OFF \
>     -DWITH_OPENEXR=OFF \
>     -DCUDA_TOOLKIT_ROOT_DIR=/usr/local/cuda-8.0 \
>     -DCUDA_ARCH_BIN=6.2 \
>     -DCUDA_ARCH_PTX="" \
>     -DINSTALL_C_EXAMPLES=ON \
>     -DINSTALL_TESTS=ON \
>     -DOPENCV_TEST_DATA_PATH=../opencv_extra/testdata \
>     ../
-- The CXX compiler identification is GNU 5.4.0
-- The C compiler identification is GNU 5.4.0
-- Check for working CXX compiler: /usr/bin/c++
-- Check for working CXX compiler: /usr/bin/c++ -- works
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Check for working C compiler: /usr/bin/cc
-- Check for working C compiler: /usr/bin/cc -- works
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Detecting C compile features
-- Detecting C compile features - done
-- Detected version of GNU GCC: 54 (504)
-- Performing Test HAVE_CXX11 (check file: cmake/checks/cxx11.cpp)
-- Performing Test HAVE_CXX11 - Failed
-- Found PythonInterp: /usr/bin/python2.7 (found suitable version "2.7.12", minimum required is "2.7") 
-- Found PythonLibs: /usr/lib/aarch64-linux-gnu/libpython2.7.so (found suitable exact version "2.7.12") 
-- Found PythonInterp: /usr/bin/python3 (found suitable version "3.5.2", minimum required is "3.4") 
-- Found PythonLibs: /usr/lib/aarch64-linux-gnu/libpython3.5m.so (found suitable exact version "3.5.2") 
-- Looking for ccache - not found
-- Performing Test HAVE_CXX_FSIGNED_CHAR
-- Performing Test HAVE_CXX_FSIGNED_CHAR - Success
-- Performing Test HAVE_C_FSIGNED_CHAR
-- Performing Test HAVE_C_FSIGNED_CHAR - Success
-- Performing Test HAVE_CXX_W
-- Performing Test HAVE_CXX_W - Success
-- Performing Test HAVE_C_W
-- Performing Test HAVE_C_W - Success
-- Performing Test HAVE_CXX_WALL
-- Performing Test HAVE_CXX_WALL - Success
-- Performing Test HAVE_C_WALL
-- Performing Test HAVE_C_WALL - Success
-- Performing Test HAVE_CXX_WERROR_RETURN_TYPE
-- Performing Test HAVE_CXX_WERROR_RETURN_TYPE - Success
-- Performing Test HAVE_C_WERROR_RETURN_TYPE
-- Performing Test HAVE_C_WERROR_RETURN_TYPE - Success
-- Performing Test HAVE_CXX_WERROR_NON_VIRTUAL_DTOR
-- Performing Test HAVE_CXX_WERROR_NON_VIRTUAL_DTOR - Success
-- Performing Test HAVE_C_WERROR_NON_VIRTUAL_DTOR
-- Performing Test HAVE_C_WERROR_NON_VIRTUAL_DTOR - Success
-- Performing Test HAVE_CXX_WERROR_ADDRESS
-- Performing Test HAVE_CXX_WERROR_ADDRESS - Success
-- Performing Test HAVE_C_WERROR_ADDRESS
-- Performing Test HAVE_C_WERROR_ADDRESS - Success
-- Performing Test HAVE_CXX_WERROR_SEQUENCE_POINT
-- Performing Test HAVE_CXX_WERROR_SEQUENCE_POINT - Success
-- Performing Test HAVE_C_WERROR_SEQUENCE_POINT
-- Performing Test HAVE_C_WERROR_SEQUENCE_POINT - Success
-- Performing Test HAVE_CXX_WFORMAT
-- Performing Test HAVE_CXX_WFORMAT - Success
-- Performing Test HAVE_C_WFORMAT
-- Performing Test HAVE_C_WFORMAT - Success
-- Performing Test HAVE_CXX_WERROR_FORMAT_SECURITY
-- Performing Test HAVE_CXX_WERROR_FORMAT_SECURITY - Success
-- Performing Test HAVE_C_WERROR_FORMAT_SECURITY
-- Performing Test HAVE_C_WERROR_FORMAT_SECURITY - Success
-- Performing Test HAVE_CXX_WMISSING_DECLARATIONS
-- Performing Test HAVE_CXX_WMISSING_DECLARATIONS - Success
-- Performing Test HAVE_C_WMISSING_DECLARATIONS
-- Performing Test HAVE_C_WMISSING_DECLARATIONS - Success
-- Performing Test HAVE_CXX_WMISSING_PROTOTYPES
-- Performing Test HAVE_CXX_WMISSING_PROTOTYPES - Failed
-- Performing Test HAVE_C_WMISSING_PROTOTYPES
-- Performing Test HAVE_C_WMISSING_PROTOTYPES - Success
-- Performing Test HAVE_CXX_WSTRICT_PROTOTYPES
-- Performing Test HAVE_CXX_WSTRICT_PROTOTYPES - Failed
-- Performing Test HAVE_C_WSTRICT_PROTOTYPES
-- Performing Test HAVE_C_WSTRICT_PROTOTYPES - Success
-- Performing Test HAVE_CXX_WUNDEF
-- Performing Test HAVE_CXX_WUNDEF - Success
-- Performing Test HAVE_C_WUNDEF
-- Performing Test HAVE_C_WUNDEF - Success
-- Performing Test HAVE_CXX_WINIT_SELF
-- Performing Test HAVE_CXX_WINIT_SELF - Success
-- Performing Test HAVE_C_WINIT_SELF
-- Performing Test HAVE_C_WINIT_SELF - Success
-- Performing Test HAVE_CXX_WPOINTER_ARITH
-- Performing Test HAVE_CXX_WPOINTER_ARITH - Success
-- Performing Test HAVE_C_WPOINTER_ARITH
-- Performing Test HAVE_C_WPOINTER_ARITH - Success
-- Performing Test HAVE_CXX_WSHADOW
-- Performing Test HAVE_CXX_WSHADOW - Success
-- Performing Test HAVE_C_WSHADOW
-- Performing Test HAVE_C_WSHADOW - Success
-- Performing Test HAVE_CXX_WSIGN_PROMO
-- Performing Test HAVE_CXX_WSIGN_PROMO - Success
-- Performing Test HAVE_C_WSIGN_PROMO
-- Performing Test HAVE_C_WSIGN_PROMO - Failed
-- Performing Test HAVE_CXX_WUNINITIALIZED
-- Performing Test HAVE_CXX_WUNINITIALIZED - Success
-- Performing Test HAVE_C_WUNINITIALIZED
-- Performing Test HAVE_C_WUNINITIALIZED - Success
-- Performing Test HAVE_CXX_WNO_NARROWING
-- Performing Test HAVE_CXX_WNO_NARROWING - Success
-- Performing Test HAVE_C_WNO_NARROWING
-- Performing Test HAVE_C_WNO_NARROWING - Success
-- Performing Test HAVE_CXX_WNO_DELETE_NON_VIRTUAL_DTOR
-- Performing Test HAVE_CXX_WNO_DELETE_NON_VIRTUAL_DTOR - Success
-- Performing Test HAVE_C_WNO_DELETE_NON_VIRTUAL_DTOR
-- Performing Test HAVE_C_WNO_DELETE_NON_VIRTUAL_DTOR - Failed
-- Performing Test HAVE_CXX_WNO_UNNAMED_TYPE_TEMPLATE_ARGS
-- Performing Test HAVE_CXX_WNO_UNNAMED_TYPE_TEMPLATE_ARGS - Failed
-- Performing Test HAVE_C_WNO_UNNAMED_TYPE_TEMPLATE_ARGS
-- Performing Test HAVE_C_WNO_UNNAMED_TYPE_TEMPLATE_ARGS - Failed
-- Performing Test HAVE_CXX_WNO_COMMENT
-- Performing Test HAVE_CXX_WNO_COMMENT - Success
-- Performing Test HAVE_C_WNO_COMMENT
-- Performing Test HAVE_C_WNO_COMMENT - Success
-- Performing Test HAVE_CXX_FDIAGNOSTICS_SHOW_OPTION
-- Performing Test HAVE_CXX_FDIAGNOSTICS_SHOW_OPTION - Success
-- Performing Test HAVE_C_FDIAGNOSTICS_SHOW_OPTION
-- Performing Test HAVE_C_FDIAGNOSTICS_SHOW_OPTION - Success
-- Performing Test HAVE_CXX_PTHREAD
-- Performing Test HAVE_CXX_PTHREAD - Success
-- Performing Test HAVE_C_PTHREAD
-- Performing Test HAVE_C_PTHREAD - Success
-- Performing Test HAVE_CXX_FOMIT_FRAME_POINTER
-- Performing Test HAVE_CXX_FOMIT_FRAME_POINTER - Success
-- Performing Test HAVE_C_FOMIT_FRAME_POINTER
-- Performing Test HAVE_C_FOMIT_FRAME_POINTER - Success
-- Performing Test HAVE_CXX_FFUNCTION_SECTIONS
-- Performing Test HAVE_CXX_FFUNCTION_SECTIONS - Success
-- Performing Test HAVE_C_FFUNCTION_SECTIONS
-- Performing Test HAVE_C_FFUNCTION_SECTIONS - Success
-- Performing Test HAVE_CPU_NEON_SUPPORT (check file: cmake/checks/cpu_neon.cpp)
-- Performing Test HAVE_CPU_NEON_SUPPORT - Success
-- Performing Test HAVE_CPU_FP16_SUPPORT (check file: cmake/checks/cpu_fp16.cpp)
-- Performing Test HAVE_CPU_FP16_SUPPORT - Success
-- Performing Test HAVE_CPU_BASELINE_FLAGS
-- Performing Test HAVE_CPU_BASELINE_FLAGS - Success
-- Performing Test HAVE_CXX_FVISIBILITY_HIDDEN
-- Performing Test HAVE_CXX_FVISIBILITY_HIDDEN - Success
-- Performing Test HAVE_C_FVISIBILITY_HIDDEN
-- Performing Test HAVE_C_FVISIBILITY_HIDDEN - Success
-- Performing Test HAVE_CXX_FVISIBILITY_INLINES_HIDDEN
-- Performing Test HAVE_CXX_FVISIBILITY_INLINES_HIDDEN - Success
-- Performing Test HAVE_C_FVISIBILITY_INLINES_HIDDEN
-- Performing Test HAVE_C_FVISIBILITY_INLINES_HIDDEN - Failed
-- Looking for pthread.h
-- Looking for pthread.h - found
-- Looking for posix_memalign
-- Looking for posix_memalign - found
-- Looking for malloc.h
-- Looking for malloc.h - found
-- Looking for memalign
-- Looking for memalign - found
-- Check if the system is big endian
-- Searching 16 bit integer
-- Looking for sys/types.h
-- Looking for sys/types.h - found
-- Looking for stdint.h
-- Looking for stdint.h - found
-- Looking for stddef.h
-- Looking for stddef.h - found
-- Check size of unsigned short
-- Check size of unsigned short - done
-- Using unsigned short
-- Check if the system is big endian - little endian
-- Found ZLIB: /usr/lib/aarch64-linux-gnu/libz.so (found suitable version "1.2.8", minimum required is "1.2.3") 
-- Found TIFF: /usr/lib/aarch64-linux-gnu/libtiff.so (found version "4.0.6") 
-- Found JPEG: /usr/lib/aarch64-linux-gnu/libjpeg.so  
-- Found WebP: /usr/lib/aarch64-linux-gnu/libwebp.so  
-- Found Jasper: /usr/lib/aarch64-linux-gnu/libjasper.so (found version "1.900.1") 
-- Found ZLIB: /usr/lib/aarch64-linux-gnu/libz.so (found version "1.2.8") 
-- Found PNG: /usr/lib/aarch64-linux-gnu/libpng.so (found version "1.2.54") 
-- Looking for /usr/include/libpng/png.h
-- Looking for /usr/include/libpng/png.h - found
-- Checking for module 'gtk+-3.0'
--   No package 'gtk+-3.0' found
-- Checking for module 'gtk+-2.0'
--   Found gtk+-2.0, version 2.24.30
-- Checking for module 'gthread-2.0'
--   Found gthread-2.0, version 2.48.1
-- Checking for module 'gstreamer-base-1.0'
--   Found gstreamer-base-1.0, version 1.8.3
-- Checking for module 'gstreamer-video-1.0'
--   Found gstreamer-video-1.0, version 1.8.3
-- Checking for module 'gstreamer-app-1.0'
--   Found gstreamer-app-1.0, version 1.8.3
-- Checking for module 'gstreamer-riff-1.0'
--   Found gstreamer-riff-1.0, version 1.8.3
-- Checking for module 'gstreamer-pbutils-1.0'
--   Found gstreamer-pbutils-1.0, version 1.8.3
-- Looking for linux/videodev.h
-- Looking for linux/videodev.h - not found
-- Looking for linux/videodev2.h
-- Looking for linux/videodev2.h - found
-- Looking for sys/videoio.h
-- Looking for sys/videoio.h - not found
-- Checking for modules 'libavcodec;libavformat;libavutil;libswscale'
--   Found libavcodec, version 56.60.100
--   Found libavformat, version 56.40.101
--   Found libavutil, version 54.31.100
--   Found libswscale, version 3.1.101
-- Checking for module 'libavresample'
--   No package 'libavresample' found
-- Checking for module 'libgphoto2'
--   No package 'libgphoto2' found
-- Found TBB: /usr/lib/aarch64-linux-gnu/libtbb.so
-- CUDA detected: 8.0
-- CUDA NVCC target flags: -gencode;arch=compute_62,code=sm_62;-D_FORCE_INLINES
-- Could not find OpenBLAS lib. Turning OpenBLAS_FOUND off
-- Could NOT find Atlas (missing:  Atlas_CLAPACK_INCLUDE_DIR) 
-- Looking for dgemm_
-- Looking for dgemm_ - found
-- Looking for pthread.h
-- Looking for pthread.h - found
-- Looking for pthread_create
-- Looking for pthread_create - found
-- Found Threads: TRUE  
-- A library with BLAS API found.
-- Looking for cheev_
-- Looking for cheev_ - found
-- A library with LAPACK API found.
-- Could NOT find Doxygen (missing:  DOXYGEN_EXECUTABLE) 
-- Could NOT find JNI (missing:  JAVA_AWT_LIBRARY JAVA_JVM_LIBRARY JAVA_INCLUDE_PATH JAVA_INCLUDE_PATH2 JAVA_AWT_INCLUDE_PATH) 
-- Could NOT find Matlab (missing:  MATLAB_MEX_SCRIPT MATLAB_INCLUDE_DIRS MATLAB_ROOT_DIR MATLAB_LIBRARIES MATLAB_LIBRARY_DIRS MATLAB_MEXEXT MATLAB_ARCH MATLAB_BIN) 
-- Performing Test CXX_HAS_MFPU_NEON
-- Performing Test CXX_HAS_MFPU_NEON - Failed
-- Performing Test C_HAS_MFPU_NEON
-- Performing Test C_HAS_MFPU_NEON - Failed
-- Performing Test HAVE_CXX_WNO_UNDEF
-- Performing Test HAVE_CXX_WNO_UNDEF - Success
-- Performing Test HAVE_CXX_WNO_MISSING_DECLARATIONS
-- Performing Test HAVE_CXX_WNO_MISSING_DECLARATIONS - Success
-- Performing Test HAVE_CXX_WNO_SHADOW
-- Performing Test HAVE_CXX_WNO_SHADOW - Success
-- Performing Test HAVE_CXX_WNO_UNUSED_PARAMETER
-- Performing Test HAVE_CXX_WNO_UNUSED_PARAMETER - Success
-- Performing Test HAVE_CXX_WNO_UNINITIALIZED
-- Performing Test HAVE_CXX_WNO_UNINITIALIZED - Success
-- Performing Test HAVE_CXX_WNO_UNUSED_FUNCTION
-- Performing Test HAVE_CXX_WNO_UNUSED_FUNCTION - Success
-- Performing Test HAVE_CXX_WNO_UNUSED_VARIABLE
-- Performing Test HAVE_CXX_WNO_UNUSED_VARIABLE - Success
-- Performing Test HAVE_CXX_WNO_ENUM_COMPARE
-- Performing Test HAVE_CXX_WNO_ENUM_COMPARE - Success
-- Looking for include file pthread.h
-- Looking for include file pthread.h - found
-- Performing Test HAVE_CXX_WNO_DEPRECATED
-- Performing Test HAVE_CXX_WNO_DEPRECATED - Success
-- Performing Test HAVE_CXX_WNO_MISSING_PROTOTYPES
-- Performing Test HAVE_CXX_WNO_MISSING_PROTOTYPES - Failed
-- Performing Test HAVE_CXX_WNO_UNUSED_LOCAL_TYPEDEFS
-- Performing Test HAVE_CXX_WNO_UNUSED_LOCAL_TYPEDEFS - Success
-- Performing Test HAVE_CXX_WNO_SIGN_COMPARE
-- Performing Test HAVE_CXX_WNO_SIGN_COMPARE - Success
-- Performing Test HAVE_CXX_WNO_SIGN_PROMO
-- Performing Test HAVE_CXX_WNO_SIGN_PROMO - Success
-- Performing Test HAVE_CXX_WNO_TAUTOLOGICAL_UNDEFINED_COMPARE
-- Performing Test HAVE_CXX_WNO_TAUTOLOGICAL_UNDEFINED_COMPARE - Failed
-- Performing Test HAVE_CXX_WNO_IGNORED_QUALIFIERS
-- Performing Test HAVE_CXX_WNO_IGNORED_QUALIFIERS - Success
-- Performing Test HAVE_CXX_WNO_EXTRA
-- Performing Test HAVE_CXX_WNO_EXTRA - Success
-- Performing Test HAVE_CXX_WNO_UNUSED_CONST_VARIABLE
-- Performing Test HAVE_CXX_WNO_UNUSED_CONST_VARIABLE - Failed
-- Performing Test HAVE_CXX_WNO_SHORTEN_64_TO_32
-- Performing Test HAVE_CXX_WNO_SHORTEN_64_TO_32 - Failed
-- Excluding from source files list: /home/nvidia/opencv/modules/core/src/convert.sse4_1.cpp
-- Excluding from source files list: /home/nvidia/opencv/modules/core/src/convert.avx2.cpp
-- Excluding from source files list: /home/nvidia/opencv/build/modules/core/mathfuncs_core.sse2.cpp
-- Excluding from source files list: /home/nvidia/opencv/build/modules/core/mathfuncs_core.avx.cpp
-- Excluding from source files list: /home/nvidia/opencv/build/modules/core/mathfuncs_core.avx2.cpp
-- Excluding from source files list: /home/nvidia/opencv/build/modules/core/stat.sse4_2.cpp
-- Excluding from source files list: /home/nvidia/opencv/build/modules/core/stat.avx2.cpp
-- Performing Test HAVE_CXX_WNO_UNUSED_BUT_SET_VARIABLE
-- Performing Test HAVE_CXX_WNO_UNUSED_BUT_SET_VARIABLE - Success
-- Excluding from source files list: /home/nvidia/opencv/modules/imgproc/src/filter.avx2.cpp
-- Excluding from source files list: /home/nvidia/opencv/modules/imgproc/src/corner.avx.cpp
-- Excluding from source files list: /home/nvidia/opencv/modules/imgproc/src/imgwarp.avx2.cpp
-- Excluding from source files list: /home/nvidia/opencv/modules/imgproc/src/imgwarp.sse4_1.cpp
-- Excluding from source files list: /home/nvidia/opencv/modules/imgproc/src/undistort.avx2.cpp
-- Excluding from source files list: /home/nvidia/opencv/build/modules/imgproc/accum.sse2.cpp
-- Excluding from source files list: /home/nvidia/opencv/build/modules/imgproc/accum.avx.cpp
-- Excluding from source files list: /home/nvidia/opencv/modules/objdetect/src/haar.avx.cpp
-- Performing Test HAVE_CXX_WNO_PARENTHESES
-- Performing Test HAVE_CXX_WNO_PARENTHESES - Success
-- Performing Test HAVE_CXX_WNO_MAYBE_UNINITIALIZED
-- Performing Test HAVE_CXX_WNO_MAYBE_UNINITIALIZED - Success
-- Performing Test HAVE_CXX_WNO_DEPRECATED_DECLARATIONS
-- Performing Test HAVE_CXX_WNO_DEPRECATED_DECLARATIONS - Success
-- Excluding from source files list: /home/nvidia/opencv/build/modules/dnn/layers/layers_common.avx.cpp
-- Excluding from source files list: /home/nvidia/opencv/build/modules/dnn/layers/layers_common.avx2.cpp
-- Torch importer has been enabled. To run the tests you have to install Torch ('th' executable should be available) and generate testdata using opencv_extra/testdata/dnn/generate_torch_models.py script.
-- Performing Test HAVE_CXX_WNO_OVERLOADED_VIRTUAL
-- Performing Test HAVE_CXX_WNO_OVERLOADED_VIRTUAL - Success
-- Performing Test HAVE_CXX_WNO_UNUSED_PRIVATE_FIELD
-- Performing Test HAVE_CXX_WNO_UNUSED_PRIVATE_FIELD - Failed
-- 
-- General configuration for OpenCV 3.3.0 =====================================
--   Version control:               3.3.0
-- 
--   Platform:
--     Timestamp:                   2017-11-26T09:54:25Z
--     Host:                        Linux 4.4.38-tegra aarch64
--     CMake:                       3.5.1
--     CMake generator:             Unix Makefiles
--     CMake build tool:            /usr/bin/make
--     Configuration:               Release
-- 
--   CPU/HW features:
--     Baseline:                    NEON FP16
--       required:                  NEON
--       disabled:                  VFPV3
-- 
--   C/C++:
--     Built as dynamic libs?:      YES
--     C++ Compiler:                /usr/bin/c++  (ver 5.4.0)
--     C++ flags (Release):         -fsigned-char -W -Wall -Werror=return-type -Werror=non-virtual-dtor -Werror=address -Werror=sequence-point -Wformat -Werror=format-security -Wmissing-declarations -Wundef -Winit-self -Wpointer-arith -Wshadow -Wsign-promo -Wuninitialized -Winit-self -Wno-narrowing -Wno-delete-non-virtual-dtor -Wno-comment -fdiagnostics-show-option -pthread -fomit-frame-pointer -ffunction-sections    -fvisibility=hidden -fvisibility-inlines-hidden -O3 -DNDEBUG  -DNDEBUG
--     C++ flags (Debug):           -fsigned-char -W -Wall -Werror=return-type -Werror=non-virtual-dtor -Werror=address -Werror=sequence-point -Wformat -Werror=format-security -Wmissing-declarations -Wundef -Winit-self -Wpointer-arith -Wshadow -Wsign-promo -Wuninitialized -Winit-self -Wno-narrowing -Wno-delete-non-virtual-dtor -Wno-comment -fdiagnostics-show-option -pthread -fomit-frame-pointer -ffunction-sections    -fvisibility=hidden -fvisibility-inlines-hidden -g  -O0 -DDEBUG -D_DEBUG
--     C Compiler:                  /usr/bin/cc
--     C flags (Release):           -fsigned-char -W -Wall -Werror=return-type -Werror=non-virtual-dtor -Werror=address -Werror=sequence-point -Wformat -Werror=format-security -Wmissing-declarations -Wmissing-prototypes -Wstrict-prototypes -Wundef -Winit-self -Wpointer-arith -Wshadow -Wuninitialized -Winit-self -Wno-narrowing -Wno-comment -fdiagnostics-show-option -pthread -fomit-frame-pointer -ffunction-sections    -fvisibility=hidden -O3 -DNDEBUG  -DNDEBUG
--     C flags (Debug):             -fsigned-char -W -Wall -Werror=return-type -Werror=non-virtual-dtor -Werror=address -Werror=sequence-point -Wformat -Werror=format-security -Wmissing-declarations -Wmissing-prototypes -Wstrict-prototypes -Wundef -Winit-self -Wpointer-arith -Wshadow -Wuninitialized -Winit-self -Wno-narrowing -Wno-comment -fdiagnostics-show-option -pthread -fomit-frame-pointer -ffunction-sections    -fvisibility=hidden -g  -O0 -DDEBUG -D_DEBUG
--     Linker flags (Release):
--     Linker flags (Debug):
--     ccache:                      NO
--     Precompiled headers:         NO
--     Extra dependencies:          gtk-x11-2.0 gdk-x11-2.0 pangocairo-1.0 atk-1.0 cairo gdk_pixbuf-2.0 gio-2.0 pangoft2-1.0 pango-1.0 fontconfig freetype gthread-2.0 /usr/lib/aarch64-linux-gnu/libwebp.so /usr/lib/aarch64-linux-gnu/libpng.so /usr/lib/aarch64-linux-gnu/libz.so /usr/lib/aarch64-linux-gnu/libtiff.so /usr/lib/aarch64-linux-gnu/libjasper.so /usr/lib/aarch64-linux-gnu/libjpeg.so gstbase-1.0 gstreamer-1.0 gobject-2.0 glib-2.0 gstvideo-1.0 gstapp-1.0 gstriff-1.0 gstpbutils-1.0 avcodec-ffmpeg avformat-ffmpeg avutil-ffmpeg swscale-ffmpeg dl m pthread rt /usr/lib/aarch64-linux-gnu/libtbb.so cudart nppc nppi npps cufft -L/usr/local/cuda-8.0/lib64
--     3rdparty dependencies:
-- 
--   OpenCV modules:
--     To be built:                 cudev core cudaarithm flann imgproc ml objdetect video cudabgsegm cudafilters cudaimgproc cudawarping dnn imgcodecs photo shape videoio cudacodec highgui ts features2d calib3d cudafeatures2d cudalegacy cudaobjdetect cudaoptflow cudastereo stitching superres videostab python2 python3
--     Disabled:                    world
--     Disabled by dependency:      -
--     Unavailable:                 java viz
-- 
--   GUI: 
--     QT:                          NO
--     GTK+ 2.x:                    YES (ver 2.24.30)
--     GThread :                    YES (ver 2.48.1)
--     GtkGlExt:                    NO
--     OpenGL support:              NO
--     VTK support:                 NO
-- 
--   Media I/O: 
--     ZLib:                        /usr/lib/aarch64-linux-gnu/libz.so (ver 1.2.8)
--     JPEG:                        /usr/lib/aarch64-linux-gnu/libjpeg.so (ver )
--     WEBP:                        /usr/lib/aarch64-linux-gnu/libwebp.so (ver encoder: 0x0202)
--     PNG:                         /usr/lib/aarch64-linux-gnu/libpng.so (ver 1.2.54)
--     TIFF:                        /usr/lib/aarch64-linux-gnu/libtiff.so (ver 42 - 4.0.6)
--     JPEG 2000:                   /usr/lib/aarch64-linux-gnu/libjasper.so (ver 1.900.1)
--     OpenEXR:                     NO
--     GDAL:                        NO
--     GDCM:                        NO
-- 
--   Video I/O:
--     DC1394 1.x:                  NO
--     DC1394 2.x:                  NO
--     FFMPEG:                      YES
--       avcodec:                   YES (ver 56.60.100)
--       avformat:                  YES (ver 56.40.101)
--       avutil:                    YES (ver 54.31.100)
--       swscale:                   YES (ver 3.1.101)
--       avresample:                NO
--     GStreamer:                   
--       base:                      YES (ver 1.8.3)
--       video:                     YES (ver 1.8.3)
--       app:                       YES (ver 1.8.3)
--       riff:                      YES (ver 1.8.3)
--       pbutils:                   YES (ver 1.8.3)
--     OpenNI:                      NO
--     OpenNI PrimeSensor Modules:  NO
--     OpenNI2:                     NO
--     PvAPI:                       NO
--     GigEVisionSDK:               NO
--     Aravis SDK:                  NO
--     UniCap:                      NO
--     UniCap ucil:                 NO
--     V4L/V4L2:                    NO/YES
--     XIMEA:                       NO
--     Xine:                        NO
--     Intel Media SDK:             NO
--     gPhoto2:                     NO
-- 
--   Parallel framework:            TBB (ver 4.4 interface 9002)
-- 
--   Trace:                         YES ()
-- 
--   Other third-party libraries:
--     Use Intel IPP:               NO
--     Use Intel IPP IW:            NO
--     Use VA:                      NO
--     Use Intel VA-API/OpenCL:     NO
--     Use Lapack:                  NO
--     Use Eigen:                   YES (ver 3.2.92)
--     Use Cuda:                    YES (ver 8.0)
--     Use OpenCL:                  NO
--     Use OpenVX:                  NO
--     Use custom HAL:              YES (carotene (ver 0.0.1))
-- 
--   NVIDIA CUDA
--     Use CUFFT:                   YES
--     Use CUBLAS:                  NO
--     USE NVCUVID:                 NO
--     NVIDIA GPU arch:             62
--     NVIDIA PTX archs:
--     Use fast math:               NO
-- 
--   Python 2:
--     Interpreter:                 /usr/bin/python2.7 (ver 2.7.12)
--     Libraries:                   /usr/lib/aarch64-linux-gnu/libpython2.7.so (ver 2.7.12)
--     numpy:                       /usr/lib/python2.7/dist-packages/numpy/core/include (ver 1.11.0)
--     packages path:               lib/python2.7/dist-packages
-- 
--   Python 3:
--     Interpreter:                 /usr/bin/python3 (ver 3.5.2)
--     Libraries:                   /usr/lib/aarch64-linux-gnu/libpython3.5m.so (ver 3.5.2)
--     numpy:                       /usr/lib/python3/dist-packages/numpy/core/include (ver 1.11.0)
--     packages path:               lib/python3.5/dist-packages
-- 
--   Python (for build):            /usr/bin/python2.7
-- 
--   Java:
--     ant:                         NO
--     JNI:                         NO
--     Java wrappers:               NO
--     Java tests:                  NO
-- 
--   Matlab:                        Matlab not found or implicitly disabled
-- 
--   Documentation:
--     Doxygen:                     NO
-- 
--   Tests and samples:
--     Tests:                       YES
--     Performance tests:           YES
--     C/C++ Examples:              YES
-- 
--   Install path:                  /usr
-- 
--   cvconfig.h is in:              /home/nvidia/opencv/build
-- -----------------------------------------------------------------
-- 
-- Configuring done
-- Generating done
-- Build files have been written to: /home/nvidia/opencv/build
nvidia@gpu:~/opencv/build$ 
nvidia@gpu:~/opencv/build$ make -j4
Scanning dependencies of target opencv_cudev
Scanning dependencies of target libprotobuf
Scanning dependencies of target carotene_objs
[  0%] Building CXX object modules/cudev/CMakeFiles/opencv_cudev.dir/src/stub.cpp.o
[  0%] Building CXX object 3rdparty/carotene/hal/carotene/CMakeFiles/carotene_objs.dir/src/blur.cpp.o
[  0%] Building CXX object 3rdparty/carotene/hal/carotene/CMakeFiles/carotene_objs.dir/src/in_range.cpp.o
[  0%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/arena.cc.o
[  0%] Linking CXX shared library ../../lib/libopencv_cudev.so
[  0%] Built target opencv_cudev
[  0%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/arenastring.cc.o
[  0%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/extension_set.cc.o
[  0%] Building CXX object 3rdparty/carotene/hal/carotene/CMakeFiles/carotene_objs.dir/src/add.cpp.o
[  0%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/generated_message_util.cc.o
[  0%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/io/coded_stream.cc.o
[  0%] Building CXX object 3rdparty/carotene/hal/carotene/CMakeFiles/carotene_objs.dir/src/remap.cpp.o
[  0%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/io/zero_copy_stream.cc.o
[  0%] Building CXX object 3rdparty/carotene/hal/carotene/CMakeFiles/carotene_objs.dir/src/convert_scale.cpp.o
[  0%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/io/zero_copy_stream_impl_lite.cc.o
[  0%] Building CXX object 3rdparty/carotene/hal/carotene/CMakeFiles/carotene_objs.dir/src/meanstddev.cpp.o
[  1%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/message_lite.cc.o
[  1%] Building CXX object 3rdparty/carotene/hal/carotene/CMakeFiles/carotene_objs.dir/src/accumulate.cpp.o
[  1%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/repeated_field.cc.o
[  1%] Building CXX object 3rdparty/carotene/hal/carotene/CMakeFiles/carotene_objs.dir/src/fast.cpp.o
[  1%] Building CXX object 3rdparty/carotene/hal/carotene/CMakeFiles/carotene_objs.dir/src/div.cpp.o
[  1%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/stubs/atomicops_internals_x86_gcc.cc.o
[  1%] Building CXX object 3rdparty/carotene/hal/carotene/CMakeFiles/carotene_objs.dir/src/reduce.cpp.o
[  1%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/stubs/bytestream.cc.o
[  1%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/stubs/common.cc.o
[  1%] Building CXX object 3rdparty/carotene/hal/carotene/CMakeFiles/carotene_objs.dir/src/laplacian.cpp.o
[  1%] Building CXX object 3rdparty/carotene/hal/carotene/CMakeFiles/carotene_objs.dir/src/channels_combine.cpp.o
[  1%] Building CXX object 3rdparty/carotene/hal/carotene/CMakeFiles/carotene_objs.dir/src/common.cpp.o
[  1%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/stubs/int128.cc.o
[  1%] Building CXX object 3rdparty/carotene/hal/carotene/CMakeFiles/carotene_objs.dir/src/scharr.cpp.o
[  2%] Building CXX object 3rdparty/carotene/hal/carotene/CMakeFiles/carotene_objs.dir/src/channel_extract.cpp.o
[  2%] Building CXX object 3rdparty/carotene/hal/carotene/CMakeFiles/carotene_objs.dir/src/convert_depth.cpp.o
[  2%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/stubs/once.cc.o
[  2%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/stubs/status.cc.o
[  2%] Building CXX object 3rdparty/carotene/hal/carotene/CMakeFiles/carotene_objs.dir/src/flip.cpp.o
[  2%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/stubs/statusor.cc.o
[  2%] Building CXX object 3rdparty/carotene/hal/carotene/CMakeFiles/carotene_objs.dir/src/pyramid.cpp.o
[  2%] Building CXX object 3rdparty/carotene/hal/carotene/CMakeFiles/carotene_objs.dir/src/threshold.cpp.o
[  2%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/stubs/stringpiece.cc.o
[  2%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/stubs/stringprintf.cc.o
[  2%] Building CXX object 3rdparty/carotene/hal/carotene/CMakeFiles/carotene_objs.dir/src/norm.cpp.o
[  2%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/stubs/structurally_valid.cc.o
[  2%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/stubs/strutil.cc.o
[  2%] Building CXX object 3rdparty/carotene/hal/carotene/CMakeFiles/carotene_objs.dir/src/fill_minmaxloc.cpp.o
[  2%] Building CXX object 3rdparty/carotene/hal/carotene/CMakeFiles/carotene_objs.dir/src/canny.cpp.o
[  2%] Building CXX object 3rdparty/carotene/hal/carotene/CMakeFiles/carotene_objs.dir/src/colorconvert.cpp.o
[  2%] Building CXX object 3rdparty/carotene/hal/carotene/CMakeFiles/carotene_objs.dir/src/absdiff.cpp.o
[  2%] Building CXX object 3rdparty/carotene/hal/carotene/CMakeFiles/carotene_objs.dir/src/dot_product.cpp.o
[  2%] Building CXX object 3rdparty/carotene/hal/carotene/CMakeFiles/carotene_objs.dir/src/template_matching.cpp.o
[  2%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/stubs/time.cc.o
[  2%] Building CXX object 3rdparty/carotene/hal/carotene/CMakeFiles/carotene_objs.dir/src/count_nonzero.cpp.o
[  2%] Building CXX object 3rdparty/carotene/hal/carotene/CMakeFiles/carotene_objs.dir/src/opticalflow.cpp.o
[  2%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/wire_format_lite.cc.o
[  2%] Building CXX object 3rdparty/carotene/hal/carotene/CMakeFiles/carotene_objs.dir/src/median_filter.cpp.o
[  2%] Building CXX object 3rdparty/carotene/hal/carotene/CMakeFiles/carotene_objs.dir/src/resize.cpp.o
[  3%] Building CXX object 3rdparty/carotene/hal/carotene/CMakeFiles/carotene_objs.dir/src/separable_filter.cpp.o
[  3%] Building CXX object 3rdparty/carotene/hal/carotene/CMakeFiles/carotene_objs.dir/src/integral.cpp.o
[  3%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/any.cc.o
[  3%] Building CXX object 3rdparty/carotene/hal/carotene/CMakeFiles/carotene_objs.dir/src/minmaxloc.cpp.o
[  4%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/any.pb.cc.o
[  4%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/api.pb.cc.o
[  4%] Building CXX object 3rdparty/carotene/hal/carotene/CMakeFiles/carotene_objs.dir/src/convert.cpp.o
[  4%] Building CXX object 3rdparty/carotene/hal/carotene/CMakeFiles/carotene_objs.dir/src/phase.cpp.o
[  4%] Building CXX object 3rdparty/carotene/hal/carotene/CMakeFiles/carotene_objs.dir/src/sobel.cpp.o
[  4%] Building CXX object 3rdparty/carotene/hal/carotene/CMakeFiles/carotene_objs.dir/src/gaussian_blur.cpp.o
[  4%] Building CXX object 3rdparty/carotene/hal/carotene/CMakeFiles/carotene_objs.dir/src/add_weighted.cpp.o
[  4%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/descriptor.cc.o
[  4%] Building CXX object 3rdparty/carotene/hal/carotene/CMakeFiles/carotene_objs.dir/src/warp_affine.cpp.o
[  4%] Building CXX object 3rdparty/carotene/hal/carotene/CMakeFiles/carotene_objs.dir/src/cmp.cpp.o
[  4%] Building CXX object 3rdparty/carotene/hal/carotene/CMakeFiles/carotene_objs.dir/src/morph.cpp.o
[  4%] Building CXX object 3rdparty/carotene/hal/carotene/CMakeFiles/carotene_objs.dir/src/sub.cpp.o
[  4%] Building CXX object 3rdparty/carotene/hal/carotene/CMakeFiles/carotene_objs.dir/src/convolution.cpp.o
[  4%] Building CXX object 3rdparty/carotene/hal/carotene/CMakeFiles/carotene_objs.dir/src/bitwise.cpp.o
[  4%] Building CXX object 3rdparty/carotene/hal/carotene/CMakeFiles/carotene_objs.dir/src/warp_perspective.cpp.o
[  5%] Building CXX object 3rdparty/carotene/hal/carotene/CMakeFiles/carotene_objs.dir/src/magnitude.cpp.o
[  5%] Building CXX object 3rdparty/carotene/hal/carotene/CMakeFiles/carotene_objs.dir/src/mul.cpp.o
[  5%] Building CXX object 3rdparty/carotene/hal/carotene/CMakeFiles/carotene_objs.dir/src/sum.cpp.o
[  5%] Building CXX object 3rdparty/carotene/hal/carotene/CMakeFiles/carotene_objs.dir/src/min_max.cpp.o
[  5%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/descriptor.pb.cc.o
[  5%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/descriptor_database.cc.o
[  5%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/duration.pb.cc.o
[  5%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/dynamic_message.cc.o
[  5%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/empty.pb.cc.o
[  5%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/extension_set_heavy.cc.o
[  5%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/field_mask.pb.cc.o
[  5%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/generated_message_reflection.cc.o
[  5%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/io/gzip_stream.cc.o
[  5%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/io/printer.cc.o
[  5%] Built target carotene_objs
Scanning dependencies of target tegra_hal
[  6%] Linking CXX static library ../../lib/libtegra_hal.a
[  6%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/io/strtod.cc.o
[  6%] Built target tegra_hal
[  6%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/io/tokenizer.cc.o
[  6%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/io/zero_copy_stream_impl.cc.o
[  7%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/map_field.cc.o
[  7%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/message.cc.o
[  7%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/reflection_ops.cc.o
[  7%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/service.cc.o
[  7%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/source_context.pb.cc.o
[  7%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/struct.pb.cc.o
[  7%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/stubs/mathlimits.cc.o
[  7%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/stubs/substitute.cc.o
[  7%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/text_format.cc.o
[  7%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/timestamp.pb.cc.o
[  7%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/type.pb.cc.o
[  7%] Generating opencl_kernels_core.cpp, opencl_kernels_core.hpp
[  7%] Building NVCC (Device) object modules/core/CMakeFiles/cuda_compile.dir/src/cuda/cuda_compile_generated_gpu_mat.cu.o
[  7%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/unknown_field_set.cc.o
[  7%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/util/field_comparator.cc.o
[  7%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/util/field_mask_util.cc.o
[  7%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/util/internal/datapiece.cc.o
[  8%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/util/internal/default_value_objectwriter.cc.o
[  8%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/util/internal/field_mask_utility.cc.o
[  8%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/util/internal/json_escaping.cc.o
[  8%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/util/internal/json_objectwriter.cc.o
[  8%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/util/internal/json_stream_parser.cc.o
[  8%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/util/internal/object_writer.cc.o
[  8%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/util/internal/proto_writer.cc.o
[  8%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/util/internal/protostream_objectsource.cc.o
[  8%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/util/internal/protostream_objectwriter.cc.o
[  8%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/util/internal/type_info.cc.o
[  8%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/util/internal/utility.cc.o
[  8%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/util/json_util.cc.o
[  8%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/util/message_differencer.cc.o
[  8%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/util/time_util.cc.o
[  8%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/util/type_resolver_util.cc.o
[  8%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/wire_format.cc.o
[  9%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/wrappers.pb.cc.o
[  9%] Linking CXX static library ../lib/liblibprotobuf.a
[  9%] Built target libprotobuf
Scanning dependencies of target opencv_core
[  9%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/types.cpp.o
[  9%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/matrix.cpp.o
[  9%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/convert.fp16.cpp.o
[  9%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/persistence.cpp.o
[  9%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/directx.cpp.o
[  9%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/cuda_info.cpp.o
[  9%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/lda.cpp.o
[  9%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/alloc.cpp.o
[  9%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/gl_core_3_1.cpp.o
[  9%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/va_intel.cpp.o
[  9%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/command_line_parser.cpp.o
[  9%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/algorithm.cpp.o
[ 10%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/out.cpp.o
[ 10%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/matmul.cpp.o
[ 10%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/conjugate_gradient.cpp.o
[ 10%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/cuda_host_mem.cpp.o
[ 10%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/hal_internal.cpp.o
[ 10%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/pca.cpp.o
[ 10%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/system.cpp.o
[ 10%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/stl.cpp.o
[ 10%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/merge.cpp.o
[ 10%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/lpsolver.cpp.o
[ 10%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/mathfuncs_core.dispatch.cpp.o
[ 10%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/cuda_stream.cpp.o
[ 10%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/ovx.cpp.o
[ 10%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/cuda_gpu_mat.cpp.o
[ 10%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/parallel.cpp.o
[ 10%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/parallel_pthreads.cpp.o
[ 11%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/split.cpp.o
[ 11%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/trace.cpp.o
[ 11%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/kmeans.cpp.o
[ 11%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/umatrix.cpp.o
[ 11%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/convert.cpp.o
[ 11%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/ocl.cpp.o
[ 11%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/stat.cpp.o
[ 11%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/downhill_simplex.cpp.o
[ 11%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/tables.cpp.o
[ 11%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/datastructs.cpp.o
[ 11%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/copy.cpp.o
[ 11%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/array.cpp.o
[ 11%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/opencl/runtime/opencl_core.cpp.o
[ 11%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/opencl/runtime/opencl_clamdfft.cpp.o
[ 11%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/opencl/runtime/opencl_clamdblas.cpp.o
[ 12%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/matrix_decomp.cpp.o
[ 12%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/softfloat.cpp.o
[ 12%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/stat.dispatch.cpp.o
[ 12%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/dxt.cpp.o
[ 12%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/glob.cpp.o
[ 12%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/rand.cpp.o
[ 12%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/mathfuncs.cpp.o
[ 12%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/arithm.cpp.o
[ 12%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/matop.cpp.o
[ 12%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/opengl.cpp.o
[ 12%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/lapack.cpp.o
[ 12%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/opencl_kernels_core.cpp.o
[ 12%] Linking CXX shared library ../../lib/libopencv_core.so
[ 12%] Built target opencv_core
[ 12%] Generating opencl_kernels_imgproc.cpp, opencl_kernels_imgproc.hpp
Scanning dependencies of target opencv_ml
[ 13%] Building NVCC (Device) object modules/cudaarithm/CMakeFiles/cuda_compile.dir/src/cuda/cuda_compile_generated_mul_scalar.cu.o
Scanning dependencies of target opencv_flann
[ 13%] Building CXX object modules/flann/CMakeFiles/opencv_flann.dir/src/miniflann.cpp.o
[ 13%] Building CXX object modules/ml/CMakeFiles/opencv_ml.dir/src/rtrees.cpp.o
Scanning dependencies of target opencv_imgproc
[ 13%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/contours.cpp.o
[ 13%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/histogram.cpp.o
[ 13%] Building CXX object modules/ml/CMakeFiles/opencv_ml.dir/src/kdtree.cpp.o
[ 13%] Building CXX object modules/ml/CMakeFiles/opencv_ml.dir/src/boost.cpp.o
[ 13%] Building CXX object modules/ml/CMakeFiles/opencv_ml.dir/src/inner_functions.cpp.o
[ 13%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/main.cpp.o
[ 13%] Building CXX object modules/ml/CMakeFiles/opencv_ml.dir/src/nbayes.cpp.o
[ 13%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/gabor.cpp.o
[ 13%] Building CXX object modules/flann/CMakeFiles/opencv_flann.dir/src/flann.cpp.o
[ 13%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/thresh.cpp.o
[ 13%] Building CXX object modules/ml/CMakeFiles/opencv_ml.dir/src/svm.cpp.o
[ 14%] Linking CXX shared library ../../lib/libopencv_flann.so
[ 14%] Built target opencv_flann
[ 15%] Building CXX object modules/ml/CMakeFiles/opencv_ml.dir/src/testset.cpp.o
[ 16%] Building NVCC (Device) object modules/cudaarithm/CMakeFiles/cuda_compile.dir/src/cuda/cuda_compile_generated_div_mat.cu.o
[ 16%] Building CXX object modules/ml/CMakeFiles/opencv_ml.dir/src/svmsgd.cpp.o
[ 17%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/emd.cpp.o
[ 17%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/accum.cpp.o
[ 17%] Building CXX object modules/ml/CMakeFiles/opencv_ml.dir/src/ann_mlp.cpp.o
[ 17%] Building CXX object modules/ml/CMakeFiles/opencv_ml.dir/src/knearest.cpp.o
[ 17%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/drawing.cpp.o
[ 17%] Building CXX object modules/ml/CMakeFiles/opencv_ml.dir/src/lr.cpp.o
[ 17%] Building CXX object modules/ml/CMakeFiles/opencv_ml.dir/src/em.cpp.o
[ 17%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/filter.cpp.o
[ 17%] Building CXX object modules/ml/CMakeFiles/opencv_ml.dir/src/gbt.cpp.o
[ 17%] Building CXX object modules/ml/CMakeFiles/opencv_ml.dir/src/data.cpp.o
[ 17%] Building CXX object modules/ml/CMakeFiles/opencv_ml.dir/src/tree.cpp.o
[ 17%] Building NVCC (Device) object modules/cudaarithm/CMakeFiles/cuda_compile.dir/src/cuda/cuda_compile_generated_normalize.cu.o
[ 17%] Building NVCC (Device) object modules/cudaarithm/CMakeFiles/cuda_compile.dir/src/cuda/cuda_compile_generated_norm.cu.o
[ 17%] Linking CXX shared library ../../lib/libopencv_ml.so
[ 17%] Built target opencv_ml
[ 17%] Building NVCC (Device) object modules/cudaarithm/CMakeFiles/cuda_compile.dir/src/cuda/cuda_compile_generated_absdiff_scalar.cu.o
[ 17%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/rotcalipers.cpp.o
[ 17%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/clahe.cpp.o
[ 17%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/geometry.cpp.o
[ 17%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/matchcontours.cpp.o
[ 17%] Building NVCC (Device) object modules/cudaarithm/CMakeFiles/cuda_compile.dir/src/cuda/cuda_compile_generated_cmp_mat.cu.o
[ 17%] Building NVCC (Device) object modules/cudaarithm/CMakeFiles/cuda_compile.dir/src/cuda/cuda_compile_generated_minmax.cu.o
[ 17%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/convhull.cpp.o
[ 17%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/intersection.cpp.o
[ 17%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/generalized_hough.cpp.o
[ 17%] Building NVCC (Device) object modules/cudaarithm/CMakeFiles/cuda_compile.dir/src/cuda/cuda_compile_generated_reduce.cu.o
[ 17%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/blend.cpp.o
[ 17%] Building NVCC (Device) object modules/cudaarithm/CMakeFiles/cuda_compile.dir/src/cuda/cuda_compile_generated_minmax_mat.cu.o
[ 17%] Building NVCC (Device) object modules/cudaarithm/CMakeFiles/cuda_compile.dir/src/cuda/cuda_compile_generated_cmp_scalar.cu.o
[ 17%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/pyramids.cpp.o
[ 17%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/connectedcomponents.cpp.o
[ 17%] Building NVCC (Device) object modules/cudaarithm/CMakeFiles/cuda_compile.dir/src/cuda/cuda_compile_generated_sum.cu.o
[ 17%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/hough.cpp.o
[ 17%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/canny.cpp.o
[ 17%] Building NVCC (Device) object modules/cudaarithm/CMakeFiles/cuda_compile.dir/src/cuda/cuda_compile_generated_copy_make_border.cu.o
[ 18%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/moments.cpp.o
[ 18%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/cornersubpix.cpp.o
[ 18%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/color.cpp.o
[ 18%] Building NVCC (Device) object modules/cudaarithm/CMakeFiles/cuda_compile.dir/src/cuda/cuda_compile_generated_add_scalar.cu.o
[ 18%] Building NVCC (Device) object modules/cudaarithm/CMakeFiles/cuda_compile.dir/src/cuda/cuda_compile_generated_bitwise_mat.cu.o
[ 18%] Building NVCC (Device) object modules/cudaarithm/CMakeFiles/cuda_compile.dir/src/cuda/cuda_compile_generated_lut.cu.o
[ 18%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/hershey_fonts.cpp.o
[ 18%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/sumpixels.cpp.o
[ 18%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/imgwarp.cpp.o
[ 18%] Building NVCC (Device) object modules/cudaarithm/CMakeFiles/cuda_compile.dir/src/cuda/cuda_compile_generated_polar_cart.cu.o
[ 18%] Building NVCC (Device) object modules/cudaarithm/CMakeFiles/cuda_compile.dir/src/cuda/cuda_compile_generated_math.cu.o
[ 19%] Building NVCC (Device) object modules/cudaarithm/CMakeFiles/cuda_compile.dir/src/cuda/cuda_compile_generated_split_merge.cu.o
[ 19%] Building NVCC (Device) object modules/cudaarithm/CMakeFiles/cuda_compile.dir/src/cuda/cuda_compile_generated_integral.cu.o
[ 19%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/smooth.cpp.o
[ 19%] Building NVCC (Device) object modules/cudaarithm/CMakeFiles/cuda_compile.dir/src/cuda/cuda_compile_generated_add_mat.cu.o
[ 19%] Building NVCC (Device) object modules/cudaarithm/CMakeFiles/cuda_compile.dir/src/cuda/cuda_compile_generated_mul_mat.cu.o
[ 19%] Building NVCC (Device) object modules/cudaarithm/CMakeFiles/cuda_compile.dir/src/cuda/cuda_compile_generated_absdiff_mat.cu.o
[ 19%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/templmatch.cpp.o
[ 19%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/phasecorr.cpp.o
[ 19%] Building NVCC (Device) object modules/cudaarithm/CMakeFiles/cuda_compile.dir/src/cuda/cuda_compile_generated_sub_mat.cu.o
[ 19%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/subdivision2d.cpp.o
[ 19%] Building NVCC (Device) object modules/cudaarithm/CMakeFiles/cuda_compile.dir/src/cuda/cuda_compile_generated_minmaxloc.cu.o
[ 19%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/grabcut.cpp.o
[ 19%] Building NVCC (Device) object modules/cudaarithm/CMakeFiles/cuda_compile.dir/src/cuda/cuda_compile_generated_threshold.cu.o
[ 19%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/tables.cpp.o
[ 19%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/corner.cpp.o
[ 19%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/lsd.cpp.o
[ 19%] Building NVCC (Device) object modules/cudaarithm/CMakeFiles/cuda_compile.dir/src/cuda/cuda_compile_generated_transpose.cu.o
[ 19%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/floodfill.cpp.o
[ 19%] Building NVCC (Device) object modules/cudaarithm/CMakeFiles/cuda_compile.dir/src/cuda/cuda_compile_generated_div_scalar.cu.o
[ 19%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/approx.cpp.o
[ 20%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/spatialgradient.cpp.o
[ 20%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/segmentation.cpp.o
[ 20%] Building NVCC (Device) object modules/cudaarithm/CMakeFiles/cuda_compile.dir/src/cuda/cuda_compile_generated_bitwise_scalar.cu.o
[ 20%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/samplers.cpp.o
[ 20%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/demosaicing.cpp.o
[ 20%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/morph.cpp.o
[ 20%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/undistort.cpp.o
[ 20%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/utils.cpp.o
[ 20%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/min_enclosing_triangle.cpp.o
[ 20%] Building NVCC (Device) object modules/cudaarithm/CMakeFiles/cuda_compile.dir/src/cuda/cuda_compile_generated_countnonzero.cu.o
[ 20%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/linefit.cpp.o
[ 20%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/deriv.cpp.o
[ 20%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/accum.dispatch.cpp.o
[ 20%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/distransform.cpp.o
[ 20%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/featureselect.cpp.o
[ 20%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/colormap.cpp.o
[ 20%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/shapedescr.cpp.o
[ 20%] Building NVCC (Device) object modules/cudaarithm/CMakeFiles/cuda_compile.dir/src/cuda/cuda_compile_generated_sub_scalar.cu.o
[ 21%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/opencl_kernels_imgproc.cpp.o
[ 21%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/accum.neon.cpp.o
[ 21%] Building NVCC (Device) object modules/cudaarithm/CMakeFiles/cuda_compile.dir/src/cuda/cuda_compile_generated_add_weighted.cu.o
[ 21%] Building NVCC (Device) object modules/cudaarithm/CMakeFiles/cuda_compile.dir/src/cuda/cuda_compile_generated_mul_spectrums.cu.o
[ 21%] Linking CXX shared library ../../lib/libopencv_imgproc.so
[ 21%] Built target opencv_imgproc
Scanning dependencies of target opencv_imgcodecs
[ 21%] Building CXX object modules/imgcodecs/CMakeFiles/opencv_imgcodecs.dir/src/loadsave.cpp.o
[ 21%] Building CXX object modules/imgcodecs/CMakeFiles/opencv_imgcodecs.dir/src/utils.cpp.o
[ 21%] Building CXX object modules/imgcodecs/CMakeFiles/opencv_imgcodecs.dir/src/grfmt_png.cpp.o
[ 21%] Building CXX object modules/imgcodecs/CMakeFiles/opencv_imgcodecs.dir/src/grfmt_bmp.cpp.o
[ 21%] Building CXX object modules/imgcodecs/CMakeFiles/opencv_imgcodecs.dir/src/grfmt_exr.cpp.o
[ 21%] Building CXX object modules/imgcodecs/CMakeFiles/opencv_imgcodecs.dir/src/grfmt_pxm.cpp.o
[ 21%] Building CXX object modules/imgcodecs/CMakeFiles/opencv_imgcodecs.dir/src/grfmt_gdcm.cpp.o
[ 21%] Building CXX object modules/imgcodecs/CMakeFiles/opencv_imgcodecs.dir/src/grfmt_hdr.cpp.o
[ 21%] Building CXX object modules/imgcodecs/CMakeFiles/opencv_imgcodecs.dir/src/grfmt_pam.cpp.o
[ 21%] Building CXX object modules/imgcodecs/CMakeFiles/opencv_imgcodecs.dir/src/grfmt_gdal.cpp.o
[ 21%] Building CXX object modules/imgcodecs/CMakeFiles/opencv_imgcodecs.dir/src/grfmt_base.cpp.o
[ 22%] Building CXX object modules/imgcodecs/CMakeFiles/opencv_imgcodecs.dir/src/grfmt_jpeg.cpp.o
[ 22%] Building CXX object modules/imgcodecs/CMakeFiles/opencv_imgcodecs.dir/src/grfmt_sunras.cpp.o
[ 22%] Building CXX object modules/imgcodecs/CMakeFiles/opencv_imgcodecs.dir/src/grfmt_webp.cpp.o
[ 22%] Building CXX object modules/imgcodecs/CMakeFiles/opencv_imgcodecs.dir/src/grfmt_jpeg2000.cpp.o
[ 22%] Building CXX object modules/imgcodecs/CMakeFiles/opencv_imgcodecs.dir/src/grfmt_tiff.cpp.o
[ 22%] Building CXX object modules/imgcodecs/CMakeFiles/opencv_imgcodecs.dir/src/bitstrm.cpp.o
[ 22%] Building CXX object modules/imgcodecs/CMakeFiles/opencv_imgcodecs.dir/src/rgbe.cpp.o
[ 22%] Building CXX object modules/imgcodecs/CMakeFiles/opencv_imgcodecs.dir/src/exif.cpp.o
[ 22%] Generating opencl_kernels_objdetect.cpp, opencl_kernels_objdetect.hpp
Scanning dependencies of target opencv_objdetect
[ 22%] Building CXX object modules/objdetect/CMakeFiles/opencv_objdetect.dir/src/main.cpp.o
[ 22%] Linking CXX shared library ../../lib/libopencv_imgcodecs.so
[ 22%] Built target opencv_imgcodecs
[ 22%] Building CXX object modules/objdetect/CMakeFiles/opencv_objdetect.dir/src/detection_based_tracker.cpp.o
[ 22%] Building CXX object modules/objdetect/CMakeFiles/opencv_objdetect.dir/src/hog.cpp.o
[ 22%] Building CXX object modules/objdetect/CMakeFiles/opencv_objdetect.dir/src/cascadedetect_convert.cpp.o
[ 22%] Building CXX object modules/objdetect/CMakeFiles/opencv_objdetect.dir/src/cascadedetect.cpp.o
[ 23%] Building CXX object modules/objdetect/CMakeFiles/opencv_objdetect.dir/src/haar.cpp.o
[ 23%] Building CXX object modules/objdetect/CMakeFiles/opencv_objdetect.dir/opencl_kernels_objdetect.cpp.o
[ 23%] Generating opencl_kernels_video.cpp, opencl_kernels_video.hpp
Scanning dependencies of target opencv_video
[ 23%] Building CXX object modules/video/CMakeFiles/opencv_video.dir/src/ecc.cpp.o
[ 23%] Building CXX object modules/video/CMakeFiles/opencv_video.dir/src/lkpyramid.cpp.o
[ 23%] Linking CXX shared library ../../lib/libopencv_objdetect.so
[ 23%] Built target opencv_objdetect
[ 23%] Building NVCC (Device) object modules/cudawarping/CMakeFiles/cuda_compile.dir/src/cuda/cuda_compile_generated_remap.cu.o
[ 24%] Building CXX object modules/video/CMakeFiles/opencv_video.dir/src/bgfg_gaussmix2.cpp.o
[ 24%] Building CXX object modules/video/CMakeFiles/opencv_video.dir/src/bgfg_KNN.cpp.o
Scanning dependencies of target opencv_cudaarithm
[ 24%] Building CXX object modules/cudaarithm/CMakeFiles/opencv_cudaarithm.dir/src/reductions.cpp.o
[ 24%] Building CXX object modules/cudaarithm/CMakeFiles/opencv_cudaarithm.dir/src/element_operations.cpp.o
[ 24%] Building CXX object modules/video/CMakeFiles/opencv_video.dir/src/tvl1flow.cpp.o
[ 24%] Building CXX object modules/cudaarithm/CMakeFiles/opencv_cudaarithm.dir/src/core.cpp.o
[ 24%] Building CXX object modules/cudaarithm/CMakeFiles/opencv_cudaarithm.dir/src/arithm.cpp.o
[ 24%] Building CXX object modules/video/CMakeFiles/opencv_video.dir/src/kalman.cpp.o
[ 24%] Linking CXX shared library ../../lib/libopencv_cudaarithm.so
[ 24%] Built target opencv_cudaarithm
[ 25%] Generating opencl_kernels_dnn.cpp, opencl_kernels_dnn.hpp
Scanning dependencies of target opencv_dnn
[ 25%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/misc/tensorflow/versions.pb.cc.o
[ 25%] Building CXX object modules/video/CMakeFiles/opencv_video.dir/src/compat_video.cpp.o
[ 25%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/misc/tensorflow/function.pb.cc.o
[ 25%] Building CXX object modules/video/CMakeFiles/opencv_video.dir/src/camshift.cpp.o
[ 25%] Building CXX object modules/video/CMakeFiles/opencv_video.dir/src/optflowgf.cpp.o
[ 25%] Building CXX object modules/video/CMakeFiles/opencv_video.dir/opencl_kernels_video.cpp.o
[ 25%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/misc/tensorflow/attr_value.pb.cc.o
[ 25%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/misc/tensorflow/types.pb.cc.o
[ 25%] Linking CXX shared library ../../lib/libopencv_video.so
[ 25%] Built target opencv_video
Scanning dependencies of target opencv_videoio
[ 25%] Building CXX object modules/videoio/CMakeFiles/opencv_videoio.dir/src/cap.cpp.o
[ 25%] Building CXX object modules/videoio/CMakeFiles/opencv_videoio.dir/src/cap_images.cpp.o
[ 25%] Building CXX object modules/videoio/CMakeFiles/opencv_videoio.dir/src/cap_mjpeg_encoder.cpp.o
[ 25%] Building CXX object modules/videoio/CMakeFiles/opencv_videoio.dir/src/cap_mjpeg_decoder.cpp.o
[ 25%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/misc/tensorflow/graph.pb.cc.o
[ 25%] Building CXX object modules/videoio/CMakeFiles/opencv_videoio.dir/src/cap_gstreamer.cpp.o
[ 25%] Building CXX object modules/videoio/CMakeFiles/opencv_videoio.dir/src/cap_v4l.cpp.o
[ 25%] Building CXX object modules/videoio/CMakeFiles/opencv_videoio.dir/src/cap_ffmpeg.cpp.o
[ 25%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/misc/tensorflow/tensor.pb.cc.o
[ 25%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/misc/tensorflow/op_def.pb.cc.o
[ 26%] Linking CXX shared library ../../lib/libopencv_videoio.so
[ 26%] Built target opencv_videoio
[ 26%] Building NVCC (Device) object modules/cudabgsegm/CMakeFiles/cuda_compile.dir/src/cuda/cuda_compile_generated_mog2.cu.o
[ 26%] Building NVCC (Device) object modules/cudabgsegm/CMakeFiles/cuda_compile.dir/src/cuda/cuda_compile_generated_mog.cu.o
[ 26%] Building NVCC (Device) object modules/cudawarping/CMakeFiles/cuda_compile.dir/src/cuda/cuda_compile_generated_warp.cu.o
[ 26%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/misc/tensorflow/tensor_shape.pb.cc.o
[ 26%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/misc/caffe/caffe.pb.cc.o
[ 26%] Building NVCC (Device) object modules/cudawarping/CMakeFiles/cuda_compile.dir/src/cuda/cuda_compile_generated_pyr_up.cu.o
Scanning dependencies of target opencv_cudabgsegm
[ 26%] Building CXX object modules/cudabgsegm/CMakeFiles/opencv_cudabgsegm.dir/src/mog.cpp.o
[ 26%] Building CXX object modules/cudabgsegm/CMakeFiles/opencv_cudabgsegm.dir/src/mog2.cpp.o
[ 26%] Linking CXX shared library ../../lib/libopencv_cudabgsegm.so
[ 26%] Built target opencv_cudabgsegm
[ 26%] Building NVCC (Device) object modules/cudafilters/CMakeFiles/cuda_compile.dir/src/cuda/cuda_compile_generated_median_filter.cu.o
[ 26%] Building NVCC (Device) object modules/cudafilters/CMakeFiles/cuda_compile.dir/src/cuda/cuda_compile_generated_column_filter.32sc1.cu.o
[ 26%] Building NVCC (Device) object modules/cudafilters/CMakeFiles/cuda_compile.dir/src/cuda/cuda_compile_generated_column_filter.8uc4.cu.o
[ 26%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/torch/torch_importer.cpp.o
[ 26%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/torch/THDiskFile.cpp.o
[ 26%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/torch/THFile.cpp.o
[ 26%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/torch/THGeneral.cpp.o
[ 26%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/dnn.cpp.o
[ 27%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/layers/elementwise_layers.cpp.o
[ 27%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/layers/normalize_bbox_layer.cpp.o
[ 27%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/layers/slice_layer.cpp.o
[ 27%] Building NVCC (Device) object modules/cudawarping/CMakeFiles/cuda_compile.dir/src/cuda/cuda_compile_generated_resize.cu.o
[ 27%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/layers/split_layer.cpp.o
[ 27%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/layers/flatten_layer.cpp.o
[ 27%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/layers/recurrent_layers.cpp.o
[ 27%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/layers/layers_common.cpp.o
[ 27%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/layers/softmax_layer.cpp.o
[ 27%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/layers/fully_connected_layer.cpp.o
[ 27%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/layers/pooling_layer.cpp.o
[ 27%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/layers/convolution_layer.cpp.o
[ 27%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/layers/prior_box_layer.cpp.o
[ 27%] Building NVCC (Device) object modules/cudawarping/CMakeFiles/cuda_compile.dir/src/cuda/cuda_compile_generated_pyr_down.cu.o
[ 27%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/layers/scale_layer.cpp.o
[ 27%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/layers/blank_layer.cpp.o
[ 27%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/layers/concat_layer.cpp.o
[ 27%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/layers/permute_layer.cpp.o
[ 28%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/layers/padding_layer.cpp.o
Scanning dependencies of target opencv_cudawarping
[ 28%] Building CXX object modules/cudawarping/CMakeFiles/opencv_cudawarping.dir/src/remap.cpp.o
[ 28%] Building CXX object modules/cudawarping/CMakeFiles/opencv_cudawarping.dir/src/pyramids.cpp.o
[ 28%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/layers/lrn_layer.cpp.o
[ 28%] Building CXX object modules/cudawarping/CMakeFiles/opencv_cudawarping.dir/src/warp.cpp.o
[ 28%] Building CXX object modules/cudawarping/CMakeFiles/opencv_cudawarping.dir/src/resize.cpp.o
[ 28%] Building NVCC (Device) object modules/cudafilters/CMakeFiles/cuda_compile.dir/src/cuda/cuda_compile_generated_row_filter.16sc1.cu.o
[ 28%] Building NVCC (Device) object modules/cudafilters/CMakeFiles/cuda_compile.dir/src/cuda/cuda_compile_generated_row_filter.16sc4.cu.o
[ 28%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/layers/detection_output_layer.cpp.o
[ 28%] Linking CXX shared library ../../lib/libopencv_cudawarping.so
[ 28%] Built target opencv_cudawarping
Scanning dependencies of target opencv_shape
[ 28%] Building CXX object modules/shape/CMakeFiles/opencv_shape.dir/src/tps_trans.cpp.o
[ 28%] Building CXX object modules/shape/CMakeFiles/opencv_shape.dir/src/emdL1.cpp.o
[ 28%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/layers/batch_norm_layer.cpp.o
[ 28%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/layers/mvn_layer.cpp.o
[ 28%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/layers/max_unpooling_layer.cpp.o
[ 28%] Building CXX object modules/shape/CMakeFiles/opencv_shape.dir/src/haus_dis.cpp.o
[ 28%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/layers/reshape_layer.cpp.o
[ 28%] Building CXX object modules/shape/CMakeFiles/opencv_shape.dir/src/hist_cost.cpp.o
[ 28%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/layers/crop_layer.cpp.o
[ 28%] Building CXX object modules/shape/CMakeFiles/opencv_shape.dir/src/aff_trans.cpp.o
[ 28%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/layers/eltwise_layer.cpp.o
[ 28%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/layers/shift_layer.cpp.o
[ 28%] Building CXX object modules/shape/CMakeFiles/opencv_shape.dir/src/sc_dis.cpp.o
[ 28%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/init.cpp.o
[ 28%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/tensorflow/tf_importer.cpp.o
[ 28%] Building NVCC (Device) object modules/cudafilters/CMakeFiles/cuda_compile.dir/src/cuda/cuda_compile_generated_column_filter.16sc3.cu.o
[ 28%] Linking CXX shared library ../../lib/libopencv_shape.so
[ 28%] Built target opencv_shape
[ 28%] Building NVCC (Device) object modules/cudacodec/CMakeFiles/cuda_compile.dir/src/cuda/cuda_compile_generated_rgb_to_yv12.cu.o
[ 28%] Building NVCC (Device) object modules/cudacodec/CMakeFiles/cuda_compile.dir/src/cuda/cuda_compile_generated_nv12_to_rgb.cu.o
[ 28%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/tensorflow/tf_io.cpp.o
[ 28%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/halide_scheduler.cpp.o
[ 28%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/caffe/caffe_io.cpp.o
Scanning dependencies of target opencv_cudacodec
[ 28%] Building CXX object modules/cudacodec/CMakeFiles/opencv_cudacodec.dir/src/video_parser.cpp.o
[ 28%] Building CXX object modules/cudacodec/CMakeFiles/opencv_cudacodec.dir/src/cuvid_video_source.cpp.o
[ 28%] Building CXX object modules/cudacodec/CMakeFiles/opencv_cudacodec.dir/src/video_reader.cpp.o
[ 29%] Building CXX object modules/cudacodec/CMakeFiles/opencv_cudacodec.dir/src/video_source.cpp.o
[ 29%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/caffe/caffe_importer.cpp.o
[ 29%] Building CXX object modules/cudacodec/CMakeFiles/opencv_cudacodec.dir/src/thread.cpp.o
[ 29%] Building CXX object modules/cudacodec/CMakeFiles/opencv_cudacodec.dir/src/ffmpeg_video_source.cpp.o
[ 29%] Building CXX object modules/cudacodec/CMakeFiles/opencv_cudacodec.dir/src/frame_queue.cpp.o
[ 29%] Building CXX object modules/cudacodec/CMakeFiles/opencv_cudacodec.dir/src/video_writer.cpp.o
[ 29%] Building CXX object modules/cudacodec/CMakeFiles/opencv_cudacodec.dir/src/video_decoder.cpp.o
[ 30%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/op_halide.cpp.o
[ 30%] Linking CXX shared library ../../lib/libopencv_cudacodec.so
[ 30%] Built target opencv_cudacodec
Scanning dependencies of target opencv_highgui
[ 30%] Building CXX object modules/highgui/CMakeFiles/opencv_highgui.dir/src/window.cpp.o
[ 30%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/opencl_kernels_dnn.cpp.o
[ 30%] Linking CXX shared library ../../lib/libopencv_dnn.so
[ 30%] Built target opencv_dnn
[ 30%] Building CXX object modules/highgui/CMakeFiles/opencv_highgui.dir/src/roiSelector.cpp.o
[ 30%] Building CXX object modules/highgui/CMakeFiles/opencv_highgui.dir/src/window_gtk.cpp.o
[ 30%] Building NVCC (Device) object modules/cudafilters/CMakeFiles/cuda_compile.dir/src/cuda/cuda_compile_generated_filter2d.cu.o
[ 30%] Building NVCC (Device) object modules/cudafilters/CMakeFiles/cuda_compile.dir/src/cuda/cuda_compile_generated_row_filter.8uc4.cu.o
[ 30%] Linking CXX shared library ../../lib/libopencv_highgui.so
[ 30%] Built target opencv_highgui
Scanning dependencies of target opencv_ts
[ 31%] Building CXX object modules/ts/CMakeFiles/opencv_ts.dir/src/cuda_test.cpp.o
[ 31%] Building CXX object modules/ts/CMakeFiles/opencv_ts.dir/src/ts_gtest.cpp.o
[ 31%] Building CXX object modules/ts/CMakeFiles/opencv_ts.dir/src/cuda_perf.cpp.o
[ 31%] Building CXX object modules/ts/CMakeFiles/opencv_ts.dir/src/ts_func.cpp.o
[ 31%] Building CXX object modules/ts/CMakeFiles/opencv_ts.dir/src/ocl_perf.cpp.o
[ 31%] Building NVCC (Device) object modules/cudafilters/CMakeFiles/cuda_compile.dir/src/cuda/cuda_compile_generated_row_filter.16uc4.cu.o
[ 31%] Building CXX object modules/ts/CMakeFiles/opencv_ts.dir/src/ts_perf.cpp.o
[ 31%] Building CXX object modules/ts/CMakeFiles/opencv_ts.dir/src/ts_arrtest.cpp.o
[ 31%] Building CXX object modules/ts/CMakeFiles/opencv_ts.dir/src/ocl_test.cpp.o
[ 31%] Building CXX object modules/ts/CMakeFiles/opencv_ts.dir/src/ts.cpp.o
[ 31%] Building NVCC (Device) object modules/cudafilters/CMakeFiles/cuda_compile.dir/src/cuda/cuda_compile_generated_row_filter.32fc1.cu.o
[ 31%] Linking CXX static library ../../lib/libopencv_ts.a
[ 31%] Built target opencv_ts
[ 31%] Generating opencl_kernels_features2d.cpp, opencl_kernels_features2d.hpp
Scanning dependencies of target opencv_features2d
[ 31%] Building CXX object modules/features2d/CMakeFiles/opencv_features2d.dir/src/mser.cpp.o
[ 31%] Building CXX object modules/features2d/CMakeFiles/opencv_features2d.dir/src/dynamic.cpp.o
[ 31%] Building CXX object modules/features2d/CMakeFiles/opencv_features2d.dir/src/agast_score.cpp.o
[ 31%] Building CXX object modules/features2d/CMakeFiles/opencv_features2d.dir/src/feature2d.cpp.o
[ 31%] Building NVCC (Device) object modules/cudafilters/CMakeFiles/cuda_compile.dir/src/cuda/cuda_compile_generated_column_filter.32fc4.cu.o
[ 31%] Building CXX object modules/features2d/CMakeFiles/opencv_features2d.dir/src/main.cpp.o
[ 31%] Building CXX object modules/features2d/CMakeFiles/opencv_features2d.dir/src/keypoint.cpp.o
[ 31%] Building CXX object modules/features2d/CMakeFiles/opencv_features2d.dir/src/bagofwords.cpp.o
[ 31%] Building CXX object modules/features2d/CMakeFiles/opencv_features2d.dir/src/orb.cpp.o
[ 31%] Building NVCC (Device) object modules/cudafilters/CMakeFiles/cuda_compile.dir/src/cuda/cuda_compile_generated_row_filter.32fc3.cu.o
[ 31%] Building CXX object modules/features2d/CMakeFiles/opencv_features2d.dir/src/fast_score.cpp.o
[ 31%] Building CXX object modules/features2d/CMakeFiles/opencv_features2d.dir/src/akaze.cpp.o
[ 31%] Building CXX object modules/features2d/CMakeFiles/opencv_features2d.dir/src/fast.cpp.o
[ 31%] Building NVCC (Device) object modules/cudafilters/CMakeFiles/cuda_compile.dir/src/cuda/cuda_compile_generated_column_filter.16sc4.cu.o
[ 32%] Building CXX object modules/features2d/CMakeFiles/opencv_features2d.dir/src/evaluation.cpp.o
[ 32%] Building CXX object modules/features2d/CMakeFiles/opencv_features2d.dir/src/gftt.cpp.o
[ 32%] Building CXX object modules/features2d/CMakeFiles/opencv_features2d.dir/src/kaze.cpp.o
[ 32%] Building CXX object modules/features2d/CMakeFiles/opencv_features2d.dir/src/kaze/AKAZEFeatures.cpp.o
[ 32%] Building CXX object modules/features2d/CMakeFiles/opencv_features2d.dir/src/kaze/KAZEFeatures.cpp.o
[ 32%] Building CXX object modules/features2d/CMakeFiles/opencv_features2d.dir/src/kaze/nldiffusion_functions.cpp.o
[ 32%] Building CXX object modules/features2d/CMakeFiles/opencv_features2d.dir/src/kaze/fed.cpp.o
[ 32%] Building CXX object modules/features2d/CMakeFiles/opencv_features2d.dir/src/matchers.cpp.o
[ 32%] Building NVCC (Device) object modules/cudafilters/CMakeFiles/cuda_compile.dir/src/cuda/cuda_compile_generated_row_filter.32sc1.cu.o
[ 32%] Building CXX object modules/features2d/CMakeFiles/opencv_features2d.dir/src/draw.cpp.o
[ 32%] Building NVCC (Device) object modules/cudafilters/CMakeFiles/cuda_compile.dir/src/cuda/cuda_compile_generated_row_filter.32fc4.cu.o
[ 32%] Building CXX object modules/features2d/CMakeFiles/opencv_features2d.dir/src/agast.cpp.o
[ 32%] Building CXX object modules/features2d/CMakeFiles/opencv_features2d.dir/src/brisk.cpp.o
[ 32%] Building CXX object modules/features2d/CMakeFiles/opencv_features2d.dir/src/blobdetector.cpp.o
[ 32%] Building CXX object modules/features2d/CMakeFiles/opencv_features2d.dir/opencl_kernels_features2d.cpp.o
[ 32%] Linking CXX shared library ../../lib/libopencv_features2d.so
[ 32%] Built target opencv_features2d
Scanning dependencies of target opencv_annotation
[ 32%] Building CXX object apps/annotation/CMakeFiles/opencv_annotation.dir/opencv_annotation.cpp.o
[ 32%] Linking CXX executable ../../bin/opencv_annotation
Scanning dependencies of target opencv_visualisation
[ 32%] Building CXX object apps/visualisation/CMakeFiles/opencv_visualisation.dir/opencv_visualisation.cpp.o
[ 32%] Built target opencv_annotation
Scanning dependencies of target opencv_version
[ 32%] Building CXX object apps/version/CMakeFiles/opencv_version.dir/opencv_version.cpp.o
[ 32%] Linking CXX executable ../../bin/opencv_version
[ 32%] Built target opencv_version
Scanning dependencies of target example_dnn_ssd_mobilenet_object_detection
[ 32%] Building CXX object samples/dnn/CMakeFiles/example_dnn_ssd_mobilenet_object_detection.dir/ssd_mobilenet_object_detection.cpp.o
[ 32%] Linking CXX executable ../../bin/example_dnn-ssd_mobilenet_object_detection
[ 32%] Built target example_dnn_ssd_mobilenet_object_detection
Scanning dependencies of target example_dnn_ssd_object_detection
[ 32%] Building CXX object samples/dnn/CMakeFiles/example_dnn_ssd_object_detection.dir/ssd_object_detection.cpp.o
[ 32%] Linking CXX executable ../../bin/opencv_visualisation
[ 32%] Built target opencv_visualisation
Scanning dependencies of target example_dnn_squeezenet_halide
[ 32%] Building CXX object samples/dnn/CMakeFiles/example_dnn_squeezenet_halide.dir/squeezenet_halide.cpp.o
[ 33%] Building NVCC (Device) object modules/cudafilters/CMakeFiles/cuda_compile.dir/src/cuda/cuda_compile_generated_column_filter.32sc3.cu.o
[ 33%] Linking CXX executable ../../bin/example_dnn-ssd_object_detection
[ 33%] Built target example_dnn_ssd_object_detection
Scanning dependencies of target example_dnn_fcn_semsegm
[ 33%] Building CXX object samples/dnn/CMakeFiles/example_dnn_fcn_semsegm.dir/fcn_semsegm.cpp.o
[ 33%] Linking CXX executable ../../bin/example_dnn-squeezenet_halide
[ 33%] Built target example_dnn_squeezenet_halide
Scanning dependencies of target example_dnn_tf_inception
[ 33%] Building CXX object samples/dnn/CMakeFiles/example_dnn_tf_inception.dir/tf_inception.cpp.o
[ 33%] Linking CXX executable ../../bin/example_dnn-fcn_semsegm
[ 33%] Built target example_dnn_fcn_semsegm
Scanning dependencies of target example_dnn_caffe_googlenet
[ 33%] Building CXX object samples/dnn/CMakeFiles/example_dnn_caffe_googlenet.dir/caffe_googlenet.cpp.o
[ 33%] Linking CXX executable ../../bin/example_dnn-tf_inception
[ 33%] Built target example_dnn_tf_inception
Scanning dependencies of target example_dnn_torch_enet
[ 33%] Building CXX object samples/dnn/CMakeFiles/example_dnn_torch_enet.dir/torch_enet.cpp.o
[ 33%] Linking CXX executable ../../bin/example_dnn-caffe_googlenet
[ 33%] Built target example_dnn_caffe_googlenet
[ 33%] Building NVCC (Device) object modules/cudev/test/CMakeFiles/opencv_test_cudev.dir/opencv_test_cudev_generated_test_reduction.cu.o
[ 33%] Linking CXX executable ../../bin/example_dnn-torch_enet
[ 33%] Built target example_dnn_torch_enet
[ 33%] Building NVCC (Device) object modules/cudev/test/CMakeFiles/opencv_test_cudev.dir/opencv_test_cudev_generated_test_arithm_func.cu.o
[ 33%] Building NVCC (Device) object modules/cudev/test/CMakeFiles/opencv_test_cudev.dir/opencv_test_cudev_generated_test_pyramids.cu.o
[ 33%] Building NVCC (Device) object modules/cudev/test/CMakeFiles/opencv_test_cudev.dir/opencv_test_cudev_generated_test_cvt.cu.o
[ 33%] Building NVCC (Device) object modules/cudafilters/CMakeFiles/cuda_compile.dir/src/cuda/cuda_compile_generated_column_filter.8uc1.cu.o
[ 34%] Building NVCC (Device) object modules/cudev/test/CMakeFiles/opencv_test_cudev.dir/opencv_test_cudev_generated_test_cmp_op.cu.o
[ 34%] Building NVCC (Device) object modules/cudev/test/CMakeFiles/opencv_test_cudev.dir/opencv_test_cudev_generated_test_bitwize_op.cu.o
[ 34%] Building NVCC (Device) object modules/cudafilters/CMakeFiles/cuda_compile.dir/src/cuda/cuda_compile_generated_row_filter.32sc4.cu.o
[ 34%] Building NVCC (Device) object modules/cudev/test/CMakeFiles/opencv_test_cudev.dir/opencv_test_cudev_generated_test_warp.cu.o
[ 34%] Building NVCC (Device) object modules/cudev/test/CMakeFiles/opencv_test_cudev.dir/opencv_test_cudev_generated_test_integral.cu.o
[ 34%] Building NVCC (Device) object modules/cudafilters/CMakeFiles/cuda_compile.dir/src/cuda/cuda_compile_generated_row_filter.8uc3.cu.o
[ 34%] Building NVCC (Device) object modules/cudev/test/CMakeFiles/opencv_test_cudev.dir/opencv_test_cudev_generated_test_split_merge.cu.o
[ 34%] Building NVCC (Device) object modules/cudev/test/CMakeFiles/opencv_test_cudev.dir/opencv_test_cudev_generated_test_deriv.cu.o
[ 34%] Building NVCC (Device) object modules/cudev/test/CMakeFiles/opencv_test_cudev.dir/opencv_test_cudev_generated_test_arithm_op.cu.o
[ 34%] Building NVCC (Device) object modules/cudev/test/CMakeFiles/opencv_test_cudev.dir/opencv_test_cudev_generated_test_color_cvt.cu.o
[ 34%] Building NVCC (Device) object modules/cudafilters/CMakeFiles/cuda_compile.dir/src/cuda/cuda_compile_generated_column_filter.32fc3.cu.o
[ 34%] Building NVCC (Device) object modules/cudev/test/CMakeFiles/opencv_test_cudev.dir/opencv_test_cudev_generated_transpose.cu.o
[ 34%] Building NVCC (Device) object modules/cudafilters/CMakeFiles/cuda_compile.dir/src/cuda/cuda_compile_generated_column_filter.32fc1.cu.o
[ 34%] Building NVCC (Device) object modules/cudev/test/CMakeFiles/opencv_test_cudev.dir/opencv_test_cudev_generated_test_lut.cu.o
Scanning dependencies of target opencv_test_core
[ 34%] Building CXX object modules/core/CMakeFiles/opencv_test_core.dir/test/test_conjugate_gradient.cpp.o
[ 34%] Building CXX object modules/core/CMakeFiles/opencv_test_core.dir/test/test_mat.cpp.o
Scanning dependencies of target opencv_test_cudev
[ 34%] Building CXX object modules/cudev/test/CMakeFiles/opencv_test_cudev.dir/test_main.cpp.o
[ 34%] Linking CXX executable ../../../bin/opencv_test_cudev
[ 34%] Built target opencv_test_cudev
Scanning dependencies of target opencv_perf_core
[ 34%] Building CXX object modules/core/CMakeFiles/opencv_perf_core.dir/perf/perf_bitwise.cpp.o
[ 34%] Building CXX object modules/core/CMakeFiles/opencv_test_core.dir/test/test_operations.cpp.o
[ 34%] Building NVCC (Device) object modules/cudafilters/CMakeFiles/cuda_compile.dir/src/cuda/cuda_compile_generated_column_filter.16uc4.cu.o
[ 34%] Building CXX object modules/core/CMakeFiles/opencv_perf_core.dir/perf/perf_addWeighted.cpp.o
[ 34%] Building CXX object modules/core/CMakeFiles/opencv_perf_core.dir/perf/cuda/perf_gpumat.cpp.o
[ 34%] Building CXX object modules/core/CMakeFiles/opencv_perf_core.dir/perf/perf_arithm.cpp.o
[ 34%] Building NVCC (Device) object modules/cudafilters/CMakeFiles/cuda_compile.dir/src/cuda/cuda_compile_generated_row_filter.16uc3.cu.o
[ 34%] Building CXX object modules/core/CMakeFiles/opencv_test_core.dir/test/test_utils.cpp.o
[ 34%] Building CXX object modules/core/CMakeFiles/opencv_perf_core.dir/perf/perf_sort.cpp.o
[ 34%] Building CXX object modules/core/CMakeFiles/opencv_test_core.dir/test/test_rand.cpp.o
[ 35%] Building CXX object modules/core/CMakeFiles/opencv_perf_core.dir/perf/perf_cvround.cpp.o
[ 35%] Building CXX object modules/core/CMakeFiles/opencv_test_core.dir/test/test_downhill_simplex.cpp.o
[ 35%] Building CXX object modules/core/CMakeFiles/opencv_perf_core.dir/perf/perf_abs.cpp.o
[ 35%] Building CXX object modules/core/CMakeFiles/opencv_test_core.dir/test/test_rotatedrect.cpp.o
[ 36%] Building CXX object modules/core/CMakeFiles/opencv_test_core.dir/test/test_misc.cpp.o
[ 36%] Building CXX object modules/core/CMakeFiles/opencv_perf_core.dir/perf/perf_io_base64.cpp.o
[ 36%] Building CXX object modules/core/CMakeFiles/opencv_test_core.dir/test/test_intrin.cpp.o
[ 36%] Building CXX object modules/core/CMakeFiles/opencv_perf_core.dir/perf/perf_math.cpp.o
[ 36%] Building CXX object modules/core/CMakeFiles/opencv_perf_core.dir/perf/perf_reduce.cpp.o
[ 36%] Building NVCC (Device) object modules/cudafilters/CMakeFiles/cuda_compile.dir/src/cuda/cuda_compile_generated_column_filter.16uc1.cu.o
[ 36%] Building CXX object modules/core/CMakeFiles/opencv_perf_core.dir/perf/perf_umat.cpp.o
[ 36%] Building CXX object modules/core/CMakeFiles/opencv_perf_core.dir/perf/perf_minmaxloc.cpp.o
[ 36%] Building CXX object modules/core/CMakeFiles/opencv_perf_core.dir/perf/perf_dft.cpp.o
[ 36%] Building CXX object modules/core/CMakeFiles/opencv_perf_core.dir/perf/perf_main.cpp.o
[ 36%] Building CXX object modules/core/CMakeFiles/opencv_perf_core.dir/perf/perf_merge.cpp.o
[ 36%] Building CXX object modules/core/CMakeFiles/opencv_test_core.dir/test/test_concatenation.cpp.o
[ 36%] Building CXX object modules/core/CMakeFiles/opencv_perf_core.dir/perf/perf_dot.cpp.o
[ 36%] Building CXX object modules/core/CMakeFiles/opencv_perf_core.dir/perf/perf_convertTo.cpp.o
[ 36%] Building CXX object modules/core/CMakeFiles/opencv_test_core.dir/test/test_lpsolver.cpp.o
[ 36%] Building CXX object modules/core/CMakeFiles/opencv_perf_core.dir/perf/perf_norm.cpp.o
[ 36%] Building CXX object modules/core/CMakeFiles/opencv_perf_core.dir/perf/perf_stat.cpp.o
[ 36%] Building CXX object modules/core/CMakeFiles/opencv_test_core.dir/test/test_umat.cpp.o
[ 36%] Building NVCC (Device) object modules/cudafilters/CMakeFiles/cuda_compile.dir/src/cuda/cuda_compile_generated_column_filter.32sc4.cu.o
[ 36%] Building CXX object modules/core/CMakeFiles/opencv_perf_core.dir/perf/perf_mat.cpp.o
[ 36%] Building CXX object modules/core/CMakeFiles/opencv_perf_core.dir/perf/perf_inRange.cpp.o
[ 37%] Building CXX object modules/core/CMakeFiles/opencv_perf_core.dir/perf/opencl/perf_bufferpool.cpp.o
[ 37%] Building CXX object modules/core/CMakeFiles/opencv_perf_core.dir/perf/opencl/perf_arithm.cpp.o
[ 37%] Building CXX object modules/core/CMakeFiles/opencv_perf_core.dir/perf/opencl/perf_channels.cpp.o
[ 37%] Building CXX object modules/core/CMakeFiles/opencv_perf_core.dir/perf/opencl/perf_gemm.cpp.o
[ 37%] Building CXX object modules/core/CMakeFiles/opencv_perf_core.dir/perf/opencl/perf_dxt.cpp.o
[ 37%] Building CXX object modules/core/CMakeFiles/opencv_perf_core.dir/perf/opencl/perf_usage_flags.cpp.o
Scanning dependencies of target opencv_perf_cudaarithm
[ 37%] Building CXX object modules/cudaarithm/CMakeFiles/opencv_perf_cudaarithm.dir/perf/perf_arithm.cpp.o
[ 37%] Building CXX object modules/core/CMakeFiles/opencv_perf_core.dir/perf/opencl/perf_matop.cpp.o
[ 37%] Building CXX object modules/core/CMakeFiles/opencv_test_core.dir/test/test_hal_core.cpp.o
[ 37%] Building CXX object modules/core/CMakeFiles/opencv_perf_core.dir/perf/perf_split.cpp.o
[ 37%] Building CXX object modules/cudaarithm/CMakeFiles/opencv_perf_cudaarithm.dir/perf/perf_reductions.cpp.o
[ 37%] Building CXX object modules/core/CMakeFiles/opencv_test_core.dir/test/test_ippasync.cpp.o
[ 37%] Building CXX object modules/core/CMakeFiles/opencv_perf_core.dir/perf/perf_compare.cpp.o
[ 37%] Building CXX object modules/core/CMakeFiles/opencv_test_core.dir/test/test_dxt.cpp.o
[ 37%] Building CXX object modules/core/CMakeFiles/opencv_perf_core.dir/perf/perf_lut.cpp.o
[ 37%] Building CXX object modules/core/CMakeFiles/opencv_test_core.dir/test/test_io.cpp.o
[ 37%] Linking CXX executable ../../bin/opencv_perf_core
[ 37%] Built target opencv_perf_core
Scanning dependencies of target opencv_test_cudaarithm
[ 37%] Building CXX object modules/cudaarithm/CMakeFiles/opencv_test_cudaarithm.dir/test/test_opengl.cpp.o
[ 37%] Building CXX object modules/cudaarithm/CMakeFiles/opencv_perf_cudaarithm.dir/perf/perf_element_operations.cpp.o
[ 37%] Building CXX object modules/cudaarithm/CMakeFiles/opencv_test_cudaarithm.dir/test/test_element_operations.cpp.o
[ 37%] Building CXX object modules/core/CMakeFiles/opencv_test_core.dir/test/test_ptr.cpp.o
[ 37%] Building CXX object modules/core/CMakeFiles/opencv_test_core.dir/test/ocl/test_dft.cpp.o
[ 37%] Building CXX object modules/core/CMakeFiles/opencv_test_core.dir/test/ocl/test_image2d.cpp.o
[ 37%] Building CXX object modules/core/CMakeFiles/opencv_test_core.dir/test/ocl/test_channels.cpp.o
[ 37%] Building NVCC (Device) object modules/cudafilters/CMakeFiles/cuda_compile.dir/src/cuda/cuda_compile_generated_column_filter.16uc3.cu.o
[ 37%] Building CXX object modules/core/CMakeFiles/opencv_test_core.dir/test/ocl/test_matrix_operation.cpp.o
[ 37%] Building CXX object modules/core/CMakeFiles/opencv_test_core.dir/test/ocl/test_gemm.cpp.o
[ 38%] Building CXX object modules/core/CMakeFiles/opencv_test_core.dir/test/ocl/test_matrix_expr.cpp.o
[ 38%] Building CXX object modules/core/CMakeFiles/opencv_test_core.dir/test/ocl/test_arithm.cpp.o
[ 38%] Building CXX object modules/cudaarithm/CMakeFiles/opencv_perf_cudaarithm.dir/perf/perf_core.cpp.o
[ 38%] Building CXX object modules/core/CMakeFiles/opencv_test_core.dir/test/test_countnonzero.cpp.o
[ 38%] Building CXX object modules/cudaarithm/CMakeFiles/opencv_test_cudaarithm.dir/test/test_gpumat.cpp.o
[ 38%] Building CXX object modules/core/CMakeFiles/opencv_test_core.dir/test/test_main.cpp.o
[ 38%] Building CXX object modules/core/CMakeFiles/opencv_test_core.dir/test/test_eigen.cpp.o
[ 38%] Building CXX object modules/cudaarithm/CMakeFiles/opencv_perf_cudaarithm.dir/perf/perf_main.cpp.o
[ 39%] Linking CXX executable ../../bin/opencv_perf_cudaarithm
[ 39%] Built target opencv_perf_cudaarithm
Scanning dependencies of target opencv_test_flann
[ 39%] Building CXX object modules/flann/CMakeFiles/opencv_test_flann.dir/test/test_lshtable_badarg.cpp.o
[ 39%] Building CXX object modules/core/CMakeFiles/opencv_test_core.dir/test/test_ds.cpp.o
[ 39%] Building CXX object modules/flann/CMakeFiles/opencv_test_flann.dir/test/test_main.cpp.o
[ 39%] Building CXX object modules/cudaarithm/CMakeFiles/opencv_test_cudaarithm.dir/test/test_core.cpp.o
[ 39%] Linking CXX executable ../../bin/opencv_test_flann
[ 39%] Built target opencv_test_flann
Scanning dependencies of target opencv_perf_imgproc
[ 39%] Building CXX object modules/imgproc/CMakeFiles/opencv_perf_imgproc.dir/perf/perf_bilateral.cpp.o
[ 39%] Building CXX object modules/core/CMakeFiles/opencv_test_core.dir/test/test_arithm.cpp.o
[ 39%] Building CXX object modules/imgproc/CMakeFiles/opencv_perf_imgproc.dir/perf/perf_threshold.cpp.o
[ 39%] Building CXX object modules/cudaarithm/CMakeFiles/opencv_test_cudaarithm.dir/test/test_stream.cpp.o
[ 39%] Building CXX object modules/imgproc/CMakeFiles/opencv_perf_imgproc.dir/perf/perf_accumulate.cpp.o
[ 39%] Building CXX object modules/cudaarithm/CMakeFiles/opencv_test_cudaarithm.dir/test/test_reductions.cpp.o
[ 39%] Building CXX object modules/imgproc/CMakeFiles/opencv_perf_imgproc.dir/perf/perf_sepfilters.cpp.o
[ 39%] Building CXX object modules/core/CMakeFiles/opencv_test_core.dir/test/test_math.cpp.o
[ 39%] Building NVCC (Device) object modules/cudafilters/CMakeFiles/cuda_compile.dir/src/cuda/cuda_compile_generated_row_filter.16sc3.cu.o
[ 39%] Building CXX object modules/imgproc/CMakeFiles/opencv_perf_imgproc.dir/perf/perf_cvt_color.cpp.o
[ 39%] Building CXX object modules/cudaarithm/CMakeFiles/opencv_test_cudaarithm.dir/test/test_buffer_pool.cpp.o
[ 40%] Building CXX object modules/cudaarithm/CMakeFiles/opencv_test_cudaarithm.dir/test/test_main.cpp.o
[ 40%] Building CXX object modules/imgproc/CMakeFiles/opencv_perf_imgproc.dir/perf/perf_morph.cpp.o
[ 40%] Building CXX object modules/cudaarithm/CMakeFiles/opencv_test_cudaarithm.dir/test/test_arithm.cpp.o
[ 40%] Linking CXX executable ../../bin/opencv_test_cudaarithm
[ 40%] Built target opencv_test_cudaarithm
Scanning dependencies of target opencv_test_imgproc
[ 40%] Building CXX object modules/imgproc/CMakeFiles/opencv_test_imgproc.dir/test/test_moments.cpp.o
[ 40%] Linking CXX executable ../../bin/opencv_test_core
[ 40%] Built target opencv_test_core
[ 40%] Building CXX object modules/imgproc/CMakeFiles/opencv_test_imgproc.dir/test/test_imgwarp_strict.cpp.o
[ 40%] Building CXX object modules/imgproc/CMakeFiles/opencv_perf_imgproc.dir/perf/perf_matchTemplate.cpp.o
[ 40%] Building CXX object modules/imgproc/CMakeFiles/opencv_test_imgproc.dir/test/test_lsd.cpp.o
[ 40%] Building CXX object modules/imgproc/CMakeFiles/opencv_test_imgproc.dir/test/test_fitellipse.cpp.o
[ 40%] Building CXX object modules/imgproc/CMakeFiles/opencv_test_imgproc.dir/test/test_pc.cpp.o
[ 40%] Building CXX object modules/imgproc/CMakeFiles/opencv_perf_imgproc.dir/perf/perf_moments.cpp.o
[ 40%] Building CXX object modules/imgproc/CMakeFiles/opencv_test_imgproc.dir/test/test_imgproc_umat.cpp.o
[ 40%] Building CXX object modules/imgproc/CMakeFiles/opencv_test_imgproc.dir/test/test_drawing.cpp.o
[ 40%] Building CXX object modules/imgproc/CMakeFiles/opencv_test_imgproc.dir/test/test_cvtyuv.cpp.o
[ 41%] Building CXX object modules/imgproc/CMakeFiles/opencv_perf_imgproc.dir/perf/perf_remap.cpp.o
[ 41%] Building CXX object modules/imgproc/CMakeFiles/opencv_test_imgproc.dir/test/test_boundingrect.cpp.o
[ 42%] Building CXX object modules/imgproc/CMakeFiles/opencv_test_imgproc.dir/test/test_approxpoly.cpp.o
[ 42%] Building CXX object modules/imgproc/CMakeFiles/opencv_test_imgproc.dir/test/test_color.cpp.o
[ 42%] Building CXX object modules/imgproc/CMakeFiles/opencv_perf_imgproc.dir/perf/perf_integral.cpp.o
[ 42%] Building CXX object modules/imgproc/CMakeFiles/opencv_test_imgproc.dir/test/test_contours.cpp.o
[ 42%] Building CXX object modules/imgproc/CMakeFiles/opencv_test_imgproc.dir/test/test_bilateral_filter.cpp.o
[ 42%] Building CXX object modules/imgproc/CMakeFiles/opencv_perf_imgproc.dir/perf/perf_houghLines.cpp.o
[ 42%] Building CXX object modules/imgproc/CMakeFiles/opencv_test_imgproc.dir/test/test_houghLines.cpp.o
[ 42%] Building CXX object modules/imgproc/CMakeFiles/opencv_test_imgproc.dir/test/test_watershed.cpp.o
[ 42%] Building NVCC (Device) object modules/cudafilters/CMakeFiles/cuda_compile.dir/src/cuda/cuda_compile_generated_row_filter.16uc1.cu.o
[ 42%] Building CXX object modules/imgproc/CMakeFiles/opencv_perf_imgproc.dir/perf/perf_phasecorr.cpp.o
[ 42%] Building CXX object modules/imgproc/CMakeFiles/opencv_test_imgproc.dir/test/test_templmatch.cpp.o
[ 42%] Building CXX object modules/imgproc/CMakeFiles/opencv_test_imgproc.dir/test/test_filter.cpp.o
[ 42%] Building CXX object modules/imgproc/CMakeFiles/opencv_test_imgproc.dir/test/test_floodfill.cpp.o
[ 42%] Building CXX object modules/imgproc/CMakeFiles/opencv_perf_imgproc.dir/perf/perf_main.cpp.o
[ 42%] Building CXX object modules/imgproc/CMakeFiles/opencv_perf_imgproc.dir/perf/perf_corners.cpp.o
[ 42%] Building CXX object modules/imgproc/CMakeFiles/opencv_test_imgproc.dir/test/test_intersection.cpp.o
[ 42%] Building CXX object modules/imgproc/CMakeFiles/opencv_test_imgproc.dir/test/test_histograms.cpp.o
[ 42%] Building CXX object modules/imgproc/CMakeFiles/opencv_test_imgproc.dir/test/test_imgwarp.cpp.o
[ 42%] Building CXX object modules/imgproc/CMakeFiles/opencv_perf_imgproc.dir/perf/perf_floodfill.cpp.o
[ 42%] Building CXX object modules/imgproc/CMakeFiles/opencv_test_imgproc.dir/test/test_canny.cpp.o
[ 42%] Building CXX object modules/imgproc/CMakeFiles/opencv_perf_imgproc.dir/perf/perf_filter2d.cpp.o
[ 42%] Building CXX object modules/imgproc/CMakeFiles/opencv_test_imgproc.dir/test/test_connectedcomponents.cpp.o
[ 42%] Building CXX object modules/imgproc/CMakeFiles/opencv_test_imgproc.dir/test/ocl/test_filter2d.cpp.o
[ 42%] Building CXX object modules/imgproc/CMakeFiles/opencv_test_imgproc.dir/test/ocl/test_imgproc.cpp.o
[ 42%] Building CXX object modules/imgproc/CMakeFiles/opencv_perf_imgproc.dir/perf/perf_blur.cpp.o
[ 43%] Building CXX object modules/imgproc/CMakeFiles/opencv_test_imgproc.dir/test/ocl/test_warp.cpp.o
[ 43%] Building CXX object modules/imgproc/CMakeFiles/opencv_test_imgproc.dir/test/ocl/test_sepfilter2D.cpp.o
[ 43%] Building NVCC (Device) object modules/cudafilters/CMakeFiles/cuda_compile.dir/src/cuda/cuda_compile_generated_column_filter.16sc1.cu.o
[ 43%] Building CXX object modules/imgproc/CMakeFiles/opencv_test_imgproc.dir/test/ocl/test_blend.cpp.o
[ 43%] Building CXX object modules/imgproc/CMakeFiles/opencv_test_imgproc.dir/test/ocl/test_color.cpp.o
[ 43%] Building CXX object modules/imgproc/CMakeFiles/opencv_test_imgproc.dir/test/ocl/test_boxfilter.cpp.o
[ 43%] Building CXX object modules/imgproc/CMakeFiles/opencv_test_imgproc.dir/test/ocl/test_filters.cpp.o
[ 43%] Building CXX object modules/imgproc/CMakeFiles/opencv_test_imgproc.dir/test/ocl/test_histogram.cpp.o
[ 43%] Building CXX object modules/imgproc/CMakeFiles/opencv_perf_imgproc.dir/perf/perf_histogram.cpp.o
[ 43%] Building CXX object modules/imgproc/CMakeFiles/opencv_test_imgproc.dir/test/ocl/test_gftt.cpp.o
[ 43%] Building CXX object modules/imgproc/CMakeFiles/opencv_test_imgproc.dir/test/ocl/test_houghlines.cpp.o
[ 43%] Building CXX object modules/imgproc/CMakeFiles/opencv_test_imgproc.dir/test/ocl/test_medianfilter.cpp.o
[ 43%] Building CXX object modules/imgproc/CMakeFiles/opencv_test_imgproc.dir/test/ocl/test_canny.cpp.o
[ 43%] Building CXX object modules/imgproc/CMakeFiles/opencv_test_imgproc.dir/test/ocl/test_accumulate.cpp.o
[ 43%] Building CXX object modules/imgproc/CMakeFiles/opencv_perf_imgproc.dir/perf/perf_warp.cpp.o
[ 43%] Building CXX object modules/imgproc/CMakeFiles/opencv_test_imgproc.dir/test/ocl/test_match_template.cpp.o
[ 43%] Building CXX object modules/imgproc/CMakeFiles/opencv_test_imgproc.dir/test/ocl/test_pyramids.cpp.o
[ 43%] Building CXX object modules/imgproc/CMakeFiles/opencv_test_imgproc.dir/test/test_grabcut.cpp.o
[ 44%] Building CXX object modules/imgproc/CMakeFiles/opencv_test_imgproc.dir/test/test_thresh.cpp.o
[ 44%] Building CXX object modules/imgproc/CMakeFiles/opencv_test_imgproc.dir/test/test_distancetransform.cpp.o
[ 44%] Building CXX object modules/imgproc/CMakeFiles/opencv_test_imgproc.dir/test/test_goodfeaturetotrack.cpp.o
[ 44%] Building CXX object modules/imgproc/CMakeFiles/opencv_perf_imgproc.dir/perf/perf_pyramids.cpp.o
[ 44%] Building CXX object modules/imgproc/CMakeFiles/opencv_test_imgproc.dir/test/test_main.cpp.o
[ 44%] Building CXX object modules/imgproc/CMakeFiles/opencv_test_imgproc.dir/test/test_convhull.cpp.o
[ 44%] Building CXX object modules/imgproc/CMakeFiles/opencv_test_imgproc.dir/test/test_emd.cpp.o
[ 44%] Building CXX object modules/imgproc/CMakeFiles/opencv_perf_imgproc.dir/perf/perf_goodFeaturesToTrack.cpp.o
[ 44%] Building CXX object modules/imgproc/CMakeFiles/opencv_perf_imgproc.dir/perf/opencl/perf_accumulate.cpp.o
[ 44%] Building NVCC (Device) object modules/cudafilters/CMakeFiles/cuda_compile.dir/src/cuda/cuda_compile_generated_row_filter.8uc1.cu.o
[ 44%] Building CXX object modules/imgproc/CMakeFiles/opencv_perf_imgproc.dir/perf/opencl/perf_matchTemplate.cpp.o
[ 44%] Building CXX object modules/imgproc/CMakeFiles/opencv_perf_imgproc.dir/perf/opencl/perf_moments.cpp.o
[ 44%] Linking CXX executable ../../bin/opencv_test_imgproc
[ 45%] Building CXX object modules/imgproc/CMakeFiles/opencv_perf_imgproc.dir/perf/opencl/perf_pyramid.cpp.o
[ 45%] Built target opencv_test_imgproc
Scanning dependencies of target opencv_test_ml
[ 45%] Building CXX object modules/ml/CMakeFiles/opencv_test_ml.dir/test/test_lr.cpp.o
[ 45%] Building CXX object modules/ml/CMakeFiles/opencv_test_ml.dir/test/test_mltests2.cpp.o
[ 45%] Building CXX object modules/imgproc/CMakeFiles/opencv_perf_imgproc.dir/perf/opencl/perf_imgproc.cpp.o
[ 45%] Building CXX object modules/ml/CMakeFiles/opencv_test_ml.dir/test/test_emknearestkmeans.cpp.o
[ 45%] Building CXX object modules/ml/CMakeFiles/opencv_test_ml.dir/test/test_svmsgd.cpp.o
[ 45%] Building CXX object modules/ml/CMakeFiles/opencv_test_ml.dir/test/test_gbttest.cpp.o
[ 45%] Building CXX object modules/ml/CMakeFiles/opencv_test_ml.dir/test/test_save_load.cpp.o
[ 45%] Building CXX object modules/ml/CMakeFiles/opencv_test_ml.dir/test/test_svmtrainauto.cpp.o
[ 45%] Building CXX object modules/ml/CMakeFiles/opencv_test_ml.dir/test/test_mltests.cpp.o
[ 45%] Building CXX object modules/ml/CMakeFiles/opencv_test_ml.dir/test/test_main.cpp.o
Scanning dependencies of target opencv_perf_objdetect
[ 45%] Building CXX object modules/objdetect/CMakeFiles/opencv_perf_objdetect.dir/perf/perf_main.cpp.o
[ 45%] Building CXX object modules/imgproc/CMakeFiles/opencv_perf_imgproc.dir/perf/opencl/perf_houghLines.cpp.o
[ 46%] Linking CXX executable ../../bin/opencv_test_ml
[ 46%] Building CXX object modules/imgproc/CMakeFiles/opencv_perf_imgproc.dir/perf/opencl/perf_gftt.cpp.o
[ 47%] Building CXX object modules/objdetect/CMakeFiles/opencv_perf_objdetect.dir/perf/opencl/perf_cascades.cpp.o
[ 47%] Built target opencv_test_ml
Scanning dependencies of target opencv_test_objdetect
[ 47%] Building CXX object modules/objdetect/CMakeFiles/opencv_test_objdetect.dir/test/opencl/test_hogdetector.cpp.o
[ 47%] Building CXX object modules/imgproc/CMakeFiles/opencv_perf_imgproc.dir/perf/opencl/perf_color.cpp.o
[ 47%] Building CXX object modules/objdetect/CMakeFiles/opencv_perf_objdetect.dir/perf/opencl/perf_hogdetect.cpp.o
[ 47%] Building CXX object modules/objdetect/CMakeFiles/opencv_test_objdetect.dir/test/test_cascadeandhog.cpp.o
[ 47%] Building CXX object modules/imgproc/CMakeFiles/opencv_perf_imgproc.dir/perf/opencl/perf_blend.cpp.o
[ 47%] Linking CXX executable ../../bin/opencv_perf_objdetect
[ 47%] Built target opencv_perf_objdetect
Scanning dependencies of target opencv_test_video
[ 47%] Building CXX object modules/video/CMakeFiles/opencv_test_video.dir/test/test_kalman.cpp.o
[ 47%] Building CXX object modules/imgproc/CMakeFiles/opencv_perf_imgproc.dir/perf/opencl/perf_3vs4.cpp.o
[ 47%] Building CXX object modules/video/CMakeFiles/opencv_test_video.dir/test/test_accum.cpp.o
[ 47%] Building CXX object modules/imgproc/CMakeFiles/opencv_perf_imgproc.dir/perf/opencl/perf_imgwarp.cpp.o
[ 47%] Building CXX object modules/objdetect/CMakeFiles/opencv_test_objdetect.dir/test/test_main.cpp.o
[ 47%] Building CXX object modules/video/CMakeFiles/opencv_test_video.dir/test/test_estimaterigid.cpp.o
[ 47%] Building NVCC (Device) object modules/cudafilters/CMakeFiles/cuda_compile.dir/src/cuda/cuda_compile_generated_row_filter.32sc3.cu.o
[ 47%] Building CXX object modules/imgproc/CMakeFiles/opencv_perf_imgproc.dir/perf/opencl/perf_filters.cpp.o
[ 47%] Linking CXX executable ../../bin/opencv_test_objdetect
[ 47%] Built target opencv_test_objdetect
Scanning dependencies of target opencv_perf_video
[ 47%] Building CXX object modules/video/CMakeFiles/opencv_perf_video.dir/perf/perf_optflowpyrlk.cpp.o
[ 47%] Building CXX object modules/imgproc/CMakeFiles/opencv_perf_imgproc.dir/perf/perf_spatialgradient.cpp.o
[ 48%] Building CXX object modules/video/CMakeFiles/opencv_test_video.dir/test/test_tvl1optflow.cpp.o
[ 48%] Building CXX object modules/video/CMakeFiles/opencv_test_video.dir/test/test_camshift.cpp.o
[ 48%] Building CXX object modules/video/CMakeFiles/opencv_test_video.dir/test/test_ecc.cpp.o
[ 48%] Building CXX object modules/imgproc/CMakeFiles/opencv_perf_imgproc.dir/perf/perf_canny.cpp.o
[ 48%] Building CXX object modules/video/CMakeFiles/opencv_perf_video.dir/perf/perf_ecc.cpp.o
[ 48%] Building CXX object modules/imgproc/CMakeFiles/opencv_perf_imgproc.dir/perf/perf_distanceTransform.cpp.o
[ 48%] Building CXX object modules/video/CMakeFiles/opencv_test_video.dir/test/ocl/test_optflow_tvl1flow.cpp.o
[ 48%] Building CXX object modules/video/CMakeFiles/opencv_test_video.dir/test/ocl/test_bgfg_mog2.cpp.o
[ 48%] Building CXX object modules/video/CMakeFiles/opencv_perf_video.dir/perf/perf_tvl1optflow.cpp.o
[ 48%] Building CXX object modules/video/CMakeFiles/opencv_test_video.dir/test/ocl/test_optflowpyrlk.cpp.o
[ 48%] Building CXX object modules/video/CMakeFiles/opencv_test_video.dir/test/ocl/test_optflow_farneback.cpp.o
[ 48%] Building CXX object modules/imgproc/CMakeFiles/opencv_perf_imgproc.dir/perf/perf_resize.cpp.o
[ 48%] Building CXX object modules/video/CMakeFiles/opencv_test_video.dir/test/test_optflowpyrlk.cpp.o
[ 48%] Building CXX object modules/video/CMakeFiles/opencv_perf_video.dir/perf/perf_main.cpp.o
[ 48%] Building CXX object modules/video/CMakeFiles/opencv_test_video.dir/test/test_main.cpp.o
[ 48%] Building CXX object modules/video/CMakeFiles/opencv_perf_video.dir/perf/opencl/perf_optflow_pyrlk.cpp.o
[ 48%] Linking CXX executable ../../bin/opencv_test_video
[ 48%] Built target opencv_test_video
Scanning dependencies of target opencv_perf_cudabgsegm
[ 48%] Building CXX object modules/cudabgsegm/CMakeFiles/opencv_perf_cudabgsegm.dir/perf/perf_main.cpp.o
[ 48%] Building CXX object modules/video/CMakeFiles/opencv_perf_video.dir/perf/opencl/perf_optflow_dualTVL1.cpp.o
[ 48%] Linking CXX executable ../../bin/opencv_perf_imgproc
[ 48%] Built target opencv_perf_imgproc
[ 48%] Building CXX object modules/cudabgsegm/CMakeFiles/opencv_perf_cudabgsegm.dir/perf/perf_bgsegm.cpp.o
[ 49%] Building NVCC (Device) object modules/cudafilters/CMakeFiles/cuda_compile.dir/src/cuda/cuda_compile_generated_column_filter.8uc3.cu.o
[ 49%] Building CXX object modules/video/CMakeFiles/opencv_perf_video.dir/perf/opencl/perf_optflow_farneback.cpp.o
[ 49%] Building CXX object modules/video/CMakeFiles/opencv_perf_video.dir/perf/opencl/perf_bgfg_mog2.cpp.o
[ 49%] Building CXX object modules/video/CMakeFiles/opencv_perf_video.dir/perf/opencl/perf_motempl.cpp.o
[ 49%] Linking CXX executable ../../bin/opencv_perf_video
[ 49%] Linking CXX executable ../../bin/opencv_perf_cudabgsegm
[ 49%] Built target opencv_perf_video
Scanning dependencies of target opencv_test_cudabgsegm
[ 49%] Building CXX object modules/cudabgsegm/CMakeFiles/opencv_test_cudabgsegm.dir/test/test_bgsegm.cpp.o
[ 49%] Built target opencv_perf_cudabgsegm
[ 49%] Building CXX object modules/cudabgsegm/CMakeFiles/opencv_test_cudabgsegm.dir/test/test_main.cpp.o
Scanning dependencies of target opencv_perf_cudawarping
[ 49%] Building CXX object modules/cudawarping/CMakeFiles/opencv_perf_cudawarping.dir/perf/perf_warping.cpp.o
[ 49%] Linking CXX executable ../../bin/opencv_test_cudabgsegm
[ 49%] Built target opencv_test_cudabgsegm
Scanning dependencies of target opencv_test_cudawarping
[ 49%] Building CXX object modules/cudawarping/CMakeFiles/opencv_test_cudawarping.dir/test/test_warp_affine.cpp.o
[ 49%] Building CXX object modules/cudawarping/CMakeFiles/opencv_perf_cudawarping.dir/perf/perf_main.cpp.o
[ 49%] Building CXX object modules/cudawarping/CMakeFiles/opencv_test_cudawarping.dir/test/test_warp_perspective.cpp.o
[ 49%] Building CXX object modules/cudawarping/CMakeFiles/opencv_test_cudawarping.dir/test/test_remap.cpp.o
[ 49%] Linking CXX executable ../../bin/opencv_perf_cudawarping
[ 49%] Built target opencv_perf_cudawarping
Scanning dependencies of target opencv_perf_dnn
[ 49%] Building CXX object modules/dnn/CMakeFiles/opencv_perf_dnn.dir/perf/perf_halide_net.cpp.o
[ 49%] Building CXX object modules/dnn/CMakeFiles/opencv_perf_dnn.dir/perf/perf_main.cpp.o
[ 49%] Building CXX object modules/dnn/CMakeFiles/opencv_perf_dnn.dir/perf/perf_convolution.cpp.o
[ 49%] Building CXX object modules/cudawarping/CMakeFiles/opencv_test_cudawarping.dir/test/test_resize.cpp.o
[ 49%] Building CXX object modules/cudawarping/CMakeFiles/opencv_test_cudawarping.dir/test/test_main.cpp.o
[ 49%] Building CXX object modules/cudawarping/CMakeFiles/opencv_test_cudawarping.dir/test/test_pyramids.cpp.o
[ 49%] Linking CXX executable ../../bin/opencv_perf_dnn
Scanning dependencies of target opencv_test_dnn
[ 49%] Built target opencv_perf_dnn
Scanning dependencies of target opencv_test_imgcodecs
[ 49%] Building CXX object modules/dnn/CMakeFiles/opencv_test_dnn.dir/test/test_halide_nets.cpp.o
[ 49%] Building CXX object modules/imgcodecs/CMakeFiles/opencv_test_imgcodecs.dir/test/test_jpeg.cpp.o
[ 49%] Building CXX object modules/dnn/CMakeFiles/opencv_test_dnn.dir/test/test_googlenet.cpp.o
[ 49%] Linking CXX executable ../../bin/opencv_test_cudawarping
[ 49%] Built target opencv_test_cudawarping
[ 50%] Building CXX object modules/imgcodecs/CMakeFiles/opencv_test_imgcodecs.dir/test/test_tiff.cpp.o
[ 51%] Building CXX object modules/dnn/CMakeFiles/opencv_test_dnn.dir/test/test_halide_layers.cpp.o
[ 51%] Building CXX object modules/imgcodecs/CMakeFiles/opencv_test_imgcodecs.dir/test/test_png.cpp.o
[ 51%] Building CXX object modules/dnn/CMakeFiles/opencv_test_dnn.dir/test/test_torch_importer.cpp.o
[ 51%] Building CXX object modules/imgcodecs/CMakeFiles/opencv_test_imgcodecs.dir/test/test_read_write.cpp.o
[ 51%] Building CXX object modules/imgcodecs/CMakeFiles/opencv_test_imgcodecs.dir/test/test_grfmt.cpp.o
[ 51%] Building CXX object modules/dnn/CMakeFiles/opencv_test_dnn.dir/test/test_layers.cpp.o
[ 51%] Building CXX object modules/dnn/CMakeFiles/opencv_test_dnn.dir/test/test_caffe_importer.cpp.o
[ 51%] Building CXX object modules/imgcodecs/CMakeFiles/opencv_test_imgcodecs.dir/test/test_webp.cpp.o
Scanning dependencies of target opencv_cudafilters
[ 51%] Building CXX object modules/cudafilters/CMakeFiles/opencv_cudafilters.dir/src/filtering.cpp.o
[ 51%] Building CXX object modules/imgcodecs/CMakeFiles/opencv_test_imgcodecs.dir/test/test_main.cpp.o
[ 51%] Building CXX object modules/dnn/CMakeFiles/opencv_test_dnn.dir/test/test_tf_importer.cpp.o
[ 51%] Linking CXX shared library ../../lib/libopencv_cudafilters.so
[ 51%] Linking CXX executable ../../bin/opencv_test_imgcodecs
[ 51%] Building CXX object modules/dnn/CMakeFiles/opencv_test_dnn.dir/test/test_main.cpp.o
[ 51%] Built target opencv_test_imgcodecs
Scanning dependencies of target opencv_perf_imgcodecs
[ 51%] Building CXX object modules/imgcodecs/CMakeFiles/opencv_perf_imgcodecs.dir/perf/perf_main.cpp.o
[ 51%] Built target opencv_cudafilters
Scanning dependencies of target opencv_test_shape
[ 52%] Building CXX object modules/shape/CMakeFiles/opencv_test_shape.dir/test/test_shape.cpp.o
[ 52%] Building CXX object modules/shape/CMakeFiles/opencv_test_shape.dir/test/test_main.cpp.o
[ 52%] Linking CXX executable ../../bin/opencv_perf_imgcodecs
[ 52%] Built target opencv_perf_imgcodecs
Scanning dependencies of target opencv_perf_videoio
[ 52%] Building CXX object modules/videoio/CMakeFiles/opencv_perf_videoio.dir/perf/perf_input.cpp.o
[ 52%] Building CXX object modules/videoio/CMakeFiles/opencv_perf_videoio.dir/perf/perf_main.cpp.o
[ 52%] Building CXX object modules/dnn/CMakeFiles/opencv_test_dnn.dir/test/cnpy.cpp.o
[ 52%] Linking CXX executable ../../bin/opencv_test_dnn
[ 52%] Building CXX object modules/videoio/CMakeFiles/opencv_perf_videoio.dir/perf/perf_output.cpp.o
[ 52%] Built target opencv_test_dnn
Scanning dependencies of target opencv_test_videoio
[ 52%] Building CXX object modules/videoio/CMakeFiles/opencv_test_videoio.dir/test/test_ffmpeg.cpp.o
[ 52%] Building CXX object modules/videoio/CMakeFiles/opencv_test_videoio.dir/test/test_video_io.cpp.o
[ 52%] Linking CXX executable ../../bin/opencv_test_shape
[ 52%] Built target opencv_test_shape
Scanning dependencies of target opencv_test_cudacodec
[ 52%] Building CXX object modules/cudacodec/CMakeFiles/opencv_test_cudacodec.dir/test/test_video.cpp.o
[ 52%] Building CXX object modules/cudacodec/CMakeFiles/opencv_test_cudacodec.dir/test/test_main.cpp.o
[ 52%] Building CXX object modules/videoio/CMakeFiles/opencv_test_videoio.dir/test/test_mfx.cpp.o
[ 52%] Linking CXX executable ../../bin/opencv_perf_videoio
[ 52%] Linking CXX executable ../../bin/opencv_test_cudacodec
[ 52%] Built target opencv_test_cudacodec
Scanning dependencies of target opencv_perf_cudacodec
[ 52%] Built target opencv_perf_videoio
Scanning dependencies of target opencv_test_highgui
[ 52%] Building CXX object modules/cudacodec/CMakeFiles/opencv_perf_cudacodec.dir/perf/perf_video.cpp.o
[ 52%] Building CXX object modules/highgui/CMakeFiles/opencv_test_highgui.dir/test/test_gui.cpp.o
[ 52%] Building CXX object modules/highgui/CMakeFiles/opencv_test_highgui.dir/test/test_main.cpp.o
[ 52%] Building CXX object modules/cudacodec/CMakeFiles/opencv_perf_cudacodec.dir/perf/perf_main.cpp.o
Scanning dependencies of target opencv_perf_features2d
[ 53%] Building CXX object modules/features2d/CMakeFiles/opencv_perf_features2d.dir/perf/perf_main.cpp.o
[ 53%] Building CXX object modules/videoio/CMakeFiles/opencv_test_videoio.dir/test/test_main.cpp.o
[ 53%] Linking CXX executable ../../bin/opencv_test_highgui
[ 53%] Built target opencv_test_highgui
[ 53%] Building CXX object modules/features2d/CMakeFiles/opencv_perf_features2d.dir/perf/perf_batchDistance.cpp.o
[ 53%] Linking CXX executable ../../bin/opencv_perf_cudacodec
[ 53%] Building CXX object modules/videoio/CMakeFiles/opencv_test_videoio.dir/test/test_fourcc.cpp.o
[ 53%] Built target opencv_perf_cudacodec
Scanning dependencies of target opencv_test_features2d
[ 53%] Building CXX object modules/features2d/CMakeFiles/opencv_test_features2d.dir/test/test_agast.cpp.o
[ 53%] Building CXX object modules/features2d/CMakeFiles/opencv_test_features2d.dir/test/test_descriptors_invariance.cpp.o
[ 53%] Building CXX object modules/features2d/CMakeFiles/opencv_test_features2d.dir/test/test_detectors_regression.cpp.o
[ 53%] Linking CXX executable ../../bin/opencv_test_videoio
[ 53%] Built target opencv_test_videoio
[ 53%] Generating opencl_kernels_calib3d.cpp, opencl_kernels_calib3d.hpp
Scanning dependencies of target opencv_calib3d
[ 53%] Building CXX object modules/calib3d/CMakeFiles/opencv_calib3d.dir/src/ap3p.cpp.o
[ 53%] Building CXX object modules/calib3d/CMakeFiles/opencv_calib3d.dir/src/ptsetreg.cpp.o
[ 53%] Building CXX object modules/features2d/CMakeFiles/opencv_perf_features2d.dir/perf/perf_feature2d.cpp.o
[ 53%] Building CXX object modules/calib3d/CMakeFiles/opencv_calib3d.dir/src/main.cpp.o
[ 53%] Building CXX object modules/features2d/CMakeFiles/opencv_test_features2d.dir/test/test_nearestneighbors.cpp.o
[ 53%] Building CXX object modules/calib3d/CMakeFiles/opencv_calib3d.dir/src/five-point.cpp.o
[ 53%] Building CXX object modules/features2d/CMakeFiles/opencv_test_features2d.dir/test/test_fast.cpp.o
[ 53%] Building CXX object modules/features2d/CMakeFiles/opencv_perf_features2d.dir/perf/opencl/perf_brute_force_matcher.cpp.o
[ 53%] Building CXX object modules/calib3d/CMakeFiles/opencv_calib3d.dir/src/fisheye.cpp.o
[ 53%] Building CXX object modules/features2d/CMakeFiles/opencv_test_features2d.dir/test/test_matchers_algorithmic.cpp.o
[ 53%] Building CXX object modules/features2d/CMakeFiles/opencv_perf_features2d.dir/perf/opencl/perf_feature2d.cpp.o
[ 53%] Linking CXX executable ../../bin/opencv_perf_features2d
[ 53%] Built target opencv_perf_features2d
[ 53%] Building NVCC (Device) object modules/cudafeatures2d/CMakeFiles/cuda_compile.dir/src/cuda/cuda_compile_generated_bf_radius_match.cu.o
[ 53%] Building CXX object modules/features2d/CMakeFiles/opencv_test_features2d.dir/test/test_descriptors_regression.cpp.o
[ 53%] Building CXX object modules/features2d/CMakeFiles/opencv_test_features2d.dir/test/test_orb.cpp.o
[ 53%] Building NVCC (Device) object modules/cudafeatures2d/CMakeFiles/cuda_compile.dir/src/cuda/cuda_compile_generated_bf_match.cu.o
[ 54%] Building CXX object modules/features2d/CMakeFiles/opencv_test_features2d.dir/test/test_akaze.cpp.o
[ 54%] Building CXX object modules/features2d/CMakeFiles/opencv_test_features2d.dir/test/test_mser.cpp.o
[ 54%] Building NVCC (Device) object modules/cudafeatures2d/CMakeFiles/cuda_compile.dir/src/cuda/cuda_compile_generated_bf_knnmatch.cu.o
[ 54%] Building CXX object modules/features2d/CMakeFiles/opencv_test_features2d.dir/test/test_keypoints.cpp.o
[ 54%] Building CXX object modules/features2d/CMakeFiles/opencv_test_features2d.dir/test/test_detectors_invariance.cpp.o
[ 54%] Building CXX object modules/features2d/CMakeFiles/opencv_test_features2d.dir/test/ocl/test_brute_force_matcher.cpp.o
[ 54%] Building NVCC (Device) object modules/cudafeatures2d/CMakeFiles/cuda_compile.dir/src/cuda/cuda_compile_generated_orb.cu.o
[ 54%] Building CXX object modules/calib3d/CMakeFiles/opencv_calib3d.dir/src/homography_decomp.cpp.o
[ 54%] Building CXX object modules/features2d/CMakeFiles/opencv_test_features2d.dir/test/test_main.cpp.o
/usr/local/cuda-8.0/include/thrust/detail/integer_traits.h(56): warning: integer conversion resulted in a change of sign

[ 54%] Building CXX object modules/features2d/CMakeFiles/opencv_test_features2d.dir/test/test_brisk.cpp.o
[ 54%] Building CXX object modules/calib3d/CMakeFiles/opencv_calib3d.dir/src/p3p.cpp.o
[ 54%] Linking CXX executable ../../bin/opencv_test_features2d
/usr/local/cuda-8.0/include/thrust/detail/integer_traits.h(56): warning: integer conversion resulted in a change of sign

[ 54%] Built target opencv_test_features2d
Scanning dependencies of target opencv_perf_cudafilters
[ 54%] Building CXX object modules/cudafilters/CMakeFiles/opencv_perf_cudafilters.dir/perf/perf_main.cpp.o
[ 54%] Building CXX object modules/cudafilters/CMakeFiles/opencv_perf_cudafilters.dir/perf/perf_filters.cpp.o
[ 54%] Building CXX object modules/calib3d/CMakeFiles/opencv_calib3d.dir/src/stereosgbm.cpp.o
[ 54%] Building CXX object modules/calib3d/CMakeFiles/opencv_calib3d.dir/src/compat_ptsetreg.cpp.o
[ 54%] Building NVCC (Device) object modules/cudafeatures2d/CMakeFiles/cuda_compile.dir/src/cuda/cuda_compile_generated_fast.cu.o
Scanning dependencies of target opencv_test_cudafilters
[ 54%] Building CXX object modules/cudafilters/CMakeFiles/opencv_test_cudafilters.dir/test/test_filters.cpp.o
[ 54%] Building CXX object modules/calib3d/CMakeFiles/opencv_calib3d.dir/src/checkchessboard.cpp.o
Scanning dependencies of target opencv_cudafeatures2d
[ 54%] Building CXX object modules/cudafeatures2d/CMakeFiles/opencv_cudafeatures2d.dir/src/orb.cpp.o
[ 54%] Linking CXX executable ../../bin/opencv_perf_cudafilters
[ 54%] Built target opencv_perf_cudafilters
[ 54%] Building CXX object modules/cudafilters/CMakeFiles/opencv_test_cudafilters.dir/test/test_main.cpp.o
[ 54%] Building CXX object modules/calib3d/CMakeFiles/opencv_calib3d.dir/src/fundam.cpp.o
[ 54%] Building CXX object modules/cudafeatures2d/CMakeFiles/opencv_cudafeatures2d.dir/src/fast.cpp.o
[ 54%] Building CXX object modules/cudafeatures2d/CMakeFiles/opencv_cudafeatures2d.dir/src/brute_force_matcher.cpp.o
[ 54%] Building CXX object modules/cudafeatures2d/CMakeFiles/opencv_cudafeatures2d.dir/src/feature2d_async.cpp.o
[ 55%] Building CXX object modules/calib3d/CMakeFiles/opencv_calib3d.dir/src/circlesgrid.cpp.o
[ 56%] Linking CXX shared library ../../lib/libopencv_cudafeatures2d.so
[ 56%] Built target opencv_cudafeatures2d
[ 56%] Building NVCC (Device) object modules/cudaimgproc/CMakeFiles/cuda_compile.dir/src/cuda/cuda_compile_generated_canny.cu.o
[ 56%] Building NVCC (Device) object modules/cudaimgproc/CMakeFiles/cuda_compile.dir/src/cuda/cuda_compile_generated_hough_lines.cu.o
/usr/local/cuda-8.0/include/thrust/detail/integer_traits.h(56): warning: integer conversion resulted in a change of sign

Scanning dependencies of target opencv_test_cudafeatures2d
[ 56%] Building CXX object modules/cudafeatures2d/CMakeFiles/opencv_test_cudafeatures2d.dir/test/test_features2d.cpp.o
[ 56%] Building CXX object modules/calib3d/CMakeFiles/opencv_calib3d.dir/src/calibinit.cpp.o
/usr/local/cuda-8.0/include/thrust/detail/integer_traits.h(56): warning: integer conversion resulted in a change of sign

[ 56%] Linking CXX executable ../../bin/opencv_test_cudafilters
[ 56%] Built target opencv_test_cudafilters
[ 56%] Building CXX object modules/cudafeatures2d/CMakeFiles/opencv_test_cudafeatures2d.dir/test/test_main.cpp.o
[ 56%] Building NVCC (Device) object modules/cudaimgproc/CMakeFiles/cuda_compile.dir/src/cuda/cuda_compile_generated_bilateral_filter.cu.o
[ 56%] Building CXX object modules/calib3d/CMakeFiles/opencv_calib3d.dir/src/stereobm.cpp.o
[ 56%] Linking CXX executable ../../bin/opencv_test_cudafeatures2d
[ 56%] Built target opencv_test_cudafeatures2d
Scanning dependencies of target opencv_perf_cudafeatures2d
[ 56%] Building CXX object modules/cudafeatures2d/CMakeFiles/opencv_perf_cudafeatures2d.dir/perf/perf_main.cpp.o
[ 56%] Building CXX object modules/cudafeatures2d/CMakeFiles/opencv_perf_cudafeatures2d.dir/perf/perf_features2d.cpp.o
[ 56%] Building CXX object modules/calib3d/CMakeFiles/opencv_calib3d.dir/src/triangulate.cpp.o
[ 56%] Building CXX object modules/calib3d/CMakeFiles/opencv_calib3d.dir/src/epnp.cpp.o
[ 56%] Building CXX object modules/calib3d/CMakeFiles/opencv_calib3d.dir/src/posit.cpp.o
[ 56%] Building NVCC (Device) object modules/cudaimgproc/CMakeFiles/cuda_compile.dir/src/cuda/cuda_compile_generated_build_point_list.cu.o
[ 56%] Building CXX object modules/calib3d/CMakeFiles/opencv_calib3d.dir/src/calibration.cpp.o
[ 56%] Building CXX object modules/calib3d/CMakeFiles/opencv_calib3d.dir/src/levmarq.cpp.o
[ 56%] Linking CXX executable ../../bin/opencv_perf_cudafeatures2d
[ 56%] Built target opencv_perf_cudafeatures2d
[ 56%] Building CXX object modules/calib3d/CMakeFiles/opencv_calib3d.dir/src/compat_stereo.cpp.o
[ 56%] Building NVCC (Device) object modules/cudaimgproc/CMakeFiles/cuda_compile.dir/src/cuda/cuda_compile_generated_hist.cu.o
[ 56%] Building CXX object modules/calib3d/CMakeFiles/opencv_calib3d.dir/src/polynom_solver.cpp.o
[ 56%] Building CXX object modules/calib3d/CMakeFiles/opencv_calib3d.dir/src/rho.cpp.o
[ 56%] Building NVCC (Device) object modules/cudaimgproc/CMakeFiles/cuda_compile.dir/src/cuda/cuda_compile_generated_clahe.cu.o
[ 56%] Building CXX object modules/calib3d/CMakeFiles/opencv_calib3d.dir/src/solvepnp.cpp.o
[ 56%] Building CXX object modules/calib3d/CMakeFiles/opencv_calib3d.dir/src/quadsubpix.cpp.o
[ 56%] Building NVCC (Device) object modules/cudaimgproc/CMakeFiles/cuda_compile.dir/src/cuda/cuda_compile_generated_gftt.cu.o
/usr/local/cuda-8.0/include/thrust/detail/integer_traits.h(56): warning: integer conversion resulted in a change of sign

[ 56%] Building CXX object modules/calib3d/CMakeFiles/opencv_calib3d.dir/src/upnp.cpp.o
[ 56%] Building CXX object modules/calib3d/CMakeFiles/opencv_calib3d.dir/src/dls.cpp.o
[ 57%] Building CXX object modules/calib3d/CMakeFiles/opencv_calib3d.dir/opencl_kernels_calib3d.cpp.o
/usr/local/cuda-8.0/include/thrust/detail/integer_traits.h(56): warning: integer conversion resulted in a change of sign

[ 57%] Building NVCC (Device) object modules/cudaimgproc/CMakeFiles/cuda_compile.dir/src/cuda/cuda_compile_generated_mean_shift.cu.o
[ 57%] Building NVCC (Device) object modules/cudaimgproc/CMakeFiles/cuda_compile.dir/src/cuda/cuda_compile_generated_corners.cu.o
[ 57%] Building NVCC (Device) object modules/cudaimgproc/CMakeFiles/cuda_compile.dir/src/cuda/cuda_compile_generated_color.cu.o
[ 57%] Building NVCC (Device) object modules/cudaimgproc/CMakeFiles/cuda_compile.dir/src/cuda/cuda_compile_generated_generalized_hough.cu.o
/usr/local/cuda-8.0/include/thrust/detail/integer_traits.h(56): warning: integer conversion resulted in a change of sign

[ 57%] Building NVCC (Device) object modules/cudaimgproc/CMakeFiles/cuda_compile.dir/src/cuda/cuda_compile_generated_hough_circles.cu.o
/usr/local/cuda-8.0/include/thrust/detail/integer_traits.h(56): warning: integer conversion resulted in a change of sign

[ 57%] Building NVCC (Device) object modules/cudaimgproc/CMakeFiles/cuda_compile.dir/src/cuda/cuda_compile_generated_blend.cu.o
[ 58%] Building NVCC (Device) object modules/cudaimgproc/CMakeFiles/cuda_compile.dir/src/cuda/cuda_compile_generated_debayer.cu.o
[ 58%] Building NVCC (Device) object modules/cudaimgproc/CMakeFiles/cuda_compile.dir/src/cuda/cuda_compile_generated_match_template.cu.o
[ 58%] Linking CXX shared library ../../lib/libopencv_calib3d.so
[ 58%] Built target opencv_calib3d
Scanning dependencies of target opencv_perf_calib3d
[ 58%] Building CXX object modules/calib3d/CMakeFiles/opencv_perf_calib3d.dir/perf/perf_stereosgbm.cpp.o
[ 58%] Building NVCC (Device) object modules/cudaimgproc/CMakeFiles/cuda_compile.dir/src/cuda/cuda_compile_generated_hough_segments.cu.o
Scanning dependencies of target opencv_test_calib3d
[ 58%] Building CXX object modules/calib3d/CMakeFiles/opencv_test_calib3d.dir/test/test_affine3.cpp.o
[ 58%] Building CXX object modules/calib3d/CMakeFiles/opencv_test_calib3d.dir/test/test_fundam.cpp.o
[ 58%] Building CXX object modules/calib3d/CMakeFiles/opencv_perf_calib3d.dir/perf/perf_pnp.cpp.o
[ 58%] Building CXX object modules/calib3d/CMakeFiles/opencv_test_calib3d.dir/test/test_affine2d_estimator.cpp.o
[ 58%] Building CXX object modules/calib3d/CMakeFiles/opencv_test_calib3d.dir/test/test_undistort.cpp.o
[ 58%] Building CXX object modules/calib3d/CMakeFiles/opencv_perf_calib3d.dir/perf/perf_main.cpp.o
[ 58%] Building CXX object modules/calib3d/CMakeFiles/opencv_test_calib3d.dir/test/test_cornerssubpix.cpp.o
[ 58%] Building CXX object modules/calib3d/CMakeFiles/opencv_perf_calib3d.dir/perf/opencl/perf_stereobm.cpp.o
[ 58%] Building NVCC (Device) object modules/cudastereo/CMakeFiles/cuda_compile.dir/src/cuda/cuda_compile_generated_disparity_bilateral_filter.cu.o
[ 58%] Building CXX object modules/calib3d/CMakeFiles/opencv_perf_calib3d.dir/perf/perf_cicrlesGrid.cpp.o
[ 59%] Building CXX object modules/calib3d/CMakeFiles/opencv_test_calib3d.dir/test/test_fisheye.cpp.o
[ 59%] Building NVCC (Device) object modules/cudastereo/CMakeFiles/cuda_compile.dir/src/cuda/cuda_compile_generated_stereobp.cu.o
[ 59%] Building CXX object modules/calib3d/CMakeFiles/opencv_perf_calib3d.dir/perf/perf_affine2d.cpp.o
[ 59%] Building NVCC (Device) object modules/cudastereo/CMakeFiles/cuda_compile.dir/src/cuda/cuda_compile_generated_util.cu.o
[ 59%] Building CXX object modules/calib3d/CMakeFiles/opencv_test_calib3d.dir/test/test_decompose_projection.cpp.o
[ 59%] Building NVCC (Device) object modules/cudastereo/CMakeFiles/cuda_compile.dir/src/cuda/cuda_compile_generated_stereobm.cu.o
[ 59%] Building CXX object modules/calib3d/CMakeFiles/opencv_test_calib3d.dir/test/test_undistort_badarg.cpp.o
[ 59%] Linking CXX executable ../../bin/opencv_perf_calib3d
[ 59%] Built target opencv_perf_calib3d
Scanning dependencies of target opencv_traincascade
[ 59%] Building CXX object apps/traincascade/CMakeFiles/opencv_traincascade.dir/traincascade.cpp.o
[ 59%] Building CXX object apps/traincascade/CMakeFiles/opencv_traincascade.dir/lbpfeatures.cpp.o
[ 59%] Building CXX object modules/calib3d/CMakeFiles/opencv_test_calib3d.dir/test/test_cameracalibration_artificial.cpp.o
[ 59%] Building CXX object apps/traincascade/CMakeFiles/opencv_traincascade.dir/boost.cpp.o
[ 59%] Building CXX object modules/calib3d/CMakeFiles/opencv_test_calib3d.dir/test/test_affine3d_estimator.cpp.o
Scanning dependencies of target opencv_cudaimgproc
[ 59%] Building CXX object apps/traincascade/CMakeFiles/opencv_traincascade.dir/old_ml_data.cpp.o
[ 59%] Building CXX object modules/cudaimgproc/CMakeFiles/opencv_cudaimgproc.dir/src/hough_circles.cpp.o
[ 59%] Building CXX object modules/calib3d/CMakeFiles/opencv_test_calib3d.dir/test/test_chesscorners.cpp.o
[ 59%] Building NVCC (Device) object modules/cudastereo/CMakeFiles/cuda_compile.dir/src/cuda/cuda_compile_generated_stereocsbp.cu.o
[ 59%] Building CXX object apps/traincascade/CMakeFiles/opencv_traincascade.dir/old_ml_boost.cpp.o
[ 59%] Building CXX object modules/calib3d/CMakeFiles/opencv_test_calib3d.dir/test/test_stereomatching.cpp.o
[ 59%] Building CXX object modules/cudaimgproc/CMakeFiles/opencv_cudaimgproc.dir/src/histogram.cpp.o
[ 59%] Building CXX object apps/traincascade/CMakeFiles/opencv_traincascade.dir/cascadeclassifier.cpp.o
[ 59%] Building CXX object modules/cudaimgproc/CMakeFiles/opencv_cudaimgproc.dir/src/match_template.cpp.o
[ 59%] Building CXX object modules/calib3d/CMakeFiles/opencv_test_calib3d.dir/test/test_compose_rt.cpp.o
Scanning dependencies of target opencv_cudastereo
[ 59%] Building CXX object apps/traincascade/CMakeFiles/opencv_traincascade.dir/features.cpp.o
[ 59%] Building CXX object modules/cudastereo/CMakeFiles/opencv_cudastereo.dir/src/stereobp.cpp.o
[ 59%] Building CXX object modules/cudaimgproc/CMakeFiles/opencv_cudaimgproc.dir/src/mean_shift.cpp.o
[ 59%] Building CXX object modules/calib3d/CMakeFiles/opencv_test_calib3d.dir/test/test_posit.cpp.o
[ 59%] Building CXX object apps/traincascade/CMakeFiles/opencv_traincascade.dir/haarfeatures.cpp.o
[ 59%] Building CXX object modules/cudastereo/CMakeFiles/opencv_cudastereo.dir/src/stereocsbp.cpp.o
[ 59%] Building CXX object modules/calib3d/CMakeFiles/opencv_test_calib3d.dir/test/test_modelest.cpp.o
[ 59%] Building CXX object modules/cudaimgproc/CMakeFiles/opencv_cudaimgproc.dir/src/gftt.cpp.o
[ 60%] Building CXX object modules/cudastereo/CMakeFiles/opencv_cudastereo.dir/src/stereobm.cpp.o
[ 60%] Building CXX object apps/traincascade/CMakeFiles/opencv_traincascade.dir/old_ml_inner_functions.cpp.o
[ 60%] Building CXX object modules/calib3d/CMakeFiles/opencv_test_calib3d.dir/test/test_undistort_points.cpp.o
[ 60%] Building CXX object modules/cudastereo/CMakeFiles/opencv_cudastereo.dir/src/util.cpp.o
[ 60%] Building CXX object modules/cudaimgproc/CMakeFiles/opencv_cudaimgproc.dir/src/generalized_hough.cpp.o
[ 60%] Building CXX object modules/cudastereo/CMakeFiles/opencv_cudastereo.dir/src/disparity_bilateral_filter.cpp.o
[ 60%] Building CXX object modules/calib3d/CMakeFiles/opencv_test_calib3d.dir/test/test_solvepnp_ransac.cpp.o
[ 60%] Building CXX object apps/traincascade/CMakeFiles/opencv_traincascade.dir/old_ml_tree.cpp.o
[ 60%] Linking CXX shared library ../../lib/libopencv_cudastereo.so
[ 60%] Built target opencv_cudastereo
Scanning dependencies of target opencv_createsamples
[ 60%] Building CXX object apps/createsamples/CMakeFiles/opencv_createsamples.dir/utility.cpp.o
[ 60%] Building CXX object modules/cudaimgproc/CMakeFiles/opencv_cudaimgproc.dir/src/blend.cpp.o
[ 60%] Building CXX object apps/createsamples/CMakeFiles/opencv_createsamples.dir/createsamples.cpp.o
[ 60%] Linking CXX executable ../../bin/opencv_createsamples
[ 60%] Built target opencv_createsamples
Scanning dependencies of target opencv_interactive-calibration
[ 60%] Building CXX object apps/interactive-calibration/CMakeFiles/opencv_interactive-calibration.dir/parametersController.cpp.o
[ 60%] Building CXX object modules/calib3d/CMakeFiles/opencv_test_calib3d.dir/test/test_cameracalibration_badarg.cpp.o
[ 60%] Building CXX object modules/cudaimgproc/CMakeFiles/opencv_cudaimgproc.dir/src/mssegmentation.cpp.o
[ 60%] Building CXX object apps/interactive-calibration/CMakeFiles/opencv_interactive-calibration.dir/main.cpp.o
[ 60%] Building CXX object apps/traincascade/CMakeFiles/opencv_traincascade.dir/imagestorage.cpp.o
[ 60%] Building CXX object apps/interactive-calibration/CMakeFiles/opencv_interactive-calibration.dir/calibPipeline.cpp.o
[ 60%] Building CXX object modules/cudaimgproc/CMakeFiles/opencv_cudaimgproc.dir/src/canny.cpp.o
[ 60%] Building CXX object apps/traincascade/CMakeFiles/opencv_traincascade.dir/HOGfeatures.cpp.o
[ 60%] Building CXX object apps/interactive-calibration/CMakeFiles/opencv_interactive-calibration.dir/frameProcessor.cpp.o
[ 60%] Building CXX object modules/calib3d/CMakeFiles/opencv_test_calib3d.dir/test/test_chesscorners_badarg.cpp.o
[ 60%] Building CXX object modules/cudaimgproc/CMakeFiles/opencv_cudaimgproc.dir/src/hough_lines.cpp.o
[ 60%] Linking CXX executable ../../bin/opencv_traincascade
[ 60%] Built target opencv_traincascade
Scanning dependencies of target example_tapi_squares
[ 61%] Building CXX object samples/tapi/CMakeFiles/example_tapi_squares.dir/squares.cpp.o
[ 61%] Building CXX object modules/calib3d/CMakeFiles/opencv_test_calib3d.dir/test/test_chesscorners_timing.cpp.o
[ 61%] Building CXX object apps/interactive-calibration/CMakeFiles/opencv_interactive-calibration.dir/calibController.cpp.o
[ 61%] Linking CXX executable ../../bin/tapi-example-squares
[ 61%] Built target example_tapi_squares
Scanning dependencies of target example_tapi_hog
[ 61%] Building CXX object samples/tapi/CMakeFiles/example_tapi_hog.dir/hog.cpp.o
[ 61%] Building CXX object modules/cudaimgproc/CMakeFiles/opencv_cudaimgproc.dir/src/corners.cpp.o
[ 61%] Building CXX object modules/calib3d/CMakeFiles/opencv_test_calib3d.dir/test/test_affine_partial2d_estimator.cpp.o
[ 61%] Linking CXX executable ../../bin/tapi-example-hog
[ 62%] Building CXX object modules/cudaimgproc/CMakeFiles/opencv_cudaimgproc.dir/src/color.cpp.o
[ 62%] Built target example_tapi_hog
Scanning dependencies of target example_tapi_clahe
[ 62%] Building CXX object samples/tapi/CMakeFiles/example_tapi_clahe.dir/clahe.cpp.o
[ 62%] Building CXX object apps/interactive-calibration/CMakeFiles/opencv_interactive-calibration.dir/rotationConverters.cpp.o
[ 62%] Linking CXX executable ../../bin/tapi-example-clahe
[ 62%] Built target example_tapi_clahe
Scanning dependencies of target example_tapi_ufacedetect
[ 62%] Building CXX object samples/tapi/CMakeFiles/example_tapi_ufacedetect.dir/ufacedetect.cpp.o
[ 63%] Building CXX object modules/calib3d/CMakeFiles/opencv_test_calib3d.dir/test/test_cameracalibration.cpp.o
[ 63%] Linking CXX executable ../../bin/opencv_interactive-calibration
[ 63%] Built target opencv_interactive-calibration
Scanning dependencies of target example_tapi_camshift
[ 63%] Building CXX object samples/tapi/CMakeFiles/example_tapi_camshift.dir/camshift.cpp.o
[ 63%] Linking CXX executable ../../bin/tapi-example-ufacedetect
[ 63%] Built target example_tapi_ufacedetect
Scanning dependencies of target example_tapi_tvl1_optical_flow
[ 63%] Building CXX object samples/tapi/CMakeFiles/example_tapi_tvl1_optical_flow.dir/tvl1_optical_flow.cpp.o
[ 63%] Building CXX object modules/cudaimgproc/CMakeFiles/opencv_cudaimgproc.dir/src/hough_segments.cpp.o
[ 63%] Linking CXX executable ../../bin/tapi-example-camshift
[ 63%] Built target example_tapi_camshift
Scanning dependencies of target example_tapi_pyrlk_optical_flow
[ 63%] Building CXX object samples/tapi/CMakeFiles/example_tapi_pyrlk_optical_flow.dir/pyrlk_optical_flow.cpp.o
[ 63%] Linking CXX executable ../../bin/tapi-example-tvl1_optical_flow
[ 63%] Built target example_tapi_tvl1_optical_flow
Scanning dependencies of target example_tapi_bgfg_segm
[ 63%] Building CXX object samples/tapi/CMakeFiles/example_tapi_bgfg_segm.dir/bgfg_segm.cpp.o
[ 63%] Linking CXX executable ../../bin/tapi-example-pyrlk_optical_flow
[ 63%] Building CXX object modules/cudaimgproc/CMakeFiles/opencv_cudaimgproc.dir/src/bilateral_filter.cpp.o
[ 63%] Built target example_tapi_pyrlk_optical_flow
Scanning dependencies of target opencv_perf_cudastereo
[ 63%] Building CXX object modules/cudastereo/CMakeFiles/opencv_perf_cudastereo.dir/perf/perf_main.cpp.o
[ 63%] Linking CXX executable ../../bin/tapi-example-bgfg_segm
[ 63%] Built target example_tapi_bgfg_segm
[ 63%] Building CXX object modules/cudastereo/CMakeFiles/opencv_perf_cudastereo.dir/perf/perf_stereo.cpp.o
[ 63%] Building CXX object modules/calib3d/CMakeFiles/opencv_test_calib3d.dir/test/test_homography_decomp.cpp.o
[ 63%] Linking CXX shared library ../../lib/libopencv_cudaimgproc.so
[ 63%] Built target opencv_cudaimgproc
Scanning dependencies of target opencv_test_cudastereo
[ 63%] Building CXX object modules/cudastereo/CMakeFiles/opencv_test_cudastereo.dir/test/test_stereo.cpp.o
[ 63%] Building CXX object modules/calib3d/CMakeFiles/opencv_test_calib3d.dir/test/test_homography.cpp.o
[ 63%] Building CXX object modules/calib3d/CMakeFiles/opencv_test_calib3d.dir/test/test_cameracalibration_tilt.cpp.o
[ 63%] Linking CXX executable ../../bin/opencv_perf_cudastereo
[ 63%] Built target opencv_perf_cudastereo
Scanning dependencies of target opencv_test_cudaimgproc
[ 63%] Building CXX object modules/cudaimgproc/CMakeFiles/opencv_test_cudaimgproc.dir/test/test_hough.cpp.o
[ 63%] Building CXX object modules/cudastereo/CMakeFiles/opencv_test_cudastereo.dir/test/test_main.cpp.o
[ 64%] Building CXX object modules/cudaimgproc/CMakeFiles/opencv_test_cudaimgproc.dir/test/test_blend.cpp.o
[ 64%] Building CXX object modules/calib3d/CMakeFiles/opencv_test_calib3d.dir/test/test_chessboardgenerator.cpp.o
[ 64%] Linking CXX executable ../../bin/opencv_test_cudastereo
[ 64%] Built target opencv_test_cudastereo
Scanning dependencies of target opencv_perf_cudaimgproc
[ 64%] Building CXX object modules/cudaimgproc/CMakeFiles/opencv_perf_cudaimgproc.dir/perf/perf_gftt.cpp.o
[ 64%] Building CXX object modules/calib3d/CMakeFiles/opencv_test_calib3d.dir/test/test_reproject_image_to_3d.cpp.o
[ 64%] Building CXX object modules/cudaimgproc/CMakeFiles/opencv_perf_cudaimgproc.dir/perf/perf_main.cpp.o
[ 64%] Building CXX object modules/cudaimgproc/CMakeFiles/opencv_test_cudaimgproc.dir/test/test_corners.cpp.o
[ 65%] Building CXX object modules/cudaimgproc/CMakeFiles/opencv_perf_cudaimgproc.dir/perf/perf_color.cpp.o
[ 65%] Building CXX object modules/cudaimgproc/CMakeFiles/opencv_perf_cudaimgproc.dir/perf/perf_corners.cpp.o
[ 65%] Building CXX object modules/calib3d/CMakeFiles/opencv_test_calib3d.dir/test/opencl/test_stereobm.cpp.o
[ 65%] Building CXX object modules/calib3d/CMakeFiles/opencv_test_calib3d.dir/test/test_main.cpp.o
[ 65%] Building CXX object modules/cudaimgproc/CMakeFiles/opencv_test_cudaimgproc.dir/test/test_color.cpp.o
[ 65%] Linking CXX executable ../../bin/opencv_test_calib3d
[ 65%] Building CXX object modules/cudaimgproc/CMakeFiles/opencv_perf_cudaimgproc.dir/perf/perf_blend.cpp.o
[ 65%] Built target opencv_test_calib3d
[ 65%] Generating opencl_kernels_photo.cpp, opencl_kernels_photo.hpp
[ 66%] Building NVCC (Device) object modules/photo/CMakeFiles/cuda_compile.dir/src/cuda/cuda_compile_generated_nlm.cu.o
[ 66%] Building CXX object modules/cudaimgproc/CMakeFiles/opencv_perf_cudaimgproc.dir/perf/perf_bilateral_filter.cpp.o
[ 66%] Building CXX object modules/cudaimgproc/CMakeFiles/opencv_perf_cudaimgproc.dir/perf/perf_hough.cpp.o
[ 66%] Building CXX object modules/cudaimgproc/CMakeFiles/opencv_perf_cudaimgproc.dir/perf/perf_histogram.cpp.o
Scanning dependencies of target opencv_photo
[ 66%] Building CXX object modules/photo/CMakeFiles/opencv_photo.dir/src/seamless_cloning_impl.cpp.o
[ 66%] Building CXX object modules/photo/CMakeFiles/opencv_photo.dir/src/inpaint.cpp.o
[ 66%] Building CXX object modules/cudaimgproc/CMakeFiles/opencv_perf_cudaimgproc.dir/perf/perf_match_template.cpp.o
[ 66%] Building CXX object modules/cudaimgproc/CMakeFiles/opencv_perf_cudaimgproc.dir/perf/perf_canny.cpp.o
[ 66%] Building CXX object modules/photo/CMakeFiles/opencv_photo.dir/src/tonemap.cpp.o
[ 66%] Building CXX object modules/cudaimgproc/CMakeFiles/opencv_perf_cudaimgproc.dir/perf/perf_mean_shift.cpp.o
[ 66%] Building CXX object modules/cudaimgproc/CMakeFiles/opencv_test_cudaimgproc.dir/test/test_bilateral_filter.cpp.o
[ 66%] Building CXX object modules/cudaimgproc/CMakeFiles/opencv_test_cudaimgproc.dir/test/test_histogram.cpp.o
[ 66%] Building CXX object modules/photo/CMakeFiles/opencv_photo.dir/src/align.cpp.o
[ 66%] Linking CXX executable ../../bin/opencv_perf_cudaimgproc
[ 66%] Building CXX object modules/cudaimgproc/CMakeFiles/opencv_test_cudaimgproc.dir/test/test_gftt.cpp.o
[ 66%] Built target opencv_perf_cudaimgproc
[ 66%] Building NVCC (Device) object modules/cudalegacy/CMakeFiles/cuda_compile.dir/src/cuda/cuda_compile_generated_calib3d.cu.o
[ 66%] Building NVCC (Device) object modules/cudalegacy/CMakeFiles/cuda_compile.dir/src/cuda/cuda_compile_generated_NCVHaarObjectDetection.cu.o
[ 66%] Building CXX object modules/photo/CMakeFiles/opencv_photo.dir/src/calibrate.cpp.o
[ 66%] Building CXX object modules/photo/CMakeFiles/opencv_photo.dir/src/npr.cpp.o
[ 66%] Building CXX object modules/cudaimgproc/CMakeFiles/opencv_test_cudaimgproc.dir/test/test_canny.cpp.o
[ 66%] Building CXX object modules/photo/CMakeFiles/opencv_photo.dir/src/merge.cpp.o
[ 66%] Building CXX object modules/photo/CMakeFiles/opencv_photo.dir/src/hdr_common.cpp.o
[ 66%] Building CXX object modules/cudaimgproc/CMakeFiles/opencv_test_cudaimgproc.dir/test/test_main.cpp.o
[ 66%] Building CXX object modules/photo/CMakeFiles/opencv_photo.dir/src/contrast_preserve.cpp.o
[ 66%] Building CXX object modules/photo/CMakeFiles/opencv_photo.dir/src/denoising.cuda.cpp.o
[ 66%] Building CXX object modules/cudaimgproc/CMakeFiles/opencv_test_cudaimgproc.dir/test/test_match_template.cpp.o
[ 66%] Building CXX object modules/photo/CMakeFiles/opencv_photo.dir/src/denoise_tvl1.cpp.o
[ 66%] Building NVCC (Device) object modules/cudalegacy/CMakeFiles/cuda_compile.dir/src/cuda/cuda_compile_generated_ccomponetns.cu.o
[ 66%] Building CXX object modules/photo/CMakeFiles/opencv_photo.dir/src/seamless_cloning.cpp.o
[ 66%] Building CXX object modules/photo/CMakeFiles/opencv_photo.dir/src/denoising.cpp.o
[ 67%] Building CXX object modules/photo/CMakeFiles/opencv_photo.dir/opencl_kernels_photo.cpp.o
[ 67%] Building NVCC (Device) object modules/cudalegacy/CMakeFiles/cuda_compile.dir/src/cuda/cuda_compile_generated_NCVPyramid.cu.o
[ 67%] Building CXX object modules/cudaimgproc/CMakeFiles/opencv_test_cudaimgproc.dir/test/test_mean_shift.cpp.o
[ 67%] Building NVCC (Device) object modules/cudalegacy/CMakeFiles/cuda_compile.dir/src/cuda/cuda_compile_generated_gmg.cu.o
[ 67%] Building NVCC (Device) object modules/cudalegacy/CMakeFiles/cuda_compile.dir/src/cuda/cuda_compile_generated_bm_fast.cu.o
[ 67%] Building NVCC (Device) object modules/cudalegacy/CMakeFiles/cuda_compile.dir/src/cuda/cuda_compile_generated_NCVBroxOpticalFlow.cu.o
[ 67%] Linking CXX executable ../../bin/opencv_test_cudaimgproc
[ 67%] Built target opencv_test_cudaimgproc
[ 67%] Building NVCC (Device) object modules/cudalegacy/CMakeFiles/cuda_compile.dir/src/cuda/cuda_compile_generated_fgd.cu.o
[ 67%] Building NVCC (Device) object modules/cudalegacy/CMakeFiles/cuda_compile.dir/src/cuda/cuda_compile_generated_bm.cu.o
[ 67%] Building NVCC (Device) object modules/cudalegacy/CMakeFiles/cuda_compile.dir/src/cuda/cuda_compile_generated_NCV.cu.o
[ 67%] Building NVCC (Device) object modules/cudalegacy/CMakeFiles/cuda_compile.dir/src/cuda/cuda_compile_generated_NPP_staging.cu.o
[ 67%] Building NVCC (Device) object modules/cudalegacy/CMakeFiles/cuda_compile.dir/src/cuda/cuda_compile_generated_needle_map.cu.o
[ 67%] Linking CXX shared library ../../lib/libopencv_photo.so
[ 67%] Built target opencv_photo
Scanning dependencies of target opencv_perf_photo
Scanning dependencies of target opencv_test_photo
[ 67%] Building CXX object modules/photo/CMakeFiles/opencv_perf_photo.dir/perf/perf_inpaint.cpp.o
[ 67%] Building CXX object modules/photo/CMakeFiles/opencv_perf_photo.dir/perf/perf_main.cpp.o
[ 67%] Building CXX object modules/photo/CMakeFiles/opencv_test_photo.dir/test/test_denoising.cuda.cpp.o
[ 67%] Building CXX object modules/photo/CMakeFiles/opencv_perf_photo.dir/perf/perf_cuda.cpp.o
[ 67%] Building CXX object modules/photo/CMakeFiles/opencv_test_photo.dir/test/test_hdr.cpp.o
Scanning dependencies of target opencv_cudalegacy
[ 68%] Building CXX object modules/cudalegacy/CMakeFiles/opencv_cudalegacy.dir/src/bm_fast.cpp.o
[ 68%] Building CXX object modules/cudalegacy/CMakeFiles/opencv_cudalegacy.dir/src/image_pyramid.cpp.o
[ 68%] Building CXX object modules/photo/CMakeFiles/opencv_perf_photo.dir/perf/opencl/perf_denoising.cpp.o
[ 68%] Building CXX object modules/cudalegacy/CMakeFiles/opencv_cudalegacy.dir/src/fgd.cpp.o
[ 68%] Building CXX object modules/photo/CMakeFiles/opencv_test_photo.dir/test/test_npr.cpp.o
[ 68%] Building CXX object modules/photo/CMakeFiles/opencv_test_photo.dir/test/test_denoise_tvl1.cpp.o
[ 68%] Linking CXX executable ../../bin/opencv_perf_photo
[ 68%] Built target opencv_perf_photo
[ 68%] Building CXX object modules/photo/CMakeFiles/opencv_test_photo.dir/test/test_inpaint.cpp.o
[ 68%] Building CXX object modules/cudalegacy/CMakeFiles/opencv_cudalegacy.dir/src/needle_map.cpp.o
[ 68%] Building CXX object modules/photo/CMakeFiles/opencv_test_photo.dir/test/test_denoising.cpp.o
[ 68%] Building CXX object modules/cudalegacy/CMakeFiles/opencv_cudalegacy.dir/src/gmg.cpp.o
[ 68%] Building CXX object modules/cudalegacy/CMakeFiles/opencv_cudalegacy.dir/src/graphcuts.cpp.o
[ 68%] Building CXX object modules/cudalegacy/CMakeFiles/opencv_cudalegacy.dir/src/interpolate_frames.cpp.o
[ 68%] Building CXX object modules/cudalegacy/CMakeFiles/opencv_cudalegacy.dir/src/bm.cpp.o
[ 68%] Building CXX object modules/photo/CMakeFiles/opencv_test_photo.dir/test/test_cloning.cpp.o
[ 68%] Building CXX object modules/photo/CMakeFiles/opencv_test_photo.dir/test/test_decolor.cpp.o
[ 68%] Building CXX object modules/cudalegacy/CMakeFiles/opencv_cudalegacy.dir/src/calib3d.cpp.o
[ 68%] Building CXX object modules/cudalegacy/CMakeFiles/opencv_cudalegacy.dir/src/NCV.cpp.o
[ 68%] Building CXX object modules/photo/CMakeFiles/opencv_test_photo.dir/test/ocl/test_denoising.cpp.o
[ 68%] Building CXX object modules/photo/CMakeFiles/opencv_test_photo.dir/test/test_main.cpp.o
[ 68%] Linking CXX shared library ../../lib/libopencv_cudalegacy.so
[ 68%] Built target opencv_cudalegacy
Scanning dependencies of target opencv_test_cudalegacy
[ 68%] Building CXX object modules/cudalegacy/CMakeFiles/opencv_test_cudalegacy.dir/test/TestTranspose.cpp.o
[ 68%] Building CXX object modules/cudalegacy/CMakeFiles/opencv_test_cudalegacy.dir/test/TestHaarCascadeLoader.cpp.o
[ 68%] Building CXX object modules/cudalegacy/CMakeFiles/opencv_test_cudalegacy.dir/test/TestHypothesesFilter.cpp.o
[ 68%] Linking CXX executable ../../bin/opencv_test_photo
[ 68%] Built target opencv_test_photo
Scanning dependencies of target opencv_perf_cudalegacy
[ 68%] Building CXX object modules/cudalegacy/CMakeFiles/opencv_perf_cudalegacy.dir/perf/perf_calib3d.cpp.o
[ 68%] Building CXX object modules/cudalegacy/CMakeFiles/opencv_perf_cudalegacy.dir/perf/perf_main.cpp.o
[ 68%] Building CXX object modules/cudalegacy/CMakeFiles/opencv_test_cudalegacy.dir/test/TestIntegralImageSquared.cpp.o
[ 69%] Building CXX object modules/cudalegacy/CMakeFiles/opencv_test_cudalegacy.dir/test/TestHaarCascadeApplication.cpp.o
[ 69%] Building CXX object modules/cudalegacy/CMakeFiles/opencv_perf_cudalegacy.dir/perf/perf_bgsegm.cpp.o
[ 69%] Building CXX object modules/cudalegacy/CMakeFiles/opencv_perf_cudalegacy.dir/perf/perf_labeling.cpp.o
[ 69%] Building NVCC (Device) object modules/cudaobjdetect/CMakeFiles/cuda_compile.dir/src/cuda/cuda_compile_generated_lbp.cu.o
[ 69%] Building CXX object modules/cudalegacy/CMakeFiles/opencv_test_cudalegacy.dir/test/TestRectStdDev.cpp.o
[ 69%] Building NVCC (Device) object modules/cudaobjdetect/CMakeFiles/cuda_compile.dir/src/cuda/cuda_compile_generated_hog.cu.o
[ 69%] Building CXX object modules/cudalegacy/CMakeFiles/opencv_test_cudalegacy.dir/test/TestCompact.cpp.o
[ 69%] Building CXX object modules/cudalegacy/CMakeFiles/opencv_test_cudalegacy.dir/test/test_nvidia.cpp.o
[ 69%] Linking CXX executable ../../bin/opencv_perf_cudalegacy
[ 69%] Built target opencv_perf_cudalegacy
[ 69%] Building CXX object modules/cudalegacy/CMakeFiles/opencv_test_cudalegacy.dir/test/test_labeling.cpp.o
Scanning dependencies of target opencv_cudaobjdetect
[ 69%] Building CXX object modules/cudaobjdetect/CMakeFiles/opencv_cudaobjdetect.dir/src/cascadeclassifier.cpp.o
[ 69%] Building CXX object modules/cudaobjdetect/CMakeFiles/opencv_cudaobjdetect.dir/src/hog.cpp.o
[ 69%] Building NVCC (Device) object modules/cudaoptflow/CMakeFiles/cuda_compile.dir/src/cuda/cuda_compile_generated_tvl1flow.cu.o
[ 69%] Building NVCC (Device) object modules/cudaoptflow/CMakeFiles/cuda_compile.dir/src/cuda/cuda_compile_generated_pyrlk.cu.o
[ 69%] Building CXX object modules/cudalegacy/CMakeFiles/opencv_test_cudalegacy.dir/test/test_calib3d.cpp.o
[ 70%] Linking CXX shared library ../../lib/libopencv_cudaobjdetect.so
[ 70%] Built target opencv_cudaobjdetect
[ 70%] Generating opencl_kernels_stitching.cpp, opencl_kernels_stitching.hpp
[ 70%] Building NVCC (Device) object modules/stitching/CMakeFiles/cuda_compile.dir/src/cuda/cuda_compile_generated_build_warp_maps.cu.o
[ 70%] Building NVCC (Device) object modules/cudaoptflow/CMakeFiles/cuda_compile.dir/src/cuda/cuda_compile_generated_farneback.cu.o
[ 71%] Building NVCC (Device) object modules/stitching/CMakeFiles/cuda_compile.dir/src/cuda/cuda_compile_generated_multiband_blend.cu.o
[ 71%] Building CXX object modules/cudalegacy/CMakeFiles/opencv_test_cudalegacy.dir/test/TestResize.cpp.o
Scanning dependencies of target opencv_stitching
[ 71%] Building CXX object modules/stitching/CMakeFiles/opencv_stitching.dir/src/warpers_cuda.cpp.o
[ 71%] Building CXX object modules/stitching/CMakeFiles/opencv_stitching.dir/src/blenders.cpp.o
[ 71%] Building CXX object modules/cudalegacy/CMakeFiles/opencv_test_cudalegacy.dir/test/TestIntegralImage.cpp.o
[ 71%] Building CXX object modules/stitching/CMakeFiles/opencv_stitching.dir/src/seam_finders.cpp.o
[ 71%] Building CXX object modules/stitching/CMakeFiles/opencv_stitching.dir/src/exposure_compensate.cpp.o
[ 71%] Building CXX object modules/cudalegacy/CMakeFiles/opencv_test_cudalegacy.dir/test/test_main.cpp.o
[ 71%] Building CXX object modules/cudalegacy/CMakeFiles/opencv_test_cudalegacy.dir/test/TestDrawRects.cpp.o
[ 71%] Building CXX object modules/stitching/CMakeFiles/opencv_stitching.dir/src/matchers.cpp.o
[ 71%] Building CXX object modules/stitching/CMakeFiles/opencv_stitching.dir/src/motion_estimators.cpp.o
[ 71%] Building CXX object modules/cudalegacy/CMakeFiles/opencv_test_cudalegacy.dir/test/main_nvidia.cpp.o
[ 71%] Building CXX object modules/stitching/CMakeFiles/opencv_stitching.dir/src/autocalib.cpp.o
[ 71%] Building CXX object modules/cudalegacy/CMakeFiles/opencv_test_cudalegacy.dir/test/TestHypothesesGrow.cpp.o
[ 71%] Building CXX object modules/stitching/CMakeFiles/opencv_stitching.dir/src/camera.cpp.o
[ 71%] Building CXX object modules/stitching/CMakeFiles/opencv_stitching.dir/src/timelapsers.cpp.o
[ 71%] Building CXX object modules/stitching/CMakeFiles/opencv_stitching.dir/src/util.cpp.o
[ 71%] Linking CXX executable ../../bin/opencv_test_cudalegacy
[ 71%] Built target opencv_test_cudalegacy
Scanning dependencies of target opencv_perf_cudaobjdetect
[ 71%] Building CXX object modules/cudaobjdetect/CMakeFiles/opencv_perf_cudaobjdetect.dir/perf/perf_main.cpp.o
[ 72%] Building CXX object modules/cudaobjdetect/CMakeFiles/opencv_perf_cudaobjdetect.dir/perf/perf_objdetect.cpp.o
[ 72%] Building CXX object modules/stitching/CMakeFiles/opencv_stitching.dir/src/warpers.cpp.o
[ 72%] Building CXX object modules/stitching/CMakeFiles/opencv_stitching.dir/src/stitcher.cpp.o
[ 72%] Linking CXX executable ../../bin/opencv_perf_cudaobjdetect
[ 72%] Built target opencv_perf_cudaobjdetect
Scanning dependencies of target opencv_test_cudaobjdetect
[ 72%] Building CXX object modules/cudaobjdetect/CMakeFiles/opencv_test_cudaobjdetect.dir/test/test_objdetect.cpp.o
[ 72%] Building CXX object modules/stitching/CMakeFiles/opencv_stitching.dir/opencl_kernels_stitching.cpp.o
[ 72%] Building CXX object modules/cudaobjdetect/CMakeFiles/opencv_test_cudaobjdetect.dir/test/test_main.cpp.o
[ 72%] Linking CXX shared library ../../lib/libopencv_stitching.so
[ 72%] Built target opencv_stitching
Scanning dependencies of target opencv_perf_stitching
[ 72%] Building CXX object modules/stitching/CMakeFiles/opencv_perf_stitching.dir/perf/perf_matchers.cpp.o
[ 72%] Building CXX object modules/stitching/CMakeFiles/opencv_perf_stitching.dir/perf/perf_main.cpp.o
[ 72%] Building CXX object modules/stitching/CMakeFiles/opencv_perf_stitching.dir/perf/perf_stich.cpp.o
[ 72%] Linking CXX executable ../../bin/opencv_test_cudaobjdetect
[ 72%] Built target opencv_test_cudaobjdetect
Scanning dependencies of target opencv_test_stitching
[ 72%] Building CXX object modules/stitching/CMakeFiles/opencv_test_stitching.dir/test/test_blenders.cuda.cpp.o
[ 72%] Building CXX object modules/stitching/CMakeFiles/opencv_test_stitching.dir/test/ocl/test_warpers.cpp.o
[ 72%] Building CXX object modules/stitching/CMakeFiles/opencv_perf_stitching.dir/perf/perf_estimators.cpp.o
[ 72%] Building CXX object modules/stitching/CMakeFiles/opencv_perf_stitching.dir/perf/opencl/perf_warpers.cpp.o
[ 72%] Building CXX object modules/stitching/CMakeFiles/opencv_test_stitching.dir/test/test_matchers.cpp.o
[ 72%] Building CXX object modules/stitching/CMakeFiles/opencv_perf_stitching.dir/perf/opencl/perf_stitch.cpp.o
[ 72%] Building CXX object modules/stitching/CMakeFiles/opencv_test_stitching.dir/test/test_main.cpp.o
[ 72%] Building CXX object modules/stitching/CMakeFiles/opencv_test_stitching.dir/test/test_blenders.cpp.o
[ 72%] Linking CXX executable ../../bin/opencv_perf_stitching
[ 72%] Built target opencv_perf_stitching
[ 72%] Linking CXX executable ../../bin/opencv_test_stitching
[ 72%] Built target opencv_test_stitching
Scanning dependencies of target opencv_cudaoptflow
[ 72%] Building CXX object modules/cudaoptflow/CMakeFiles/opencv_cudaoptflow.dir/src/tvl1flow.cpp.o
[ 72%] Building CXX object modules/cudaoptflow/CMakeFiles/opencv_cudaoptflow.dir/src/brox.cpp.o
[ 72%] Building CXX object modules/cudaoptflow/CMakeFiles/opencv_cudaoptflow.dir/src/pyrlk.cpp.o
[ 72%] Building CXX object modules/cudaoptflow/CMakeFiles/opencv_cudaoptflow.dir/src/farneback.cpp.o
[ 72%] Linking CXX shared library ../../lib/libopencv_cudaoptflow.so
[ 72%] Built target opencv_cudaoptflow
Scanning dependencies of target opencv_perf_cudaoptflow
[ 72%] Generating opencl_kernels_superres.cpp, opencl_kernels_superres.hpp
[ 72%] Building NVCC (Device) object modules/videostab/CMakeFiles/cuda_compile.dir/src/cuda/cuda_compile_generated_global_motion.cu.o
Scanning dependencies of target opencv_test_cudaoptflow
[ 73%] Building NVCC (Device) object modules/superres/CMakeFiles/cuda_compile.dir/src/cuda/cuda_compile_generated_btv_l1_gpu.cu.o
[ 74%] Building CXX object modules/cudaoptflow/CMakeFiles/opencv_test_cudaoptflow.dir/test/test_optflow.cpp.o
[ 74%] Building CXX object modules/cudaoptflow/CMakeFiles/opencv_perf_cudaoptflow.dir/perf/perf_main.cpp.o
/usr/local/cuda-8.0/include/thrust/detail/integer_traits.h(56): warning: integer conversion resulted in a change of sign

[ 74%] Building CXX object modules/cudaoptflow/CMakeFiles/opencv_perf_cudaoptflow.dir/perf/perf_optflow.cpp.o
/usr/local/cuda-8.0/include/thrust/detail/integer_traits.h(56): warning: integer conversion resulted in a change of sign

Scanning dependencies of target opencv_superres
[ 74%] Building CXX object modules/superres/CMakeFiles/opencv_superres.dir/src/btv_l1_cuda.cpp.o
[ 74%] Building CXX object modules/cudaoptflow/CMakeFiles/opencv_test_cudaoptflow.dir/test/test_main.cpp.o
[ 74%] Linking CXX executable ../../bin/opencv_perf_cudaoptflow
[ 74%] Linking CXX executable ../../bin/opencv_test_cudaoptflow
[ 74%] Built target opencv_perf_cudaoptflow
[ 74%] Building CXX object modules/superres/CMakeFiles/opencv_superres.dir/src/super_resolution.cpp.o
[ 74%] Built target opencv_test_cudaoptflow
[ 74%] Building CXX object modules/superres/CMakeFiles/opencv_superres.dir/src/btv_l1.cpp.o
[ 74%] Building CXX object modules/superres/CMakeFiles/opencv_superres.dir/src/optical_flow.cpp.o
[ 74%] Building CXX object modules/superres/CMakeFiles/opencv_superres.dir/src/frame_source.cpp.o
Scanning dependencies of target opencv_videostab
[ 74%] Building CXX object modules/videostab/CMakeFiles/opencv_videostab.dir/src/fast_marching.cpp.o
[ 74%] Building CXX object modules/videostab/CMakeFiles/opencv_videostab.dir/src/outlier_rejection.cpp.o
[ 74%] Building CXX object modules/superres/CMakeFiles/opencv_superres.dir/src/input_array_utility.cpp.o
[ 74%] Building CXX object modules/videostab/CMakeFiles/opencv_videostab.dir/src/motion_stabilizing.cpp.o
[ 74%] Building CXX object modules/superres/CMakeFiles/opencv_superres.dir/opencl_kernels_superres.cpp.o
[ 74%] Building CXX object modules/videostab/CMakeFiles/opencv_videostab.dir/src/log.cpp.o
[ 74%] Building CXX object modules/videostab/CMakeFiles/opencv_videostab.dir/src/optical_flow.cpp.o
[ 74%] Linking CXX shared library ../../lib/libopencv_superres.so
[ 74%] Built target opencv_superres
Scanning dependencies of target opencv_perf_superres
[ 74%] Building CXX object modules/superres/CMakeFiles/opencv_perf_superres.dir/perf/perf_main.cpp.o
[ 75%] Building CXX object modules/superres/CMakeFiles/opencv_perf_superres.dir/perf/perf_superres.cpp.o
[ 75%] Building CXX object modules/videostab/CMakeFiles/opencv_videostab.dir/src/wobble_suppression.cpp.o
[ 75%] Building CXX object modules/videostab/CMakeFiles/opencv_videostab.dir/src/global_motion.cpp.o
[ 75%] Building CXX object modules/videostab/CMakeFiles/opencv_videostab.dir/src/deblurring.cpp.o
[ 75%] Building CXX object modules/videostab/CMakeFiles/opencv_videostab.dir/src/frame_source.cpp.o
[ 75%] Building CXX object modules/videostab/CMakeFiles/opencv_videostab.dir/src/inpainting.cpp.o
[ 75%] Linking CXX executable ../../bin/opencv_perf_superres
[ 75%] Building CXX object modules/videostab/CMakeFiles/opencv_videostab.dir/src/stabilizer.cpp.o
[ 75%] Built target opencv_perf_superres
Scanning dependencies of target opencv_test_superres
[ 75%] Building CXX object modules/superres/CMakeFiles/opencv_test_superres.dir/test/test_superres.cpp.o
[ 75%] Building CXX object modules/superres/CMakeFiles/opencv_test_superres.dir/test/test_main.cpp.o
Scanning dependencies of target example_gpu_generalized_hough
[ 75%] Building CXX object samples/gpu/CMakeFiles/example_gpu_generalized_hough.dir/generalized_hough.cpp.o
[ 75%] Linking CXX executable ../../bin/gpu-example-generalized_hough
[ 75%] Built target example_gpu_generalized_hough
Scanning dependencies of target example_gpu_cascadeclassifier_nvidia_api
[ 75%] Building CXX object samples/gpu/CMakeFiles/example_gpu_cascadeclassifier_nvidia_api.dir/cascadeclassifier_nvidia_api.cpp.o
[ 75%] Linking CXX executable ../../bin/opencv_test_superres
[ 75%] Built target opencv_test_superres
Scanning dependencies of target example_gpu_video_reader
[ 75%] Building CXX object samples/gpu/CMakeFiles/example_gpu_video_reader.dir/video_reader.cpp.o
Scanning dependencies of target example_gpu_surf_keypoint_matcher
[ 76%] Building CXX object samples/gpu/CMakeFiles/example_gpu_surf_keypoint_matcher.dir/surf_keypoint_matcher.cpp.o
[ 76%] Linking CXX shared library ../../lib/libopencv_videostab.so
[ 76%] Linking CXX executable ../../bin/gpu-example-surf_keypoint_matcher
[ 76%] Built target opencv_videostab
Scanning dependencies of target example_gpu_farneback_optical_flow
[ 76%] Building CXX object samples/gpu/CMakeFiles/example_gpu_farneback_optical_flow.dir/farneback_optical_flow.cpp.o
[ 76%] Built target example_gpu_surf_keypoint_matcher
Scanning dependencies of target example_gpu_performance
[ 76%] Building CXX object samples/gpu/CMakeFiles/example_gpu_performance.dir/performance/performance.cpp.o
[ 76%] Linking CXX executable ../../bin/gpu-example-video_reader
[ 76%] Built target example_gpu_video_reader
[ 76%] Building CXX object samples/gpu/CMakeFiles/example_gpu_performance.dir/performance/tests.cpp.o
[ 76%] Linking CXX executable ../../bin/gpu-example-cascadeclassifier_nvidia_api
[ 76%] Built target example_gpu_cascadeclassifier_nvidia_api
Scanning dependencies of target example_gpu_stereo_match
[ 76%] Building CXX object samples/gpu/CMakeFiles/example_gpu_stereo_match.dir/stereo_match.cpp.o
[ 76%] Linking CXX executable ../../bin/gpu-example-farneback_optical_flow
[ 76%] Built target example_gpu_farneback_optical_flow
Scanning dependencies of target example_gpu_optical_flow
[ 77%] Building CXX object samples/gpu/CMakeFiles/example_gpu_optical_flow.dir/optical_flow.cpp.o
Scanning dependencies of target example_gpu_houghlines
[ 77%] Building CXX object samples/gpu/CMakeFiles/example_gpu_houghlines.dir/houghlines.cpp.o
[ 77%] Linking CXX executable ../../bin/gpu-example-houghlines
[ 77%] Built target example_gpu_houghlines
Scanning dependencies of target example_gpu_hog
[ 77%] Building CXX object samples/gpu/CMakeFiles/example_gpu_hog.dir/hog.cpp.o
[ 77%] Linking CXX executable ../../bin/gpu-example-optical_flow
[ 77%] Built target example_gpu_optical_flow
Scanning dependencies of target example_gpu_multi
[ 77%] Building CXX object samples/gpu/CMakeFiles/example_gpu_multi.dir/multi.cpp.o
[ 77%] Linking CXX executable ../../bin/gpu-example-stereo_match
[ 77%] Built target example_gpu_stereo_match
Scanning dependencies of target example_gpu_video_writer
[ 77%] Building CXX object samples/gpu/CMakeFiles/example_gpu_video_writer.dir/video_writer.cpp.o
[ 77%] Linking CXX executable ../../bin/gpu-example-video_writer
[ 77%] Built target example_gpu_video_writer
Scanning dependencies of target example_gpu_alpha_comp
[ 77%] Building CXX object samples/gpu/CMakeFiles/example_gpu_alpha_comp.dir/alpha_comp.cpp.o
[ 77%] Linking CXX executable ../../bin/gpu-example-multi
[ 77%] Built target example_gpu_multi
Scanning dependencies of target example_gpu_cascadeclassifier
[ 77%] Building CXX object samples/gpu/CMakeFiles/example_gpu_cascadeclassifier.dir/cascadeclassifier.cpp.o
[ 77%] Linking CXX executable ../../bin/gpu-example-alpha_comp
[ 77%] Built target example_gpu_alpha_comp
Scanning dependencies of target example_gpu_super_resolution
[ 77%] Building CXX object samples/gpu/CMakeFiles/example_gpu_super_resolution.dir/super_resolution.cpp.o
[ 77%] Linking CXX executable ../../bin/performance_gpu
[ 77%] Linking CXX executable ../../bin/gpu-example-hog
[ 77%] Built target example_gpu_performance
Scanning dependencies of target example_gpu_driver_api_stereo_multi
[ 77%] Building CXX object samples/gpu/CMakeFiles/example_gpu_driver_api_stereo_multi.dir/driver_api_stereo_multi.cpp.o
[ 77%] Built target example_gpu_hog
Scanning dependencies of target example_gpu_pyrlk_optical_flow
[ 77%] Building CXX object samples/gpu/CMakeFiles/example_gpu_pyrlk_optical_flow.dir/pyrlk_optical_flow.cpp.o
[ 77%] Linking CXX executable ../../bin/gpu-example-cascadeclassifier
[ 77%] Linking CXX executable ../../bin/gpu-example-super_resolution
[ 77%] Built target example_gpu_cascadeclassifier
Scanning dependencies of target example_gpu_bgfg_segm
[ 77%] Building CXX object samples/gpu/CMakeFiles/example_gpu_bgfg_segm.dir/bgfg_segm.cpp.o
[ 77%] Built target example_gpu_super_resolution
Scanning dependencies of target example_gpu_morphology
[ 77%] Building CXX object samples/gpu/CMakeFiles/example_gpu_morphology.dir/morphology.cpp.o
[ 77%] Linking CXX executable ../../bin/gpu-example-driver_api_stereo_multi
[ 77%] Built target example_gpu_driver_api_stereo_multi
Scanning dependencies of target example_gpu_opticalflow_nvidia_api
[ 77%] Linking CXX executable ../../bin/gpu-example-pyrlk_optical_flow
[ 77%] Building CXX object samples/gpu/CMakeFiles/example_gpu_opticalflow_nvidia_api.dir/opticalflow_nvidia_api.cpp.o
[ 77%] Built target example_gpu_pyrlk_optical_flow
Scanning dependencies of target example_gpu_stereo_multi
[ 77%] Building CXX object samples/gpu/CMakeFiles/example_gpu_stereo_multi.dir/stereo_multi.cpp.o
[ 77%] Linking CXX executable ../../bin/gpu-example-morphology
[ 77%] Linking CXX executable ../../bin/gpu-example-bgfg_segm
[ 77%] Built target example_gpu_morphology
Scanning dependencies of target example_gpu_driver_api_multi
[ 78%] Building CXX object samples/gpu/CMakeFiles/example_gpu_driver_api_multi.dir/driver_api_multi.cpp.o
[ 78%] Built target example_gpu_bgfg_segm
Scanning dependencies of target opencv_test_videostab
[ 79%] Building CXX object modules/videostab/CMakeFiles/opencv_test_videostab.dir/test/test_motion_estimation.cpp.o
[ 79%] Linking CXX executable ../../bin/gpu-example-driver_api_multi
[ 79%] Built target example_gpu_driver_api_multi
[ 79%] Building CXX object modules/videostab/CMakeFiles/opencv_test_videostab.dir/test/test_main.cpp.o
[ 79%] Linking CXX executable ../../bin/gpu-example-opticalflow_nvidia_api
[ 79%] Linking CXX executable ../../bin/gpu-example-stereo_multi
[ 79%] Built target example_gpu_opticalflow_nvidia_api
[ 79%] Generating pyopencv_generated_include.h, pyopencv_generated_funcs.h, pyopencv_generated_types.h, pyopencv_generated_type_reg.h, pyopencv_generated_ns_reg.h
[ 79%] Built target example_gpu_stereo_multi
[ 79%] Generating pyopencv_generated_include.h, pyopencv_generated_funcs.h, pyopencv_generated_types.h, pyopencv_generated_type_reg.h, pyopencv_generated_ns_reg.h
Scanning dependencies of target cpp-tutorial-pnp_detection
[ 79%] Building CXX object samples/cpp/CMakeFiles/cpp-tutorial-pnp_detection.dir/tutorial_code/calib3d/real_time_pose_estimation/src/main_detection.cpp.o
[ 79%] Linking CXX executable ../../bin/opencv_test_videostab
[ 79%] Built target opencv_test_videostab
[ 79%] Building CXX object samples/cpp/CMakeFiles/cpp-tutorial-pnp_detection.dir/tutorial_code/calib3d/real_time_pose_estimation/src/CsvReader.cpp.o
Scanning dependencies of target opencv_python2
[ 79%] Building CXX object modules/python2/CMakeFiles/opencv_python2.dir/__/src2/cv2.cpp.o
Scanning dependencies of target opencv_python3
[ 79%] Building CXX object modules/python3/CMakeFiles/opencv_python3.dir/__/src2/cv2.cpp.o
[ 79%] Building CXX object samples/cpp/CMakeFiles/cpp-tutorial-pnp_detection.dir/tutorial_code/calib3d/real_time_pose_estimation/src/CsvWriter.cpp.o
[ 79%] Building CXX object samples/cpp/CMakeFiles/cpp-tutorial-pnp_detection.dir/tutorial_code/calib3d/real_time_pose_estimation/src/ModelRegistration.cpp.o
[ 79%] Building CXX object samples/cpp/CMakeFiles/cpp-tutorial-pnp_detection.dir/tutorial_code/calib3d/real_time_pose_estimation/src/Mesh.cpp.o
[ 79%] Building CXX object samples/cpp/CMakeFiles/cpp-tutorial-pnp_detection.dir/tutorial_code/calib3d/real_time_pose_estimation/src/Model.cpp.o
[ 79%] Building CXX object samples/cpp/CMakeFiles/cpp-tutorial-pnp_detection.dir/tutorial_code/calib3d/real_time_pose_estimation/src/PnPProblem.cpp.o
[ 79%] Building CXX object samples/cpp/CMakeFiles/cpp-tutorial-pnp_detection.dir/tutorial_code/calib3d/real_time_pose_estimation/src/Utils.cpp.o
[ 79%] Building CXX object samples/cpp/CMakeFiles/cpp-tutorial-pnp_detection.dir/tutorial_code/calib3d/real_time_pose_estimation/src/RobustMatcher.cpp.o
Scanning dependencies of target example_minarea
[ 79%] Building CXX object samples/cpp/CMakeFiles/example_minarea.dir/minarea.cpp.o
[ 79%] Linking CXX executable ../../bin/cpp-tutorial-pnp_detection
[ 79%] Built target cpp-tutorial-pnp_detection
Scanning dependencies of target example_houghlines
[ 79%] Building CXX object samples/cpp/CMakeFiles/example_houghlines.dir/houghlines.cpp.o
[ 79%] Linking CXX executable ../../bin/cpp-example-minarea
[ 79%] Built target example_minarea
Scanning dependencies of target example_facial_features
[ 79%] Building CXX object samples/cpp/CMakeFiles/example_facial_features.dir/facial_features.cpp.o
[ 79%] Linking CXX executable ../../bin/cpp-example-houghlines
[ 79%] Built target example_houghlines
Scanning dependencies of target example_mask_tmpl
[ 79%] Building CXX object samples/cpp/CMakeFiles/example_mask_tmpl.dir/mask_tmpl.cpp.o
[ 79%] Linking CXX executable ../../bin/cpp-example-facial_features
[ 79%] Built target example_facial_features
Scanning dependencies of target example_npr_demo
[ 79%] Building CXX object samples/cpp/CMakeFiles/example_npr_demo.dir/npr_demo.cpp.o
[ 79%] Linking CXX executable ../../bin/cpp-example-mask_tmpl
[ 79%] Built target example_mask_tmpl
Scanning dependencies of target example_letter_recog
[ 79%] Building CXX object samples/cpp/CMakeFiles/example_letter_recog.dir/letter_recog.cpp.o
[ 79%] Linking CXX executable ../../bin/cpp-example-npr_demo
[ 79%] Built target example_npr_demo
Scanning dependencies of target example_tree_engine
[ 79%] Building CXX object samples/cpp/CMakeFiles/example_tree_engine.dir/tree_engine.cpp.o
[ 79%] Linking CXX executable ../../bin/cpp-example-letter_recog
[ 79%] Linking CXX executable ../../bin/cpp-example-tree_engine
[ 79%] Built target example_letter_recog
Scanning dependencies of target example_bgfg_segm
[ 79%] Building CXX object samples/cpp/CMakeFiles/example_bgfg_segm.dir/bgfg_segm.cpp.o
[ 79%] Built target example_tree_engine
Scanning dependencies of target example_logistic_regression
[ 79%] Building CXX object samples/cpp/CMakeFiles/example_logistic_regression.dir/logistic_regression.cpp.o
[ 79%] Linking CXX executable ../../bin/cpp-example-bgfg_segm
[ 79%] Built target example_bgfg_segm
Scanning dependencies of target example_kmeans
[ 79%] Linking CXX executable ../../bin/cpp-example-logistic_regression
[ 79%] Building CXX object samples/cpp/CMakeFiles/example_kmeans.dir/kmeans.cpp.o
[ 79%] Built target example_logistic_regression
Scanning dependencies of target cpp-tutorial-pnp_registration
[ 79%] Building CXX object samples/cpp/CMakeFiles/cpp-tutorial-pnp_registration.dir/tutorial_code/calib3d/real_time_pose_estimation/src/main_registration.cpp.o
[ 79%] Linking CXX executable ../../bin/cpp-example-kmeans
[ 79%] Built target example_kmeans
[ 79%] Building CXX object samples/cpp/CMakeFiles/cpp-tutorial-pnp_registration.dir/tutorial_code/calib3d/real_time_pose_estimation/src/CsvReader.cpp.o
[ 80%] Building CXX object samples/cpp/CMakeFiles/cpp-tutorial-pnp_registration.dir/tutorial_code/calib3d/real_time_pose_estimation/src/CsvWriter.cpp.o
[ 80%] Building CXX object samples/cpp/CMakeFiles/cpp-tutorial-pnp_registration.dir/tutorial_code/calib3d/real_time_pose_estimation/src/ModelRegistration.cpp.o
[ 80%] Building CXX object samples/cpp/CMakeFiles/cpp-tutorial-pnp_registration.dir/tutorial_code/calib3d/real_time_pose_estimation/src/Mesh.cpp.o
[ 80%] Building CXX object samples/cpp/CMakeFiles/cpp-tutorial-pnp_registration.dir/tutorial_code/calib3d/real_time_pose_estimation/src/Model.cpp.o
[ 80%] Building CXX object samples/cpp/CMakeFiles/cpp-tutorial-pnp_registration.dir/tutorial_code/calib3d/real_time_pose_estimation/src/PnPProblem.cpp.o
[ 80%] Building CXX object samples/cpp/CMakeFiles/cpp-tutorial-pnp_registration.dir/tutorial_code/calib3d/real_time_pose_estimation/src/Utils.cpp.o
[ 80%] Building CXX object samples/cpp/CMakeFiles/cpp-tutorial-pnp_registration.dir/tutorial_code/calib3d/real_time_pose_estimation/src/RobustMatcher.cpp.o
Scanning dependencies of target example_lsd_lines
[ 80%] Building CXX object samples/cpp/CMakeFiles/example_lsd_lines.dir/lsd_lines.cpp.o
[ 80%] Linking CXX executable ../../bin/cpp-tutorial-pnp_registration
[ 80%] Built target cpp-tutorial-pnp_registration
Scanning dependencies of target example_dft
[ 80%] Building CXX object samples/cpp/CMakeFiles/example_dft.dir/dft.cpp.o
[ 80%] Linking CXX executable ../../bin/cpp-example-lsd_lines
[ 80%] Built target example_lsd_lines
Scanning dependencies of target example_calibration
[ 81%] Building CXX object samples/cpp/CMakeFiles/example_calibration.dir/calibration.cpp.o
[ 81%] Linking CXX executable ../../bin/cpp-example-dft
[ 81%] Built target example_dft
Scanning dependencies of target example_tvl1_optical_flow
[ 81%] Building CXX object samples/cpp/CMakeFiles/example_tvl1_optical_flow.dir/tvl1_optical_flow.cpp.o
[ 81%] Linking CXX executable ../../bin/cpp-example-tvl1_optical_flow
[ 81%] Built target example_tvl1_optical_flow
Scanning dependencies of target example_watershed
[ 81%] Building CXX object samples/cpp/CMakeFiles/example_watershed.dir/watershed.cpp.o
[ 81%] Linking CXX executable ../../bin/cpp-example-calibration
[ 81%] Linking CXX executable ../../bin/cpp-example-watershed
[ 81%] Built target example_calibration
Scanning dependencies of target example_stereo_calib
[ 81%] Built target example_watershed
Scanning dependencies of target example_stitching_detailed
[ 81%] Building CXX object samples/cpp/CMakeFiles/example_stereo_calib.dir/stereo_calib.cpp.o
[ 81%] Building CXX object samples/cpp/CMakeFiles/example_stitching_detailed.dir/stitching_detailed.cpp.o
[ 81%] Linking CXX executable ../../bin/cpp-example-stereo_calib
[ 81%] Built target example_stereo_calib
Scanning dependencies of target example_intelperc_capture
[ 81%] Building CXX object samples/cpp/CMakeFiles/example_intelperc_capture.dir/intelperc_capture.cpp.o
[ 81%] Linking CXX executable ../../bin/cpp-example-intelperc_capture
[ 81%] Built target example_intelperc_capture
Scanning dependencies of target example_videocapture_basic
[ 81%] Building CXX object samples/cpp/CMakeFiles/example_videocapture_basic.dir/videocapture_basic.cpp.o
[ 81%] Linking CXX executable ../../bin/cpp-example-videocapture_basic
[ 81%] Built target example_videocapture_basic
Scanning dependencies of target example_cloning_demo
[ 81%] Building CXX object samples/cpp/CMakeFiles/example_cloning_demo.dir/cloning_demo.cpp.o
[ 81%] Linking CXX executable ../../bin/cpp-example-stitching_detailed
[ 81%] Built target example_stitching_detailed
Scanning dependencies of target example_imagelist_creator
[ 81%] Building CXX object samples/cpp/CMakeFiles/example_imagelist_creator.dir/imagelist_creator.cpp.o
[ 81%] Linking CXX executable ../../bin/cpp-example-imagelist_creator
[ 81%] Built target example_imagelist_creator
Scanning dependencies of target example_pca
[ 81%] Linking CXX executable ../../bin/cpp-example-cloning_demo
[ 81%] Building CXX object samples/cpp/CMakeFiles/example_pca.dir/pca.cpp.o
[ 81%] Built target example_cloning_demo
Scanning dependencies of target example_filestorage
[ 81%] Building CXX object samples/cpp/CMakeFiles/example_filestorage.dir/filestorage.cpp.o
[ 81%] Linking CXX executable ../../bin/cpp-example-filestorage
[ 81%] Built target example_filestorage
Scanning dependencies of target example_demhist
[ 81%] Building CXX object samples/cpp/CMakeFiles/example_demhist.dir/demhist.cpp.o
[ 81%] Linking CXX executable ../../bin/cpp-example-pca
[ 81%] Built target example_pca
Scanning dependencies of target example_points_classifier
[ 81%] Building CXX object samples/cpp/CMakeFiles/example_points_classifier.dir/points_classifier.cpp.o
[ 81%] Linking CXX executable ../../bin/cpp-example-demhist
[ 81%] Built target example_demhist
Scanning dependencies of target example_train_HOG
[ 81%] Building CXX object samples/cpp/CMakeFiles/example_train_HOG.dir/train_HOG.cpp.o
[ 81%] Linking CXX executable ../../bin/cpp-example-points_classifier
[ 81%] Built target example_points_classifier
Scanning dependencies of target example_camshiftdemo
[ 81%] Building CXX object samples/cpp/CMakeFiles/example_camshiftdemo.dir/camshiftdemo.cpp.o
[ 81%] Linking CXX executable ../../bin/cpp-example-camshiftdemo
[ 81%] Built target example_camshiftdemo
Scanning dependencies of target example_morphology2
[ 81%] Building CXX object samples/cpp/CMakeFiles/example_morphology2.dir/morphology2.cpp.o
[ 81%] Linking CXX executable ../../bin/cpp-example-train_HOG
[ 81%] Built target example_train_HOG
Scanning dependencies of target tutorial_AKAZE_match
[ 81%] Building CXX object samples/cpp/CMakeFiles/tutorial_AKAZE_match.dir/tutorial_code/features2D/AKAZE_match.cpp.o
[ 81%] Linking CXX executable ../../bin/cpp-example-morphology2
[ 81%] Built target example_morphology2
Scanning dependencies of target tutorial_non_linear_svms
[ 81%] Building CXX object samples/cpp/CMakeFiles/tutorial_non_linear_svms.dir/tutorial_code/ml/non_linear_svms/non_linear_svms.cpp.o
[ 81%] Linking CXX executable ../../bin/cpp-tutorial-non_linear_svms
[ 81%] Built target tutorial_non_linear_svms
Scanning dependencies of target tutorial_mat_mask_operations
[ 81%] Building CXX object samples/cpp/CMakeFiles/tutorial_mat_mask_operations.dir/tutorial_code/core/mat_mask_operations/mat_mask_operations.cpp.o
[ 81%] Linking CXX executable ../../bin/cpp-tutorial-AKAZE_match
[ 81%] Built target tutorial_AKAZE_match
Scanning dependencies of target tutorial_Drawing_2
[ 82%] Building CXX object samples/cpp/CMakeFiles/tutorial_Drawing_2.dir/tutorial_code/core/Matrix/Drawing_2.cpp.o
[ 82%] Linking CXX executable ../../bin/cpp-tutorial-mat_mask_operations
[ 82%] Linking CXX executable ../../bin/cpp-tutorial-Drawing_2
[ 82%] Built target tutorial_mat_mask_operations
Scanning dependencies of target example_falsecolor
[ 82%] Building CXX object samples/cpp/CMakeFiles/example_falsecolor.dir/falsecolor.cpp.o
[ 82%] Built target tutorial_Drawing_2
Scanning dependencies of target example_cout_mat
[ 82%] Building CXX object samples/cpp/CMakeFiles/example_cout_mat.dir/cout_mat.cpp.o
[ 83%] Linking CXX executable ../../bin/cpp-example-cout_mat
[ 83%] Built target example_cout_mat
Scanning dependencies of target tutorial_AddingImages
[ 83%] Building CXX object samples/cpp/CMakeFiles/tutorial_AddingImages.dir/tutorial_code/core/AddingImages/AddingImages.cpp.o
[ 83%] Linking CXX executable ../../bin/cpp-tutorial-AddingImages
[ 83%] Linking CXX executable ../../bin/cpp-example-falsecolor
[ 83%] Built target tutorial_AddingImages
Scanning dependencies of target example_train_svmsgd
[ 83%] Built target example_falsecolor
Scanning dependencies of target tutorial_introduction_to_svm
[ 83%] Building CXX object samples/cpp/CMakeFiles/example_train_svmsgd.dir/train_svmsgd.cpp.o
[ 83%] Building CXX object samples/cpp/CMakeFiles/tutorial_introduction_to_svm.dir/tutorial_code/ml/introduction_to_svm/introduction_to_svm.cpp.o
[ 83%] Linking CXX executable ../../bin/cpp-tutorial-introduction_to_svm
[ 83%] Built target tutorial_introduction_to_svm
Scanning dependencies of target example_kalman
[ 83%] Building CXX object samples/cpp/CMakeFiles/example_kalman.dir/kalman.cpp.o
[ 83%] Linking CXX executable ../../bin/cpp-example-train_svmsgd
[ 83%] Built target example_train_svmsgd
Scanning dependencies of target example_image_sequence
[ 84%] Building CXX object samples/cpp/CMakeFiles/example_image_sequence.dir/image_sequence.cpp.o
[ 84%] Linking CXX executable ../../bin/cpp-example-kalman
[ 84%] Built target example_kalman
Scanning dependencies of target tutorial_display_image
[ 84%] Building CXX object samples/cpp/CMakeFiles/tutorial_display_image.dir/tutorial_code/introduction/display_image/display_image.cpp.o
[ 84%] Linking CXX executable ../../bin/cpp-example-image_sequence
[ 84%] Built target example_image_sequence
Scanning dependencies of target example_example
[ 84%] Building CXX object samples/cpp/CMakeFiles/example_example.dir/example_cmake/example.cpp.o
[ 84%] Linking CXX executable ../../bin/cpp-tutorial-display_image
[ 84%] Built target tutorial_display_image
Scanning dependencies of target tutorial_Drawing_1
[ 84%] Building CXX object samples/cpp/CMakeFiles/tutorial_Drawing_1.dir/tutorial_code/core/Matrix/Drawing_1.cpp.o
[ 84%] Linking CXX executable ../../bin/cpp-example-example
[ 84%] Built target example_example
Scanning dependencies of target example_distrans
[ 84%] Building CXX object samples/cpp/CMakeFiles/example_distrans.dir/distrans.cpp.o
[ 84%] Linking CXX executable ../../bin/cpp-tutorial-Drawing_1
[ 84%] Built target tutorial_Drawing_1
Scanning dependencies of target tutorial_filter2D_demo
[ 84%] Building CXX object samples/cpp/CMakeFiles/tutorial_filter2D_demo.dir/tutorial_code/ImgTrans/filter2D_demo.cpp.o
[ 85%] Linking CXX executable ../../bin/cpp-example-distrans
[ 85%] Built target example_distrans
Scanning dependencies of target tutorial_hull_demo
[ 86%] Building CXX object samples/cpp/CMakeFiles/tutorial_hull_demo.dir/tutorial_code/ShapeDescriptors/hull_demo.cpp.o
[ 86%] Linking CXX executable ../../bin/cpp-tutorial-filter2D_demo
[ 86%] Built target tutorial_filter2D_demo
Scanning dependencies of target tutorial_discrete_fourier_transform
[ 86%] Building CXX object samples/cpp/CMakeFiles/tutorial_discrete_fourier_transform.dir/tutorial_code/core/discrete_fourier_transform/discrete_fourier_transform.cpp.o
[ 86%] Linking CXX executable ../../bin/cpp-tutorial-hull_demo
[ 86%] Built target tutorial_hull_demo
Scanning dependencies of target tutorial_file_input_output
[ 86%] Building CXX object samples/cpp/CMakeFiles/tutorial_file_input_output.dir/tutorial_code/core/file_input_output/file_input_output.cpp.o
[ 86%] Linking CXX executable ../../bin/cpp-tutorial-discrete_fourier_transform
[ 86%] Built target tutorial_discrete_fourier_transform
Scanning dependencies of target example_delaunay2
[ 86%] Building CXX object samples/cpp/CMakeFiles/example_delaunay2.dir/delaunay2.cpp.o
[ 86%] Linking CXX executable ../../bin/cpp-tutorial-file_input_output
[ 86%] Built target tutorial_file_input_output
Scanning dependencies of target example_neural_network
[ 86%] Building CXX object samples/cpp/CMakeFiles/example_neural_network.dir/neural_network.cpp.o
[ 86%] Linking CXX executable ../../bin/cpp-example-delaunay2
[ 86%] Built target example_delaunay2
Scanning dependencies of target example_grabcut
[ 86%] Building CXX object samples/cpp/CMakeFiles/example_grabcut.dir/grabcut.cpp.o
[ 87%] Linking CXX executable ../../bin/cpp-example-neural_network
[ 87%] Built target example_neural_network
Scanning dependencies of target tutorial_how_to_use_OpenCV_parallel_for_
[ 87%] Building CXX object samples/cpp/CMakeFiles/tutorial_how_to_use_OpenCV_parallel_for_.dir/tutorial_code/core/how_to_use_OpenCV_parallel_for_/how_to_use_OpenCV_parallel_for_.cpp.o
[ 87%] Linking CXX executable ../../bin/cpp-example-grabcut
[ 87%] Linking CXX executable ../../bin/cpp-tutorial-how_to_use_OpenCV_parallel_for_
[ 87%] Linking CXX shared module ../../lib/cv2.so
[ 87%] Linking CXX shared module ../../lib/python3/cv2.cpython-35m-aarch64-linux-gnu.so
[ 87%] Built target example_grabcut
[ 87%] Built target tutorial_how_to_use_OpenCV_parallel_for_
Scanning dependencies of target tutorial_findContours_demo
Scanning dependencies of target example_peopledetect
[ 87%] Building CXX object samples/cpp/CMakeFiles/tutorial_findContours_demo.dir/tutorial_code/ShapeDescriptors/findContours_demo.cpp.o
[ 87%] Building CXX object samples/cpp/CMakeFiles/example_peopledetect.dir/peopledetect.cpp.o
[ 87%] Built target opencv_python2
Scanning dependencies of target example_contours2
[ 87%] Building CXX object samples/cpp/CMakeFiles/example_contours2.dir/contours2.cpp.o
[ 87%] Built target opencv_python3
Scanning dependencies of target example_dbt_face_detection
[ 87%] Building CXX object samples/cpp/CMakeFiles/example_dbt_face_detection.dir/dbt_face_detection.cpp.o
[ 87%] Linking CXX executable ../../bin/cpp-tutorial-findContours_demo
[ 87%] Linking CXX executable ../../bin/cpp-example-dbt_face_detection
[ 87%] Built target tutorial_findContours_demo
Scanning dependencies of target tutorial_moments_demo
[ 88%] Building CXX object samples/cpp/CMakeFiles/tutorial_moments_demo.dir/tutorial_code/ShapeDescriptors/moments_demo.cpp.o
[ 88%] Linking CXX executable ../../bin/cpp-example-peopledetect
[ 88%] Built target example_dbt_face_detection
[ 88%] Linking CXX executable ../../bin/cpp-example-contours2
Scanning dependencies of target example_em
[ 88%] Building CXX object samples/cpp/CMakeFiles/example_em.dir/em.cpp.o
[ 88%] Built target example_peopledetect
Scanning dependencies of target example_filestorage_base64
[ 88%] Built target example_contours2
Scanning dependencies of target tutorial_calcHist_Demo
[ 88%] Building CXX object samples/cpp/CMakeFiles/example_filestorage_base64.dir/filestorage_base64.cpp.o
[ 88%] Building CXX object samples/cpp/CMakeFiles/tutorial_calcHist_Demo.dir/tutorial_code/Histograms_Matching/calcHist_Demo.cpp.o
[ 88%] Linking CXX executable ../../bin/cpp-tutorial-moments_demo
[ 88%] Linking CXX executable ../../bin/cpp-example-filestorage_base64
[ 88%] Linking CXX executable ../../bin/cpp-example-em
[ 88%] Built target example_filestorage_base64
[ 88%] Built target tutorial_moments_demo
Scanning dependencies of target tutorial_calcBackProject_Demo2
Scanning dependencies of target tutorial_copyMakeBorder_demo
[ 88%] Building CXX object samples/cpp/CMakeFiles/tutorial_copyMakeBorder_demo.dir/tutorial_code/ImgTrans/copyMakeBorder_demo.cpp.o
[ 88%] Built target example_em
Scanning dependencies of target tutorial_documentation
[ 88%] Building CXX object samples/cpp/CMakeFiles/tutorial_calcBackProject_Demo2.dir/tutorial_code/Histograms_Matching/calcBackProject_Demo2.cpp.o
[ 88%] Building CXX object samples/cpp/CMakeFiles/tutorial_documentation.dir/tutorial_code/introduction/documentation/documentation.cpp.o
[ 88%] Linking CXX executable ../../bin/cpp-tutorial-calcHist_Demo
[ 88%] Built target tutorial_calcHist_Demo
[ 88%] Linking CXX executable ../../bin/cpp-tutorial-documentation
Scanning dependencies of target example_phase_corr
[ 88%] Building CXX object samples/cpp/CMakeFiles/example_phase_corr.dir/phase_corr.cpp.o
[ 88%] Built target tutorial_documentation
Scanning dependencies of target example_inpaint
[ 88%] Building CXX object samples/cpp/CMakeFiles/example_inpaint.dir/inpaint.cpp.o
[ 88%] Linking CXX executable ../../bin/cpp-tutorial-calcBackProject_Demo2
[ 88%] Linking CXX executable ../../bin/cpp-tutorial-copyMakeBorder_demo
[ 88%] Linking CXX executable ../../bin/cpp-example-phase_corr
[ 88%] Built target tutorial_calcBackProject_Demo2
Scanning dependencies of target tutorial_BasicLinearTransformsTrackbar
[ 88%] Built target tutorial_copyMakeBorder_demo
[ 88%] Building CXX object samples/cpp/CMakeFiles/tutorial_BasicLinearTransformsTrackbar.dir/tutorial_code/HighGUI/BasicLinearTransformsTrackbar.cpp.o
Scanning dependencies of target tutorial_how_to_scan_images
[ 88%] Building CXX object samples/cpp/CMakeFiles/tutorial_how_to_scan_images.dir/tutorial_code/core/how_to_scan_images/how_to_scan_images.cpp.o
[ 88%] Built target example_phase_corr
Scanning dependencies of target example_openni_capture
[ 88%] Linking CXX executable ../../bin/cpp-example-inpaint
[ 88%] Building CXX object samples/cpp/CMakeFiles/example_openni_capture.dir/openni_capture.cpp.o
[ 88%] Built target example_inpaint
Scanning dependencies of target example_videocapture_starter
[ 89%] Building CXX object samples/cpp/CMakeFiles/example_videocapture_starter.dir/videocapture_starter.cpp.o
[ 89%] Linking CXX executable ../../bin/cpp-tutorial-BasicLinearTransformsTrackbar
[ 89%] Built target tutorial_BasicLinearTransformsTrackbar
Scanning dependencies of target example_select3dobj
[ 89%] Building CXX object samples/cpp/CMakeFiles/example_select3dobj.dir/select3dobj.cpp.o
[ 89%] Linking CXX executable ../../bin/cpp-example-videocapture_starter
[ 89%] Linking CXX executable ../../bin/cpp-tutorial-how_to_scan_images
[ 89%] Linking CXX executable ../../bin/cpp-example-openni_capture
[ 89%] Built target tutorial_how_to_scan_images
Scanning dependencies of target tutorial_cornerDetector_Demo
[ 89%] Building CXX object samples/cpp/CMakeFiles/tutorial_cornerDetector_Demo.dir/tutorial_code/TrackingMotion/cornerDetector_Demo.cpp.o
[ 89%] Built target example_videocapture_starter
Scanning dependencies of target example_create_mask
[ 89%] Building CXX object samples/cpp/CMakeFiles/example_create_mask.dir/create_mask.cpp.o
[ 89%] Built target example_openni_capture
Scanning dependencies of target tutorial_generalContours_demo2
[ 89%] Building CXX object samples/cpp/CMakeFiles/tutorial_generalContours_demo2.dir/tutorial_code/ShapeDescriptors/generalContours_demo2.cpp.o
[ 89%] Linking CXX executable ../../bin/cpp-tutorial-cornerDetector_Demo
[ 89%] Linking CXX executable ../../bin/cpp-example-create_mask
[ 89%] Built target tutorial_cornerDetector_Demo
Scanning dependencies of target tutorial_decolor
[ 89%] Building CXX object samples/cpp/CMakeFiles/tutorial_decolor.dir/tutorial_code/photo/decolorization/decolor.cpp.o
[ 89%] Linking CXX executable ../../bin/cpp-tutorial-generalContours_demo2
[ 89%] Built target example_create_mask
Scanning dependencies of target tutorial_objectDetection
[ 89%] Building CXX object samples/cpp/CMakeFiles/tutorial_objectDetection.dir/tutorial_code/objectDetection/objectDetection.cpp.o
[ 89%] Built target tutorial_generalContours_demo2
Scanning dependencies of target example_squares
[ 89%] Building CXX object samples/cpp/CMakeFiles/example_squares.dir/squares.cpp.o
[ 89%] Linking CXX executable ../../bin/cpp-tutorial-decolor
[ 89%] Built target tutorial_decolor
Scanning dependencies of target tutorial_SBM_Sample
[ 89%] Building CXX object samples/cpp/CMakeFiles/tutorial_SBM_Sample.dir/tutorial_code/calib3d/stereoBM/SBM_Sample.cpp.o
[ 89%] Linking CXX executable ../../bin/cpp-tutorial-objectDetection
[ 89%] Built target tutorial_objectDetection
Scanning dependencies of target tutorial_planar_tracking
[ 89%] Building CXX object samples/cpp/CMakeFiles/tutorial_planar_tracking.dir/tutorial_code/features2D/AKAZE_tracking/planar_tracking.cpp.o
[ 89%] Linking CXX executable ../../bin/cpp-example-squares
[ 89%] Built target example_squares
Scanning dependencies of target tutorial_Morphology_1
[ 89%] Building CXX object samples/cpp/CMakeFiles/tutorial_Morphology_1.dir/tutorial_code/ImgProc/Morphology_1.cpp.o
[ 89%] Linking CXX executable ../../bin/cpp-tutorial-SBM_Sample
[ 89%] Built target tutorial_SBM_Sample
Scanning dependencies of target example_laplace
[ 89%] Building CXX object samples/cpp/CMakeFiles/example_laplace.dir/laplace.cpp.o
[ 89%] Linking CXX executable ../../bin/cpp-example-select3dobj
[ 89%] Built target example_select3dobj
Scanning dependencies of target tutorial_calcBackProject_Demo1
[ 89%] Building CXX object samples/cpp/CMakeFiles/tutorial_calcBackProject_Demo1.dir/tutorial_code/Histograms_Matching/calcBackProject_Demo1.cpp.o
[ 89%] Linking CXX executable ../../bin/cpp-tutorial-Morphology_1
[ 89%] Built target tutorial_Morphology_1
Scanning dependencies of target example_application_trace
[ 89%] Building CXX object samples/cpp/CMakeFiles/example_application_trace.dir/application_trace.cpp.o
[ 89%] Linking CXX executable ../../bin/cpp-example-laplace
[ 89%] Built target example_laplace
Scanning dependencies of target tutorial_cloning_gui
[ 89%] Building CXX object samples/cpp/CMakeFiles/tutorial_cloning_gui.dir/tutorial_code/photo/seamless_cloning/cloning_gui.cpp.o
[ 89%] Linking CXX executable ../../bin/cpp-tutorial-calcBackProject_Demo1
[ 89%] Built target tutorial_calcBackProject_Demo1
Scanning dependencies of target tutorial_interoperability_with_OpenCV_1
[ 89%] Building CXX object samples/cpp/CMakeFiles/tutorial_interoperability_with_OpenCV_1.dir/tutorial_code/core/interoperability_with_OpenCV_1/interoperability_with_OpenCV_1.cpp.o
[ 89%] Linking CXX executable ../../bin/cpp-tutorial-planar_tracking
[ 89%] Linking CXX executable ../../bin/cpp-example-application_trace
[ 89%] Linking CXX executable ../../bin/cpp-tutorial-interoperability_with_OpenCV_1
[ 89%] Built target tutorial_planar_tracking
Scanning dependencies of target example_houghcircles
[ 89%] Built target example_application_trace
Scanning dependencies of target example_image
[ 89%] Building CXX object samples/cpp/CMakeFiles/example_houghcircles.dir/houghcircles.cpp.o
[ 89%] Built target tutorial_interoperability_with_OpenCV_1
Scanning dependencies of target example_polar_transforms
[ 89%] Building CXX object samples/cpp/CMakeFiles/example_image.dir/image.cpp.o
[ 89%] Building CXX object samples/cpp/CMakeFiles/example_polar_transforms.dir/polar_transforms.cpp.o
[ 89%] Linking CXX executable ../../bin/cpp-tutorial-cloning_gui
[ 89%] Built target tutorial_cloning_gui
Scanning dependencies of target tutorial_hdr_imaging
[ 89%] Building CXX object samples/cpp/CMakeFiles/tutorial_hdr_imaging.dir/tutorial_code/photo/hdr_imaging/hdr_imaging.cpp.o
[ 89%] Linking CXX executable ../../bin/cpp-example-houghcircles
[ 89%] Linking CXX executable ../../bin/cpp-example-image
[ 90%] Linking CXX executable ../../bin/cpp-example-polar_transforms
[ 90%] Built target example_image
Scanning dependencies of target tutorial_introduction_to_pca
[ 90%] Built target example_houghcircles
[ 90%] Building CXX object samples/cpp/CMakeFiles/tutorial_introduction_to_pca.dir/tutorial_code/ml/introduction_to_pca/introduction_to_pca.cpp.o
Scanning dependencies of target tutorial_camera_calibration
[ 90%] Building CXX object samples/cpp/CMakeFiles/tutorial_camera_calibration.dir/tutorial_code/calib3d/camera_calibration/camera_calibration.cpp.o
[ 90%] Built target example_polar_transforms
Scanning dependencies of target tutorial_introduction_windows_vs
[ 90%] Building CXX object samples/cpp/CMakeFiles/tutorial_introduction_windows_vs.dir/tutorial_code/introduction/windows_visual_studio_Opencv/introduction_windows_vs.cpp.o
[ 90%] Linking CXX executable ../../bin/cpp-tutorial-hdr_imaging
[ 90%] Built target tutorial_hdr_imaging
Scanning dependencies of target tutorial_generalContours_demo1
[ 90%] Building CXX object samples/cpp/CMakeFiles/tutorial_generalContours_demo1.dir/tutorial_code/ShapeDescriptors/generalContours_demo1.cpp.o
[ 90%] Linking CXX executable ../../bin/cpp-tutorial-introduction_windows_vs
[ 90%] Built target tutorial_introduction_windows_vs
Scanning dependencies of target tutorial_AddingImagesTrackbar
[ 90%] Building CXX object samples/cpp/CMakeFiles/tutorial_AddingImagesTrackbar.dir/tutorial_code/HighGUI/AddingImagesTrackbar.cpp.o
[ 90%] Linking CXX executable ../../bin/cpp-tutorial-introduction_to_pca
[ 90%] Built target tutorial_introduction_to_pca
Scanning dependencies of target example_cloning_gui
[ 90%] Building CXX object samples/cpp/CMakeFiles/example_cloning_gui.dir/cloning_gui.cpp.o
[ 90%] Linking CXX executable ../../bin/cpp-tutorial-generalContours_demo1
[ 90%] Built target tutorial_generalContours_demo1
Scanning dependencies of target tutorial_gdal-image
[ 90%] Building CXX object samples/cpp/CMakeFiles/tutorial_gdal-image.dir/tutorial_code/imgcodecs/GDAL_IO/gdal-image.cpp.o
[ 90%] Linking CXX executable ../../bin/cpp-tutorial-AddingImagesTrackbar
[ 90%] Built target tutorial_AddingImagesTrackbar
Scanning dependencies of target tutorial_Laplace_Demo
[ 90%] Building CXX object samples/cpp/CMakeFiles/tutorial_Laplace_Demo.dir/tutorial_code/ImgTrans/Laplace_Demo.cpp.o
[ 91%] Linking CXX executable ../../bin/cpp-tutorial-gdal-image
[ 91%] Built target tutorial_gdal-image
Scanning dependencies of target tutorial_EqualizeHist_Demo
[ 91%] Building CXX object samples/cpp/CMakeFiles/tutorial_EqualizeHist_Demo.dir/tutorial_code/Histograms_Matching/EqualizeHist_Demo.cpp.o
[ 91%] Linking CXX executable ../../bin/cpp-tutorial-Laplace_Demo
[ 91%] Built target tutorial_Laplace_Demo
Scanning dependencies of target example_image_alignment
[ 91%] Building CXX object samples/cpp/CMakeFiles/example_image_alignment.dir/image_alignment.cpp.o
[ 92%] Linking CXX executable ../../bin/cpp-tutorial-camera_calibration
[ 92%] Linking CXX executable ../../bin/cpp-example-cloning_gui
[ 92%] Built target example_cloning_gui
Scanning dependencies of target example_detect_mser
[ 92%] Built target tutorial_camera_calibration
Scanning dependencies of target tutorial_HoughLines_Demo
[ 92%] Building CXX object samples/cpp/CMakeFiles/example_detect_mser.dir/detect_mser.cpp.o
[ 92%] Building CXX object samples/cpp/CMakeFiles/tutorial_HoughLines_Demo.dir/tutorial_code/ImgTrans/HoughLines_Demo.cpp.o
[ 92%] Linking CXX executable ../../bin/cpp-tutorial-EqualizeHist_Demo
[ 92%] Built target tutorial_EqualizeHist_Demo
Scanning dependencies of target tutorial_cloning_demo
[ 92%] Building CXX object samples/cpp/CMakeFiles/tutorial_cloning_demo.dir/tutorial_code/photo/seamless_cloning/cloning_demo.cpp.o
[ 92%] Linking CXX executable ../../bin/cpp-tutorial-HoughLines_Demo
[ 92%] Built target tutorial_HoughLines_Demo
Scanning dependencies of target tutorial_imageSegmentation
[ 92%] Building CXX object samples/cpp/CMakeFiles/tutorial_imageSegmentation.dir/tutorial_code/ImgTrans/imageSegmentation.cpp.o
[ 92%] Linking CXX executable ../../bin/cpp-example-image_alignment
[ 92%] Built target example_image_alignment
Scanning dependencies of target example_smiledetect
[ 92%] Building CXX object samples/cpp/CMakeFiles/example_smiledetect.dir/smiledetect.cpp.o
[ 92%] Linking CXX executable ../../bin/cpp-tutorial-cloning_demo
[ 92%] Built target tutorial_cloning_demo
Scanning dependencies of target tutorial_Remap_Demo
[ 92%] Building CXX object samples/cpp/CMakeFiles/tutorial_Remap_Demo.dir/tutorial_code/ImgTrans/Remap_Demo.cpp.o
[ 92%] Linking CXX executable ../../bin/cpp-example-smiledetect
[ 92%] Built target example_smiledetect
Scanning dependencies of target tutorial_cornerSubPix_Demo
[ 92%] Building CXX object samples/cpp/CMakeFiles/tutorial_cornerSubPix_Demo.dir/tutorial_code/TrackingMotion/cornerSubPix_Demo.cpp.o
[ 92%] Linking CXX executable ../../bin/cpp-tutorial-Remap_Demo
[ 92%] Built target tutorial_Remap_Demo
Scanning dependencies of target tutorial_Morphology_2
[ 92%] Building CXX object samples/cpp/CMakeFiles/tutorial_Morphology_2.dir/tutorial_code/ImgProc/Morphology_2.cpp.o
[ 92%] Linking CXX executable ../../bin/cpp-tutorial-imageSegmentation
[ 92%] Linking CXX executable ../../bin/cpp-example-detect_mser
[ 92%] Built target tutorial_imageSegmentation
Scanning dependencies of target tutorial_Geometric_Transforms_Demo
[ 92%] Built target example_detect_mser
Scanning dependencies of target tutorial_MatchTemplate_Demo
[ 92%] Building CXX object samples/cpp/CMakeFiles/tutorial_Geometric_Transforms_Demo.dir/tutorial_code/ImgTrans/Geometric_Transforms_Demo.cpp.o
[ 93%] Building CXX object samples/cpp/CMakeFiles/tutorial_MatchTemplate_Demo.dir/tutorial_code/Histograms_Matching/MatchTemplate_Demo.cpp.o
[ 94%] Linking CXX executable ../../bin/cpp-tutorial-cornerSubPix_Demo
[ 94%] Built target tutorial_cornerSubPix_Demo
Scanning dependencies of target example_drawing
[ 94%] Building CXX object samples/cpp/CMakeFiles/example_drawing.dir/drawing.cpp.o
[ 94%] Linking CXX executable ../../bin/cpp-tutorial-Morphology_2
[ 94%] Built target tutorial_Morphology_2
Scanning dependencies of target tutorial_Sobel_Demo
[ 94%] Linking CXX executable ../../bin/cpp-tutorial-Geometric_Transforms_Demo
[ 95%] Building CXX object samples/cpp/CMakeFiles/tutorial_Sobel_Demo.dir/tutorial_code/ImgTrans/Sobel_Demo.cpp.o
[ 95%] Linking CXX executable ../../bin/cpp-tutorial-MatchTemplate_Demo
[ 95%] Built target tutorial_Geometric_Transforms_Demo
Scanning dependencies of target tutorial_HoughCircle_Demo
[ 95%] Built target tutorial_MatchTemplate_Demo
[ 95%] Building CXX object samples/cpp/CMakeFiles/tutorial_HoughCircle_Demo.dir/tutorial_code/ImgTrans/HoughCircle_Demo.cpp.o
Scanning dependencies of target example_matchmethod_orb_akaze_brisk
[ 95%] Building CXX object samples/cpp/CMakeFiles/example_matchmethod_orb_akaze_brisk.dir/matchmethod_orb_akaze_brisk.cpp.o
[ 96%] Linking CXX executable ../../bin/cpp-example-drawing
[ 96%] Built target example_drawing
Scanning dependencies of target example_videostab
[ 96%] Building CXX object samples/cpp/CMakeFiles/example_videostab.dir/videostab.cpp.o
[ 96%] Linking CXX executable ../../bin/cpp-tutorial-Sobel_Demo
[ 96%] Built target tutorial_Sobel_Demo
Scanning dependencies of target tutorial_video-input-psnr-ssim
[ 96%] Building CXX object samples/cpp/CMakeFiles/tutorial_video-input-psnr-ssim.dir/tutorial_code/videoio/video-input-psnr-ssim/video-input-psnr-ssim.cpp.o
[ 96%] Linking CXX executable ../../bin/cpp-tutorial-HoughCircle_Demo
[ 96%] Built target tutorial_HoughCircle_Demo
Scanning dependencies of target tutorial_Smoothing
[ 96%] Building CXX object samples/cpp/CMakeFiles/tutorial_Smoothing.dir/tutorial_code/ImgProc/Smoothing.cpp.o
[ 96%] Linking CXX executable ../../bin/cpp-tutorial-Smoothing
[ 96%] Built target tutorial_Smoothing
Scanning dependencies of target example_fitellipse
[ 96%] Building CXX object samples/cpp/CMakeFiles/example_fitellipse.dir/fitellipse.cpp.o
[ 96%] Linking CXX executable ../../bin/cpp-tutorial-video-input-psnr-ssim
[ 96%] Linking CXX executable ../../bin/cpp-example-matchmethod_orb_akaze_brisk
[ 96%] Built target example_matchmethod_orb_akaze_brisk
[ 96%] Built target tutorial_video-input-psnr-ssim
Scanning dependencies of target example_facedetect
Scanning dependencies of target example_shape_example
[ 96%] Building CXX object samples/cpp/CMakeFiles/example_facedetect.dir/facedetect.cpp.o
[ 96%] Building CXX object samples/cpp/CMakeFiles/example_shape_example.dir/shape_example.cpp.o
[ 96%] Linking CXX executable ../../bin/cpp-example-fitellipse
[ 96%] Built target example_fitellipse
Scanning dependencies of target example_videowriter_basic
[ 96%] Building CXX object samples/cpp/CMakeFiles/example_videowriter_basic.dir/videowriter_basic.cpp.o
[ 96%] Linking CXX executable ../../bin/cpp-example-videostab
[ 96%] Built target example_videostab
Scanning dependencies of target tutorial_video-write
[ 96%] Linking CXX executable ../../bin/cpp-example-shape_example
[ 96%] Linking CXX executable ../../bin/cpp-example-facedetect
[ 96%] Building CXX object samples/cpp/CMakeFiles/tutorial_video-write.dir/tutorial_code/videoio/video-write/video-write.cpp.o
[ 96%] Built target example_shape_example
Scanning dependencies of target tutorial_compareHist_Demo
[ 96%] Built target example_facedetect
Scanning dependencies of target tutorial_cornerHarris_Demo
[ 96%] Building CXX object samples/cpp/CMakeFiles/tutorial_compareHist_Demo.dir/tutorial_code/Histograms_Matching/compareHist_Demo.cpp.o
[ 96%] Building CXX object samples/cpp/CMakeFiles/tutorial_cornerHarris_Demo.dir/tutorial_code/TrackingMotion/cornerHarris_Demo.cpp.o
[ 97%] Linking CXX executable ../../bin/cpp-tutorial-video-write
[ 97%] Linking CXX executable ../../bin/cpp-example-videowriter_basic
[ 97%] Built target tutorial_video-write
Scanning dependencies of target example_stereo_match
[ 97%] Linking CXX executable ../../bin/cpp-tutorial-compareHist_Demo
[ 97%] Building CXX object samples/cpp/CMakeFiles/example_stereo_match.dir/stereo_match.cpp.o
[ 97%] Built target example_videowriter_basic
Scanning dependencies of target tutorial_LATCH_match
[ 97%] Linking CXX executable ../../bin/cpp-tutorial-cornerHarris_Demo
[ 97%] Built target tutorial_compareHist_Demo
[ 97%] Building CXX object samples/cpp/CMakeFiles/tutorial_LATCH_match.dir/tutorial_code/xfeatures2D/LATCH_match.cpp.o
Scanning dependencies of target tutorial_Threshold
[ 97%] Building CXX object samples/cpp/CMakeFiles/tutorial_Threshold.dir/tutorial_code/ImgProc/Threshold.cpp.o
[ 97%] Built target tutorial_cornerHarris_Demo
Scanning dependencies of target example_stitching
[ 97%] Linking CXX executable ../../bin/cpp-tutorial-LATCH_match
[ 97%] Building CXX object samples/cpp/CMakeFiles/example_stitching.dir/stitching.cpp.o
[ 97%] Built target tutorial_LATCH_match
Scanning dependencies of target tutorial_bg_sub
[ 97%] Building CXX object samples/cpp/CMakeFiles/tutorial_bg_sub.dir/tutorial_code/video/bg_sub.cpp.o
[ 97%] Linking CXX executable ../../bin/cpp-tutorial-Threshold
[ 98%] Linking CXX executable ../../bin/cpp-example-stereo_match
[ 98%] Built target tutorial_Threshold
Scanning dependencies of target tutorial_goodFeaturesToTrack_Demo
[ 98%] Building CXX object samples/cpp/CMakeFiles/tutorial_goodFeaturesToTrack_Demo.dir/tutorial_code/TrackingMotion/goodFeaturesToTrack_Demo.cpp.o
[ 98%] Built target example_stereo_match
Scanning dependencies of target tutorial_BasicLinearTransforms
[ 98%] Building CXX object samples/cpp/CMakeFiles/tutorial_BasicLinearTransforms.dir/tutorial_code/ImgProc/BasicLinearTransforms.cpp.o
[ 98%] Linking CXX executable ../../bin/cpp-tutorial-bg_sub
[ 98%] Built target tutorial_bg_sub
Scanning dependencies of target tutorial_HitMiss
[ 98%] Building CXX object samples/cpp/CMakeFiles/tutorial_HitMiss.dir/tutorial_code/ImgProc/HitMiss.cpp.o
[ 98%] Linking CXX executable ../../bin/cpp-example-stitching
[ 98%] Built target example_stitching
Scanning dependencies of target tutorial_CannyDetector_Demo
[ 98%] Building CXX object samples/cpp/CMakeFiles/tutorial_CannyDetector_Demo.dir/tutorial_code/ImgTrans/CannyDetector_Demo.cpp.o
[ 98%] Linking CXX executable ../../bin/cpp-tutorial-goodFeaturesToTrack_Demo
[ 98%] Linking CXX executable ../../bin/cpp-tutorial-BasicLinearTransforms
[ 98%] Built target tutorial_goodFeaturesToTrack_Demo
Scanning dependencies of target tutorial_Threshold_inRange
[ 98%] Built target tutorial_BasicLinearTransforms
Scanning dependencies of target example_connected_components
[ 98%] Building CXX object samples/cpp/CMakeFiles/tutorial_Threshold_inRange.dir/tutorial_code/ImgProc/Threshold_inRange.cpp.o
[ 98%] Building CXX object samples/cpp/CMakeFiles/example_connected_components.dir/connected_components.cpp.o
[ 98%] Linking CXX executable ../../bin/cpp-tutorial-CannyDetector_Demo
[ 98%] Built target tutorial_CannyDetector_Demo
Scanning dependencies of target tutorial_Pyramids
[ 98%] Linking CXX executable ../../bin/cpp-tutorial-HitMiss
[ 98%] Building CXX object samples/cpp/CMakeFiles/tutorial_Pyramids.dir/tutorial_code/ImgProc/Pyramids.cpp.o
[ 98%] Built target tutorial_HitMiss
Scanning dependencies of target example_starter_imagelist
[ 98%] Building CXX object samples/cpp/CMakeFiles/example_starter_imagelist.dir/starter_imagelist.cpp.o
[ 98%] Linking CXX executable ../../bin/cpp-tutorial-Threshold_inRange
[ 98%] Linking CXX executable ../../bin/cpp-example-connected_components
[ 98%] Built target example_connected_components
Scanning dependencies of target tutorial_npr_demo
[ 98%] Building CXX object samples/cpp/CMakeFiles/tutorial_npr_demo.dir/tutorial_code/photo/non_photorealistic_rendering/npr_demo.cpp.o
[ 98%] Built target tutorial_Threshold_inRange
Scanning dependencies of target tutorial_Morphology_3
[ 98%] Building CXX object samples/cpp/CMakeFiles/tutorial_Morphology_3.dir/tutorial_code/ImgProc/Morphology_3.cpp.o
[ 98%] Linking CXX executable ../../bin/cpp-tutorial-Pyramids
[ 98%] Built target tutorial_Pyramids
Scanning dependencies of target example_autofocus
[ 98%] Building CXX object samples/cpp/CMakeFiles/example_autofocus.dir/autofocus.cpp.o
[ 98%] Linking CXX executable ../../bin/cpp-example-starter_imagelist
[ 98%] Linking CXX executable ../../bin/cpp-tutorial-npr_demo
[ 98%] Built target example_starter_imagelist
Scanning dependencies of target example_ffilldemo
[ 99%] Building CXX object samples/cpp/CMakeFiles/example_ffilldemo.dir/ffilldemo.cpp.o
[ 99%] Built target tutorial_npr_demo
Scanning dependencies of target example_detect_blob
[ 99%] Building CXX object samples/cpp/CMakeFiles/example_detect_blob.dir/detect_blob.cpp.o
[ 99%] Linking CXX executable ../../bin/cpp-tutorial-Morphology_3
[ 99%] Linking CXX executable ../../bin/cpp-example-ffilldemo
[ 99%] Built target tutorial_Morphology_3
Scanning dependencies of target tutorial_gpu-basics-similarity
[ 99%] Built target example_ffilldemo
Scanning dependencies of target tutorial_changing_contrast_brightness_image
[ 99%] Building CXX object samples/cpp/CMakeFiles/tutorial_gpu-basics-similarity.dir/tutorial_code/gpu/gpu-basics-similarity/gpu-basics-similarity.cpp.o
[ 99%] Building CXX object samples/cpp/CMakeFiles/tutorial_changing_contrast_brightness_image.dir/tutorial_code/ImgProc/changing_contrast_brightness_image/changing_contrast_brightness_image.cpp.o
[ 99%] Linking CXX executable ../../bin/cpp-example-autofocus
[ 99%] Built target example_autofocus
Scanning dependencies of target example_opencv_version
[ 99%] Building CXX object samples/cpp/CMakeFiles/example_opencv_version.dir/opencv_version.cpp.o
[ 99%] Linking CXX executable ../../bin/cpp-tutorial-changing_contrast_brightness_image
[ 99%] Built target tutorial_changing_contrast_brightness_image
Scanning dependencies of target tutorial_pointPolygonTest_demo
[ 99%] Building CXX object samples/cpp/CMakeFiles/tutorial_pointPolygonTest_demo.dir/tutorial_code/ShapeDescriptors/pointPolygonTest_demo.cpp.o
[ 99%] Linking CXX executable ../../bin/cpp-example-opencv_version
[ 99%] Built target example_opencv_version
Scanning dependencies of target example_fback
[ 99%] Building CXX object samples/cpp/CMakeFiles/example_fback.dir/fback.cpp.o
[ 99%] Linking CXX executable ../../bin/cpp-example-detect_blob
[ 99%] Built target example_detect_blob
Scanning dependencies of target example_convexhull
[ 99%] Building CXX object samples/cpp/CMakeFiles/example_convexhull.dir/convexhull.cpp.o
[ 99%] Linking CXX executable ../../bin/cpp-tutorial-pointPolygonTest_demo
[ 99%] Linking CXX executable ../../bin/cpp-tutorial-gpu-basics-similarity
[ 99%] Built target tutorial_gpu-basics-similarity
Scanning dependencies of target example_edge
[ 99%] Built target tutorial_pointPolygonTest_demo
Scanning dependencies of target example_3calibration
[ 99%] Building CXX object samples/cpp/CMakeFiles/example_edge.dir/edge.cpp.o
[ 99%] Building CXX object samples/cpp/CMakeFiles/example_3calibration.dir/3calibration.cpp.o
[ 99%] Linking CXX executable ../../bin/cpp-example-fback
[ 99%] Built target example_fback
[ 99%] Linking CXX executable ../../bin/cpp-example-convexhull
Scanning dependencies of target example_segment_objects
[ 99%] Building CXX object samples/cpp/CMakeFiles/example_segment_objects.dir/segment_objects.cpp.o
[ 99%] Built target example_convexhull
Scanning dependencies of target tutorial_mat_the_basic_image_container
[ 99%] Building CXX object samples/cpp/CMakeFiles/tutorial_mat_the_basic_image_container.dir/tutorial_code/core/mat_the_basic_image_container/mat_the_basic_image_container.cpp.o
[ 99%] Linking CXX executable ../../bin/cpp-example-edge
[ 99%] Built target example_edge
Scanning dependencies of target example_lkdemo
[100%] Building CXX object samples/cpp/CMakeFiles/example_lkdemo.dir/lkdemo.cpp.o
[100%] Linking CXX executable ../../bin/cpp-example-segment_objects
[100%] Linking CXX executable ../../bin/cpp-tutorial-mat_the_basic_image_container
[100%] Built target example_segment_objects
[100%] Built target tutorial_mat_the_basic_image_container
[100%] Linking CXX executable ../../bin/cpp-example-lkdemo
[100%] Built target example_lkdemo
[100%] Linking CXX executable ../../bin/cpp-example-3calibration
[100%] Built target example_3calibration
nvidia@gpu:~/opencv/build$ sudo make install
[sudo] password for nvidia: 
-- Detected version of GNU GCC: 54 (504)
-- Looking for ccache - not found
-- Found ZLIB: /usr/lib/aarch64-linux-gnu/libz.so (found suitable version "1.2.8", minimum required is "1.2.3") 
-- Found ZLIB: /usr/lib/aarch64-linux-gnu/libz.so (found version "1.2.8") 
-- Checking for module 'gtk+-3.0'
--   No package 'gtk+-3.0' found
-- Looking for linux/videodev.h
-- Looking for linux/videodev.h - not found
-- Looking for linux/videodev2.h
-- Looking for linux/videodev2.h - found
-- Looking for sys/videoio.h
-- Looking for sys/videoio.h - not found
-- Checking for module 'libavresample'
--   No package 'libavresample' found
-- Checking for module 'libgphoto2'
--   No package 'libgphoto2' found
-- Found TBB: /usr/lib/aarch64-linux-gnu/libtbb.so
-- CUDA detected: 8.0
-- CUDA NVCC target flags: -gencode;arch=compute_62,code=sm_62;-D_FORCE_INLINES
-- Could not find OpenBLAS lib. Turning OpenBLAS_FOUND off
-- Could NOT find Atlas (missing:  Atlas_CLAPACK_INCLUDE_DIR) 
-- A library with BLAS API found.
-- A library with LAPACK API found.
-- Could NOT find Doxygen (missing:  DOXYGEN_EXECUTABLE) 
-- Could NOT find JNI (missing:  JAVA_AWT_LIBRARY JAVA_JVM_LIBRARY JAVA_INCLUDE_PATH JAVA_INCLUDE_PATH2 JAVA_AWT_INCLUDE_PATH) 
-- Could NOT find Matlab (missing:  MATLAB_MEX_SCRIPT MATLAB_INCLUDE_DIRS MATLAB_ROOT_DIR MATLAB_LIBRARIES MATLAB_LIBRARY_DIRS MATLAB_MEXEXT MATLAB_ARCH MATLAB_BIN) 
-- Excluding from source files list: /home/nvidia/opencv/modules/core/src/convert.sse4_1.cpp
-- Excluding from source files list: /home/nvidia/opencv/modules/core/src/convert.avx2.cpp
-- Excluding from source files list: /home/nvidia/opencv/build/modules/core/mathfuncs_core.sse2.cpp
-- Excluding from source files list: /home/nvidia/opencv/build/modules/core/mathfuncs_core.avx.cpp
-- Excluding from source files list: /home/nvidia/opencv/build/modules/core/mathfuncs_core.avx2.cpp
-- Excluding from source files list: /home/nvidia/opencv/build/modules/core/stat.sse4_2.cpp
-- Excluding from source files list: /home/nvidia/opencv/build/modules/core/stat.avx2.cpp
-- Excluding from source files list: /home/nvidia/opencv/modules/imgproc/src/filter.avx2.cpp
-- Excluding from source files list: /home/nvidia/opencv/modules/imgproc/src/corner.avx.cpp
-- Excluding from source files list: /home/nvidia/opencv/modules/imgproc/src/imgwarp.avx2.cpp
-- Excluding from source files list: /home/nvidia/opencv/modules/imgproc/src/imgwarp.sse4_1.cpp
-- Excluding from source files list: /home/nvidia/opencv/modules/imgproc/src/undistort.avx2.cpp
-- Excluding from source files list: /home/nvidia/opencv/build/modules/imgproc/accum.sse2.cpp
-- Excluding from source files list: /home/nvidia/opencv/build/modules/imgproc/accum.avx.cpp
-- Excluding from source files list: /home/nvidia/opencv/modules/objdetect/src/haar.avx.cpp
-- Excluding from source files list: /home/nvidia/opencv/build/modules/dnn/layers/layers_common.avx.cpp
-- Excluding from source files list: /home/nvidia/opencv/build/modules/dnn/layers/layers_common.avx2.cpp
-- Torch importer has been enabled. To run the tests you have to install Torch ('th' executable should be available) and generate testdata using opencv_extra/testdata/dnn/generate_torch_models.py script.
-- 
-- General configuration for OpenCV 3.3.0 =====================================
--   Version control:               3.3.0
-- 
--   Platform:
--     Timestamp:                   2017-11-26T11:05:49Z
--     Host:                        Linux 4.4.38-tegra aarch64
--     CMake:                       3.5.1
--     CMake generator:             Unix Makefiles
--     CMake build tool:            /usr/bin/make
--     Configuration:               Release
-- 
--   CPU/HW features:
--     Baseline:                    NEON FP16
--       required:                  NEON
--       disabled:                  VFPV3
-- 
--   C/C++:
--     Built as dynamic libs?:      YES
--     C++ Compiler:                /usr/bin/c++  (ver 5.4.0)
--     C++ flags (Release):         -fsigned-char -W -Wall -Werror=return-type -Werror=non-virtual-dtor -Werror=address -Werror=sequence-point -Wformat -Werror=format-security -Wmissing-declarations -Wundef -Winit-self -Wpointer-arith -Wshadow -Wsign-promo -Wuninitialized -Winit-self -Wno-narrowing -Wno-delete-non-virtual-dtor -Wno-comment -fdiagnostics-show-option -pthread -fomit-frame-pointer -ffunction-sections    -fvisibility=hidden -fvisibility-inlines-hidden -O3 -DNDEBUG  -DNDEBUG
--     C++ flags (Debug):           -fsigned-char -W -Wall -Werror=return-type -Werror=non-virtual-dtor -Werror=address -Werror=sequence-point -Wformat -Werror=format-security -Wmissing-declarations -Wundef -Winit-self -Wpointer-arith -Wshadow -Wsign-promo -Wuninitialized -Winit-self -Wno-narrowing -Wno-delete-non-virtual-dtor -Wno-comment -fdiagnostics-show-option -pthread -fomit-frame-pointer -ffunction-sections    -fvisibility=hidden -fvisibility-inlines-hidden -g  -O0 -DDEBUG -D_DEBUG
--     C Compiler:                  /usr/bin/cc
--     C flags (Release):           -fsigned-char -W -Wall -Werror=return-type -Werror=non-virtual-dtor -Werror=address -Werror=sequence-point -Wformat -Werror=format-security -Wmissing-declarations -Wmissing-prototypes -Wstrict-prototypes -Wundef -Winit-self -Wpointer-arith -Wshadow -Wuninitialized -Winit-self -Wno-narrowing -Wno-comment -fdiagnostics-show-option -pthread -fomit-frame-pointer -ffunction-sections    -fvisibility=hidden -O3 -DNDEBUG  -DNDEBUG
--     C flags (Debug):             -fsigned-char -W -Wall -Werror=return-type -Werror=non-virtual-dtor -Werror=address -Werror=sequence-point -Wformat -Werror=format-security -Wmissing-declarations -Wmissing-prototypes -Wstrict-prototypes -Wundef -Winit-self -Wpointer-arith -Wshadow -Wuninitialized -Winit-self -Wno-narrowing -Wno-comment -fdiagnostics-show-option -pthread -fomit-frame-pointer -ffunction-sections    -fvisibility=hidden -g  -O0 -DDEBUG -D_DEBUG
--     Linker flags (Release):
--     Linker flags (Debug):
--     ccache:                      NO
--     Precompiled headers:         NO
--     Extra dependencies:          gtk-x11-2.0 gdk-x11-2.0 pangocairo-1.0 atk-1.0 cairo gdk_pixbuf-2.0 gio-2.0 pangoft2-1.0 pango-1.0 fontconfig freetype gthread-2.0 /usr/lib/aarch64-linux-gnu/libwebp.so /usr/lib/aarch64-linux-gnu/libpng.so /usr/lib/aarch64-linux-gnu/libz.so /usr/lib/aarch64-linux-gnu/libtiff.so /usr/lib/aarch64-linux-gnu/libjasper.so /usr/lib/aarch64-linux-gnu/libjpeg.so gstbase-1.0 gstreamer-1.0 gobject-2.0 glib-2.0 gstvideo-1.0 gstapp-1.0 gstriff-1.0 gstpbutils-1.0 avcodec-ffmpeg avformat-ffmpeg avutil-ffmpeg swscale-ffmpeg dl m pthread rt /usr/lib/aarch64-linux-gnu/libtbb.so cudart nppc nppi npps cufft -L/usr/local/cuda-8.0/lib64
--     3rdparty dependencies:
-- 
--   OpenCV modules:
--     To be built:                 cudev core cudaarithm flann imgproc ml objdetect video cudabgsegm cudafilters cudaimgproc cudawarping dnn imgcodecs photo shape videoio cudacodec highgui ts features2d calib3d cudafeatures2d cudalegacy cudaobjdetect cudaoptflow cudastereo stitching superres videostab python2 python3
--     Disabled:                    world
--     Disabled by dependency:      -
--     Unavailable:                 java viz
-- 
--   GUI: 
--     QT:                          NO
--     GTK+ 2.x:                    YES (ver 2.24.30)
--     GThread :                    YES (ver 2.48.1)
--     GtkGlExt:                    NO
--     OpenGL support:              NO
--     VTK support:                 NO
-- 
--   Media I/O: 
--     ZLib:                        /usr/lib/aarch64-linux-gnu/libz.so (ver 1.2.8)
--     JPEG:                        /usr/lib/aarch64-linux-gnu/libjpeg.so (ver )
--     WEBP:                        /usr/lib/aarch64-linux-gnu/libwebp.so (ver encoder: 0x0202)
--     PNG:                         /usr/lib/aarch64-linux-gnu/libpng.so (ver 1.2.54)
--     TIFF:                        /usr/lib/aarch64-linux-gnu/libtiff.so (ver 42 - 4.0.6)
--     JPEG 2000:                   /usr/lib/aarch64-linux-gnu/libjasper.so (ver 1.900.1)
--     OpenEXR:                     NO
--     GDAL:                        NO
--     GDCM:                        NO
-- 
--   Video I/O:
--     DC1394 1.x:                  NO
--     DC1394 2.x:                  NO
--     FFMPEG:                      YES
--       avcodec:                   YES (ver 56.60.100)
--       avformat:                  YES (ver 56.40.101)
--       avutil:                    YES (ver 54.31.100)
--       swscale:                   YES (ver 3.1.101)
--       avresample:                NO
--     GStreamer:                   
--       base:                      YES (ver 1.8.3)
--       video:                     YES (ver 1.8.3)
--       app:                       YES (ver 1.8.3)
--       riff:                      YES (ver 1.8.3)
--       pbutils:                   YES (ver 1.8.3)
--     OpenNI:                      NO
--     OpenNI PrimeSensor Modules:  NO
--     OpenNI2:                     NO
--     PvAPI:                       NO
--     GigEVisionSDK:               NO
--     Aravis SDK:                  NO
--     UniCap:                      NO
--     UniCap ucil:                 NO
--     V4L/V4L2:                    NO/YES
--     XIMEA:                       NO
--     Xine:                        NO
--     Intel Media SDK:             NO
--     gPhoto2:                     NO
-- 
--   Parallel framework:            TBB (ver 4.4 interface 9002)
-- 
--   Trace:                         YES ()
-- 
--   Other third-party libraries:
--     Use Intel IPP:               NO
--     Use Intel IPP IW:            NO
--     Use VA:                      NO
--     Use Intel VA-API/OpenCL:     NO
--     Use Lapack:                  NO
--     Use Eigen:                   YES (ver 3.2.92)
--     Use Cuda:                    YES (ver 8.0)
--     Use OpenCL:                  NO
--     Use OpenVX:                  NO
--     Use custom HAL:              YES (carotene (ver 0.0.1))
-- 
--   NVIDIA CUDA
--     Use CUFFT:                   YES
--     Use CUBLAS:                  NO
--     USE NVCUVID:                 NO
--     NVIDIA GPU arch:             62
--     NVIDIA PTX archs:
--     Use fast math:               NO
-- 
--   Python 2:
--     Interpreter:                 /usr/bin/python2.7 (ver 2.7.12)
--     Libraries:                   /usr/lib/aarch64-linux-gnu/libpython2.7.so (ver 2.7.12)
--     numpy:                       /usr/lib/python2.7/dist-packages/numpy/core/include (ver 1.11.0)
--     packages path:               lib/python2.7/dist-packages
-- 
--   Python 3:
--     Interpreter:                 /usr/bin/python3 (ver 3.5.2)
--     Libraries:                   /usr/lib/aarch64-linux-gnu/libpython3.5m.so (ver 3.5.2)
--     numpy:                       /usr/lib/python3/dist-packages/numpy/core/include (ver 1.11.0)
--     packages path:               lib/python3.5/dist-packages
-- 
--   Python (for build):            /usr/bin/python2.7
-- 
--   Java:
--     ant:                         NO
--     JNI:                         NO
--     Java wrappers:               NO
--     Java tests:                  NO
-- 
--   Matlab:                        Matlab not found or implicitly disabled
-- 
--   Documentation:
--     Doxygen:                     NO
-- 
--   Tests and samples:
--     Tests:                       YES
--     Performance tests:           YES
--     C/C++ Examples:              YES
-- 
--   Install path:                  /usr
-- 
--   cvconfig.h is in:              /home/nvidia/opencv/build
-- -----------------------------------------------------------------
-- 
-- Configuring done
-- Generating done
-- Build files have been written to: /home/nvidia/opencv/build
[  3%] Built target carotene_objs
[  4%] Built target tegra_hal
[  9%] Built target libprotobuf
[  9%] Built target opencv_cudev
Scanning dependencies of target opencv_core
[  9%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/system.cpp.o
[  9%] Linking CXX shared library ../../lib/libopencv_core.so
[ 12%] Built target opencv_core
[ 12%] Linking CXX shared library ../../lib/libopencv_imgproc.so
[ 16%] Built target opencv_imgproc
[ 16%] Linking CXX shared library ../../lib/libopencv_imgcodecs.so
[ 17%] Built target opencv_imgcodecs
[ 18%] Linking CXX shared library ../../lib/libopencv_videoio.so
[ 18%] Built target opencv_videoio
[ 18%] Linking CXX shared library ../../lib/libopencv_highgui.so
[ 18%] Built target opencv_highgui
[ 19%] Built target opencv_ts
[ 19%] Linking CXX executable ../../../bin/opencv_test_cudev
[ 20%] Built target opencv_test_cudev
[ 20%] Linking CXX executable ../../bin/opencv_test_core
[ 22%] Built target opencv_test_core
[ 22%] Linking CXX executable ../../bin/opencv_perf_core
[ 24%] Built target opencv_perf_core
[ 24%] Linking CXX shared library ../../lib/libopencv_cudaarithm.so
[ 27%] Built target opencv_cudaarithm
[ 28%] Linking CXX executable ../../bin/opencv_perf_cudaarithm
[ 28%] Built target opencv_perf_cudaarithm
[ 28%] Linking CXX executable ../../bin/opencv_test_cudaarithm
[ 29%] Built target opencv_test_cudaarithm
[ 30%] Linking CXX shared library ../../lib/libopencv_flann.so
[ 30%] Built target opencv_flann
[ 30%] Linking CXX executable ../../bin/opencv_test_flann
[ 30%] Built target opencv_test_flann
[ 30%] Linking CXX executable ../../bin/opencv_perf_imgproc
[ 32%] Built target opencv_perf_imgproc
[ 32%] Linking CXX executable ../../bin/opencv_test_imgproc
[ 35%] Built target opencv_test_imgproc
[ 35%] Linking CXX shared library ../../lib/libopencv_ml.so
[ 36%] Built target opencv_ml
[ 37%] Linking CXX executable ../../bin/opencv_test_ml
[ 37%] Built target opencv_test_ml
[ 37%] Linking CXX shared library ../../lib/libopencv_objdetect.so
[ 38%] Built target opencv_objdetect
[ 38%] Linking CXX executable ../../bin/opencv_perf_objdetect
[ 39%] Built target opencv_perf_objdetect
[ 39%] Linking CXX executable ../../bin/opencv_test_objdetect
[ 39%] Built target opencv_test_objdetect
[ 39%] Linking CXX shared library ../../lib/libopencv_video.so
[ 40%] Built target opencv_video
[ 40%] Linking CXX executable ../../bin/opencv_test_video
[ 41%] Built target opencv_test_video
[ 41%] Linking CXX executable ../../bin/opencv_perf_video
[ 41%] Built target opencv_perf_video
[ 41%] Linking CXX shared library ../../lib/libopencv_cudabgsegm.so
[ 41%] Built target opencv_cudabgsegm
[ 41%] Linking CXX executable ../../bin/opencv_perf_cudabgsegm
[ 41%] Built target opencv_perf_cudabgsegm
[ 41%] Linking CXX executable ../../bin/opencv_test_cudabgsegm
[ 41%] Built target opencv_test_cudabgsegm
[ 41%] Linking CXX shared library ../../lib/libopencv_cudafilters.so
[ 43%] Built target opencv_cudafilters
[ 43%] Linking CXX executable ../../bin/opencv_perf_cudafilters
[ 43%] Built target opencv_perf_cudafilters
[ 43%] Linking CXX executable ../../bin/opencv_test_cudafilters
[ 43%] Built target opencv_test_cudafilters
[ 43%] Linking CXX shared library ../../lib/libopencv_cudaimgproc.so
[ 45%] Built target opencv_cudaimgproc
[ 45%] Linking CXX executable ../../bin/opencv_test_cudaimgproc
[ 46%] Built target opencv_test_cudaimgproc
[ 46%] Linking CXX executable ../../bin/opencv_perf_cudaimgproc
[ 47%] Built target opencv_perf_cudaimgproc
[ 47%] Linking CXX shared library ../../lib/libopencv_cudawarping.so
[ 47%] Built target opencv_cudawarping
[ 47%] Linking CXX executable ../../bin/opencv_perf_cudawarping
[ 47%] Built target opencv_perf_cudawarping
[ 47%] Linking CXX executable ../../bin/opencv_test_cudawarping
[ 47%] Built target opencv_test_cudawarping
[ 47%] Linking CXX shared library ../../lib/libopencv_dnn.so
[ 51%] Built target opencv_dnn
[ 51%] Linking CXX executable ../../bin/opencv_perf_dnn
[ 51%] Built target opencv_perf_dnn
[ 51%] Linking CXX executable ../../bin/opencv_test_dnn
[ 52%] Built target opencv_test_dnn
[ 52%] Linking CXX executable ../../bin/opencv_test_imgcodecs
[ 53%] Built target opencv_test_imgcodecs
[ 53%] Linking CXX executable ../../bin/opencv_perf_imgcodecs
[ 53%] Built target opencv_perf_imgcodecs
[ 53%] Linking CXX shared library ../../lib/libopencv_photo.so
[ 55%] Built target opencv_photo
[ 55%] Linking CXX executable ../../bin/opencv_perf_photo
[ 55%] Built target opencv_perf_photo
[ 55%] Linking CXX executable ../../bin/opencv_test_photo
[ 55%] Built target opencv_test_photo
[ 55%] Linking CXX shared library ../../lib/libopencv_shape.so
[ 55%] Built target opencv_shape
[ 55%] Linking CXX executable ../../bin/opencv_test_shape
[ 56%] Built target opencv_test_shape
[ 56%] Linking CXX executable ../../bin/opencv_perf_videoio
[ 56%] Built target opencv_perf_videoio
[ 56%] Linking CXX executable ../../bin/opencv_test_videoio
[ 56%] Built target opencv_test_videoio
[ 56%] Linking CXX shared library ../../lib/libopencv_cudacodec.so
[ 57%] Built target opencv_cudacodec
[ 57%] Linking CXX executable ../../bin/opencv_test_cudacodec
[ 57%] Built target opencv_test_cudacodec
[ 57%] Linking CXX executable ../../bin/opencv_perf_cudacodec
[ 57%] Built target opencv_perf_cudacodec
[ 57%] Linking CXX executable ../../bin/opencv_test_highgui
[ 57%] Built target opencv_test_highgui
[ 57%] Linking CXX shared library ../../lib/libopencv_features2d.so
[ 58%] Built target opencv_features2d
[ 58%] Linking CXX executable ../../bin/opencv_perf_features2d
[ 59%] Built target opencv_perf_features2d
[ 59%] Linking CXX executable ../../bin/opencv_test_features2d
[ 60%] Built target opencv_test_features2d
[ 60%] Linking CXX shared library ../../lib/libopencv_calib3d.so
[ 62%] Built target opencv_calib3d
[ 62%] Linking CXX executable ../../bin/opencv_perf_calib3d
[ 62%] Built target opencv_perf_calib3d
[ 62%] Linking CXX executable ../../bin/opencv_test_calib3d
[ 64%] Built target opencv_test_calib3d
[ 65%] Linking CXX shared library ../../lib/libopencv_cudafeatures2d.so
[ 65%] Built target opencv_cudafeatures2d
[ 65%] Linking CXX executable ../../bin/opencv_test_cudafeatures2d
[ 65%] Built target opencv_test_cudafeatures2d
[ 65%] Linking CXX executable ../../bin/opencv_perf_cudafeatures2d
[ 65%] Built target opencv_perf_cudafeatures2d
[ 65%] Linking CXX shared library ../../lib/libopencv_cudalegacy.so
[ 66%] Built target opencv_cudalegacy
[ 66%] Linking CXX executable ../../bin/opencv_test_cudalegacy
[ 67%] Built target opencv_test_cudalegacy
[ 67%] Linking CXX executable ../../bin/opencv_perf_cudalegacy
[ 67%] Built target opencv_perf_cudalegacy
[ 68%] Linking CXX shared library ../../lib/libopencv_cudaobjdetect.so
[ 68%] Built target opencv_cudaobjdetect
[ 68%] Linking CXX executable ../../bin/opencv_perf_cudaobjdetect
[ 69%] Built target opencv_perf_cudaobjdetect
[ 69%] Linking CXX executable ../../bin/opencv_test_cudaobjdetect
[ 69%] Built target opencv_test_cudaobjdetect
[ 69%] Linking CXX shared library ../../lib/libopencv_cudaoptflow.so
[ 69%] Built target opencv_cudaoptflow
[ 69%] Linking CXX executable ../../bin/opencv_perf_cudaoptflow
[ 69%] Built target opencv_perf_cudaoptflow
[ 69%] Linking CXX executable ../../bin/opencv_test_cudaoptflow
[ 70%] Built target opencv_test_cudaoptflow
[ 70%] Linking CXX shared library ../../lib/libopencv_cudastereo.so
[ 71%] Built target opencv_cudastereo
[ 71%] Linking CXX executable ../../bin/opencv_perf_cudastereo
[ 71%] Built target opencv_perf_cudastereo
[ 71%] Linking CXX executable ../../bin/opencv_test_cudastereo
[ 71%] Built target opencv_test_cudastereo
[ 71%] Linking CXX shared library ../../lib/libopencv_stitching.so
[ 72%] Built target opencv_stitching
[ 72%] Linking CXX executable ../../bin/opencv_perf_stitching
[ 72%] Built target opencv_perf_stitching
[ 72%] Linking CXX executable ../../bin/opencv_test_stitching
[ 72%] Built target opencv_test_stitching
[ 72%] Linking CXX shared library ../../lib/libopencv_superres.so
[ 73%] Built target opencv_superres
[ 73%] Linking CXX executable ../../bin/opencv_perf_superres
[ 74%] Built target opencv_perf_superres
[ 74%] Linking CXX executable ../../bin/opencv_test_superres
[ 74%] Built target opencv_test_superres
[ 74%] Linking CXX shared library ../../lib/libopencv_videostab.so
[ 74%] Built target opencv_videostab
[ 74%] Linking CXX executable ../../bin/opencv_test_videostab
[ 75%] Built target opencv_test_videostab
[ 75%] Generating pyopencv_generated_include.h, pyopencv_generated_funcs.h, pyopencv_generated_types.h, pyopencv_generated_type_reg.h, pyopencv_generated_ns_reg.h
Scanning dependencies of target opencv_python2
[ 75%] Building CXX object modules/python2/CMakeFiles/opencv_python2.dir/__/src2/cv2.cpp.o
[ 75%] Linking CXX shared module ../../lib/cv2.so
[ 75%] Built target opencv_python2
[ 75%] Generating pyopencv_generated_include.h, pyopencv_generated_funcs.h, pyopencv_generated_types.h, pyopencv_generated_type_reg.h, pyopencv_generated_ns_reg.h
Scanning dependencies of target opencv_python3
[ 75%] Building CXX object modules/python3/CMakeFiles/opencv_python3.dir/__/src2/cv2.cpp.o
[ 75%] Linking CXX shared module ../../lib/python3/cv2.cpython-35m-aarch64-linux-gnu.so
[ 75%] Built target opencv_python3
[ 75%] Linking CXX executable ../../bin/opencv_traincascade
[ 75%] Built target opencv_traincascade
[ 75%] Linking CXX executable ../../bin/opencv_createsamples
[ 75%] Built target opencv_createsamples
[ 75%] Linking CXX executable ../../bin/opencv_annotation
[ 75%] Built target opencv_annotation
[ 75%] Linking CXX executable ../../bin/opencv_visualisation
[ 75%] Built target opencv_visualisation
[ 75%] Linking CXX executable ../../bin/opencv_interactive-calibration
[ 75%] Built target opencv_interactive-calibration
[ 75%] Linking CXX executable ../../bin/opencv_version
[ 75%] Built target opencv_version
[ 75%] Linking CXX executable ../../bin/cpp-tutorial-pnp_detection
[ 75%] Built target cpp-tutorial-pnp_detection
[ 75%] Linking CXX executable ../../bin/cpp-example-minarea
[ 75%] Built target example_minarea
[ 75%] Linking CXX executable ../../bin/cpp-example-houghlines
[ 75%] Built target example_houghlines
[ 75%] Linking CXX executable ../../bin/cpp-example-facial_features
[ 75%] Built target example_facial_features
[ 75%] Linking CXX executable ../../bin/cpp-example-mask_tmpl
[ 75%] Built target example_mask_tmpl
[ 75%] Linking CXX executable ../../bin/cpp-example-npr_demo
[ 75%] Built target example_npr_demo
[ 75%] Linking CXX executable ../../bin/cpp-example-letter_recog
[ 75%] Built target example_letter_recog
[ 75%] Linking CXX executable ../../bin/cpp-example-tree_engine
[ 75%] Built target example_tree_engine
[ 75%] Linking CXX executable ../../bin/cpp-example-bgfg_segm
[ 75%] Built target example_bgfg_segm
[ 75%] Linking CXX executable ../../bin/cpp-example-logistic_regression
[ 75%] Built target example_logistic_regression
[ 75%] Linking CXX executable ../../bin/cpp-example-kmeans
[ 75%] Built target example_kmeans
[ 75%] Linking CXX executable ../../bin/cpp-tutorial-pnp_registration
[ 76%] Built target cpp-tutorial-pnp_registration
[ 76%] Linking CXX executable ../../bin/cpp-example-lsd_lines
[ 76%] Built target example_lsd_lines
[ 76%] Linking CXX executable ../../bin/cpp-example-dft
[ 76%] Built target example_dft
[ 76%] Linking CXX executable ../../bin/cpp-example-calibration
[ 77%] Built target example_calibration
[ 77%] Linking CXX executable ../../bin/cpp-example-tvl1_optical_flow
[ 77%] Built target example_tvl1_optical_flow
[ 77%] Linking CXX executable ../../bin/cpp-example-watershed
[ 77%] Built target example_watershed
[ 77%] Linking CXX executable ../../bin/cpp-example-stereo_calib
[ 77%] Built target example_stereo_calib
[ 77%] Linking CXX executable ../../bin/cpp-example-stitching_detailed
[ 77%] Built target example_stitching_detailed
[ 77%] Linking CXX executable ../../bin/cpp-example-intelperc_capture
[ 77%] Built target example_intelperc_capture
[ 77%] Linking CXX executable ../../bin/cpp-example-videocapture_basic
[ 77%] Built target example_videocapture_basic
[ 77%] Linking CXX executable ../../bin/cpp-example-cloning_demo
[ 77%] Built target example_cloning_demo
[ 77%] Linking CXX executable ../../bin/cpp-example-imagelist_creator
[ 77%] Built target example_imagelist_creator
[ 77%] Linking CXX executable ../../bin/cpp-example-pca
[ 77%] Built target example_pca
[ 77%] Linking CXX executable ../../bin/cpp-example-filestorage
[ 77%] Built target example_filestorage
[ 77%] Linking CXX executable ../../bin/cpp-example-demhist
[ 77%] Built target example_demhist
[ 77%] Linking CXX executable ../../bin/cpp-example-points_classifier
[ 77%] Built target example_points_classifier
[ 77%] Linking CXX executable ../../bin/cpp-example-train_HOG
[ 77%] Built target example_train_HOG
[ 77%] Linking CXX executable ../../bin/cpp-example-camshiftdemo
[ 77%] Built target example_camshiftdemo
[ 77%] Linking CXX executable ../../bin/cpp-example-morphology2
[ 77%] Built target example_morphology2
[ 77%] Linking CXX executable ../../bin/cpp-tutorial-AKAZE_match
[ 77%] Built target tutorial_AKAZE_match
[ 77%] Linking CXX executable ../../bin/cpp-tutorial-non_linear_svms
[ 77%] Built target tutorial_non_linear_svms
[ 77%] Linking CXX executable ../../bin/cpp-tutorial-mat_mask_operations
[ 77%] Built target tutorial_mat_mask_operations
[ 77%] Linking CXX executable ../../bin/cpp-tutorial-Drawing_2
[ 78%] Built target tutorial_Drawing_2
[ 78%] Linking CXX executable ../../bin/cpp-example-falsecolor
[ 78%] Built target example_falsecolor
[ 79%] Linking CXX executable ../../bin/cpp-example-cout_mat
[ 79%] Built target example_cout_mat
[ 79%] Linking CXX executable ../../bin/cpp-tutorial-AddingImages
[ 79%] Built target tutorial_AddingImages
[ 79%] Linking CXX executable ../../bin/cpp-example-train_svmsgd
[ 79%] Built target example_train_svmsgd
[ 79%] Linking CXX executable ../../bin/cpp-tutorial-introduction_to_svm
[ 79%] Built target tutorial_introduction_to_svm
[ 79%] Linking CXX executable ../../bin/cpp-example-kalman
[ 79%] Built target example_kalman
[ 79%] Linking CXX executable ../../bin/cpp-example-image_sequence
[ 80%] Built target example_image_sequence
[ 80%] Linking CXX executable ../../bin/cpp-tutorial-display_image
[ 80%] Built target tutorial_display_image
[ 80%] Linking CXX executable ../../bin/cpp-example-example
[ 80%] Built target example_example
[ 80%] Linking CXX executable ../../bin/cpp-tutorial-Drawing_1
[ 80%] Built target tutorial_Drawing_1
[ 81%] Linking CXX executable ../../bin/cpp-example-distrans
[ 81%] Built target example_distrans
[ 81%] Linking CXX executable ../../bin/cpp-tutorial-filter2D_demo
[ 81%] Built target tutorial_filter2D_demo
[ 81%] Linking CXX executable ../../bin/cpp-tutorial-hull_demo
[ 82%] Built target tutorial_hull_demo
[ 82%] Linking CXX executable ../../bin/cpp-tutorial-discrete_fourier_transform
[ 82%] Built target tutorial_discrete_fourier_transform
[ 82%] Linking CXX executable ../../bin/cpp-tutorial-file_input_output
[ 82%] Built target tutorial_file_input_output
[ 82%] Linking CXX executable ../../bin/cpp-example-delaunay2
[ 82%] Built target example_delaunay2
[ 83%] Linking CXX executable ../../bin/cpp-example-neural_network
[ 83%] Built target example_neural_network
[ 83%] Linking CXX executable ../../bin/cpp-example-grabcut
[ 83%] Built target example_grabcut
[ 83%] Linking CXX executable ../../bin/cpp-tutorial-how_to_use_OpenCV_parallel_for_
[ 83%] Built target tutorial_how_to_use_OpenCV_parallel_for_
[ 83%] Linking CXX executable ../../bin/cpp-tutorial-findContours_demo
[ 83%] Built target tutorial_findContours_demo
[ 83%] Linking CXX executable ../../bin/cpp-example-peopledetect
[ 83%] Built target example_peopledetect
[ 83%] Linking CXX executable ../../bin/cpp-example-contours2
[ 83%] Built target example_contours2
[ 83%] Linking CXX executable ../../bin/cpp-example-dbt_face_detection
[ 83%] Built target example_dbt_face_detection
[ 83%] Linking CXX executable ../../bin/cpp-tutorial-moments_demo
[ 84%] Built target tutorial_moments_demo
[ 84%] Linking CXX executable ../../bin/cpp-example-em
[ 84%] Built target example_em
[ 84%] Linking CXX executable ../../bin/cpp-example-filestorage_base64
[ 84%] Built target example_filestorage_base64
[ 84%] Linking CXX executable ../../bin/cpp-tutorial-calcHist_Demo
[ 84%] Built target tutorial_calcHist_Demo
[ 84%] Linking CXX executable ../../bin/cpp-tutorial-copyMakeBorder_demo
[ 84%] Built target tutorial_copyMakeBorder_demo
[ 84%] Linking CXX executable ../../bin/cpp-tutorial-calcBackProject_Demo2
[ 84%] Built target tutorial_calcBackProject_Demo2
[ 84%] Linking CXX executable ../../bin/cpp-tutorial-documentation
[ 84%] Built target tutorial_documentation
[ 84%] Linking CXX executable ../../bin/cpp-example-phase_corr
[ 84%] Built target example_phase_corr
[ 84%] Linking CXX executable ../../bin/cpp-example-inpaint
[ 84%] Built target example_inpaint
[ 84%] Linking CXX executable ../../bin/cpp-tutorial-BasicLinearTransformsTrackbar
[ 84%] Built target tutorial_BasicLinearTransformsTrackbar
[ 84%] Linking CXX executable ../../bin/cpp-tutorial-how_to_scan_images
[ 84%] Built target tutorial_how_to_scan_images
[ 84%] Linking CXX executable ../../bin/cpp-example-openni_capture
[ 84%] Built target example_openni_capture
[ 84%] Linking CXX executable ../../bin/cpp-example-videocapture_starter
[ 85%] Built target example_videocapture_starter
[ 85%] Linking CXX executable ../../bin/cpp-example-select3dobj
[ 85%] Built target example_select3dobj
[ 85%] Linking CXX executable ../../bin/cpp-tutorial-cornerDetector_Demo
[ 85%] Built target tutorial_cornerDetector_Demo
[ 85%] Linking CXX executable ../../bin/cpp-example-create_mask
[ 85%] Built target example_create_mask
[ 85%] Linking CXX executable ../../bin/cpp-tutorial-generalContours_demo2
[ 85%] Built target tutorial_generalContours_demo2
[ 85%] Linking CXX executable ../../bin/cpp-tutorial-decolor
[ 85%] Built target tutorial_decolor
[ 85%] Linking CXX executable ../../bin/cpp-tutorial-objectDetection
[ 85%] Built target tutorial_objectDetection
[ 85%] Linking CXX executable ../../bin/cpp-example-squares
[ 85%] Built target example_squares
[ 85%] Linking CXX executable ../../bin/cpp-tutorial-SBM_Sample
[ 85%] Built target tutorial_SBM_Sample
[ 85%] Linking CXX executable ../../bin/cpp-tutorial-planar_tracking
[ 85%] Built target tutorial_planar_tracking
[ 85%] Linking CXX executable ../../bin/cpp-tutorial-Morphology_1
[ 85%] Built target tutorial_Morphology_1
[ 85%] Linking CXX executable ../../bin/cpp-example-laplace
[ 85%] Built target example_laplace
[ 85%] Linking CXX executable ../../bin/cpp-tutorial-calcBackProject_Demo1
[ 85%] Built target tutorial_calcBackProject_Demo1
[ 85%] Linking CXX executable ../../bin/cpp-example-application_trace
[ 85%] Built target example_application_trace
[ 85%] Linking CXX executable ../../bin/cpp-tutorial-cloning_gui
[ 85%] Built target tutorial_cloning_gui
[ 85%] Linking CXX executable ../../bin/cpp-tutorial-interoperability_with_OpenCV_1
[ 85%] Built target tutorial_interoperability_with_OpenCV_1
[ 85%] Linking CXX executable ../../bin/cpp-example-houghcircles
[ 85%] Built target example_houghcircles
[ 85%] Linking CXX executable ../../bin/cpp-example-image
[ 85%] Built target example_image
[ 86%] Linking CXX executable ../../bin/cpp-example-polar_transforms
[ 86%] Built target example_polar_transforms
[ 86%] Linking CXX executable ../../bin/cpp-tutorial-hdr_imaging
[ 86%] Built target tutorial_hdr_imaging
[ 86%] Linking CXX executable ../../bin/cpp-tutorial-introduction_to_pca
[ 86%] Built target tutorial_introduction_to_pca
[ 87%] Linking CXX executable ../../bin/cpp-tutorial-camera_calibration
[ 87%] Built target tutorial_camera_calibration
[ 87%] Linking CXX executable ../../bin/cpp-tutorial-introduction_windows_vs
[ 87%] Built target tutorial_introduction_windows_vs
[ 87%] Linking CXX executable ../../bin/cpp-tutorial-generalContours_demo1
[ 87%] Built target tutorial_generalContours_demo1
[ 87%] Linking CXX executable ../../bin/cpp-tutorial-AddingImagesTrackbar
[ 87%] Built target tutorial_AddingImagesTrackbar
[ 87%] Linking CXX executable ../../bin/cpp-example-cloning_gui
[ 87%] Built target example_cloning_gui
[ 88%] Linking CXX executable ../../bin/cpp-tutorial-gdal-image
[ 88%] Built target tutorial_gdal-image
[ 88%] Linking CXX executable ../../bin/cpp-tutorial-Laplace_Demo
[ 88%] Built target tutorial_Laplace_Demo
[ 88%] Linking CXX executable ../../bin/cpp-tutorial-EqualizeHist_Demo
[ 88%] Built target tutorial_EqualizeHist_Demo
[ 88%] Linking CXX executable ../../bin/cpp-example-image_alignment
[ 88%] Built target example_image_alignment
[ 88%] Linking CXX executable ../../bin/cpp-example-detect_mser
[ 88%] Built target example_detect_mser
[ 88%] Linking CXX executable ../../bin/cpp-tutorial-HoughLines_Demo
[ 88%] Built target tutorial_HoughLines_Demo
[ 88%] Linking CXX executable ../../bin/cpp-tutorial-cloning_demo
[ 88%] Built target tutorial_cloning_demo
[ 88%] Linking CXX executable ../../bin/cpp-tutorial-imageSegmentation
[ 88%] Built target tutorial_imageSegmentation
[ 88%] Linking CXX executable ../../bin/cpp-example-smiledetect
[ 88%] Built target example_smiledetect
[ 88%] Linking CXX executable ../../bin/cpp-tutorial-Remap_Demo
[ 88%] Built target tutorial_Remap_Demo
[ 89%] Linking CXX executable ../../bin/cpp-tutorial-cornerSubPix_Demo
[ 89%] Built target tutorial_cornerSubPix_Demo
[ 89%] Linking CXX executable ../../bin/cpp-tutorial-Morphology_2
[ 89%] Built target tutorial_Morphology_2
[ 89%] Linking CXX executable ../../bin/cpp-tutorial-Geometric_Transforms_Demo
[ 89%] Built target tutorial_Geometric_Transforms_Demo
[ 89%] Linking CXX executable ../../bin/cpp-tutorial-MatchTemplate_Demo
[ 90%] Built target tutorial_MatchTemplate_Demo
[ 91%] Linking CXX executable ../../bin/cpp-example-drawing
[ 91%] Built target example_drawing
[ 91%] Linking CXX executable ../../bin/cpp-tutorial-Sobel_Demo
[ 92%] Built target tutorial_Sobel_Demo
[ 92%] Linking CXX executable ../../bin/cpp-tutorial-HoughCircle_Demo
[ 92%] Built target tutorial_HoughCircle_Demo
[ 92%] Linking CXX executable ../../bin/cpp-example-matchmethod_orb_akaze_brisk
[ 92%] Built target example_matchmethod_orb_akaze_brisk
[ 92%] Linking CXX executable ../../bin/cpp-example-videostab
[ 92%] Built target example_videostab
[ 92%] Linking CXX executable ../../bin/cpp-tutorial-video-input-psnr-ssim
[ 92%] Built target tutorial_video-input-psnr-ssim
[ 92%] Linking CXX executable ../../bin/cpp-tutorial-Smoothing
[ 92%] Built target tutorial_Smoothing
[ 92%] Linking CXX executable ../../bin/cpp-example-fitellipse
[ 92%] Built target example_fitellipse
[ 92%] Linking CXX executable ../../bin/cpp-example-facedetect
[ 92%] Built target example_facedetect
[ 92%] Linking CXX executable ../../bin/cpp-example-shape_example
[ 92%] Built target example_shape_example
[ 92%] Linking CXX executable ../../bin/cpp-example-videowriter_basic
[ 92%] Built target example_videowriter_basic
[ 93%] Linking CXX executable ../../bin/cpp-tutorial-video-write
[ 93%] Built target tutorial_video-write
[ 93%] Linking CXX executable ../../bin/cpp-tutorial-compareHist_Demo
[ 93%] Built target tutorial_compareHist_Demo
[ 93%] Linking CXX executable ../../bin/cpp-tutorial-cornerHarris_Demo
[ 93%] Built target tutorial_cornerHarris_Demo
[ 94%] Linking CXX executable ../../bin/cpp-example-stereo_match
[ 94%] Built target example_stereo_match
[ 94%] Linking CXX executable ../../bin/cpp-tutorial-LATCH_match
[ 94%] Built target tutorial_LATCH_match
[ 94%] Linking CXX executable ../../bin/cpp-tutorial-Threshold
[ 94%] Built target tutorial_Threshold
[ 94%] Linking CXX executable ../../bin/cpp-example-stitching
[ 94%] Built target example_stitching
[ 94%] Linking CXX executable ../../bin/cpp-tutorial-bg_sub
[ 94%] Built target tutorial_bg_sub
[ 94%] Linking CXX executable ../../bin/cpp-tutorial-goodFeaturesToTrack_Demo
[ 94%] Built target tutorial_goodFeaturesToTrack_Demo
[ 94%] Linking CXX executable ../../bin/cpp-tutorial-BasicLinearTransforms
[ 94%] Built target tutorial_BasicLinearTransforms
[ 94%] Linking CXX executable ../../bin/cpp-tutorial-HitMiss
[ 94%] Built target tutorial_HitMiss
[ 94%] Linking CXX executable ../../bin/cpp-tutorial-CannyDetector_Demo
[ 94%] Built target tutorial_CannyDetector_Demo
[ 94%] Linking CXX executable ../../bin/cpp-tutorial-Threshold_inRange
[ 94%] Built target tutorial_Threshold_inRange
[ 94%] Linking CXX executable ../../bin/cpp-example-connected_components
[ 94%] Built target example_connected_components
[ 94%] Linking CXX executable ../../bin/cpp-tutorial-Pyramids
[ 94%] Built target tutorial_Pyramids
[ 94%] Linking CXX executable ../../bin/cpp-example-starter_imagelist
[ 94%] Built target example_starter_imagelist
[ 94%] Linking CXX executable ../../bin/cpp-tutorial-npr_demo
[ 94%] Built target tutorial_npr_demo
[ 94%] Linking CXX executable ../../bin/cpp-tutorial-Morphology_3
[ 94%] Built target tutorial_Morphology_3
[ 94%] Linking CXX executable ../../bin/cpp-example-autofocus
[ 94%] Built target example_autofocus
[ 94%] Linking CXX executable ../../bin/cpp-example-ffilldemo
[ 95%] Built target example_ffilldemo
[ 95%] Linking CXX executable ../../bin/cpp-example-detect_blob
[ 95%] Built target example_detect_blob
[ 95%] Linking CXX executable ../../bin/cpp-tutorial-gpu-basics-similarity
[ 95%] Built target tutorial_gpu-basics-similarity
[ 95%] Linking CXX executable ../../bin/cpp-tutorial-changing_contrast_brightness_image
[ 95%] Built target tutorial_changing_contrast_brightness_image
[ 95%] Linking CXX executable ../../bin/cpp-example-opencv_version
[ 95%] Built target example_opencv_version
[ 95%] Linking CXX executable ../../bin/cpp-tutorial-pointPolygonTest_demo
[ 95%] Built target tutorial_pointPolygonTest_demo
[ 95%] Linking CXX executable ../../bin/cpp-example-fback
[ 95%] Built target example_fback
[ 95%] Linking CXX executable ../../bin/cpp-example-convexhull
[ 95%] Built target example_convexhull
[ 95%] Linking CXX executable ../../bin/cpp-example-edge
[ 95%] Built target example_edge
[ 95%] Linking CXX executable ../../bin/cpp-example-3calibration
[ 95%] Built target example_3calibration
[ 95%] Linking CXX executable ../../bin/cpp-example-segment_objects
[ 95%] Built target example_segment_objects
[ 95%] Linking CXX executable ../../bin/cpp-tutorial-mat_the_basic_image_container
[ 95%] Built target tutorial_mat_the_basic_image_container
[ 95%] Linking CXX executable ../../bin/cpp-example-lkdemo
[ 96%] Built target example_lkdemo
[ 96%] Linking CXX executable ../../bin/example_dnn-ssd_mobilenet_object_detection
[ 96%] Built target example_dnn_ssd_mobilenet_object_detection
[ 96%] Linking CXX executable ../../bin/example_dnn-ssd_object_detection
[ 96%] Built target example_dnn_ssd_object_detection
[ 96%] Linking CXX executable ../../bin/example_dnn-squeezenet_halide
[ 96%] Built target example_dnn_squeezenet_halide
[ 96%] Linking CXX executable ../../bin/example_dnn-fcn_semsegm
[ 96%] Built target example_dnn_fcn_semsegm
[ 96%] Linking CXX executable ../../bin/example_dnn-tf_inception
[ 96%] Built target example_dnn_tf_inception
[ 96%] Linking CXX executable ../../bin/example_dnn-caffe_googlenet
[ 96%] Built target example_dnn_caffe_googlenet
[ 96%] Linking CXX executable ../../bin/example_dnn-torch_enet
[ 96%] Built target example_dnn_torch_enet
[ 96%] Linking CXX executable ../../bin/gpu-example-generalized_hough
[ 96%] Built target example_gpu_generalized_hough
[ 96%] Linking CXX executable ../../bin/gpu-example-cascadeclassifier_nvidia_api
[ 96%] Built target example_gpu_cascadeclassifier_nvidia_api
[ 96%] Linking CXX executable ../../bin/gpu-example-video_reader
[ 96%] Built target example_gpu_video_reader
[ 96%] Linking CXX executable ../../bin/gpu-example-surf_keypoint_matcher
[ 97%] Built target example_gpu_surf_keypoint_matcher
[ 97%] Linking CXX executable ../../bin/gpu-example-farneback_optical_flow
[ 97%] Built target example_gpu_farneback_optical_flow
[ 97%] Linking CXX executable ../../bin/performance_gpu
[ 97%] Built target example_gpu_performance
[ 97%] Linking CXX executable ../../bin/gpu-example-stereo_match
[ 97%] Built target example_gpu_stereo_match
[ 97%] Linking CXX executable ../../bin/gpu-example-optical_flow
[ 98%] Built target example_gpu_optical_flow
[ 98%] Linking CXX executable ../../bin/gpu-example-houghlines
[ 98%] Built target example_gpu_houghlines
[ 98%] Linking CXX executable ../../bin/gpu-example-hog
[ 98%] Built target example_gpu_hog
[ 98%] Linking CXX executable ../../bin/gpu-example-multi
[ 98%] Built target example_gpu_multi
[ 98%] Linking CXX executable ../../bin/gpu-example-video_writer
[ 98%] Built target example_gpu_video_writer
[ 98%] Linking CXX executable ../../bin/gpu-example-alpha_comp
[ 98%] Built target example_gpu_alpha_comp
[ 98%] Linking CXX executable ../../bin/gpu-example-cascadeclassifier
[ 98%] Built target example_gpu_cascadeclassifier
[ 98%] Linking CXX executable ../../bin/gpu-example-super_resolution
[ 98%] Built target example_gpu_super_resolution
[ 98%] Linking CXX executable ../../bin/gpu-example-driver_api_stereo_multi
[ 98%] Built target example_gpu_driver_api_stereo_multi
[ 98%] Linking CXX executable ../../bin/gpu-example-pyrlk_optical_flow
[ 98%] Built target example_gpu_pyrlk_optical_flow
[ 98%] Linking CXX executable ../../bin/gpu-example-bgfg_segm
[ 98%] Built target example_gpu_bgfg_segm
[ 98%] Linking CXX executable ../../bin/gpu-example-morphology
[ 98%] Built target example_gpu_morphology
[ 98%] Linking CXX executable ../../bin/gpu-example-opticalflow_nvidia_api
[ 98%] Built target example_gpu_opticalflow_nvidia_api
[ 98%] Linking CXX executable ../../bin/gpu-example-stereo_multi
[ 98%] Built target example_gpu_stereo_multi
[ 98%] Linking CXX executable ../../bin/gpu-example-driver_api_multi
[ 99%] Built target example_gpu_driver_api_multi
[ 99%] Linking CXX executable ../../bin/tapi-example-squares
[100%] Built target example_tapi_squares
[100%] Linking CXX executable ../../bin/tapi-example-hog
[100%] Built target example_tapi_hog
[100%] Linking CXX executable ../../bin/tapi-example-clahe
[100%] Built target example_tapi_clahe
[100%] Linking CXX executable ../../bin/tapi-example-ufacedetect
[100%] Built target example_tapi_ufacedetect
[100%] Linking CXX executable ../../bin/tapi-example-camshift
[100%] Built target example_tapi_camshift
[100%] Linking CXX executable ../../bin/tapi-example-tvl1_optical_flow
[100%] Built target example_tapi_tvl1_optical_flow
[100%] Linking CXX executable ../../bin/tapi-example-pyrlk_optical_flow
[100%] Built target example_tapi_pyrlk_optical_flow
[100%] Linking CXX executable ../../bin/tapi-example-bgfg_segm
[100%] Built target example_tapi_bgfg_segm
Install the project...
-- Install configuration: "Release"
-- Installing: /usr/include/opencv2/cvconfig.h
-- Installing: /usr/include/opencv2/opencv_modules.hpp
-- Installing: /usr/lib/pkgconfig/opencv.pc
-- Old export file "/usr/share/OpenCV/OpenCVModules.cmake" will be replaced.  Removing files [/usr/share/OpenCV/OpenCVModules-release.cmake].
-- Installing: /usr/share/OpenCV/OpenCVModules.cmake
-- Installing: /usr/share/OpenCV/OpenCVModules-release.cmake
-- Installing: /usr/share/OpenCV/OpenCVConfig-version.cmake
-- Installing: /usr/share/OpenCV/OpenCVConfig.cmake
-- Installing: /usr/bin/opencv_run_all_tests.sh
-- Installing: /usr/share/OpenCV/valgrind.supp
-- Installing: /usr/share/OpenCV/valgrind_3rdparty.supp
-- Installing: /usr/include/opencv/highgui.h
-- Installing: /usr/include/opencv/cvwimage.h
-- Installing: /usr/include/opencv/cxcore.h
-- Installing: /usr/include/opencv/cvaux.h
-- Installing: /usr/include/opencv/ml.h
-- Installing: /usr/include/opencv/cvaux.hpp
-- Installing: /usr/include/opencv/cxcore.hpp
-- Installing: /usr/include/opencv/cv.h
-- Installing: /usr/include/opencv/cxeigen.hpp
-- Installing: /usr/include/opencv/cv.hpp
-- Installing: /usr/include/opencv/cxmisc.h
-- Installing: /usr/include/opencv2/opencv.hpp
-- Installing: /usr/lib/libopencv_cudev.so.3.3.0
-- Installing: /usr/lib/libopencv_cudev.so.3.3
-- Set runtime path of "/usr/lib/libopencv_cudev.so.3.3.0" to "/usr/lib:/usr/local/cuda-8.0/lib64"
-- Installing: /usr/lib/libopencv_cudev.so
-- Installing: /usr/include/opencv2/cudev/warp/detail/reduce_key_val.hpp
-- Installing: /usr/include/opencv2/cudev/warp/detail/reduce.hpp
-- Installing: /usr/include/opencv2/cudev/warp/reduce.hpp
-- Installing: /usr/include/opencv2/cudev/warp/shuffle.hpp
-- Installing: /usr/include/opencv2/cudev/warp/warp.hpp
-- Installing: /usr/include/opencv2/cudev/warp/scan.hpp
-- Installing: /usr/include/opencv2/cudev/util/detail/tuple.hpp
-- Installing: /usr/include/opencv2/cudev/util/detail/type_traits.hpp
-- Installing: /usr/include/opencv2/cudev/util/saturate_cast.hpp
-- Installing: /usr/include/opencv2/cudev/util/atomic.hpp
-- Installing: /usr/include/opencv2/cudev/util/tuple.hpp
-- Installing: /usr/include/opencv2/cudev/util/type_traits.hpp
-- Installing: /usr/include/opencv2/cudev/util/limits.hpp
-- Installing: /usr/include/opencv2/cudev/util/simd_functions.hpp
-- Installing: /usr/include/opencv2/cudev/util/vec_math.hpp
-- Installing: /usr/include/opencv2/cudev/util/vec_traits.hpp
-- Installing: /usr/include/opencv2/cudev/block/block.hpp
-- Installing: /usr/include/opencv2/cudev/block/detail/reduce_key_val.hpp
-- Installing: /usr/include/opencv2/cudev/block/detail/reduce.hpp
-- Installing: /usr/include/opencv2/cudev/block/dynamic_smem.hpp
-- Installing: /usr/include/opencv2/cudev/block/reduce.hpp
-- Installing: /usr/include/opencv2/cudev/block/vec_distance.hpp
-- Installing: /usr/include/opencv2/cudev/block/scan.hpp
-- Installing: /usr/include/opencv2/cudev/grid/detail/reduce_to_column.hpp
-- Installing: /usr/include/opencv2/cudev/grid/detail/transform.hpp
-- Installing: /usr/include/opencv2/cudev/grid/detail/pyr_down.hpp
-- Installing: /usr/include/opencv2/cudev/grid/detail/integral.hpp
-- Installing: /usr/include/opencv2/cudev/grid/detail/reduce.hpp
-- Installing: /usr/include/opencv2/cudev/grid/detail/histogram.hpp
-- Installing: /usr/include/opencv2/cudev/grid/detail/transpose.hpp
-- Installing: /usr/include/opencv2/cudev/grid/detail/pyr_up.hpp
-- Installing: /usr/include/opencv2/cudev/grid/detail/copy.hpp
-- Installing: /usr/include/opencv2/cudev/grid/detail/minmaxloc.hpp
-- Installing: /usr/include/opencv2/cudev/grid/detail/split_merge.hpp
-- Installing: /usr/include/opencv2/cudev/grid/detail/reduce_to_row.hpp
-- Installing: /usr/include/opencv2/cudev/grid/reduce_to_vec.hpp
-- Installing: /usr/include/opencv2/cudev/grid/pyramids.hpp
-- Installing: /usr/include/opencv2/cudev/grid/transform.hpp
-- Installing: /usr/include/opencv2/cudev/grid/integral.hpp
-- Installing: /usr/include/opencv2/cudev/grid/reduce.hpp
-- Installing: /usr/include/opencv2/cudev/grid/histogram.hpp
-- Installing: /usr/include/opencv2/cudev/grid/transpose.hpp
-- Installing: /usr/include/opencv2/cudev/grid/copy.hpp
-- Installing: /usr/include/opencv2/cudev/grid/split_merge.hpp
-- Installing: /usr/include/opencv2/cudev/expr/per_element_func.hpp
-- Installing: /usr/include/opencv2/cudev/expr/warping.hpp
-- Installing: /usr/include/opencv2/cudev/expr/color.hpp
-- Installing: /usr/include/opencv2/cudev/expr/reduction.hpp
-- Installing: /usr/include/opencv2/cudev/expr/deriv.hpp
-- Installing: /usr/include/opencv2/cudev/expr/binary_func.hpp
-- Installing: /usr/include/opencv2/cudev/expr/binary_op.hpp
-- Installing: /usr/include/opencv2/cudev/expr/unary_op.hpp
-- Installing: /usr/include/opencv2/cudev/expr/expr.hpp
-- Installing: /usr/include/opencv2/cudev/expr/unary_func.hpp
-- Installing: /usr/include/opencv2/cudev/ptr2d/glob.hpp
-- Installing: /usr/include/opencv2/cudev/ptr2d/detail/gpumat.hpp
-- Installing: /usr/include/opencv2/cudev/ptr2d/resize.hpp
-- Installing: /usr/include/opencv2/cudev/ptr2d/mask.hpp
-- Installing: /usr/include/opencv2/cudev/ptr2d/warping.hpp
-- Installing: /usr/include/opencv2/cudev/ptr2d/transform.hpp
-- Installing: /usr/include/opencv2/cudev/ptr2d/constant.hpp
-- Installing: /usr/include/opencv2/cudev/ptr2d/traits.hpp
-- Installing: /usr/include/opencv2/cudev/ptr2d/texture.hpp
-- Installing: /usr/include/opencv2/cudev/ptr2d/deriv.hpp
-- Installing: /usr/include/opencv2/cudev/ptr2d/zip.hpp
-- Installing: /usr/include/opencv2/cudev/ptr2d/gpumat.hpp
-- Installing: /usr/include/opencv2/cudev/ptr2d/interpolation.hpp
-- Installing: /usr/include/opencv2/cudev/ptr2d/remap.hpp
-- Installing: /usr/include/opencv2/cudev/ptr2d/extrapolation.hpp
-- Installing: /usr/include/opencv2/cudev/ptr2d/lut.hpp
-- Installing: /usr/include/opencv2/cudev/common.hpp
-- Installing: /usr/include/opencv2/cudev/functional/detail/color_cvt.hpp
-- Installing: /usr/include/opencv2/cudev/functional/color_cvt.hpp
-- Installing: /usr/include/opencv2/cudev/functional/functional.hpp
-- Installing: /usr/include/opencv2/cudev/functional/tuple_adapter.hpp
-- Installing: /usr/include/opencv2/cudev.hpp
-- Up-to-date: /usr/include/opencv2/cudev/common.hpp
-- Installing: /usr/bin/opencv_test_cudev
-- Set runtime path of "/usr/bin/opencv_test_cudev" to "/usr/lib:/usr/local/cuda-8.0/lib64"
-- Installing: /usr/lib/libopencv_core.so.3.3.0
-- Installing: /usr/lib/libopencv_core.so.3.3
-- Set runtime path of "/usr/lib/libopencv_core.so.3.3.0" to "/usr/lib:/usr/local/cuda-8.0/lib64"
-- Installing: /usr/lib/libopencv_core.so
-- Installing: /usr/include/opencv2/core/cuda/block.hpp
-- Installing: /usr/include/opencv2/core/cuda/border_interpolate.hpp
-- Installing: /usr/include/opencv2/core/cuda/saturate_cast.hpp
-- Installing: /usr/include/opencv2/core/cuda/emulation.hpp
-- Installing: /usr/include/opencv2/core/cuda/transform.hpp
-- Installing: /usr/include/opencv2/core/cuda/datamov_utils.hpp
-- Installing: /usr/include/opencv2/core/cuda/functional.hpp
-- Installing: /usr/include/opencv2/core/cuda/funcattrib.hpp
-- Installing: /usr/include/opencv2/core/cuda/dynamic_smem.hpp
-- Installing: /usr/include/opencv2/core/cuda/filters.hpp
-- Installing: /usr/include/opencv2/core/cuda/reduce.hpp
-- Installing: /usr/include/opencv2/core/cuda/color.hpp
-- Installing: /usr/include/opencv2/core/cuda/warp_reduce.hpp
-- Installing: /usr/include/opencv2/core/cuda/type_traits.hpp
-- Installing: /usr/include/opencv2/core/cuda/vec_distance.hpp
-- Installing: /usr/include/opencv2/core/cuda/common.hpp
-- Installing: /usr/include/opencv2/core/cuda/utility.hpp
-- Installing: /usr/include/opencv2/core/cuda/limits.hpp
-- Installing: /usr/include/opencv2/core/cuda/warp_shuffle.hpp
-- Installing: /usr/include/opencv2/core/cuda/simd_functions.hpp
-- Installing: /usr/include/opencv2/core/cuda/vec_math.hpp
-- Installing: /usr/include/opencv2/core/cuda/warp.hpp
-- Installing: /usr/include/opencv2/core/cuda/scan.hpp
-- Installing: /usr/include/opencv2/core/cuda/vec_traits.hpp
-- Installing: /usr/include/opencv2/core/cuda/detail/reduce_key_val.hpp
-- Installing: /usr/include/opencv2/core/cuda/detail/type_traits_detail.hpp
-- Installing: /usr/include/opencv2/core/cuda/detail/vec_distance_detail.hpp
-- Installing: /usr/include/opencv2/core/cuda/detail/reduce.hpp
-- Installing: /usr/include/opencv2/core/cuda/detail/color_detail.hpp
-- Installing: /usr/include/opencv2/core/cuda/detail/transform_detail.hpp
-- Installing: /usr/include/opencv2/core.hpp
-- Installing: /usr/include/opencv2/core/cuda.inl.hpp
-- Installing: /usr/include/opencv2/core/softfloat.hpp
-- Installing: /usr/include/opencv2/core/ptr.inl.hpp
-- Installing: /usr/include/opencv2/core/version.hpp
-- Installing: /usr/include/opencv2/core/va_intel.hpp
-- Installing: /usr/include/opencv2/core/ocl.hpp
-- Installing: /usr/include/opencv2/core/persistence.hpp
-- Installing: /usr/include/opencv2/core/opengl.hpp
-- Installing: /usr/include/opencv2/core/cvstd.inl.hpp
-- Installing: /usr/include/opencv2/core/optim.hpp
-- Installing: /usr/include/opencv2/core/cuda_types.hpp
-- Installing: /usr/include/opencv2/core/matx.hpp
-- Installing: /usr/include/opencv2/core/ippasync.hpp
-- Installing: /usr/include/opencv2/core/mat.hpp
-- Installing: /usr/include/opencv2/core/mat.inl.hpp
-- Installing: /usr/include/opencv2/core/affine.hpp
-- Installing: /usr/include/opencv2/core/operations.hpp
-- Installing: /usr/include/opencv2/core/bufferpool.hpp
-- Installing: /usr/include/opencv2/core/traits.hpp
-- Installing: /usr/include/opencv2/core/wimage.hpp
-- Installing: /usr/include/opencv2/core/ovx.hpp
-- Installing: /usr/include/opencv2/core/fast_math.hpp
-- Installing: /usr/include/opencv2/core/cuda.hpp
-- Installing: /usr/include/opencv2/core/utility.hpp
-- Installing: /usr/include/opencv2/core/neon_utils.hpp
-- Installing: /usr/include/opencv2/core/sse_utils.hpp
-- Installing: /usr/include/opencv2/core/types.hpp
-- Installing: /usr/include/opencv2/core/eigen.hpp
-- Installing: /usr/include/opencv2/core/base.hpp
-- Installing: /usr/include/opencv2/core/directx.hpp
-- Installing: /usr/include/opencv2/core/cvstd.hpp
-- Installing: /usr/include/opencv2/core/saturate.hpp
-- Installing: /usr/include/opencv2/core/cuda_stream_accessor.hpp
-- Installing: /usr/include/opencv2/core/core.hpp
-- Installing: /usr/include/opencv2/core/ocl_genbase.hpp
-- Installing: /usr/include/opencv2/core/types_c.h
-- Installing: /usr/include/opencv2/core/cv_cpu_dispatch.h
-- Installing: /usr/include/opencv2/core/core_c.h
-- Installing: /usr/include/opencv2/core/cv_cpu_helper.h
-- Installing: /usr/include/opencv2/core/cvdef.h
-- Installing: /usr/include/opencv2/core/hal/intrin_cpp.hpp
-- Installing: /usr/include/opencv2/core/hal/hal.hpp
-- Installing: /usr/include/opencv2/core/hal/intrin_neon.hpp
-- Installing: /usr/include/opencv2/core/hal/intrin.hpp
-- Installing: /usr/include/opencv2/core/hal/intrin_sse.hpp
-- Installing: /usr/include/opencv2/core/hal/interface.h
-- Installing: /usr/include/opencv2/core/utils/trace.hpp
-- Installing: /usr/include/opencv2/core/utils/logger.hpp
-- Installing: /usr/bin/opencv_test_core
-- Set runtime path of "/usr/bin/opencv_test_core" to "/usr/lib:/usr/local/cuda-8.0/lib64"
-- Installing: /usr/bin/opencv_perf_core
-- Set runtime path of "/usr/bin/opencv_perf_core" to "/usr/lib:/usr/local/cuda-8.0/lib64"
-- Installing: /usr/lib/libopencv_cudaarithm.so.3.3.0
-- Installing: /usr/lib/libopencv_cudaarithm.so.3.3
-- Set runtime path of "/usr/lib/libopencv_cudaarithm.so.3.3.0" to "/usr/lib:/usr/local/cuda-8.0/lib64"
-- Installing: /usr/lib/libopencv_cudaarithm.so
-- Installing: /usr/include/opencv2/cudaarithm.hpp
-- Installing: /usr/bin/opencv_test_cudaarithm
-- Set runtime path of "/usr/bin/opencv_test_cudaarithm" to "/usr/lib:/usr/local/cuda-8.0/lib64"
-- Installing: /usr/bin/opencv_perf_cudaarithm
-- Set runtime path of "/usr/bin/opencv_perf_cudaarithm" to "/usr/lib:/usr/local/cuda-8.0/lib64"
-- Installing: /usr/lib/libopencv_flann.so.3.3.0
-- Installing: /usr/lib/libopencv_flann.so.3.3
-- Set runtime path of "/usr/lib/libopencv_flann.so.3.3.0" to "/usr/lib:/usr/local/cuda-8.0/lib64"
-- Installing: /usr/lib/libopencv_flann.so
-- Installing: /usr/include/opencv2/flann.hpp
-- Installing: /usr/include/opencv2/flann/miniflann.hpp
-- Installing: /usr/include/opencv2/flann/flann.hpp
-- Installing: /usr/include/opencv2/flann/flann_base.hpp
-- Installing: /usr/include/opencv2/flann/all_indices.h
-- Installing: /usr/include/opencv2/flann/allocator.h
-- Installing: /usr/include/opencv2/flann/nn_index.h
-- Installing: /usr/include/opencv2/flann/simplex_downhill.h
-- Installing: /usr/include/opencv2/flann/any.h
-- Installing: /usr/include/opencv2/flann/heap.h
-- Installing: /usr/include/opencv2/flann/params.h
-- Installing: /usr/include/opencv2/flann/hierarchical_clustering_index.h
-- Installing: /usr/include/opencv2/flann/timer.h
-- Installing: /usr/include/opencv2/flann/composite_index.h
-- Installing: /usr/include/opencv2/flann/saving.h
-- Installing: /usr/include/opencv2/flann/random.h
-- Installing: /usr/include/opencv2/flann/sampling.h
-- Installing: /usr/include/opencv2/flann/object_factory.h
-- Installing: /usr/include/opencv2/flann/index_testing.h
-- Installing: /usr/include/opencv2/flann/kdtree_index.h
-- Installing: /usr/include/opencv2/flann/matrix.h
-- Installing: /usr/include/opencv2/flann/kdtree_single_index.h
-- Installing: /usr/include/opencv2/flann/linear_index.h
-- Installing: /usr/include/opencv2/flann/ground_truth.h
-- Installing: /usr/include/opencv2/flann/dist.h
-- Installing: /usr/include/opencv2/flann/general.h
-- Installing: /usr/include/opencv2/flann/hdf5.h
-- Installing: /usr/include/opencv2/flann/result_set.h
-- Installing: /usr/include/opencv2/flann/dynamic_bitset.h
-- Installing: /usr/include/opencv2/flann/kmeans_index.h
-- Installing: /usr/include/opencv2/flann/config.h
-- Installing: /usr/include/opencv2/flann/lsh_index.h
-- Installing: /usr/include/opencv2/flann/lsh_table.h
-- Installing: /usr/include/opencv2/flann/dummy.h
-- Installing: /usr/include/opencv2/flann/defines.h
-- Installing: /usr/include/opencv2/flann/autotuned_index.h
-- Installing: /usr/include/opencv2/flann/logger.h
-- Installing: /usr/bin/opencv_test_flann
-- Set runtime path of "/usr/bin/opencv_test_flann" to "/usr/lib:/usr/local/cuda-8.0/lib64"
-- Installing: /usr/lib/libopencv_imgproc.so.3.3.0
-- Installing: /usr/lib/libopencv_imgproc.so.3.3
-- Set runtime path of "/usr/lib/libopencv_imgproc.so.3.3.0" to "/usr/lib:/usr/local/cuda-8.0/lib64"
-- Installing: /usr/lib/libopencv_imgproc.so
-- Installing: /usr/include/opencv2/imgproc.hpp
-- Installing: /usr/include/opencv2/imgproc/imgproc.hpp
-- Installing: /usr/include/opencv2/imgproc/types_c.h
-- Installing: /usr/include/opencv2/imgproc/imgproc_c.h
-- Installing: /usr/include/opencv2/imgproc/hal/hal.hpp
-- Installing: /usr/include/opencv2/imgproc/hal/interface.h
-- Installing: /usr/include/opencv2/imgproc/detail/distortion_model.hpp
-- Installing: /usr/bin/opencv_test_imgproc
-- Set runtime path of "/usr/bin/opencv_test_imgproc" to "/usr/lib:/usr/local/cuda-8.0/lib64"
-- Installing: /usr/bin/opencv_perf_imgproc
-- Set runtime path of "/usr/bin/opencv_perf_imgproc" to "/usr/lib:/usr/local/cuda-8.0/lib64"
-- Installing: /usr/lib/libopencv_ml.so.3.3.0
-- Installing: /usr/lib/libopencv_ml.so.3.3
-- Set runtime path of "/usr/lib/libopencv_ml.so.3.3.0" to "/usr/lib:/usr/local/cuda-8.0/lib64"
-- Installing: /usr/lib/libopencv_ml.so
-- Installing: /usr/include/opencv2/ml.hpp
-- Installing: /usr/include/opencv2/ml/ml.hpp
-- Installing: /usr/bin/opencv_test_ml
-- Set runtime path of "/usr/bin/opencv_test_ml" to "/usr/lib:/usr/local/cuda-8.0/lib64"
-- Installing: /usr/lib/libopencv_objdetect.so.3.3.0
-- Installing: /usr/lib/libopencv_objdetect.so.3.3
-- Set runtime path of "/usr/lib/libopencv_objdetect.so.3.3.0" to "/usr/lib:/usr/local/cuda-8.0/lib64"
-- Installing: /usr/lib/libopencv_objdetect.so
-- Installing: /usr/include/opencv2/objdetect.hpp
-- Installing: /usr/include/opencv2/objdetect/objdetect.hpp
-- Installing: /usr/include/opencv2/objdetect/detection_based_tracker.hpp
-- Installing: /usr/include/opencv2/objdetect/objdetect_c.h
-- Installing: /usr/bin/opencv_test_objdetect
-- Set runtime path of "/usr/bin/opencv_test_objdetect" to "/usr/lib:/usr/local/cuda-8.0/lib64"
-- Installing: /usr/bin/opencv_perf_objdetect
-- Set runtime path of "/usr/bin/opencv_perf_objdetect" to "/usr/lib:/usr/local/cuda-8.0/lib64"
-- Installing: /usr/lib/libopencv_video.so.3.3.0
-- Installing: /usr/lib/libopencv_video.so.3.3
-- Set runtime path of "/usr/lib/libopencv_video.so.3.3.0" to "/usr/lib:/usr/local/cuda-8.0/lib64"
-- Installing: /usr/lib/libopencv_video.so
-- Installing: /usr/include/opencv2/video.hpp
-- Installing: /usr/include/opencv2/video/video.hpp
-- Installing: /usr/include/opencv2/video/background_segm.hpp
-- Installing: /usr/include/opencv2/video/tracking.hpp
-- Installing: /usr/include/opencv2/video/tracking_c.h
-- Installing: /usr/bin/opencv_test_video
-- Set runtime path of "/usr/bin/opencv_test_video" to "/usr/lib:/usr/local/cuda-8.0/lib64"
-- Installing: /usr/bin/opencv_perf_video
-- Set runtime path of "/usr/bin/opencv_perf_video" to "/usr/lib:/usr/local/cuda-8.0/lib64"
-- Installing: /usr/lib/libopencv_cudabgsegm.so.3.3.0
-- Installing: /usr/lib/libopencv_cudabgsegm.so.3.3
-- Set runtime path of "/usr/lib/libopencv_cudabgsegm.so.3.3.0" to "/usr/lib:/usr/local/cuda-8.0/lib64"
-- Installing: /usr/lib/libopencv_cudabgsegm.so
-- Installing: /usr/include/opencv2/cudabgsegm.hpp
-- Installing: /usr/bin/opencv_test_cudabgsegm
-- Set runtime path of "/usr/bin/opencv_test_cudabgsegm" to "/usr/lib:/usr/local/cuda-8.0/lib64"
-- Installing: /usr/bin/opencv_perf_cudabgsegm
-- Set runtime path of "/usr/bin/opencv_perf_cudabgsegm" to "/usr/lib:/usr/local/cuda-8.0/lib64"
-- Installing: /usr/lib/libopencv_cudafilters.so.3.3.0
-- Installing: /usr/lib/libopencv_cudafilters.so.3.3
-- Set runtime path of "/usr/lib/libopencv_cudafilters.so.3.3.0" to "/usr/lib:/usr/local/cuda-8.0/lib64"
-- Installing: /usr/lib/libopencv_cudafilters.so
-- Installing: /usr/include/opencv2/cudafilters.hpp
-- Installing: /usr/bin/opencv_test_cudafilters
-- Set runtime path of "/usr/bin/opencv_test_cudafilters" to "/usr/lib:/usr/local/cuda-8.0/lib64"
-- Installing: /usr/bin/opencv_perf_cudafilters
-- Set runtime path of "/usr/bin/opencv_perf_cudafilters" to "/usr/lib:/usr/local/cuda-8.0/lib64"
-- Installing: /usr/lib/libopencv_cudaimgproc.so.3.3.0
-- Installing: /usr/lib/libopencv_cudaimgproc.so.3.3
-- Set runtime path of "/usr/lib/libopencv_cudaimgproc.so.3.3.0" to "/usr/lib:/usr/local/cuda-8.0/lib64"
-- Installing: /usr/lib/libopencv_cudaimgproc.so
-- Installing: /usr/include/opencv2/cudaimgproc.hpp
-- Installing: /usr/bin/opencv_test_cudaimgproc
-- Set runtime path of "/usr/bin/opencv_test_cudaimgproc" to "/usr/lib:/usr/local/cuda-8.0/lib64"
-- Installing: /usr/bin/opencv_perf_cudaimgproc
-- Set runtime path of "/usr/bin/opencv_perf_cudaimgproc" to "/usr/lib:/usr/local/cuda-8.0/lib64"
-- Installing: /usr/lib/libopencv_cudawarping.so.3.3.0
-- Installing: /usr/lib/libopencv_cudawarping.so.3.3
-- Set runtime path of "/usr/lib/libopencv_cudawarping.so.3.3.0" to "/usr/lib:/usr/local/cuda-8.0/lib64"
-- Installing: /usr/lib/libopencv_cudawarping.so
-- Installing: /usr/include/opencv2/cudawarping.hpp
-- Installing: /usr/bin/opencv_test_cudawarping
-- Set runtime path of "/usr/bin/opencv_test_cudawarping" to "/usr/lib:/usr/local/cuda-8.0/lib64"
-- Installing: /usr/bin/opencv_perf_cudawarping
-- Set runtime path of "/usr/bin/opencv_perf_cudawarping" to "/usr/lib:/usr/local/cuda-8.0/lib64"
-- Installing: /usr/lib/libopencv_dnn.so.3.3.0
-- Installing: /usr/lib/libopencv_dnn.so.3.3
-- Set runtime path of "/usr/lib/libopencv_dnn.so.3.3.0" to "/usr/lib:/usr/local/cuda-8.0/lib64"
-- Installing: /usr/lib/libopencv_dnn.so
-- Installing: /usr/include/opencv2/dnn.hpp
-- Installing: /usr/include/opencv2/dnn/dnn.hpp
-- Installing: /usr/include/opencv2/dnn/all_layers.hpp
-- Installing: /usr/include/opencv2/dnn/shape_utils.hpp
-- Installing: /usr/include/opencv2/dnn/layer.details.hpp
-- Installing: /usr/include/opencv2/dnn/dict.hpp
-- Installing: /usr/include/opencv2/dnn/layer.hpp
-- Installing: /usr/include/opencv2/dnn/dnn.inl.hpp
-- Installing: /usr/bin/opencv_test_dnn
-- Set runtime path of "/usr/bin/opencv_test_dnn" to "/usr/lib:/usr/local/cuda-8.0/lib64"
-- Installing: /usr/bin/opencv_perf_dnn
-- Set runtime path of "/usr/bin/opencv_perf_dnn" to "/usr/lib:/usr/local/cuda-8.0/lib64"
-- Installing: /usr/lib/libopencv_imgcodecs.so.3.3.0
-- Installing: /usr/lib/libopencv_imgcodecs.so.3.3
-- Set runtime path of "/usr/lib/libopencv_imgcodecs.so.3.3.0" to "/usr/lib:/usr/local/cuda-8.0/lib64"
-- Installing: /usr/lib/libopencv_imgcodecs.so
-- Installing: /usr/include/opencv2/imgcodecs.hpp
-- Installing: /usr/include/opencv2/imgcodecs/imgcodecs.hpp
-- Installing: /usr/include/opencv2/imgcodecs/ios.h
-- Installing: /usr/include/opencv2/imgcodecs/imgcodecs_c.h
-- Installing: /usr/bin/opencv_test_imgcodecs
-- Set runtime path of "/usr/bin/opencv_test_imgcodecs" to "/usr/lib:/usr/local/cuda-8.0/lib64"
-- Installing: /usr/bin/opencv_perf_imgcodecs
-- Set runtime path of "/usr/bin/opencv_perf_imgcodecs" to "/usr/lib:/usr/local/cuda-8.0/lib64"
-- Installing: /usr/lib/libopencv_photo.so.3.3.0
-- Installing: /usr/lib/libopencv_photo.so.3.3
-- Set runtime path of "/usr/lib/libopencv_photo.so.3.3.0" to "/usr/lib:/usr/local/cuda-8.0/lib64"
-- Installing: /usr/lib/libopencv_photo.so
-- Installing: /usr/include/opencv2/photo.hpp
-- Installing: /usr/include/opencv2/photo/cuda.hpp
-- Installing: /usr/include/opencv2/photo/photo.hpp
-- Installing: /usr/include/opencv2/photo/photo_c.h
-- Installing: /usr/bin/opencv_test_photo
-- Set runtime path of "/usr/bin/opencv_test_photo" to "/usr/lib:/usr/local/cuda-8.0/lib64"
-- Installing: /usr/bin/opencv_perf_photo
-- Set runtime path of "/usr/bin/opencv_perf_photo" to "/usr/lib:/usr/local/cuda-8.0/lib64"
-- Installing: /usr/lib/libopencv_shape.so.3.3.0
-- Installing: /usr/lib/libopencv_shape.so.3.3
-- Set runtime path of "/usr/lib/libopencv_shape.so.3.3.0" to "/usr/lib:/usr/local/cuda-8.0/lib64"
-- Installing: /usr/lib/libopencv_shape.so
-- Installing: /usr/include/opencv2/shape.hpp
-- Installing: /usr/include/opencv2/shape/shape_distance.hpp
-- Installing: /usr/include/opencv2/shape/hist_cost.hpp
-- Installing: /usr/include/opencv2/shape/emdL1.hpp
-- Installing: /usr/include/opencv2/shape/shape_transformer.hpp
-- Installing: /usr/include/opencv2/shape/shape.hpp
-- Installing: /usr/bin/opencv_test_shape
-- Set runtime path of "/usr/bin/opencv_test_shape" to "/usr/lib:/usr/local/cuda-8.0/lib64"
-- Installing: /usr/lib/libopencv_videoio.so.3.3.0
-- Installing: /usr/lib/libopencv_videoio.so.3.3
-- Set runtime path of "/usr/lib/libopencv_videoio.so.3.3.0" to "/usr/lib:/usr/local/cuda-8.0/lib64"
-- Installing: /usr/lib/libopencv_videoio.so
-- Installing: /usr/include/opencv2/videoio.hpp
-- Installing: /usr/include/opencv2/videoio/videoio.hpp
-- Installing: /usr/include/opencv2/videoio/videoio_c.h
-- Installing: /usr/include/opencv2/videoio/cap_ios.h
-- Installing: /usr/bin/opencv_test_videoio
-- Set runtime path of "/usr/bin/opencv_test_videoio" to "/usr/lib:/usr/local/cuda-8.0/lib64"
-- Installing: /usr/bin/opencv_perf_videoio
-- Set runtime path of "/usr/bin/opencv_perf_videoio" to "/usr/lib:/usr/local/cuda-8.0/lib64"
-- Installing: /usr/lib/libopencv_cudacodec.so.3.3.0
-- Installing: /usr/lib/libopencv_cudacodec.so.3.3
-- Set runtime path of "/usr/lib/libopencv_cudacodec.so.3.3.0" to "/usr/lib:/usr/local/cuda-8.0/lib64"
-- Installing: /usr/lib/libopencv_cudacodec.so
-- Installing: /usr/include/opencv2/cudacodec.hpp
-- Installing: /usr/bin/opencv_test_cudacodec
-- Set runtime path of "/usr/bin/opencv_test_cudacodec" to "/usr/lib:/usr/local/cuda-8.0/lib64"
-- Installing: /usr/bin/opencv_perf_cudacodec
-- Set runtime path of "/usr/bin/opencv_perf_cudacodec" to "/usr/lib:/usr/local/cuda-8.0/lib64"
-- Installing: /usr/lib/libopencv_highgui.so.3.3.0
-- Installing: /usr/lib/libopencv_highgui.so.3.3
-- Set runtime path of "/usr/lib/libopencv_highgui.so.3.3.0" to "/usr/lib:/usr/local/cuda-8.0/lib64"
-- Installing: /usr/lib/libopencv_highgui.so
-- Installing: /usr/include/opencv2/highgui.hpp
-- Installing: /usr/include/opencv2/highgui/highgui.hpp
-- Installing: /usr/include/opencv2/highgui/highgui_c.h
-- Installing: /usr/bin/opencv_test_highgui
-- Set runtime path of "/usr/bin/opencv_test_highgui" to "/usr/lib:/usr/local/cuda-8.0/lib64"
-- Installing: /usr/lib/libopencv_features2d.so.3.3.0
-- Installing: /usr/lib/libopencv_features2d.so.3.3
-- Set runtime path of "/usr/lib/libopencv_features2d.so.3.3.0" to "/usr/lib:/usr/local/cuda-8.0/lib64"
-- Installing: /usr/lib/libopencv_features2d.so
-- Installing: /usr/include/opencv2/features2d.hpp
-- Installing: /usr/include/opencv2/features2d/features2d.hpp
-- Installing: /usr/bin/opencv_test_features2d
-- Set runtime path of "/usr/bin/opencv_test_features2d" to "/usr/lib:/usr/local/cuda-8.0/lib64"
-- Installing: /usr/bin/opencv_perf_features2d
-- Set runtime path of "/usr/bin/opencv_perf_features2d" to "/usr/lib:/usr/local/cuda-8.0/lib64"
-- Installing: /usr/lib/libopencv_calib3d.so.3.3.0
-- Installing: /usr/lib/libopencv_calib3d.so.3.3
-- Set runtime path of "/usr/lib/libopencv_calib3d.so.3.3.0" to "/usr/lib:/usr/local/cuda-8.0/lib64"
-- Installing: /usr/lib/libopencv_calib3d.so
-- Installing: /usr/include/opencv2/calib3d.hpp
-- Installing: /usr/include/opencv2/calib3d/calib3d.hpp
-- Installing: /usr/include/opencv2/calib3d/calib3d_c.h
-- Installing: /usr/bin/opencv_test_calib3d
-- Set runtime path of "/usr/bin/opencv_test_calib3d" to "/usr/lib:/usr/local/cuda-8.0/lib64"
-- Installing: /usr/bin/opencv_perf_calib3d
-- Set runtime path of "/usr/bin/opencv_perf_calib3d" to "/usr/lib:/usr/local/cuda-8.0/lib64"
-- Installing: /usr/lib/libopencv_cudafeatures2d.so.3.3.0
-- Installing: /usr/lib/libopencv_cudafeatures2d.so.3.3
-- Set runtime path of "/usr/lib/libopencv_cudafeatures2d.so.3.3.0" to "/usr/lib:/usr/local/cuda-8.0/lib64"
-- Installing: /usr/lib/libopencv_cudafeatures2d.so
-- Installing: /usr/include/opencv2/cudafeatures2d.hpp
-- Installing: /usr/bin/opencv_test_cudafeatures2d
-- Set runtime path of "/usr/bin/opencv_test_cudafeatures2d" to "/usr/lib:/usr/local/cuda-8.0/lib64"
-- Installing: /usr/bin/opencv_perf_cudafeatures2d
-- Set runtime path of "/usr/bin/opencv_perf_cudafeatures2d" to "/usr/lib:/usr/local/cuda-8.0/lib64"
-- Installing: /usr/lib/libopencv_cudalegacy.so.3.3.0
-- Installing: /usr/lib/libopencv_cudalegacy.so.3.3
-- Set runtime path of "/usr/lib/libopencv_cudalegacy.so.3.3.0" to "/usr/lib:/usr/local/cuda-8.0/lib64"
-- Installing: /usr/lib/libopencv_cudalegacy.so
-- Installing: /usr/include/opencv2/cudalegacy.hpp
-- Installing: /usr/include/opencv2/cudalegacy/NCV.hpp
-- Installing: /usr/include/opencv2/cudalegacy/NCVBroxOpticalFlow.hpp
-- Installing: /usr/include/opencv2/cudalegacy/NPP_staging.hpp
-- Installing: /usr/include/opencv2/cudalegacy/NCVHaarObjectDetection.hpp
-- Installing: /usr/include/opencv2/cudalegacy/NCVPyramid.hpp
-- Installing: /usr/bin/opencv_test_cudalegacy
-- Set runtime path of "/usr/bin/opencv_test_cudalegacy" to "/usr/lib:/usr/local/cuda-8.0/lib64"
-- Installing: /usr/bin/opencv_perf_cudalegacy
-- Set runtime path of "/usr/bin/opencv_perf_cudalegacy" to "/usr/lib:/usr/local/cuda-8.0/lib64"
-- Installing: /usr/lib/libopencv_cudaobjdetect.so.3.3.0
-- Installing: /usr/lib/libopencv_cudaobjdetect.so.3.3
-- Set runtime path of "/usr/lib/libopencv_cudaobjdetect.so.3.3.0" to "/usr/lib:/usr/local/cuda-8.0/lib64"
-- Installing: /usr/lib/libopencv_cudaobjdetect.so
-- Installing: /usr/include/opencv2/cudaobjdetect.hpp
-- Installing: /usr/bin/opencv_test_cudaobjdetect
-- Set runtime path of "/usr/bin/opencv_test_cudaobjdetect" to "/usr/lib:/usr/local/cuda-8.0/lib64"
-- Installing: /usr/bin/opencv_perf_cudaobjdetect
-- Set runtime path of "/usr/bin/opencv_perf_cudaobjdetect" to "/usr/lib:/usr/local/cuda-8.0/lib64"
-- Installing: /usr/lib/libopencv_cudaoptflow.so.3.3.0
-- Installing: /usr/lib/libopencv_cudaoptflow.so.3.3
-- Set runtime path of "/usr/lib/libopencv_cudaoptflow.so.3.3.0" to "/usr/lib:/usr/local/cuda-8.0/lib64"
-- Installing: /usr/lib/libopencv_cudaoptflow.so
-- Installing: /usr/include/opencv2/cudaoptflow.hpp
-- Installing: /usr/bin/opencv_test_cudaoptflow
-- Set runtime path of "/usr/bin/opencv_test_cudaoptflow" to "/usr/lib:/usr/local/cuda-8.0/lib64"
-- Installing: /usr/bin/opencv_perf_cudaoptflow
-- Set runtime path of "/usr/bin/opencv_perf_cudaoptflow" to "/usr/lib:/usr/local/cuda-8.0/lib64"
-- Installing: /usr/lib/libopencv_cudastereo.so.3.3.0
-- Installing: /usr/lib/libopencv_cudastereo.so.3.3
-- Set runtime path of "/usr/lib/libopencv_cudastereo.so.3.3.0" to "/usr/lib:/usr/local/cuda-8.0/lib64"
-- Installing: /usr/lib/libopencv_cudastereo.so
-- Installing: /usr/include/opencv2/cudastereo.hpp
-- Installing: /usr/bin/opencv_test_cudastereo
-- Set runtime path of "/usr/bin/opencv_test_cudastereo" to "/usr/lib:/usr/local/cuda-8.0/lib64"
-- Installing: /usr/bin/opencv_perf_cudastereo
-- Set runtime path of "/usr/bin/opencv_perf_cudastereo" to "/usr/lib:/usr/local/cuda-8.0/lib64"
-- Installing: /usr/lib/libopencv_stitching.so.3.3.0
-- Installing: /usr/lib/libopencv_stitching.so.3.3
-- Set runtime path of "/usr/lib/libopencv_stitching.so.3.3.0" to "/usr/lib:/usr/local/cuda-8.0/lib64"
-- Installing: /usr/lib/libopencv_stitching.so
-- Installing: /usr/include/opencv2/stitching.hpp
-- Installing: /usr/include/opencv2/stitching/warpers.hpp
-- Installing: /usr/include/opencv2/stitching/detail/seam_finders.hpp
-- Installing: /usr/include/opencv2/stitching/detail/util_inl.hpp
-- Installing: /usr/include/opencv2/stitching/detail/camera.hpp
-- Installing: /usr/include/opencv2/stitching/detail/warpers_inl.hpp
-- Installing: /usr/include/opencv2/stitching/detail/blenders.hpp
-- Installing: /usr/include/opencv2/stitching/detail/exposure_compensate.hpp
-- Installing: /usr/include/opencv2/stitching/detail/warpers.hpp
-- Installing: /usr/include/opencv2/stitching/detail/util.hpp
-- Installing: /usr/include/opencv2/stitching/detail/matchers.hpp
-- Installing: /usr/include/opencv2/stitching/detail/motion_estimators.hpp
-- Installing: /usr/include/opencv2/stitching/detail/autocalib.hpp
-- Installing: /usr/include/opencv2/stitching/detail/timelapsers.hpp
-- Installing: /usr/bin/opencv_test_stitching
-- Set runtime path of "/usr/bin/opencv_test_stitching" to "/usr/lib:/usr/local/cuda-8.0/lib64"
-- Installing: /usr/bin/opencv_perf_stitching
-- Set runtime path of "/usr/bin/opencv_perf_stitching" to "/usr/lib:/usr/local/cuda-8.0/lib64"
-- Installing: /usr/lib/libopencv_superres.so.3.3.0
-- Installing: /usr/lib/libopencv_superres.so.3.3
-- Set runtime path of "/usr/lib/libopencv_superres.so.3.3.0" to "/usr/lib:/usr/local/cuda-8.0/lib64"
-- Installing: /usr/lib/libopencv_superres.so
-- Installing: /usr/include/opencv2/superres.hpp
-- Installing: /usr/include/opencv2/superres/optical_flow.hpp
-- Installing: /usr/bin/opencv_test_superres
-- Set runtime path of "/usr/bin/opencv_test_superres" to "/usr/lib:/usr/local/cuda-8.0/lib64"
-- Installing: /usr/bin/opencv_perf_superres
-- Set runtime path of "/usr/bin/opencv_perf_superres" to "/usr/lib:/usr/local/cuda-8.0/lib64"
-- Installing: /usr/lib/libopencv_videostab.so.3.3.0
-- Installing: /usr/lib/libopencv_videostab.so.3.3
-- Set runtime path of "/usr/lib/libopencv_videostab.so.3.3.0" to "/usr/lib:/usr/local/cuda-8.0/lib64"
-- Installing: /usr/lib/libopencv_videostab.so
-- Installing: /usr/include/opencv2/videostab.hpp
-- Installing: /usr/include/opencv2/videostab/inpainting.hpp
-- Installing: /usr/include/opencv2/videostab/ring_buffer.hpp
-- Installing: /usr/include/opencv2/videostab/log.hpp
-- Installing: /usr/include/opencv2/videostab/deblurring.hpp
-- Installing: /usr/include/opencv2/videostab/optical_flow.hpp
-- Installing: /usr/include/opencv2/videostab/frame_source.hpp
-- Installing: /usr/include/opencv2/videostab/fast_marching_inl.hpp
-- Installing: /usr/include/opencv2/videostab/motion_core.hpp
-- Installing: /usr/include/opencv2/videostab/global_motion.hpp
-- Installing: /usr/include/opencv2/videostab/wobble_suppression.hpp
-- Installing: /usr/include/opencv2/videostab/motion_stabilizing.hpp
-- Installing: /usr/include/opencv2/videostab/stabilizer.hpp
-- Installing: /usr/include/opencv2/videostab/fast_marching.hpp
-- Installing: /usr/include/opencv2/videostab/outlier_rejection.hpp
-- Installing: /usr/bin/opencv_test_videostab
-- Set runtime path of "/usr/bin/opencv_test_videostab" to "/usr/lib:/usr/local/cuda-8.0/lib64"
-- Installing: /usr/lib/python2.7/dist-packages/cv2.so
-- Set runtime path of "/usr/lib/python2.7/dist-packages/cv2.so" to "/usr/lib:/usr/local/cuda-8.0/lib64"
-- Installing: /usr/lib/python3.5/dist-packages/cv2.cpython-35m-aarch64-linux-gnu.so
-- Set runtime path of "/usr/lib/python3.5/dist-packages/cv2.cpython-35m-aarch64-linux-gnu.so" to "/usr/lib:/usr/local/cuda-8.0/lib64"
-- Installing: /usr/share/OpenCV/haarcascades/haarcascade_frontalcatface_extended.xml
-- Installing: /usr/share/OpenCV/haarcascades/haarcascade_smile.xml
-- Installing: /usr/share/OpenCV/haarcascades/haarcascade_lowerbody.xml
-- Installing: /usr/share/OpenCV/haarcascades/haarcascade_eye_tree_eyeglasses.xml
-- Installing: /usr/share/OpenCV/haarcascades/haarcascade_fullbody.xml
-- Installing: /usr/share/OpenCV/haarcascades/haarcascade_frontalface_alt_tree.xml
-- Installing: /usr/share/OpenCV/haarcascades/haarcascade_righteye_2splits.xml
-- Installing: /usr/share/OpenCV/haarcascades/haarcascade_frontalface_default.xml
-- Installing: /usr/share/OpenCV/haarcascades/haarcascade_eye.xml
-- Installing: /usr/share/OpenCV/haarcascades/haarcascade_lefteye_2splits.xml
-- Installing: /usr/share/OpenCV/haarcascades/haarcascade_frontalcatface.xml
-- Installing: /usr/share/OpenCV/haarcascades/haarcascade_upperbody.xml
-- Installing: /usr/share/OpenCV/haarcascades/haarcascade_russian_plate_number.xml
-- Installing: /usr/share/OpenCV/haarcascades/haarcascade_frontalface_alt.xml
-- Installing: /usr/share/OpenCV/haarcascades/haarcascade_licence_plate_rus_16stages.xml
-- Installing: /usr/share/OpenCV/haarcascades/haarcascade_frontalface_alt2.xml
-- Installing: /usr/share/OpenCV/haarcascades/haarcascade_profileface.xml
-- Installing: /usr/share/OpenCV/lbpcascades/lbpcascade_profileface.xml
-- Installing: /usr/share/OpenCV/lbpcascades/lbpcascade_frontalface.xml
-- Installing: /usr/share/OpenCV/lbpcascades/lbpcascade_frontalcatface.xml
-- Installing: /usr/share/OpenCV/lbpcascades/lbpcascade_frontalface_improved.xml
-- Installing: /usr/share/OpenCV/lbpcascades/lbpcascade_silverware.xml
-- Installing: /usr/share/OpenCV/testdata
-- Installing: /usr/share/OpenCV/testdata/highgui
-- Installing: /usr/share/OpenCV/testdata/highgui/readwrite
-- Installing: /usr/share/OpenCV/testdata/highgui/readwrite/test_4_c3.png
-- Installing: /usr/share/OpenCV/testdata/highgui/readwrite/test_5_c3.jpg
-- Installing: /usr/share/OpenCV/testdata/highgui/readwrite/uint16-mono2.dcm
-- Installing: /usr/share/OpenCV/testdata/highgui/readwrite/test_3_c1.png
-- Installing: /usr/share/OpenCV/testdata/highgui/readwrite/test_1_c1.png
-- Installing: /usr/share/OpenCV/testdata/highgui/readwrite/ordinary.bmp
-- Installing: /usr/share/OpenCV/testdata/highgui/readwrite/multipage_p1.tif
-- Installing: /usr/share/OpenCV/testdata/highgui/readwrite/test_5_c1.png
-- Installing: /usr/share/OpenCV/testdata/highgui/readwrite/Bretagne2.jp2
-- Installing: /usr/share/OpenCV/testdata/highgui/readwrite/testExifOrientation_6.jpg
-- Installing: /usr/share/OpenCV/testdata/highgui/readwrite/uint8-rgb.dcm
-- Installing: /usr/share/OpenCV/testdata/highgui/readwrite/tiled_16.tif
-- Installing: /usr/share/OpenCV/testdata/highgui/readwrite/Rome.jp2
-- Installing: /usr/share/OpenCV/testdata/highgui/readwrite/test_5_c1.jpg
-- Installing: /usr/share/OpenCV/testdata/highgui/readwrite/multipage_p3.tif
-- Installing: /usr/share/OpenCV/testdata/highgui/readwrite/testExifOrientation_5.jpg
-- Installing: /usr/share/OpenCV/testdata/highgui/readwrite/multipage.tif
-- Installing: /usr/share/OpenCV/testdata/highgui/readwrite/test_2_c1.jpg
-- Installing: /usr/share/OpenCV/testdata/highgui/readwrite/testExifOrientation_8.jpg
-- Installing: /usr/share/OpenCV/testdata/highgui/readwrite/test_3_c3.jpg
-- Installing: /usr/share/OpenCV/testdata/highgui/readwrite/color_palette_alpha.png
-- Installing: /usr/share/OpenCV/testdata/highgui/readwrite/int16-mono1.dcm
-- Installing: /usr/share/OpenCV/testdata/highgui/readwrite/test_2_c3.jpg
-- Installing: /usr/share/OpenCV/testdata/highgui/readwrite/test_3_c3.png
-- Installing: /usr/share/OpenCV/testdata/highgui/readwrite/multipage_p5.tif
-- Installing: /usr/share/OpenCV/testdata/highgui/readwrite/multipage_p6.tif
-- Installing: /usr/share/OpenCV/testdata/highgui/readwrite/uint8-mono2.dcm
-- Installing: /usr/share/OpenCV/testdata/highgui/readwrite/test_3_c1.jpg
-- Installing: /usr/share/OpenCV/testdata/highgui/readwrite/testExifOrientation_2.jpg
-- Installing: /usr/share/OpenCV/testdata/highgui/readwrite/color_palette_no_alpha.png
-- Installing: /usr/share/OpenCV/testdata/highgui/readwrite/test_1_c1.jpg
-- Installing: /usr/share/OpenCV/testdata/highgui/readwrite/tiled_8.tif
-- Installing: /usr/share/OpenCV/testdata/highgui/readwrite/rle8.bmp
-- Installing: /usr/share/OpenCV/testdata/highgui/readwrite/multipage_p2.tif
-- Installing: /usr/share/OpenCV/testdata/highgui/readwrite/test_5_c3.png
-- Installing: /usr/share/OpenCV/testdata/highgui/readwrite/test_2_c3.png
-- Installing: /usr/share/OpenCV/testdata/highgui/readwrite/testExifOrientation_7.jpg
-- Installing: /usr/share/OpenCV/testdata/highgui/readwrite/multipage_p4.tif
-- Installing: /usr/share/OpenCV/testdata/highgui/readwrite/rle.hdr
-- Installing: /usr/share/OpenCV/testdata/highgui/readwrite/test_4_c1.jpg
-- Installing: /usr/share/OpenCV/testdata/highgui/readwrite/test_4_c3.jpg
-- Installing: /usr/share/OpenCV/testdata/highgui/readwrite/testExifOrientation_3.jpg
-- Installing: /usr/share/OpenCV/testdata/highgui/readwrite/read.png
-- Installing: /usr/share/OpenCV/testdata/highgui/readwrite/non_tiled.tif
-- Installing: /usr/share/OpenCV/testdata/highgui/readwrite/test_2_c1.png
-- Installing: /usr/share/OpenCV/testdata/highgui/readwrite/test_1_c3.png
-- Installing: /usr/share/OpenCV/testdata/highgui/readwrite/testExifOrientation_1.jpg
-- Installing: /usr/share/OpenCV/testdata/highgui/readwrite/lena.pam
-- Installing: /usr/share/OpenCV/testdata/highgui/readwrite/Grey.jp2
-- Installing: /usr/share/OpenCV/testdata/highgui/readwrite/testExifOrientation_4.jpg
-- Installing: /usr/share/OpenCV/testdata/highgui/readwrite/test_4_c1.png
-- Installing: /usr/share/OpenCV/testdata/highgui/readwrite/no_rle.hdr
-- Installing: /usr/share/OpenCV/testdata/highgui/readwrite/test_1_c3.jpg
-- Installing: /usr/share/OpenCV/testdata/highgui/drawing
-- Installing: /usr/share/OpenCV/testdata/highgui/drawing/image.png
-- Installing: /usr/share/OpenCV/testdata/highgui/video
-- Installing: /usr/share/OpenCV/testdata/highgui/video/sample_sorenson.avi
-- Installing: /usr/share/OpenCV/testdata/highgui/video/big_buck_bunny.avi
-- Installing: /usr/share/OpenCV/testdata/highgui/video/VID00003-20100701-2204.mpg
-- Installing: /usr/share/OpenCV/testdata/highgui/video/sample_sorenson.mov
-- Installing: /usr/share/OpenCV/testdata/highgui/video/sample_sorenson.wmv
-- Installing: /usr/share/OpenCV/testdata/highgui/video/VID00003-20100701-2204.avi
-- Installing: /usr/share/OpenCV/testdata/highgui/video/big_buck_bunny.mov
-- Installing: /usr/share/OpenCV/testdata/highgui/video/big_buck_bunny.mjpg.avi
-- Installing: /usr/share/OpenCV/testdata/highgui/video/VID00003-20100701-2204.3GP
-- Installing: /usr/share/OpenCV/testdata/highgui/video/big_buck_bunny.wmv
-- Installing: /usr/share/OpenCV/testdata/highgui/video/big_buck_bunny.mpg
-- Installing: /usr/share/OpenCV/testdata/highgui/video/big_buck_bunny.mp4
-- Installing: /usr/share/OpenCV/testdata/highgui/video/VID00003-20100701-2204.wmv
-- Installing: /usr/share/OpenCV/testdata/perf
-- Installing: /usr/share/OpenCV/testdata/perf/cudafilters.xml
-- Installing: /usr/share/OpenCV/testdata/perf/highgui.xml
-- Installing: /usr/share/OpenCV/testdata/perf/clean_unused.py
-- Installing: /usr/share/OpenCV/testdata/perf/tracking.xml
-- Installing: /usr/share/OpenCV/testdata/perf/320x260.png
-- Installing: /usr/share/OpenCV/testdata/perf/cudawarping.xml
-- Installing: /usr/share/OpenCV/testdata/perf/1920x1080.png
-- Installing: /usr/share/OpenCV/testdata/perf/xphoto.xml
-- Installing: /usr/share/OpenCV/testdata/perf/photo.xml
-- Installing: /usr/share/OpenCV/testdata/perf/clean_regex.py
-- Installing: /usr/share/OpenCV/testdata/perf/objdetect.xml
-- Installing: /usr/share/OpenCV/testdata/perf/cudastereo.xml
-- Installing: /usr/share/OpenCV/testdata/perf/cudaarithm.xml
-- Installing: /usr/share/OpenCV/testdata/perf/cudaimgproc.xml
-- Installing: /usr/share/OpenCV/testdata/perf/append.py
-- Installing: /usr/share/OpenCV/testdata/perf/cudaoptflow.xml
-- Installing: /usr/share/OpenCV/testdata/perf/640x512.png
-- Installing: /usr/share/OpenCV/testdata/perf/cudaobjdetect.xml
-- Installing: /usr/share/OpenCV/testdata/perf/cudalegacy.xml
-- Installing: /usr/share/OpenCV/testdata/perf/imgproc.xml
-- Installing: /usr/share/OpenCV/testdata/perf/features2d.xml
-- Installing: /usr/share/OpenCV/testdata/perf/1280x1024.png
-- Installing: /usr/share/OpenCV/testdata/perf/nonfree.xml
-- Installing: /usr/share/OpenCV/testdata/perf/stitching.xml
-- Installing: /usr/share/OpenCV/testdata/perf/superres.xml
-- Installing: /usr/share/OpenCV/testdata/perf/xfeatures2d.xml
-- Installing: /usr/share/OpenCV/testdata/perf/core.xml
-- Installing: /usr/share/OpenCV/testdata/perf/video.xml
-- Installing: /usr/share/OpenCV/testdata/perf/400x320.png
-- Installing: /usr/share/OpenCV/testdata/perf/videoio.xml
-- Installing: /usr/share/OpenCV/testdata/perf/calib3d.xml
-- Installing: /usr/share/OpenCV/testdata/perf/1680x1050.png
-- Installing: /usr/share/OpenCV/testdata/perf/cudafeatures2d.xml
-- Installing: /usr/share/OpenCV/testdata/perf/cudacodec.xml
-- Installing: /usr/share/OpenCV/testdata/perf/800x600.png
-- Installing: /usr/share/OpenCV/testdata/perf/512x512.png
-- Installing: /usr/share/OpenCV/testdata/perf/video
-- Installing: /usr/share/OpenCV/testdata/perf/video/048.png
-- Installing: /usr/share/OpenCV/testdata/perf/video/006.png
-- Installing: /usr/share/OpenCV/testdata/perf/video/022.png
-- Installing: /usr/share/OpenCV/testdata/perf/video/025.png
-- Installing: /usr/share/OpenCV/testdata/perf/video/027.png
-- Installing: /usr/share/OpenCV/testdata/perf/video/026.png
-- Installing: /usr/share/OpenCV/testdata/perf/video/084.png
-- Installing: /usr/share/OpenCV/testdata/perf/video/087.png
-- Installing: /usr/share/OpenCV/testdata/perf/video/108.png
-- Installing: /usr/share/OpenCV/testdata/perf/video/038.png
-- Installing: /usr/share/OpenCV/testdata/perf/video/120.png
-- Installing: /usr/share/OpenCV/testdata/perf/video/053.png
-- Installing: /usr/share/OpenCV/testdata/perf/video/037.png
-- Installing: /usr/share/OpenCV/testdata/perf/video/043.png
-- Installing: /usr/share/OpenCV/testdata/perf/video/070.png
-- Installing: /usr/share/OpenCV/testdata/perf/video/102.png
-- Installing: /usr/share/OpenCV/testdata/perf/video/121.png
-- Installing: /usr/share/OpenCV/testdata/perf/video/107.png
-- Installing: /usr/share/OpenCV/testdata/perf/video/096.png
-- Installing: /usr/share/OpenCV/testdata/perf/video/050.png
-- Installing: /usr/share/OpenCV/testdata/perf/video/079.png
-- Installing: /usr/share/OpenCV/testdata/perf/video/005.png
-- Installing: /usr/share/OpenCV/testdata/perf/video/049.png
-- Installing: /usr/share/OpenCV/testdata/perf/video/101.png
-- Installing: /usr/share/OpenCV/testdata/perf/video/075.png
-- Installing: /usr/share/OpenCV/testdata/perf/video/031.png
-- Installing: /usr/share/OpenCV/testdata/perf/video/big_buck_bunny.avi
-- Installing: /usr/share/OpenCV/testdata/perf/video/100.png
-- Installing: /usr/share/OpenCV/testdata/perf/video/078.png
-- Installing: /usr/share/OpenCV/testdata/perf/video/000.png
-- Installing: /usr/share/OpenCV/testdata/perf/video/083.png
-- Installing: /usr/share/OpenCV/testdata/perf/video/007.png
-- Installing: /usr/share/OpenCV/testdata/perf/video/036.png
-- Installing: /usr/share/OpenCV/testdata/perf/video/063.png
-- Installing: /usr/share/OpenCV/testdata/perf/video/113.png
-- Installing: /usr/share/OpenCV/testdata/perf/video/023.png
-- Installing: /usr/share/OpenCV/testdata/perf/video/095.png
-- Installing: /usr/share/OpenCV/testdata/perf/video/119.png
-- Installing: /usr/share/OpenCV/testdata/perf/video/097.png
-- Installing: /usr/share/OpenCV/testdata/perf/video/072.png
-- Installing: /usr/share/OpenCV/testdata/perf/video/021.png
-- Installing: /usr/share/OpenCV/testdata/perf/video/110.png
-- Installing: /usr/share/OpenCV/testdata/perf/video/034.png
-- Installing: /usr/share/OpenCV/testdata/perf/video/012.png
-- Installing: /usr/share/OpenCV/testdata/perf/video/060.png
-- Installing: /usr/share/OpenCV/testdata/perf/video/124.png
-- Installing: /usr/share/OpenCV/testdata/perf/video/015.png
-- Installing: /usr/share/OpenCV/testdata/perf/video/010.png
-- Installing: /usr/share/OpenCV/testdata/perf/video/058.png
-- Installing: /usr/share/OpenCV/testdata/perf/video/059.png
-- Installing: /usr/share/OpenCV/testdata/perf/video/028.png
-- Installing: /usr/share/OpenCV/testdata/perf/video/045.png
-- Installing: /usr/share/OpenCV/testdata/perf/video/035.png
-- Installing: /usr/share/OpenCV/testdata/perf/video/112.png
-- Installing: /usr/share/OpenCV/testdata/perf/video/040.png
-- Installing: /usr/share/OpenCV/testdata/perf/video/041.png
-- Installing: /usr/share/OpenCV/testdata/perf/video/105.png
-- Installing: /usr/share/OpenCV/testdata/perf/video/115.png
-- Installing: /usr/share/OpenCV/testdata/perf/video/047.png
-- Installing: /usr/share/OpenCV/testdata/perf/video/052.png
-- Installing: /usr/share/OpenCV/testdata/perf/video/039.png
-- Installing: /usr/share/OpenCV/testdata/perf/video/116.png
-- Installing: /usr/share/OpenCV/testdata/perf/video/019.png
-- Installing: /usr/share/OpenCV/testdata/perf/video/057.png
-- Installing: /usr/share/OpenCV/testdata/perf/video/082.png
-- Installing: /usr/share/OpenCV/testdata/perf/video/104.png
-- Installing: /usr/share/OpenCV/testdata/perf/video/103.png
-- Installing: /usr/share/OpenCV/testdata/perf/video/055.png
-- Installing: /usr/share/OpenCV/testdata/perf/video/106.png
-- Installing: /usr/share/OpenCV/testdata/perf/video/093.png
-- Installing: /usr/share/OpenCV/testdata/perf/video/011.png
-- Installing: /usr/share/OpenCV/testdata/perf/video/046.png
-- Installing: /usr/share/OpenCV/testdata/perf/video/051.png
-- Installing: /usr/share/OpenCV/testdata/perf/video/081.png
-- Installing: /usr/share/OpenCV/testdata/perf/video/042.png
-- Installing: /usr/share/OpenCV/testdata/perf/video/077.png
-- Installing: /usr/share/OpenCV/testdata/perf/video/089.png
-- Installing: /usr/share/OpenCV/testdata/perf/video/122.png
-- Installing: /usr/share/OpenCV/testdata/perf/video/062.png
-- Installing: /usr/share/OpenCV/testdata/perf/video/054.png
-- Installing: /usr/share/OpenCV/testdata/perf/video/020.png
-- Installing: /usr/share/OpenCV/testdata/perf/video/009.png
-- Installing: /usr/share/OpenCV/testdata/perf/video/003.png
-- Installing: /usr/share/OpenCV/testdata/perf/video/068.png
-- Installing: /usr/share/OpenCV/testdata/perf/video/086.png
-- Installing: /usr/share/OpenCV/testdata/perf/video/080.png
-- Installing: /usr/share/OpenCV/testdata/perf/video/073.png
-- Installing: /usr/share/OpenCV/testdata/perf/video/044.png
-- Installing: /usr/share/OpenCV/testdata/perf/video/014.png
-- Installing: /usr/share/OpenCV/testdata/perf/video/099.png
-- Installing: /usr/share/OpenCV/testdata/perf/video/117.png
-- Installing: /usr/share/OpenCV/testdata/perf/video/001.png
-- Installing: /usr/share/OpenCV/testdata/perf/video/092.png
-- Installing: /usr/share/OpenCV/testdata/perf/video/024.png
-- Installing: /usr/share/OpenCV/testdata/perf/video/016.png
-- Installing: /usr/share/OpenCV/testdata/perf/video/094.png
-- Installing: /usr/share/OpenCV/testdata/perf/video/118.png
-- Installing: /usr/share/OpenCV/testdata/perf/video/076.png
-- Installing: /usr/share/OpenCV/testdata/perf/video/004.png
-- Installing: /usr/share/OpenCV/testdata/perf/video/013.png
-- Installing: /usr/share/OpenCV/testdata/perf/video/018.png
-- Installing: /usr/share/OpenCV/testdata/perf/video/030.png
-- Installing: /usr/share/OpenCV/testdata/perf/video/032.png
-- Installing: /usr/share/OpenCV/testdata/perf/video/056.png
-- Installing: /usr/share/OpenCV/testdata/perf/video/111.png
-- Installing: /usr/share/OpenCV/testdata/perf/video/071.png
-- Installing: /usr/share/OpenCV/testdata/perf/video/114.png
-- Installing: /usr/share/OpenCV/testdata/perf/video/091.png
-- Installing: /usr/share/OpenCV/testdata/perf/video/002.png
-- Installing: /usr/share/OpenCV/testdata/perf/video/098.png
-- Installing: /usr/share/OpenCV/testdata/perf/video/088.png
-- Installing: /usr/share/OpenCV/testdata/perf/video/090.png
-- Installing: /usr/share/OpenCV/testdata/perf/video/123.png
-- Installing: /usr/share/OpenCV/testdata/perf/video/064.png
-- Installing: /usr/share/OpenCV/testdata/perf/video/061.png
-- Installing: /usr/share/OpenCV/testdata/perf/video/029.png
-- Installing: /usr/share/OpenCV/testdata/perf/video/109.png
-- Installing: /usr/share/OpenCV/testdata/perf/video/065.png
-- Installing: /usr/share/OpenCV/testdata/perf/video/033.png
-- Installing: /usr/share/OpenCV/testdata/perf/video/017.png
-- Installing: /usr/share/OpenCV/testdata/perf/video/085.png
-- Installing: /usr/share/OpenCV/testdata/perf/video/008.png
-- Installing: /usr/share/OpenCV/testdata/perf/video/067.png
-- Installing: /usr/share/OpenCV/testdata/perf/video/066.png
-- Installing: /usr/share/OpenCV/testdata/perf/video/074.png
-- Installing: /usr/share/OpenCV/testdata/perf/video/069.png
-- Installing: /usr/share/OpenCV/testdata/perf/2560x1600.png
-- Installing: /usr/share/OpenCV/testdata/perf/cudabgsegm.xml
-- Installing: /usr/share/OpenCV/testdata/gpu
-- Installing: /usr/share/OpenCV/testdata/gpu/lbpcascade
-- Installing: /usr/share/OpenCV/testdata/gpu/lbpcascade/er.png
-- Installing: /usr/share/OpenCV/testdata/gpu/lbpcascade/lbpcascade_frontalface.xml
-- Installing: /usr/share/OpenCV/testdata/gpu/perf
-- Installing: /usr/share/OpenCV/testdata/gpu/perf/aloe.png
-- Installing: /usr/share/OpenCV/testdata/gpu/perf/haarcascade_frontalface_alt.xml
-- Installing: /usr/share/OpenCV/testdata/gpu/perf/aloeR.png
-- Installing: /usr/share/OpenCV/testdata/gpu/csstereobp
-- Installing: /usr/share/OpenCV/testdata/gpu/csstereobp/aloe-R.png
-- Installing: /usr/share/OpenCV/testdata/gpu/csstereobp/aloe-disp_CC1X.png
-- Installing: /usr/share/OpenCV/testdata/gpu/csstereobp/aloe-disp.png
-- Installing: /usr/share/OpenCV/testdata/gpu/csstereobp/aloe-L.png
-- Installing: /usr/share/OpenCV/testdata/gpu/opticalflow
-- Installing: /usr/share/OpenCV/testdata/gpu/opticalflow/rubberwhale2.png
-- Installing: /usr/share/OpenCV/testdata/gpu/opticalflow/rubberwhale1.png
-- Installing: /usr/share/OpenCV/testdata/gpu/opticalflow/brox_optical_flow.bin
-- Installing: /usr/share/OpenCV/testdata/gpu/opticalflow/frame0.png
-- Installing: /usr/share/OpenCV/testdata/gpu/opticalflow/frame1.png
-- Installing: /usr/share/OpenCV/testdata/gpu/opticalflow/brox_optical_flow_cc20.bin
-- Installing: /usr/share/OpenCV/testdata/gpu/denoising
-- Installing: /usr/share/OpenCV/testdata/gpu/denoising/nlm_denoised_lena_bgr.png
-- Installing: /usr/share/OpenCV/testdata/gpu/denoising/nlm_denoised_lena_gray.png
-- Installing: /usr/share/OpenCV/testdata/gpu/denoising/fnlm_denoised_lena_gray.png
-- Installing: /usr/share/OpenCV/testdata/gpu/denoising/fnlm_denoised_lena_bgr.png
-- Installing: /usr/share/OpenCV/testdata/gpu/denoising/lena_noised_gaussian_sigma=20_multi_0.png
-- Installing: /usr/share/OpenCV/testdata/gpu/caltech
-- Installing: /usr/share/OpenCV/testdata/gpu/caltech/image_00000527_0.png
-- Installing: /usr/share/OpenCV/testdata/gpu/caltech/image_00000469_0.png
-- Installing: /usr/share/OpenCV/testdata/gpu/caltech/image_00000574_0.png
-- Installing: /usr/share/OpenCV/testdata/gpu/caltech/image_00000032_0.png
-- Installing: /usr/share/OpenCV/testdata/gpu/caltech/image_00000165_0.png
-- Installing: /usr/share/OpenCV/testdata/gpu/caltech/image_00000261_0.png
-- Installing: /usr/share/OpenCV/testdata/gpu/caltech/image_00000009_0.png
-- Installing: /usr/share/OpenCV/testdata/gpu/labeling
-- Installing: /usr/share/OpenCV/testdata/gpu/labeling/label.png
-- Installing: /usr/share/OpenCV/testdata/gpu/labeling/aloe-disp.png
-- Installing: /usr/share/OpenCV/testdata/gpu/hog
-- Installing: /usr/share/OpenCV/testdata/gpu/hog/positive3.png
-- Installing: /usr/share/OpenCV/testdata/gpu/hog/negative3.png
-- Installing: /usr/share/OpenCV/testdata/gpu/hog/positive2.png
-- Installing: /usr/share/OpenCV/testdata/gpu/hog/negative1.png
-- Installing: /usr/share/OpenCV/testdata/gpu/hog/positive1.png
-- Installing: /usr/share/OpenCV/testdata/gpu/hog/negative2.png
-- Installing: /usr/share/OpenCV/testdata/gpu/hog/expected_output.bin
-- Installing: /usr/share/OpenCV/testdata/gpu/hog/road.png
-- Installing: /usr/share/OpenCV/testdata/gpu/hog/train_data.png
-- Installing: /usr/share/OpenCV/testdata/gpu/stereobp
-- Installing: /usr/share/OpenCV/testdata/gpu/stereobp/aloe-R.png
-- Installing: /usr/share/OpenCV/testdata/gpu/stereobp/aloe-disp.png
-- Installing: /usr/share/OpenCV/testdata/gpu/stereobp/aloe-L.png
-- Installing: /usr/share/OpenCV/testdata/gpu/features2d
-- Installing: /usr/share/OpenCV/testdata/gpu/features2d/aloe.png
-- Installing: /usr/share/OpenCV/testdata/gpu/stereobm
-- Installing: /usr/share/OpenCV/testdata/gpu/stereobm/aloe-R.png
-- Installing: /usr/share/OpenCV/testdata/gpu/stereobm/aloe-disp.png
-- Installing: /usr/share/OpenCV/testdata/gpu/stereobm/aloe-L.png
-- Installing: /usr/share/OpenCV/testdata/gpu/meanshift
-- Installing: /usr/share/OpenCV/testdata/gpu/meanshift/con_result.png
-- Installing: /usr/share/OpenCV/testdata/gpu/meanshift/cones_segmented_sp10_sr10_minsize4.png
-- Installing: /usr/share/OpenCV/testdata/gpu/meanshift/con_result_CC1X.png
-- Installing: /usr/share/OpenCV/testdata/gpu/meanshift/cones_segmented_sp10_sr10_minsize1364.png
-- Installing: /usr/share/OpenCV/testdata/gpu/meanshift/spmap.yaml
-- Installing: /usr/share/OpenCV/testdata/gpu/meanshift/cones.png
-- Installing: /usr/share/OpenCV/testdata/gpu/meanshift/cones_segmented_sp10_sr10_minsize340.png
-- Installing: /usr/share/OpenCV/testdata/gpu/meanshift/cones_segmented_sp10_sr10_minsize340_CC1X.png
-- Installing: /usr/share/OpenCV/testdata/gpu/meanshift/cones_segmented_sp10_sr10_minsize84_CC1X.png
-- Installing: /usr/share/OpenCV/testdata/gpu/meanshift/cones_segmented_sp10_sr10_minsize4_CC1X.png
-- Installing: /usr/share/OpenCV/testdata/gpu/meanshift/cones_segmented_sp10_sr10_minsize20.png
-- Installing: /usr/share/OpenCV/testdata/gpu/meanshift/cones_segmented_sp10_sr10_minsize1364_CC1X.png
-- Installing: /usr/share/OpenCV/testdata/gpu/meanshift/cones_segmented_sp10_sr10_minsize0.png
-- Installing: /usr/share/OpenCV/testdata/gpu/meanshift/cones_segmented_sp10_sr10_minsize84.png
-- Installing: /usr/share/OpenCV/testdata/gpu/meanshift/spmap_CC1X.yaml
-- Installing: /usr/share/OpenCV/testdata/gpu/meanshift/cones_segmented_sp10_sr10_minsize20_CC1X.png
-- Installing: /usr/share/OpenCV/testdata/gpu/meanshift/cones_segmented_sp10_sr10_minsize0_CC1X.png
-- Installing: /usr/share/OpenCV/testdata/gpu/haarcascade
-- Installing: /usr/share/OpenCV/testdata/gpu/haarcascade/basketball1.png
-- Installing: /usr/share/OpenCV/testdata/gpu/haarcascade/haarcascade_eye_tree_eyeglasses.xml
-- Installing: /usr/share/OpenCV/testdata/gpu/haarcascade/haarcascade_frontalface_alt_tree.xml
-- Installing: /usr/share/OpenCV/testdata/gpu/haarcascade/haarcascade_eye.xml
-- Installing: /usr/share/OpenCV/testdata/gpu/haarcascade/haarcascade_frontalface_alt.xml
-- Installing: /usr/share/OpenCV/testdata/gpu/haarcascade/haarcascade_frontalface_alt2.xml
-- Installing: /usr/share/OpenCV/testdata/gpu/haarcascade/group_1_640x480_VGA.pgm
-- Installing: /usr/share/OpenCV/testdata/gpu/video
-- Installing: /usr/share/OpenCV/testdata/gpu/video/768x576.avi
-- Installing: /usr/share/OpenCV/testdata/gpu/video/1920x1080.avi
-- Installing: /usr/share/OpenCV/testdata/gpu/matchtemplate
-- Installing: /usr/share/OpenCV/testdata/gpu/matchtemplate/target-0.png
-- Installing: /usr/share/OpenCV/testdata/gpu/matchtemplate/source-1.png
-- Installing: /usr/share/OpenCV/testdata/gpu/matchtemplate/cat.png
-- Installing: /usr/share/OpenCV/testdata/gpu/matchtemplate/target-1.png
-- Installing: /usr/share/OpenCV/testdata/gpu/matchtemplate/scene.png
-- Installing: /usr/share/OpenCV/testdata/gpu/matchtemplate/black.png
-- Installing: /usr/share/OpenCV/testdata/gpu/matchtemplate/source-0.png
-- Installing: /usr/share/OpenCV/testdata/gpu/matchtemplate/template.png
-- Installing: /usr/share/OpenCV/testdata/ml
-- Installing: /usr/share/OpenCV/testdata/ml/car.data
-- Installing: /usr/share/OpenCV/testdata/ml/protocol.txt
-- Installing: /usr/share/OpenCV/testdata/ml/vehicle.data
-- Installing: /usr/share/OpenCV/testdata/ml/spambase.data
-- Installing: /usr/share/OpenCV/testdata/ml/iris.data
-- Installing: /usr/share/OpenCV/testdata/ml/letter.data
-- Installing: /usr/share/OpenCV/testdata/ml/adult.data
-- Installing: /usr/share/OpenCV/testdata/ml/housing_.data
-- Installing: /usr/share/OpenCV/testdata/ml/abalone.data
-- Installing: /usr/share/OpenCV/testdata/ml/twonorm.data
-- Installing: /usr/share/OpenCV/testdata/ml/legacy
-- Installing: /usr/share/OpenCV/testdata/ml/legacy/boost_adult.xml
-- Installing: /usr/share/OpenCV/testdata/ml/legacy/dtree_mushroom.xml
-- Installing: /usr/share/OpenCV/testdata/ml/legacy/dtree_abalone.xml
-- Installing: /usr/share/OpenCV/testdata/ml/legacy/boost_2.xml
-- Installing: /usr/share/OpenCV/testdata/ml/legacy/boost_1.xml
-- Installing: /usr/share/OpenCV/testdata/ml/legacy/svm_waveform.xml
-- Installing: /usr/share/OpenCV/testdata/ml/legacy/boost_3.xml
-- Installing: /usr/share/OpenCV/testdata/ml/legacy/ann_waveform.xml
-- Installing: /usr/share/OpenCV/testdata/ml/legacy/rtrees_waveform.xml
-- Installing: /usr/share/OpenCV/testdata/ml/legacy/nbayes_waveform.xml
-- Installing: /usr/share/OpenCV/testdata/ml/legacy/svm_poletelecomm.xml
-- Installing: /usr/share/OpenCV/testdata/ml/legacy/svmsgd_waveform.xml
-- Installing: /usr/share/OpenCV/testdata/ml/poletelecomm.data
-- Installing: /usr/share/OpenCV/testdata/ml/automobile.data
-- Installing: /usr/share/OpenCV/testdata/ml/ringnorm.data
-- Installing: /usr/share/OpenCV/testdata/ml/housing.data
-- Installing: /usr/share/OpenCV/testdata/ml/slvalidation.xml
-- Installing: /usr/share/OpenCV/testdata/ml/waveform.data
-- Installing: /usr/share/OpenCV/testdata/ml/avalidation.xml
-- Installing: /usr/share/OpenCV/testdata/ml/mushroom.data
-- Installing: /usr/share/OpenCV/testdata/cv
-- Installing: /usr/share/OpenCV/testdata/cv/shared
-- Installing: /usr/share/OpenCV/testdata/cv/shared/pic3.png
-- Installing: /usr/share/OpenCV/testdata/cv/shared/pic4.png
-- Installing: /usr/share/OpenCV/testdata/cv/shared/1_itseez-0001438.png
-- Installing: /usr/share/OpenCV/testdata/cv/shared/fruits.png
-- Installing: /usr/share/OpenCV/testdata/cv/shared/box_in_scene.png
-- Installing: /usr/share/OpenCV/testdata/cv/shared/baboon.png
-- Installing: /usr/share/OpenCV/testdata/cv/shared/pic5.png
-- Installing: /usr/share/OpenCV/testdata/cv/shared/1_itseez-0000573.png
-- Installing: /usr/share/OpenCV/testdata/cv/shared/5MP.png
-- Installing: /usr/share/OpenCV/testdata/cv/shared/1_itseez-0000892.png
-- Installing: /usr/share/OpenCV/testdata/cv/shared/1_itseez-0000247.png
-- Installing: /usr/share/OpenCV/testdata/cv/shared/video_for_test.avi
-- Installing: /usr/share/OpenCV/testdata/cv/shared/1_itseez-0000289.png
-- Installing: /usr/share/OpenCV/testdata/cv/shared/airplane.png
-- Installing: /usr/share/OpenCV/testdata/cv/shared/pic6.png
-- Installing: /usr/share/OpenCV/testdata/cv/shared/1_itseez-0000492.png
-- Installing: /usr/share/OpenCV/testdata/cv/shared/fruits_ecc.png
-- Installing: /usr/share/OpenCV/testdata/cv/shared/templ.png
-- Installing: /usr/share/OpenCV/testdata/cv/shared/graffiti.png
-- Installing: /usr/share/OpenCV/testdata/cv/shared/1_itseez-0001238.png
-- Installing: /usr/share/OpenCV/testdata/cv/shared/3MP.png
-- Installing: /usr/share/OpenCV/testdata/cv/shared/lena.png
-- Installing: /usr/share/OpenCV/testdata/cv/shared/pic2.png
-- Installing: /usr/share/OpenCV/testdata/cv/shared/1_itseez-0000984.png
-- Installing: /usr/share/OpenCV/testdata/cv/shared/1_itseez-0000803.png
-- Installing: /usr/share/OpenCV/testdata/cv/shared/pic1.png
-- Installing: /usr/share/OpenCV/testdata/cv/shared/box.png
-- Installing: /usr/share/OpenCV/testdata/cv/shared/1_itseez-0002524.png
-- Installing: /usr/share/OpenCV/testdata/cv/edgefilter
-- Installing: /usr/share/OpenCV/testdata/cv/edgefilter/statue.png
-- Installing: /usr/share/OpenCV/testdata/cv/edgefilter/fgs
-- Installing: /usr/share/OpenCV/testdata/cv/edgefilter/fgs/kodim23_lambda=1000_sigma=10.png
-- Installing: /usr/share/OpenCV/testdata/cv/edgefilter/dt
-- Installing: /usr/share/OpenCV/testdata/cv/edgefilter/dt/authors_statue_RF_ss30_sc0.2.png
-- Installing: /usr/share/OpenCV/testdata/cv/edgefilter/dt/authors_statue_NC_ss30_sc0.2.png
-- Installing: /usr/share/OpenCV/testdata/cv/edgefilter/dt/authors_statue_IC_ss30_sc0.2.png
-- Installing: /usr/share/OpenCV/testdata/cv/edgefilter/amf
-- Installing: /usr/share/OpenCV/testdata/cv/edgefilter/amf/kodim23_amf_ss5_sr0.1_outliers_ref.png
-- Installing: /usr/share/OpenCV/testdata/cv/edgefilter/amf/kodim23_amf_ss50_sr0.3_ref.png
-- Installing: /usr/share/OpenCV/testdata/cv/edgefilter/amf/kodim23_amf_ss50_sr0.5_outliers_ref.png
-- Installing: /usr/share/OpenCV/testdata/cv/edgefilter/amf/kodim23_amf_ss30_sr0.1_ref.png
-- Installing: /usr/share/OpenCV/testdata/cv/edgefilter/amf/kodim23_amf_ss15_sr0.3_outliers_ref.png
-- Installing: /usr/share/OpenCV/testdata/cv/edgefilter/amf/kodim23_amf_ss5_sr0.3_ref.png
-- Installing: /usr/share/OpenCV/testdata/cv/edgefilter/kodim23.png
-- Installing: /usr/share/OpenCV/testdata/cv/cvtcolor_strict
-- Installing: /usr/share/OpenCV/testdata/cv/cvtcolor_strict/rglena.png
-- Installing: /usr/share/OpenCV/testdata/cv/cvtcolor_strict/grlena.png
-- Installing: /usr/share/OpenCV/testdata/cv/cvtcolor_strict/bglena.png
-- Installing: /usr/share/OpenCV/testdata/cv/cvtcolor_strict/lena.png
-- Installing: /usr/share/OpenCV/testdata/cv/cvtcolor_strict/gblena.png
-- Installing: /usr/share/OpenCV/testdata/cv/ximgproc
-- Installing: /usr/share/OpenCV/testdata/cv/ximgproc/sources
-- Installing: /usr/share/OpenCV/testdata/cv/ximgproc/sources/10.png
-- Installing: /usr/share/OpenCV/testdata/cv/ximgproc/sources/08.png
-- Installing: /usr/share/OpenCV/testdata/cv/ximgproc/sources/03.png
-- Installing: /usr/share/OpenCV/testdata/cv/ximgproc/sources/06.png
-- Installing: /usr/share/OpenCV/testdata/cv/ximgproc/sources/12.png
-- Installing: /usr/share/OpenCV/testdata/cv/ximgproc/sources/09.png
-- Installing: /usr/share/OpenCV/testdata/cv/ximgproc/sources/02.png
-- Installing: /usr/share/OpenCV/testdata/cv/ximgproc/sources/05.png
-- Installing: /usr/share/OpenCV/testdata/cv/ximgproc/sources/04.png
-- Installing: /usr/share/OpenCV/testdata/cv/ximgproc/sources/01.png
-- Installing: /usr/share/OpenCV/testdata/cv/ximgproc/sources/07.png
-- Installing: /usr/share/OpenCV/testdata/cv/ximgproc/sources/11.png
-- Installing: /usr/share/OpenCV/testdata/cv/ximgproc/model.yml.gz
-- Installing: /usr/share/OpenCV/testdata/cv/ximgproc/results
-- Installing: /usr/share/OpenCV/testdata/cv/ximgproc/results/10.png
-- Installing: /usr/share/OpenCV/testdata/cv/ximgproc/results/08.png
-- Installing: /usr/share/OpenCV/testdata/cv/ximgproc/results/03.png
-- Installing: /usr/share/OpenCV/testdata/cv/ximgproc/results/06.png
-- Installing: /usr/share/OpenCV/testdata/cv/ximgproc/results/12.png
-- Installing: /usr/share/OpenCV/testdata/cv/ximgproc/results/09.png
-- Installing: /usr/share/OpenCV/testdata/cv/ximgproc/results/02.png
-- Installing: /usr/share/OpenCV/testdata/cv/ximgproc/results/05.png
-- Installing: /usr/share/OpenCV/testdata/cv/ximgproc/results/04.png
-- Installing: /usr/share/OpenCV/testdata/cv/ximgproc/results/01.png
-- Installing: /usr/share/OpenCV/testdata/cv/ximgproc/results/07.png
-- Installing: /usr/share/OpenCV/testdata/cv/ximgproc/results/11.png
-- Installing: /usr/share/OpenCV/testdata/cv/structured_light
-- Installing: /usr/share/OpenCV/testdata/cv/structured_light/data
-- Installing: /usr/share/OpenCV/testdata/cv/structured_light/data/pattern_cam1_im30.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/structured_light/data/pattern_cam1_im20.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/structured_light/data/pattern_cam2_im43.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/structured_light/data/pattern_cam2_im44.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/structured_light/data/pattern_cam2_im22.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/structured_light/data/pattern_cam2_im38.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/structured_light/data/unwrappedFtpTest.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/structured_light/data/pattern_cam2_im15.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/structured_light/data/pattern_cam2_im25.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/structured_light/data/pattern_cam2_im30.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/structured_light/data/pattern_cam2_im28.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/structured_light/data/pattern_cam2_im34.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/structured_light/data/pattern_cam1_im35.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/structured_light/data/pattern_cam1_im23.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/structured_light/data/pattern_cam1_im13.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/structured_light/data/pattern_cam2_im17.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/structured_light/data/pattern_cam1_im4.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/structured_light/data/pattern_cam2_im7.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/structured_light/data/pattern_cam2_im35.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/structured_light/data/pattern_cam1_im11.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/structured_light/data/pattern_cam1_im42.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/structured_light/data/pattern_cam1_im21.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/structured_light/data/pattern_cam1_im39.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/structured_light/data/pattern_cam1_im43.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/structured_light/data/pattern_cam2_im33.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/structured_light/data/pattern_cam2_im27.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/structured_light/data/pattern_cam2_im6.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/structured_light/data/pattern_cam1_im36.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/structured_light/data/pattern_cam2_im11.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/structured_light/data/unwrappedFapsTest.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/structured_light/data/pattern_cam2_im9.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/structured_light/data/pattern_cam2_im4.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/structured_light/data/pattern_cam2_im16.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/structured_light/data/pattern_cam1_im32.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/structured_light/data/pattern_cam2_im23.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/structured_light/data/pattern_cam1_im38.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/structured_light/data/pattern_cam1_im19.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/structured_light/data/pattern_cam2_im18.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/structured_light/data/pattern_cam1_im22.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/structured_light/data/pattern_cam1_im41.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/structured_light/data/pattern_cam2_im36.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/structured_light/data/pattern_cam2_im42.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/structured_light/data/pattern_cam1_im5.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/structured_light/data/pattern_cam1_im33.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/structured_light/data/pattern_cam1_im26.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/structured_light/data/pattern_cam2_im37.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/structured_light/data/pattern_cam1_im34.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/structured_light/data/pattern_cam2_im39.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/structured_light/data/pattern_cam2_im24.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/structured_light/data/pattern_cam2_im5.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/structured_light/data/pattern_cam1_im15.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/structured_light/data/pattern_cam1_im3.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/structured_light/data/pattern_cam2_im31.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/structured_light/data/pattern_cam2_im2.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/structured_light/data/pattern_cam1_im27.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/structured_light/data/pattern_cam1_im24.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/structured_light/data/calibrationParameters.yml
-- Installing: /usr/share/OpenCV/testdata/cv/structured_light/data/pattern_cam1_im17.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/structured_light/data/pattern_cam2_im10.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/structured_light/data/pattern_cam1_im28.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/structured_light/data/pattern_cam1_im25.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/structured_light/data/capture_sin_1.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/structured_light/data/pattern_cam2_im32.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/structured_light/data/pattern_cam1_im10.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/structured_light/data/pattern_cam2_im14.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/structured_light/data/pattern_cam1_im1.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/structured_light/data/pattern_cam1_im31.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/structured_light/data/pattern_cam1_im9.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/structured_light/data/pattern_cam1_im12.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/structured_light/data/pattern_cam1_im44.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/structured_light/data/pattern_cam1_im16.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/structured_light/data/gt_plane.yml
-- Installing: /usr/share/OpenCV/testdata/cv/structured_light/data/pattern_cam1_im18.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/structured_light/data/pattern_cam2_im1.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/structured_light/data/pattern_cam2_im41.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/structured_light/data/unwrappedPspTest.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/structured_light/data/pattern_cam1_im6.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/structured_light/data/pattern_cam2_im20.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/structured_light/data/pattern_cam1_im40.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/structured_light/data/pattern_cam2_im8.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/structured_light/data/pattern_cam2_im19.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/structured_light/data/pattern_cam2_im26.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/structured_light/data/pattern_cam1_im8.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/structured_light/data/pattern_cam2_im3.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/structured_light/data/pattern_cam1_im37.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/structured_light/data/pattern_cam1_im29.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/structured_light/data/pattern_cam2_im40.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/structured_light/data/pattern_cam2_im21.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/structured_light/data/pattern_cam2_im12.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/structured_light/data/pattern_cam1_im2.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/structured_light/data/pattern_cam1_im14.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/structured_light/data/pattern_cam2_im13.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/structured_light/data/pattern_cam1_im7.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/structured_light/data/capture_sin_2.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/structured_light/data/pattern_cam2_im29.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/structured_light/data/capture_sin_0.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/tracking
-- Installing: /usr/share/OpenCV/testdata/cv/tracking/dudek
-- Installing: /usr/share/OpenCV/testdata/cv/tracking/dudek/data
-- Installing: /usr/share/OpenCV/testdata/cv/tracking/dudek/data/dudek.webm
-- Installing: /usr/share/OpenCV/testdata/cv/tracking/dudek/initOmit
-- Installing: /usr/share/OpenCV/testdata/cv/tracking/dudek/initOmit/dudek.txt
-- Installing: /usr/share/OpenCV/testdata/cv/tracking/dudek/dudek.yml
-- Installing: /usr/share/OpenCV/testdata/cv/tracking/dudek/gt.txt
-- Installing: /usr/share/OpenCV/testdata/cv/tracking/faceocc2
-- Installing: /usr/share/OpenCV/testdata/cv/tracking/faceocc2/data
-- Installing: /usr/share/OpenCV/testdata/cv/tracking/faceocc2/data/faceocc2.webm
-- Installing: /usr/share/OpenCV/testdata/cv/tracking/faceocc2/faceocc2.yml
-- Installing: /usr/share/OpenCV/testdata/cv/tracking/faceocc2/initOmit
-- Installing: /usr/share/OpenCV/testdata/cv/tracking/faceocc2/initOmit/faceocc2.txt
-- Installing: /usr/share/OpenCV/testdata/cv/tracking/faceocc2/gt.txt
-- Installing: /usr/share/OpenCV/testdata/cv/tracking/README.md
-- Installing: /usr/share/OpenCV/testdata/cv/tracking/david
-- Installing: /usr/share/OpenCV/testdata/cv/tracking/david/data
-- Installing: /usr/share/OpenCV/testdata/cv/tracking/david/data/david.webm
-- Installing: /usr/share/OpenCV/testdata/cv/tracking/david/david.yml
-- Installing: /usr/share/OpenCV/testdata/cv/tracking/david/initOmit
-- Installing: /usr/share/OpenCV/testdata/cv/tracking/david/initOmit/david.txt
-- Installing: /usr/share/OpenCV/testdata/cv/tracking/david/gt.txt
-- Installing: /usr/share/OpenCV/testdata/cv/disparityfilter
-- Installing: /usr/share/OpenCV/testdata/cv/disparityfilter/ROI.xml
-- Installing: /usr/share/OpenCV/testdata/cv/disparityfilter/GT.png
-- Installing: /usr/share/OpenCV/testdata/cv/disparityfilter/disparity_right_raw.png
-- Installing: /usr/share/OpenCV/testdata/cv/disparityfilter/reference_accuracy.xml
-- Installing: /usr/share/OpenCV/testdata/cv/disparityfilter/left_view.png
-- Installing: /usr/share/OpenCV/testdata/cv/disparityfilter/disparity_left_raw.png
-- Installing: /usr/share/OpenCV/testdata/cv/shape
-- Installing: /usr/share/OpenCV/testdata/cv/shape/mpeg_test
-- Installing: /usr/share/OpenCV/testdata/cv/shape/mpeg_test/children-13.png
-- Installing: /usr/share/OpenCV/testdata/cv/shape/mpeg_test/children-8.png
-- Installing: /usr/share/OpenCV/testdata/cv/shape/mpeg_test/device7-18.png
-- Installing: /usr/share/OpenCV/testdata/cv/shape/mpeg_test/apple-13.png
-- Installing: /usr/share/OpenCV/testdata/cv/shape/mpeg_test/apple-8.png
-- Installing: /usr/share/OpenCV/testdata/cv/shape/mpeg_test/children-10.png
-- Installing: /usr/share/OpenCV/testdata/cv/shape/mpeg_test/teddy-11.png
-- Installing: /usr/share/OpenCV/testdata/cv/shape/mpeg_test/children-11.png
-- Installing: /usr/share/OpenCV/testdata/cv/shape/mpeg_test/teddy-19.png
-- Installing: /usr/share/OpenCV/testdata/cv/shape/mpeg_test/device7-4.png
-- Installing: /usr/share/OpenCV/testdata/cv/shape/mpeg_test/device7-19.png
-- Installing: /usr/share/OpenCV/testdata/cv/shape/mpeg_test/teddy-3.png
-- Installing: /usr/share/OpenCV/testdata/cv/shape/mpeg_test/Heart-20.png
-- Installing: /usr/share/OpenCV/testdata/cv/shape/mpeg_test/Heart-4.png
-- Installing: /usr/share/OpenCV/testdata/cv/shape/mpeg_test/teddy-20.png
-- Installing: /usr/share/OpenCV/testdata/cv/shape/mpeg_test/Heart-7.png
-- Installing: /usr/share/OpenCV/testdata/cv/shape/mpeg_test/Heart-5.png
-- Installing: /usr/share/OpenCV/testdata/cv/shape/mpeg_test/teddy-6.png
-- Installing: /usr/share/OpenCV/testdata/cv/shape/mpeg_test/teddy-16.png
-- Installing: /usr/share/OpenCV/testdata/cv/shape/mpeg_test/children-7.png
-- Installing: /usr/share/OpenCV/testdata/cv/shape/mpeg_test/teddy-13.png
-- Installing: /usr/share/OpenCV/testdata/cv/shape/mpeg_test/apple-10.png
-- Installing: /usr/share/OpenCV/testdata/cv/shape/mpeg_test/children-19.png
-- Installing: /usr/share/OpenCV/testdata/cv/shape/mpeg_test/Heart-1.png
-- Installing: /usr/share/OpenCV/testdata/cv/shape/mpeg_test/device7-20.png
-- Installing: /usr/share/OpenCV/testdata/cv/shape/mpeg_test/apple-19.png
-- Installing: /usr/share/OpenCV/testdata/cv/shape/mpeg_test/children-12.png
-- Installing: /usr/share/OpenCV/testdata/cv/shape/mpeg_test/device7-14.png
-- Installing: /usr/share/OpenCV/testdata/cv/shape/mpeg_test/device7-10.png
-- Installing: /usr/share/OpenCV/testdata/cv/shape/mpeg_test/device7-17.png
-- Installing: /usr/share/OpenCV/testdata/cv/shape/mpeg_test/device7-16.png
-- Installing: /usr/share/OpenCV/testdata/cv/shape/mpeg_test/children-3.png
-- Installing: /usr/share/OpenCV/testdata/cv/shape/mpeg_test/device7-13.png
-- Installing: /usr/share/OpenCV/testdata/cv/shape/mpeg_test/apple-3.png
-- Installing: /usr/share/OpenCV/testdata/cv/shape/mpeg_test/Heart-10.png
-- Installing: /usr/share/OpenCV/testdata/cv/shape/mpeg_test/teddy-18.png
-- Installing: /usr/share/OpenCV/testdata/cv/shape/mpeg_test/apple-1.png
-- Installing: /usr/share/OpenCV/testdata/cv/shape/mpeg_test/children-6.png
-- Installing: /usr/share/OpenCV/testdata/cv/shape/mpeg_test/teddy-14.png
-- Installing: /usr/share/OpenCV/testdata/cv/shape/mpeg_test/apple-5.png
-- Installing: /usr/share/OpenCV/testdata/cv/shape/mpeg_test/children-20.png
-- Installing: /usr/share/OpenCV/testdata/cv/shape/mpeg_test/apple-7.png
-- Installing: /usr/share/OpenCV/testdata/cv/shape/mpeg_test/teddy-1.png
-- Installing: /usr/share/OpenCV/testdata/cv/shape/mpeg_test/device7-5.png
-- Installing: /usr/share/OpenCV/testdata/cv/shape/mpeg_test/device7-7.png
-- Installing: /usr/share/OpenCV/testdata/cv/shape/mpeg_test/Heart-14.png
-- Installing: /usr/share/OpenCV/testdata/cv/shape/mpeg_test/children-2.png
-- Installing: /usr/share/OpenCV/testdata/cv/shape/mpeg_test/Heart-6.png
-- Installing: /usr/share/OpenCV/testdata/cv/shape/mpeg_test/teddy-5.png
-- Installing: /usr/share/OpenCV/testdata/cv/shape/mpeg_test/teddy-10.png
-- Installing: /usr/share/OpenCV/testdata/cv/shape/mpeg_test/Heart-11.png
-- Installing: /usr/share/OpenCV/testdata/cv/shape/mpeg_test/Heart-15.png
-- Installing: /usr/share/OpenCV/testdata/cv/shape/mpeg_test/children-15.png
-- Installing: /usr/share/OpenCV/testdata/cv/shape/mpeg_test/apple-2.png
-- Installing: /usr/share/OpenCV/testdata/cv/shape/mpeg_test/children-4.png
-- Installing: /usr/share/OpenCV/testdata/cv/shape/mpeg_test/device7-9.png
-- Installing: /usr/share/OpenCV/testdata/cv/shape/mpeg_test/children-1.png
-- Installing: /usr/share/OpenCV/testdata/cv/shape/mpeg_test/apple-4.png
-- Installing: /usr/share/OpenCV/testdata/cv/shape/mpeg_test/teddy-17.png
-- Installing: /usr/share/OpenCV/testdata/cv/shape/mpeg_test/Heart-8.png
-- Installing: /usr/share/OpenCV/testdata/cv/shape/mpeg_test/Heart-17.png
-- Installing: /usr/share/OpenCV/testdata/cv/shape/mpeg_test/Heart-13.png
-- Installing: /usr/share/OpenCV/testdata/cv/shape/mpeg_test/teddy-8.png
-- Installing: /usr/share/OpenCV/testdata/cv/shape/mpeg_test/apple-16.png
-- Installing: /usr/share/OpenCV/testdata/cv/shape/mpeg_test/children-17.png
-- Installing: /usr/share/OpenCV/testdata/cv/shape/mpeg_test/device7-15.png
-- Installing: /usr/share/OpenCV/testdata/cv/shape/mpeg_test/apple-20.png
-- Installing: /usr/share/OpenCV/testdata/cv/shape/mpeg_test/apple-17.png
-- Installing: /usr/share/OpenCV/testdata/cv/shape/mpeg_test/device7-8.png
-- Installing: /usr/share/OpenCV/testdata/cv/shape/mpeg_test/device7-2.png
-- Installing: /usr/share/OpenCV/testdata/cv/shape/mpeg_test/apple-12.png
-- Installing: /usr/share/OpenCV/testdata/cv/shape/mpeg_test/Heart-16.png
-- Installing: /usr/share/OpenCV/testdata/cv/shape/mpeg_test/children-18.png
-- Installing: /usr/share/OpenCV/testdata/cv/shape/mpeg_test/Heart-19.png
-- Installing: /usr/share/OpenCV/testdata/cv/shape/mpeg_test/apple-18.png
-- Installing: /usr/share/OpenCV/testdata/cv/shape/mpeg_test/children-14.png
-- Installing: /usr/share/OpenCV/testdata/cv/shape/mpeg_test/apple-15.png
-- Installing: /usr/share/OpenCV/testdata/cv/shape/mpeg_test/Heart-2.png
-- Installing: /usr/share/OpenCV/testdata/cv/shape/mpeg_test/Heart-9.png
-- Installing: /usr/share/OpenCV/testdata/cv/shape/mpeg_test/children-9.png
-- Installing: /usr/share/OpenCV/testdata/cv/shape/mpeg_test/teddy-15.png
-- Installing: /usr/share/OpenCV/testdata/cv/shape/mpeg_test/teddy-9.png
-- Installing: /usr/share/OpenCV/testdata/cv/shape/mpeg_test/children-5.png
-- Installing: /usr/share/OpenCV/testdata/cv/shape/mpeg_test/teddy-2.png
-- Installing: /usr/share/OpenCV/testdata/cv/shape/mpeg_test/Heart-18.png
-- Installing: /usr/share/OpenCV/testdata/cv/shape/mpeg_test/device7-6.png
-- Installing: /usr/share/OpenCV/testdata/cv/shape/mpeg_test/apple-11.png
-- Installing: /usr/share/OpenCV/testdata/cv/shape/mpeg_test/Heart-3.png
-- Installing: /usr/share/OpenCV/testdata/cv/shape/mpeg_test/device7-1.png
-- Installing: /usr/share/OpenCV/testdata/cv/shape/mpeg_test/teddy-7.png
-- Installing: /usr/share/OpenCV/testdata/cv/shape/mpeg_test/teddy-4.png
-- Installing: /usr/share/OpenCV/testdata/cv/shape/mpeg_test/Heart-12.png
-- Installing: /usr/share/OpenCV/testdata/cv/shape/mpeg_test/apple-9.png
-- Installing: /usr/share/OpenCV/testdata/cv/shape/mpeg_test/teddy-12.png
-- Installing: /usr/share/OpenCV/testdata/cv/shape/mpeg_test/device7-3.png
-- Installing: /usr/share/OpenCV/testdata/cv/shape/mpeg_test/apple-6.png
-- Installing: /usr/share/OpenCV/testdata/cv/shape/mpeg_test/children-16.png
-- Installing: /usr/share/OpenCV/testdata/cv/shape/mpeg_test/device7-12.png
-- Installing: /usr/share/OpenCV/testdata/cv/shape/mpeg_test/device7-11.png
-- Installing: /usr/share/OpenCV/testdata/cv/shape/mpeg_test/apple-14.png
-- Installing: /usr/share/OpenCV/testdata/cv/shape/samples
-- Installing: /usr/share/OpenCV/testdata/cv/shape/samples/2.png
-- Installing: /usr/share/OpenCV/testdata/cv/shape/samples/1.png
-- Installing: /usr/share/OpenCV/testdata/cv/cloning
-- Installing: /usr/share/OpenCV/testdata/cv/cloning/color_change
-- Installing: /usr/share/OpenCV/testdata/cv/cloning/color_change/source1.png
-- Installing: /usr/share/OpenCV/testdata/cv/cloning/color_change/mask.png
-- Installing: /usr/share/OpenCV/testdata/cv/cloning/color_change/reference.png
-- Installing: /usr/share/OpenCV/testdata/cv/cloning/Mixed_Cloning
-- Installing: /usr/share/OpenCV/testdata/cv/cloning/Mixed_Cloning/source1.png
-- Installing: /usr/share/OpenCV/testdata/cv/cloning/Mixed_Cloning/destination1.png
-- Installing: /usr/share/OpenCV/testdata/cv/cloning/Mixed_Cloning/mask.png
-- Installing: /usr/share/OpenCV/testdata/cv/cloning/Mixed_Cloning/reference.png
-- Installing: /usr/share/OpenCV/testdata/cv/cloning/Normal_Cloning
-- Installing: /usr/share/OpenCV/testdata/cv/cloning/Normal_Cloning/source1.png
-- Installing: /usr/share/OpenCV/testdata/cv/cloning/Normal_Cloning/destination1.png
-- Installing: /usr/share/OpenCV/testdata/cv/cloning/Normal_Cloning/mask.png
-- Installing: /usr/share/OpenCV/testdata/cv/cloning/Normal_Cloning/reference.png
-- Installing: /usr/share/OpenCV/testdata/cv/cloning/Texture_Flattening
-- Installing: /usr/share/OpenCV/testdata/cv/cloning/Texture_Flattening/source1.png
-- Installing: /usr/share/OpenCV/testdata/cv/cloning/Texture_Flattening/mask.png
-- Installing: /usr/share/OpenCV/testdata/cv/cloning/Texture_Flattening/reference.png
-- Installing: /usr/share/OpenCV/testdata/cv/cloning/Monochrome_Transfer
-- Installing: /usr/share/OpenCV/testdata/cv/cloning/Monochrome_Transfer/source1.png
-- Installing: /usr/share/OpenCV/testdata/cv/cloning/Monochrome_Transfer/destination1.png
-- Installing: /usr/share/OpenCV/testdata/cv/cloning/Monochrome_Transfer/mask.png
-- Installing: /usr/share/OpenCV/testdata/cv/cloning/Monochrome_Transfer/reference.png
-- Installing: /usr/share/OpenCV/testdata/cv/cloning/Illumination_Change
-- Installing: /usr/share/OpenCV/testdata/cv/cloning/Illumination_Change/source1.png
-- Installing: /usr/share/OpenCV/testdata/cv/cloning/Illumination_Change/mask.png
-- Installing: /usr/share/OpenCV/testdata/cv/cloning/Illumination_Change/reference.png
-- Installing: /usr/share/OpenCV/testdata/cv/rgbd
-- Installing: /usr/share/OpenCV/testdata/cv/rgbd/rgb.png
-- Installing: /usr/share/OpenCV/testdata/cv/rgbd/depth.png
-- Installing: /usr/share/OpenCV/testdata/cv/phase_unwrapping
-- Installing: /usr/share/OpenCV/testdata/cv/phase_unwrapping/data
-- Installing: /usr/share/OpenCV/testdata/cv/phase_unwrapping/data/wrappedpeaks.yml
-- Installing: /usr/share/OpenCV/testdata/cv/xphoto
-- Installing: /usr/share/OpenCV/testdata/cv/xphoto/simple_white_balance
-- Installing: /usr/share/OpenCV/testdata/cv/xphoto/simple_white_balance/sources
-- Installing: /usr/share/OpenCV/testdata/cv/xphoto/simple_white_balance/sources/08.png
-- Installing: /usr/share/OpenCV/testdata/cv/xphoto/simple_white_balance/sources/03.png
-- Installing: /usr/share/OpenCV/testdata/cv/xphoto/simple_white_balance/sources/06.png
-- Installing: /usr/share/OpenCV/testdata/cv/xphoto/simple_white_balance/sources/02.png
-- Installing: /usr/share/OpenCV/testdata/cv/xphoto/simple_white_balance/sources/05.png
-- Installing: /usr/share/OpenCV/testdata/cv/xphoto/simple_white_balance/sources/04.png
-- Installing: /usr/share/OpenCV/testdata/cv/xphoto/simple_white_balance/sources/01.png
-- Installing: /usr/share/OpenCV/testdata/cv/xphoto/simple_white_balance/sources/07.png
-- Installing: /usr/share/OpenCV/testdata/cv/xphoto/simple_white_balance/results
-- Installing: /usr/share/OpenCV/testdata/cv/xphoto/simple_white_balance/results/06.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/xphoto/simple_white_balance/results/03.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/xphoto/simple_white_balance/results/08.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/xphoto/simple_white_balance/results/04.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/xphoto/simple_white_balance/results/07.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/xphoto/simple_white_balance/results/05.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/xphoto/simple_white_balance/results/02.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/xphoto/simple_white_balance/results/01.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/xphoto/bm3d_image_denoising
-- Installing: /usr/share/OpenCV/testdata/cv/xphoto/bm3d_image_denoising/lena_noised_denoised_bm3d_grayscale_l1_tw=4_sw=16_h=10_bm=2500.png
-- Installing: /usr/share/OpenCV/testdata/cv/xphoto/bm3d_image_denoising/lena_noised_gaussian_sigma=10.png
-- Installing: /usr/share/OpenCV/testdata/cv/xphoto/bm3d_image_denoising/lena_noised_denoised_bm3d_grayscale_l2_tw=4_sw=16_h=10_bm=2500.png
-- Installing: /usr/share/OpenCV/testdata/cv/xphoto/bm3d_image_denoising/lena_noised_denoised_bm3d_grayscale_l2_tw=8_sw=16_h=10_bm=2500.png
-- Installing: /usr/share/OpenCV/testdata/cv/xphoto/bm3d_image_denoising/lena_noised_denoised_bm3d_wiener_grayscale_l2_tw=4_sw=16_h=10_bm=400.png
-- Installing: /usr/share/OpenCV/testdata/cv/xphoto/bm3d_image_denoising/lena_orig_grayscale.png
-- Installing: /usr/share/OpenCV/testdata/cv/xphoto/dct_image_denoising
-- Installing: /usr/share/OpenCV/testdata/cv/xphoto/dct_image_denoising/sources
-- Installing: /usr/share/OpenCV/testdata/cv/xphoto/dct_image_denoising/sources/01.png
-- Installing: /usr/share/OpenCV/testdata/cv/xphoto/dct_image_denoising/results
-- Installing: /usr/share/OpenCV/testdata/cv/xphoto/dct_image_denoising/results/01.png
-- Installing: /usr/share/OpenCV/testdata/cv/xphoto/inpainting
-- Installing: /usr/share/OpenCV/testdata/cv/xphoto/inpainting/mask_1.png
-- Installing: /usr/share/OpenCV/testdata/cv/xphoto/inpainting/src_1.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/planar
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/planar/box_in_scene.png
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/planar/box.png
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/one_way_train_images
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/one_way_train_images/one_way_train_0001.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/one_way_train_images/one_way_train_images.txt
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/one_way_train_images/one_way_train_0000.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/keypoints_datasets
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/keypoints_datasets/SURF_graf.xml.gz
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/keypoints_datasets/SURF_bikes.xml.gz
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/keypoints_datasets/SURF_trees.xml.gz
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/keypoints_datasets/SURF_boat.xml.gz
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/keypoints_datasets/SURF_bark.xml.gz
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/keypoints_datasets/SURF_ubc.xml.gz
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/keypoints_datasets/SURF_leuven.xml.gz
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/keypoints_datasets/SURF_wall.xml.gz
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/descriptors
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/descriptors/SIFT_res.xml
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/descriptors/SURF_res.xml
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/descriptors/SIFT_params.xml
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/descriptors/SURF_params.xml
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/descriptors/plots
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/descriptors/plots/FERN_ubc.csv
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/descriptors/plots/SURF_wall.csv
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/descriptors/plots/SIFT_leuven.csv
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/descriptors/plots/SURF_bikes.csv
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/descriptors/plots/Calonder_boat.csv
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/descriptors/plots/createPlots.sh
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/descriptors/plots/Calonder_bark.csv
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/descriptors/plots/Calonder_leuven.csv
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/descriptors/plots/SIFT_bark.csv
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/descriptors/plots/SIFT_trees.csv
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/descriptors/plots/SIFT_bikes.csv
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/descriptors/plots/SURF_bark.csv
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/descriptors/plots/SIFT_graf.csv
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/descriptors/plots/Calonder_wall.csv
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/descriptors/plots/SURF_leuven.csv
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/descriptors/plots/SURF_trees.csv
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/descriptors/plots/SURF_ubc.csv
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/descriptors/plots/FERN_bark.csv
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/descriptors/plots/wall.png
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/descriptors/plots/ubc.png
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/descriptors/plots/SIFT_wall.csv
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/descriptors/plots/graf.png
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/descriptors/plots/bikes.png
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/descriptors/plots/SURF_boat.csv
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/descriptors/plots/FERN_boat.csv
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/descriptors/plots/FERN_graf.csv
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/descriptors/plots/Calonder_ubc.csv
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/descriptors/plots/Calonder_graf.csv
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/descriptors/plots/SIFT_boat.csv
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/descriptors/plots/SURF_graf.csv
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/descriptors/plots/trees.png
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/descriptors/plots/leuven.png
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/descriptors/plots/boat.png
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/descriptors/plots/SIFT_ubc.csv
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/descriptors/plots/FERN_wall.csv
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/descriptors/plots/FERN_leuven.csv
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/descriptors/plots/FERN_trees.csv
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/descriptors/plots/FERN_bikes.csv
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/descriptors/plots/Calonder_bikes.csv
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/descriptors/plots/Calonder_trees.csv
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/descriptors/plots/bark.png
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/descriptors/FERN_params.xml
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/descriptors/FERN_res.xml
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/descriptors/Calonder_res.xml
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/descriptors/Calonder_params.xml
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/evaluation_test_description.txt
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/images_datasets
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/images_datasets/bikes
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/images_datasets/bikes/H1to6p.xml
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/images_datasets/bikes/H1to2p.xml
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/images_datasets/bikes/img5.png
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/images_datasets/bikes/img4.png
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/images_datasets/bikes/H1to5p.xml
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/images_datasets/bikes/img2.png
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/images_datasets/bikes/H1to3p.xml
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/images_datasets/bikes/H1to4p.xml
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/images_datasets/bikes/img6.png
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/images_datasets/bikes/img1.png
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/images_datasets/bikes/img3.png
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/images_datasets/wall
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/images_datasets/wall/H1to6p.xml
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/images_datasets/wall/H1to2p.xml
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/images_datasets/wall/img5.png
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/images_datasets/wall/img4.png
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/images_datasets/wall/H1to5p.xml
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/images_datasets/wall/img2.png
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/images_datasets/wall/H1to3p.xml
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/images_datasets/wall/H1to4p.xml
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/images_datasets/wall/img6.png
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/images_datasets/wall/img1.png
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/images_datasets/wall/img3.png
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/images_datasets/graf
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/images_datasets/graf/H1to6p.xml
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/images_datasets/graf/H1to2p.xml
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/images_datasets/graf/img5.png
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/images_datasets/graf/img4.png
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/images_datasets/graf/H1to5p.xml
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/images_datasets/graf/img2.png
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/images_datasets/graf/H1to3p.xml
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/images_datasets/graf/H1to4p.xml
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/images_datasets/graf/img6.png
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/images_datasets/graf/img1.png
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/images_datasets/graf/img3.png
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/images_datasets/trees
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/images_datasets/trees/H1to6p.xml
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/images_datasets/trees/H1to2p.xml
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/images_datasets/trees/img5.png
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/images_datasets/trees/img4.png
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/images_datasets/trees/H1to5p.xml
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/images_datasets/trees/img2.png
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/images_datasets/trees/H1to3p.xml
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/images_datasets/trees/H1to4p.xml
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/images_datasets/trees/img6.png
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/images_datasets/trees/img1.png
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/images_datasets/trees/img3.png
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/images_datasets/bark
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/images_datasets/bark/H1to6p.xml
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/images_datasets/bark/H1to2p.xml
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/images_datasets/bark/img5.png
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/images_datasets/bark/img4.png
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/images_datasets/bark/H1to5p.xml
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/images_datasets/bark/img2.png
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/images_datasets/bark/H1to3p.xml
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/images_datasets/bark/H1to4p.xml
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/images_datasets/bark/img6.png
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/images_datasets/bark/img1.png
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/images_datasets/bark/img3.png
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/images_datasets/leuven
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/images_datasets/leuven/H1to6p.xml
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/images_datasets/leuven/H1to2p.xml
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/images_datasets/leuven/img5.png
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/images_datasets/leuven/img4.png
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/images_datasets/leuven/H1to5p.xml
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/images_datasets/leuven/img2.png
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/images_datasets/leuven/H1to3p.xml
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/images_datasets/leuven/H1to4p.xml
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/images_datasets/leuven/img6.png
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/images_datasets/leuven/img1.png
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/images_datasets/leuven/img3.png
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/images_datasets/ubc
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/images_datasets/ubc/H1to6p.xml
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/images_datasets/ubc/H1to2p.xml
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/images_datasets/ubc/img5.png
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/images_datasets/ubc/img4.png
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/images_datasets/ubc/H1to5p.xml
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/images_datasets/ubc/img2.png
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/images_datasets/ubc/H1to3p.xml
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/images_datasets/ubc/H1to4p.xml
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/images_datasets/ubc/img6.png
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/images_datasets/ubc/img1.png
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/images_datasets/ubc/img3.png
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/images_datasets/boat
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/images_datasets/boat/H1to6p.xml
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/images_datasets/boat/H1to2p.xml
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/images_datasets/boat/img5.png
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/images_datasets/boat/img4.png
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/images_datasets/boat/H1to5p.xml
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/images_datasets/boat/img2.png
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/images_datasets/boat/H1to3p.xml
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/images_datasets/boat/H1to4p.xml
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/images_datasets/boat/img6.png
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/images_datasets/boat/img1.png
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/images_datasets/boat/img3.png
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/detectors
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/detectors/STAR_res.xml
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/detectors/GFTT_res.xml
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/detectors/HARRIS_params.xml
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/detectors/FAST_res.xml
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/detectors/MSER_params.xml
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/detectors/STAR_params.xml
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/detectors/SIFT_res.xml
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/detectors/SURF_res.xml
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/detectors/SIFT_params.xml
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/detectors/SURF_params.xml
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/detectors/HARRIS_res.xml
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/detectors/plots
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/detectors/plots/leuven_correspondenceCount.png
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/detectors/plots/MSER_leuven_repeatability.csv
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/detectors/plots/FAST_graf_correspondenceCount.csv
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/detectors/plots/boat_correspondenceCount.png
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/detectors/plots/STAR_graf_correspondenceCount.csv
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/detectors/plots/MSER_bikes_repeatability.csv
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/detectors/plots/FAST_leuven_repeatability.csv
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/detectors/plots/SIFT_trees_repeatability.csv
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/detectors/plots/HARRIS_average_correspondenceCount.csv
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/detectors/plots/MSER_bikes_correspondenceCount.csv
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/detectors/plots/HARRIS_bikes_repeatability.csv
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/detectors/plots/STAR_leuven_correspondenceCount.csv
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/detectors/plots/STAR_trees_correspondenceCount.csv
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/detectors/plots/GFTT_leuven_repeatability.csv
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/detectors/plots/SURF_bikes_repeatability.csv
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/detectors/plots/SURF_leuven_repeatability.csv
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/detectors/plots/GFTT_wall_repeatability.csv
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/detectors/plots/STAR_average_correspondenceCount.csv
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/detectors/plots/wall_repeatability.png
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/detectors/plots/STAR_trees_repeatability.csv
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/detectors/plots/STAR_graf_repeatability.csv
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/detectors/plots/SURF_ubc_repeatability.csv
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/detectors/plots/SIFT_leuven_correspondenceCount.csv
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/detectors/plots/FAST_wall_correspondenceCount.csv
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/detectors/plots/MSER_bark_correspondenceCount.csv
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/detectors/plots/SURF_graf_correspondenceCount.csv
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/detectors/plots/MSER_average_repeatability.csv
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/detectors/plots/STAR_boat_correspondenceCount.csv
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/detectors/plots/GFTT_trees_correspondenceCount.csv
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/detectors/plots/trees_correspondenceCount.png
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/detectors/plots/SIFT_boat_correspondenceCount.csv
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/detectors/plots/MSER_leuven_correspondenceCount.csv
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/detectors/plots/GFTT_average_repeatability.csv
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/detectors/plots/HARRIS_leuven_repeatability.csv
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/detectors/plots/MSER_boat_repeatability.csv
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/detectors/plots/STAR_boat_repeatability.csv
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/detectors/plots/FAST_bikes_correspondenceCount.csv
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/detectors/plots/GFTT_average_correspondenceCount.csv
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/detectors/plots/FAST_average_correspondenceCount.csv
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/detectors/plots/MSER_trees_repeatability.csv
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/detectors/plots/STAR_average_repeatability.csv
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/detectors/plots/HARRIS_graf_repeatability.csv
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/detectors/plots/HARRIS_bark_correspondenceCount.csv
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/detectors/plots/STAR_wall_correspondenceCount.csv
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/detectors/plots/SIFT_wall_repeatability.csv
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/detectors/plots/FAST_leuven_correspondenceCount.csv
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/detectors/plots/SURF_ubc_correspondenceCount.csv
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/detectors/plots/HARRIS_wall_correspondenceCount.csv
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/detectors/plots/GFTT_ubc_correspondenceCount.csv
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/detectors/plots/GFTT_bark_correspondenceCount.csv
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/detectors/plots/HARRIS_bikes_correspondenceCount.csv
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/detectors/plots/SIFT_trees_correspondenceCount.csv
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/detectors/plots/MSER_ubc_repeatability.csv
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/detectors/plots/MSER_trees_correspondenceCount.csv
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/detectors/plots/leuven_repeatability.png
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/detectors/plots/SURF_bikes_correspondenceCount.csv
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/detectors/plots/HARRIS_bark_repeatability.csv
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/detectors/plots/GFTT_leuven_correspondenceCount.csv
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/detectors/plots/FAST_trees_correspondenceCount.csv
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/detectors/plots/MSER_ubc_correspondenceCount.csv
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/detectors/plots/HARRIS_trees_repeatability.csv
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/detectors/plots/HARRIS_wall_repeatability.csv
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/detectors/plots/SIFT_bikes_repeatability.csv
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/detectors/plots/SIFT_bikes_correspondenceCount.csv
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/detectors/plots/graf_repeatability.png
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/detectors/plots/boat_repeatability.png
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/detectors/plots/GFTT_boat_repeatability.csv
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/detectors/plots/FAST_boat_repeatability.csv
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/detectors/plots/GFTT_wall_correspondenceCount.csv
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/detectors/plots/GFTT_bikes_correspondenceCount.csv
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/detectors/plots/FAST_graf_repeatability.csv
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/detectors/plots/SURF_boat_repeatability.csv
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/detectors/plots/SIFT_graf_repeatability.csv
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/detectors/plots/HARRIS_boat_correspondenceCount.csv
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/detectors/plots/HARRIS_average_repeatability.csv
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/detectors/plots/STAR_bark_repeatability.csv
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/detectors/plots/FAST_bark_repeatability.csv
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/detectors/plots/SURF_bark_repeatability.csv
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/detectors/plots/FAST_average_repeatability.csv
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/detectors/plots/HARRIS_trees_correspondenceCount.csv
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/detectors/plots/STAR_ubc_correspondenceCount.csv
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/detectors/plots/GFTT_graf_repeatability.csv
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/detectors/plots/SURF_graf_repeatability.csv
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/detectors/plots/STAR_wall_repeatability.csv
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/detectors/plots/SURF_average_correspondenceCount.csv
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/detectors/plots/HARRIS_ubc_repeatability.csv
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/detectors/plots/SURF_wall_repeatability.csv
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/detectors/plots/STAR_ubc_repeatability.csv
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/detectors/plots/HARRIS_boat_repeatability.csv
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/detectors/plots/SIFT_average_repeatability.csv
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/detectors/plots/bikes_correspondenceCount.png
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/detectors/plots/SIFT_ubc_repeatability.csv
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/detectors/plots/HARRIS_graf_correspondenceCount.csv
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/detectors/plots/GFTT_ubc_repeatability.csv
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/detectors/plots/MSER_boat_correspondenceCount.csv
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/detectors/plots/STAR_bikes_repeatability.csv
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/detectors/plots/GFTT_bark_repeatability.csv
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/detectors/plots/FAST_boat_correspondenceCount.csv
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/detectors/plots/MSER_graf_correspondenceCount.csv
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/detectors/plots/bark_repeatability.png
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/detectors/plots/HARRIS_leuven_correspondenceCount.csv
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/detectors/plots/bark_correspondenceCount.png
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/detectors/plots/FAST_bikes_repeatability.csv
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/detectors/plots/FAST_wall_repeatability.csv
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/detectors/plots/SIFT_wall_correspondenceCount.csv
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/detectors/plots/GFTT_graf_correspondenceCount.csv
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/detectors/plots/GFTT_boat_correspondenceCount.csv
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/detectors/plots/createPlots.p
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/detectors/plots/ubc_repeatability.png
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/detectors/plots/FAST_ubc_correspondenceCount.csv
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/detectors/plots/SIFT_graf_correspondenceCount.csv
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/detectors/plots/STAR_leuven_repeatability.csv
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/detectors/plots/GFTT_trees_repeatability.csv
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/detectors/plots/SURF_boat_correspondenceCount.csv
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/detectors/plots/SIFT_ubc_correspondenceCount.csv
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/detectors/plots/SIFT_average_correspondenceCount.csv
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/detectors/plots/SURF_average_repeatability.csv
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/detectors/plots/SURF_wall_correspondenceCount.csv
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/detectors/plots/ubc_correspondenceCount.png
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/detectors/plots/SURF_trees_correspondenceCount.csv
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/detectors/plots/SURF_trees_repeatability.csv
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/detectors/plots/trees_repeatability.png
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/detectors/plots/SIFT_boat_repeatability.csv
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/detectors/plots/bikes_repeatability.png
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/detectors/plots/MSER_wall_correspondenceCount.csv
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/detectors/plots/MSER_bark_repeatability.csv
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/detectors/plots/SURF_leuven_correspondenceCount.csv
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/detectors/plots/FAST_ubc_repeatability.csv
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/detectors/plots/MSER_wall_repeatability.csv
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/detectors/plots/SIFT_bark_repeatability.csv
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/detectors/plots/SIFT_leuven_repeatability.csv
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/detectors/plots/wall_correspondenceCount.png
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/detectors/plots/STAR_bikes_correspondenceCount.csv
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/detectors/plots/STAR_bark_correspondenceCount.csv
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/detectors/plots/MSER_average_correspondenceCount.csv
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/detectors/plots/SURF_bark_correspondenceCount.csv
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/detectors/plots/FAST_trees_repeatability.csv
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/detectors/plots/GFTT_bikes_repeatability.csv
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/detectors/plots/MSER_graf_repeatability.csv
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/detectors/plots/graf_correspondenceCount.png
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/detectors/plots/SIFT_bark_correspondenceCount.csv
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/detectors/plots/HARRIS_ubc_correspondenceCount.csv
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/detectors/plots/FAST_bark_correspondenceCount.csv
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/detectors/FAST_params.xml
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/detectors/GFTT_params.xml
-- Installing: /usr/share/OpenCV/testdata/cv/detectors_descriptors_evaluation/detectors/MSER_res.xml
-- Installing: /usr/share/OpenCV/testdata/cv/hdr
-- Installing: /usr/share/OpenCV/testdata/cv/hdr/tonemap
-- Installing: /usr/share/OpenCV/testdata/cv/hdr/tonemap/reinhard.png
-- Installing: /usr/share/OpenCV/testdata/cv/hdr/tonemap/image.hdr
-- Installing: /usr/share/OpenCV/testdata/cv/hdr/tonemap/mantiuk.png
-- Installing: /usr/share/OpenCV/testdata/cv/hdr/tonemap/durand.png
-- Installing: /usr/share/OpenCV/testdata/cv/hdr/tonemap/linear.png
-- Installing: /usr/share/OpenCV/testdata/cv/hdr/tonemap/drago.png
-- Installing: /usr/share/OpenCV/testdata/cv/hdr/merge
-- Installing: /usr/share/OpenCV/testdata/cv/hdr/merge/mertens.png
-- Installing: /usr/share/OpenCV/testdata/cv/hdr/merge/debevec.hdr
-- Installing: /usr/share/OpenCV/testdata/cv/hdr/merge/robertson.hdr
-- Installing: /usr/share/OpenCV/testdata/cv/hdr/calibrate
-- Installing: /usr/share/OpenCV/testdata/cv/hdr/calibrate/debevec.csv
-- Installing: /usr/share/OpenCV/testdata/cv/hdr/calibrate/robertson.csv
-- Installing: /usr/share/OpenCV/testdata/cv/hdr/exposures
-- Installing: /usr/share/OpenCV/testdata/cv/hdr/exposures/memorial07.png
-- Installing: /usr/share/OpenCV/testdata/cv/hdr/exposures/response.csv
-- Installing: /usr/share/OpenCV/testdata/cv/hdr/exposures/memorial14.png
-- Installing: /usr/share/OpenCV/testdata/cv/hdr/exposures/memorial01.png
-- Installing: /usr/share/OpenCV/testdata/cv/hdr/exposures/memorial12.png
-- Installing: /usr/share/OpenCV/testdata/cv/hdr/exposures/memorial06.png
-- Installing: /usr/share/OpenCV/testdata/cv/hdr/exposures/readme.txt
-- Installing: /usr/share/OpenCV/testdata/cv/hdr/exposures/memorial00.png
-- Installing: /usr/share/OpenCV/testdata/cv/hdr/exposures/memorial02.png
-- Installing: /usr/share/OpenCV/testdata/cv/hdr/exposures/memorial10.png
-- Installing: /usr/share/OpenCV/testdata/cv/hdr/exposures/memorial15.png
-- Installing: /usr/share/OpenCV/testdata/cv/hdr/exposures/list.txt
-- Installing: /usr/share/OpenCV/testdata/cv/hdr/exposures/memorial08.png
-- Installing: /usr/share/OpenCV/testdata/cv/hdr/exposures/memorial03.png
-- Installing: /usr/share/OpenCV/testdata/cv/hdr/exposures/memorial04.png
-- Installing: /usr/share/OpenCV/testdata/cv/hdr/exposures/memorial13.png
-- Installing: /usr/share/OpenCV/testdata/cv/hdr/exposures/memorial05.png
-- Installing: /usr/share/OpenCV/testdata/cv/hdr/exposures/memorial09.png
-- Installing: /usr/share/OpenCV/testdata/cv/hdr/exposures/memorial11.png
-- Installing: /usr/share/OpenCV/testdata/cv/decolor
-- Installing: /usr/share/OpenCV/testdata/cv/decolor/boost_reference.png
-- Installing: /usr/share/OpenCV/testdata/cv/decolor/grayscale_reference.png
-- Installing: /usr/share/OpenCV/testdata/cv/decolor/color_image_4.png
-- Installing: /usr/share/OpenCV/testdata/cv/decolor/color_image_1.png
-- Installing: /usr/share/OpenCV/testdata/cv/decolor/color_image_3.png
-- Installing: /usr/share/OpenCV/testdata/cv/decolor/color_image_2.png
-- Installing: /usr/share/OpenCV/testdata/cv/stereomatching
-- Installing: /usr/share/OpenCV/testdata/cv/stereomatching/algorithms
-- Installing: /usr/share/OpenCV/testdata/cv/stereomatching/algorithms/stereobm_params.xml
-- Installing: /usr/share/OpenCV/testdata/cv/stereomatching/algorithms/stereosgbm_params.xml
-- Installing: /usr/share/OpenCV/testdata/cv/stereomatching/algorithms/stereogc_res.xml
-- Installing: /usr/share/OpenCV/testdata/cv/stereomatching/algorithms/stereobm_res.xml
-- Installing: /usr/share/OpenCV/testdata/cv/stereomatching/algorithms/stereosgbm_res.xml
-- Installing: /usr/share/OpenCV/testdata/cv/stereomatching/algorithms/stereogc_params.xml
-- Installing: /usr/share/OpenCV/testdata/cv/stereomatching/datasets
-- Installing: /usr/share/OpenCV/testdata/cv/stereomatching/datasets/bull
-- Installing: /usr/share/OpenCV/testdata/cv/stereomatching/datasets/bull/disp2.png
-- Installing: /usr/share/OpenCV/testdata/cv/stereomatching/datasets/bull/disp6.png
-- Installing: /usr/share/OpenCV/testdata/cv/stereomatching/datasets/bull/im6.png
-- Installing: /usr/share/OpenCV/testdata/cv/stereomatching/datasets/bull/im2.png
-- Installing: /usr/share/OpenCV/testdata/cv/stereomatching/datasets/barn2
-- Installing: /usr/share/OpenCV/testdata/cv/stereomatching/datasets/barn2/disp2.png
-- Installing: /usr/share/OpenCV/testdata/cv/stereomatching/datasets/barn2/disp6.png
-- Installing: /usr/share/OpenCV/testdata/cv/stereomatching/datasets/barn2/im6.png
-- Installing: /usr/share/OpenCV/testdata/cv/stereomatching/datasets/barn2/im2.png
-- Installing: /usr/share/OpenCV/testdata/cv/stereomatching/datasets/cones
-- Installing: /usr/share/OpenCV/testdata/cv/stereomatching/datasets/cones/disp2.png
-- Installing: /usr/share/OpenCV/testdata/cv/stereomatching/datasets/cones/disp6.png
-- Installing: /usr/share/OpenCV/testdata/cv/stereomatching/datasets/cones/im6.png
-- Installing: /usr/share/OpenCV/testdata/cv/stereomatching/datasets/cones/im2.png
-- Installing: /usr/share/OpenCV/testdata/cv/stereomatching/datasets/venus
-- Installing: /usr/share/OpenCV/testdata/cv/stereomatching/datasets/venus/disp2.png
-- Installing: /usr/share/OpenCV/testdata/cv/stereomatching/datasets/venus/disp6.png
-- Installing: /usr/share/OpenCV/testdata/cv/stereomatching/datasets/venus/im6.png
-- Installing: /usr/share/OpenCV/testdata/cv/stereomatching/datasets/venus/im2.png
-- Installing: /usr/share/OpenCV/testdata/cv/stereomatching/datasets/tsukuba
-- Installing: /usr/share/OpenCV/testdata/cv/stereomatching/datasets/tsukuba/disp2.png
-- Installing: /usr/share/OpenCV/testdata/cv/stereomatching/datasets/tsukuba/im6.png
-- Installing: /usr/share/OpenCV/testdata/cv/stereomatching/datasets/tsukuba/im2.png
-- Installing: /usr/share/OpenCV/testdata/cv/stereomatching/datasets/poster
-- Installing: /usr/share/OpenCV/testdata/cv/stereomatching/datasets/poster/disp2.png
-- Installing: /usr/share/OpenCV/testdata/cv/stereomatching/datasets/poster/disp6.png
-- Installing: /usr/share/OpenCV/testdata/cv/stereomatching/datasets/poster/im6.png
-- Installing: /usr/share/OpenCV/testdata/cv/stereomatching/datasets/poster/im2.png
-- Installing: /usr/share/OpenCV/testdata/cv/stereomatching/datasets/datasets.xml
-- Installing: /usr/share/OpenCV/testdata/cv/stereomatching/datasets/sawtooth
-- Installing: /usr/share/OpenCV/testdata/cv/stereomatching/datasets/sawtooth/disp2.png
-- Installing: /usr/share/OpenCV/testdata/cv/stereomatching/datasets/sawtooth/disp6.png
-- Installing: /usr/share/OpenCV/testdata/cv/stereomatching/datasets/sawtooth/im6.png
-- Installing: /usr/share/OpenCV/testdata/cv/stereomatching/datasets/sawtooth/im2.png
-- Installing: /usr/share/OpenCV/testdata/cv/stereomatching/datasets/teddy
-- Installing: /usr/share/OpenCV/testdata/cv/stereomatching/datasets/teddy/disp2.png
-- Installing: /usr/share/OpenCV/testdata/cv/stereomatching/datasets/teddy/disp6.png
-- Installing: /usr/share/OpenCV/testdata/cv/stereomatching/datasets/teddy/disp2_hh4.png
-- Installing: /usr/share/OpenCV/testdata/cv/stereomatching/datasets/teddy/im6.png
-- Installing: /usr/share/OpenCV/testdata/cv/stereomatching/datasets/teddy/im2.png
-- Installing: /usr/share/OpenCV/testdata/cv/line_descriptor
-- Installing: /usr/share/OpenCV/testdata/cv/line_descriptor/edl_detector_keylines_cameraman.yaml
-- Installing: /usr/share/OpenCV/testdata/cv/line_descriptor/cameraman.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/line_descriptor/lbd_descriptors_cameraman
-- Installing: /usr/share/OpenCV/testdata/cv/denoising
-- Installing: /usr/share/OpenCV/testdata/cv/denoising/lena_noised_gaussian_sigma=10.png
-- Installing: /usr/share/OpenCV/testdata/cv/denoising/lena_orig.png
-- Installing: /usr/share/OpenCV/testdata/cv/denoising/lena_noised_denoised_multi_lab12_tw=7_sw=21_h=10_h2=15.png
-- Installing: /usr/share/OpenCV/testdata/cv/denoising/lena_orig_grayscale.png
-- Installing: /usr/share/OpenCV/testdata/cv/denoising/lena_noised_gaussian_sigma=20_multi_2.png
-- Installing: /usr/share/OpenCV/testdata/cv/denoising/lena_noised_denoised_lab12_tw=7_sw=21_h=10_h2=10.png
-- Installing: /usr/share/OpenCV/testdata/cv/denoising/lena_noised_denoised_grayscale_tw=7_sw=21_h=10.png
-- Installing: /usr/share/OpenCV/testdata/cv/denoising/lena_noised_denoised_multi_tw=7_sw=21_h=15.png
-- Installing: /usr/share/OpenCV/testdata/cv/denoising/lena_noised_gaussian_sigma=20_multi_1.png
-- Installing: /usr/share/OpenCV/testdata/cv/denoising/lena_noised_gaussian_sigma=20_multi_0.png
-- Installing: /usr/share/OpenCV/testdata/cv/grabcut
-- Installing: /usr/share/OpenCV/testdata/cv/grabcut/exp_mask1.png
-- Installing: /usr/share/OpenCV/testdata/cv/grabcut/exp_mask1py.png
-- Installing: /usr/share/OpenCV/testdata/cv/grabcut/image1652.ppm
-- Installing: /usr/share/OpenCV/testdata/cv/grabcut/exp_mask2py.png
-- Installing: /usr/share/OpenCV/testdata/cv/grabcut/exp_mask2.png
-- Installing: /usr/share/OpenCV/testdata/cv/grabcut/mask_prob.png
-- Installing: /usr/share/OpenCV/testdata/cv/grabcut/mask1652.ppm
-- Installing: /usr/share/OpenCV/testdata/cv/grabcut/mask_probpy.png
-- Installing: /usr/share/OpenCV/testdata/cv/cascadeandhog
-- Installing: /usr/share/OpenCV/testdata/cv/cascadeandhog/images
-- Installing: /usr/share/OpenCV/testdata/cv/cascadeandhog/images/er.png
-- Installing: /usr/share/OpenCV/testdata/cv/cascadeandhog/images/rehg-thanksgiving-1994.png
-- Installing: /usr/share/OpenCV/testdata/cv/cascadeandhog/images/addams-family.png
-- Installing: /usr/share/OpenCV/testdata/cv/cascadeandhog/images/class57.png
-- Installing: /usr/share/OpenCV/testdata/cv/cascadeandhog/images/bttf301.png
-- Installing: /usr/share/OpenCV/testdata/cv/cascadeandhog/images/image_00000000_0.png
-- Installing: /usr/share/OpenCV/testdata/cv/cascadeandhog/images/karen-and-rob.png
-- Installing: /usr/share/OpenCV/testdata/cv/cascadeandhog/images/churchill-downs.png
-- Installing: /usr/share/OpenCV/testdata/cv/cascadeandhog/images/mickymouse-self-p.png
-- Installing: /usr/share/OpenCV/testdata/cv/cascadeandhog/images/mona-lisa.png
-- Installing: /usr/share/OpenCV/testdata/cv/cascadeandhog/images/waynesworld2.png
-- Installing: /usr/share/OpenCV/testdata/cv/cascadeandhog/images/larroquette.png
-- Installing: /usr/share/OpenCV/testdata/cv/cascadeandhog/images/audrybt1.png
-- Installing: /usr/share/OpenCV/testdata/cv/cascadeandhog/hog.xml
-- Installing: /usr/share/OpenCV/testdata/cv/cascadeandhog/_cascade.xml
-- Installing: /usr/share/OpenCV/testdata/cv/cascadeandhog/sample_training_set
-- Installing: /usr/share/OpenCV/testdata/cv/cascadeandhog/sample_training_set/octave_0
-- Installing: /usr/share/OpenCV/testdata/cv/cascadeandhog/sample_training_set/octave_0/sample_4.png
-- Installing: /usr/share/OpenCV/testdata/cv/cascadeandhog/sample_training_set/octave_0/sample_2.png
-- Installing: /usr/share/OpenCV/testdata/cv/cascadeandhog/sample_training_set/octave_0/sample_3.png
-- Installing: /usr/share/OpenCV/testdata/cv/cascadeandhog/sample_training_set/octave_0/.zip
-- Installing: /usr/share/OpenCV/testdata/cv/cascadeandhog/sample_training_set/octave_0/sample_0.png
-- Installing: /usr/share/OpenCV/testdata/cv/cascadeandhog/sample_training_set/octave_0/sample_8.png
-- Installing: /usr/share/OpenCV/testdata/cv/cascadeandhog/sample_training_set/octave_0/sample_9.png
-- Installing: /usr/share/OpenCV/testdata/cv/cascadeandhog/sample_training_set/octave_0/sample_1.png
-- Installing: /usr/share/OpenCV/testdata/cv/cascadeandhog/sample_training_set/octave_0/sample_7.png
-- Installing: /usr/share/OpenCV/testdata/cv/cascadeandhog/sample_training_set/octave_0/sample_6.png
-- Installing: /usr/share/OpenCV/testdata/cv/cascadeandhog/sample_training_set/octave_0/sample_5.png
-- Installing: /usr/share/OpenCV/testdata/cv/cascadeandhog/sample_training_set/negative_sample_1.png
-- Installing: /usr/share/OpenCV/testdata/cv/cascadeandhog/sample_training_set/negative_sample_0.png
-- Installing: /usr/share/OpenCV/testdata/cv/cascadeandhog/sample_training_set/octave_-1
-- Installing: /usr/share/OpenCV/testdata/cv/cascadeandhog/sample_training_set/octave_-1/sample_4.png
-- Installing: /usr/share/OpenCV/testdata/cv/cascadeandhog/sample_training_set/octave_-1/sample_2.png
-- Installing: /usr/share/OpenCV/testdata/cv/cascadeandhog/sample_training_set/octave_-1/sample_3.png
-- Installing: /usr/share/OpenCV/testdata/cv/cascadeandhog/sample_training_set/octave_-1/sample_0.png
-- Installing: /usr/share/OpenCV/testdata/cv/cascadeandhog/sample_training_set/octave_-1/sample_8.png
-- Installing: /usr/share/OpenCV/testdata/cv/cascadeandhog/sample_training_set/octave_-1/sample_9.png
-- Installing: /usr/share/OpenCV/testdata/cv/cascadeandhog/sample_training_set/octave_-1/sample_1.png
-- Installing: /usr/share/OpenCV/testdata/cv/cascadeandhog/sample_training_set/octave_-1/sample_7.png
-- Installing: /usr/share/OpenCV/testdata/cv/cascadeandhog/sample_training_set/octave_-1/sample_6.png
-- Installing: /usr/share/OpenCV/testdata/cv/cascadeandhog/sample_training_set/octave_-1/sample_5.png
-- Installing: /usr/share/OpenCV/testdata/cv/cascadeandhog/cascade.xml
-- Installing: /usr/share/OpenCV/testdata/cv/cascadeandhog/cascades
-- Installing: /usr/share/OpenCV/testdata/cv/cascadeandhog/cascades/haarcascade_frontalface_alt2_old.xml
-- Installing: /usr/share/OpenCV/testdata/cv/cascadeandhog/cascades/haarcascade_1.xml
-- Installing: /usr/share/OpenCV/testdata/cv/cascadeandhog/cascades/lbpcascade_frontalface.xml
-- Installing: /usr/share/OpenCV/testdata/cv/cascadeandhog/cascades/haarcascade_frontalface_alt_old.xml
-- Installing: /usr/share/OpenCV/testdata/cv/cascadeandhog/cascades/haarcascade_3.xml
-- Installing: /usr/share/OpenCV/testdata/cv/cascadeandhog/cascades/haarcascade_frontalface_default_old.xml
-- Installing: /usr/share/OpenCV/testdata/cv/cascadeandhog/cascades/haarcascade_frontalface_default.xml
-- Installing: /usr/share/OpenCV/testdata/cv/cascadeandhog/cascades/inria_caltech-17.01.2013.xml
-- Installing: /usr/share/OpenCV/testdata/cv/cascadeandhog/cascades/haarcascade_frontalface_alt.xml
-- Installing: /usr/share/OpenCV/testdata/cv/cascadeandhog/cascades/haarcascade_frontalface_alt2.xml
-- Installing: /usr/share/OpenCV/testdata/cv/cascadeandhog/cascades/lbpcascade_frontalface_alt3.xml
-- Installing: /usr/share/OpenCV/testdata/cv/cascadeandhog/_hog.xml
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/random_pattern
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/random_pattern/random_patter
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/random_pattern/random_patter/2.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/random_pattern/random_patter/0.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/random_pattern/random_patter/3.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/random_pattern/random_patter/pattern_small.png
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/random_pattern/random_patter/5.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/random_pattern/random_patter/4.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/random_pattern/random_patter/6.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/random_pattern/random_patter/1.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/random_pattern/image_list.xml
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/chess2.png
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/chess5.png
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/chess9.png
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/small_chessboard3.png
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/fisheye
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/fisheye/calib-3_stereo_from_JY
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/fisheye/calib-3_stereo_from_JY/left.xml
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/fisheye/calib-3_stereo_from_JY/object.xml
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/fisheye/calib-3_stereo_from_JY/left
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/fisheye/calib-3_stereo_from_JY/left/stereo_pair_010.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/fisheye/calib-3_stereo_from_JY/left/stereo_pair_005.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/fisheye/calib-3_stereo_from_JY/left/stereo_pair_025.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/fisheye/calib-3_stereo_from_JY/left/stereo_pair_028.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/fisheye/calib-3_stereo_from_JY/left/stereo_pair_014.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/fisheye/calib-3_stereo_from_JY/left/stereo_pair_016.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/fisheye/calib-3_stereo_from_JY/left/stereo_pair_013.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/fisheye/calib-3_stereo_from_JY/left/stereo_pair_020.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/fisheye/calib-3_stereo_from_JY/left/stereo_pair_023.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/fisheye/calib-3_stereo_from_JY/left/stereo_pair_018.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/fisheye/calib-3_stereo_from_JY/left/stereo_pair_030.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/fisheye/calib-3_stereo_from_JY/left/stereo_pair_024.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/fisheye/calib-3_stereo_from_JY/left/stereo_pair_032.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/fisheye/calib-3_stereo_from_JY/left/stereo_pair_009.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/fisheye/calib-3_stereo_from_JY/left/stereo_pair_019.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/fisheye/calib-3_stereo_from_JY/left/stereo_pair_004.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/fisheye/calib-3_stereo_from_JY/left/stereo_pair_012.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/fisheye/calib-3_stereo_from_JY/left/stereo_pair_021.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/fisheye/calib-3_stereo_from_JY/left/stereo_pair_000.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/fisheye/calib-3_stereo_from_JY/left/stereo_pair_008.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/fisheye/calib-3_stereo_from_JY/left/stereo_pair_022.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/fisheye/calib-3_stereo_from_JY/left/stereo_pair_001.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/fisheye/calib-3_stereo_from_JY/left/stereo_pair_029.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/fisheye/calib-3_stereo_from_JY/left/stereo_pair_002.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/fisheye/calib-3_stereo_from_JY/left/stereo_pair_027.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/fisheye/calib-3_stereo_from_JY/left/stereo_pair_003.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/fisheye/calib-3_stereo_from_JY/left/stereo_pair_031.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/fisheye/calib-3_stereo_from_JY/left/stereo_pair_007.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/fisheye/calib-3_stereo_from_JY/left/stereo_pair_011.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/fisheye/calib-3_stereo_from_JY/left/stereo_pair_015.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/fisheye/calib-3_stereo_from_JY/left/stereo_pair_017.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/fisheye/calib-3_stereo_from_JY/left/stereo_pair_006.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/fisheye/calib-3_stereo_from_JY/left/stereo_pair_026.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/fisheye/calib-3_stereo_from_JY/left/stereo_pair_033.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/fisheye/calib-3_stereo_from_JY/right.xml
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/fisheye/calib-3_stereo_from_JY/right
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/fisheye/calib-3_stereo_from_JY/right/stereo_pair_010.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/fisheye/calib-3_stereo_from_JY/right/stereo_pair_005.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/fisheye/calib-3_stereo_from_JY/right/stereo_pair_025.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/fisheye/calib-3_stereo_from_JY/right/stereo_pair_028.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/fisheye/calib-3_stereo_from_JY/right/stereo_pair_014.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/fisheye/calib-3_stereo_from_JY/right/stereo_pair_016.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/fisheye/calib-3_stereo_from_JY/right/stereo_pair_013.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/fisheye/calib-3_stereo_from_JY/right/stereo_pair_020.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/fisheye/calib-3_stereo_from_JY/right/stereo_pair_023.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/fisheye/calib-3_stereo_from_JY/right/stereo_pair_018.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/fisheye/calib-3_stereo_from_JY/right/stereo_pair_030.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/fisheye/calib-3_stereo_from_JY/right/stereo_pair_024.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/fisheye/calib-3_stereo_from_JY/right/stereo_pair_032.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/fisheye/calib-3_stereo_from_JY/right/stereo_pair_009.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/fisheye/calib-3_stereo_from_JY/right/stereo_pair_019.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/fisheye/calib-3_stereo_from_JY/right/stereo_pair_004.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/fisheye/calib-3_stereo_from_JY/right/stereo_pair_012.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/fisheye/calib-3_stereo_from_JY/right/stereo_pair_021.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/fisheye/calib-3_stereo_from_JY/right/stereo_pair_000.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/fisheye/calib-3_stereo_from_JY/right/stereo_pair_008.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/fisheye/calib-3_stereo_from_JY/right/stereo_pair_022.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/fisheye/calib-3_stereo_from_JY/right/stereo_pair_001.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/fisheye/calib-3_stereo_from_JY/right/stereo_pair_029.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/fisheye/calib-3_stereo_from_JY/right/stereo_pair_002.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/fisheye/calib-3_stereo_from_JY/right/stereo_pair_027.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/fisheye/calib-3_stereo_from_JY/right/stereo_pair_003.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/fisheye/calib-3_stereo_from_JY/right/stereo_pair_031.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/fisheye/calib-3_stereo_from_JY/right/stereo_pair_007.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/fisheye/calib-3_stereo_from_JY/right/stereo_pair_011.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/fisheye/calib-3_stereo_from_JY/right/stereo_pair_015.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/fisheye/calib-3_stereo_from_JY/right/stereo_pair_017.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/fisheye/calib-3_stereo_from_JY/right/stereo_pair_006.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/fisheye/calib-3_stereo_from_JY/right/stereo_pair_026.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/fisheye/calib-3_stereo_from_JY/right/stereo_pair_033.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/chess_corners8.dat
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/small_chessboard3.dat
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/BoardStereoR2.png
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/chess_corners3.dat
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/chessboard-artificial1.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/BoardStereoL2.png
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/chess4.png
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/chess_corners5.dat
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/negative_2.dat
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/omnidir
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/omnidir/imagelist.xml
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/omnidir/omnidir_images
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/omnidir/omnidir_images/12.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/omnidir/omnidir_images/15.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/omnidir/omnidir_images/2.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/omnidir/omnidir_images/9.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/omnidir/omnidir_images/7.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/omnidir/omnidir_images/14.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/omnidir/omnidir_images/17.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/omnidir/omnidir_images/3.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/omnidir/omnidir_images/10.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/omnidir/omnidir_images/18.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/omnidir/omnidir_images/5.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/omnidir/omnidir_images/16.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/omnidir/omnidir_images/11.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/omnidir/omnidir_images/13.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/omnidir/omnidir_images/4.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/omnidir/omnidir_images/6.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/omnidir/omnidir_images/1.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/omnidir/omnidir_images/8.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/negative_3.dat
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/asymmetric_circles
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/asymmetric_circles/acircles8.png
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/asymmetric_circles/acircles4.png
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/asymmetric_circles/acircles9.png
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/asymmetric_circles/acircles5.png
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/asymmetric_circles/acircles2.png
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/asymmetric_circles/acircles_corners8.dat
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/asymmetric_circles/acircles_corners2.dat
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/asymmetric_circles/acircles1.png
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/asymmetric_circles/acircles_list.dat
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/asymmetric_circles/acircles6.png
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/asymmetric_circles/acircles3.png
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/asymmetric_circles/acircles_corners3.dat
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/asymmetric_circles/acircles_corners5.dat
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/asymmetric_circles/acircles_corners4.dat
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/asymmetric_circles/acircles_corners7.dat
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/asymmetric_circles/acircles_corners1.dat
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/asymmetric_circles/acircles_corners6.dat
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/asymmetric_circles/acircles_corners9.dat
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/asymmetric_circles/acircles7.png
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/chess7.png
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/chessboard_hires.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/chess3.png
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/small_chessboard1.dat
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/negative_3.png
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/chessboard-artificial1.png
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/negative_2.png
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/chess6.png
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/chessboard-artificial2.png
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/chessboard_timing_list.dat
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/BoardStereoR3.png
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/chess1.png
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/circles
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/circles/circles_corners6.dat
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/circles/circles9.png
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/circles/circles_corners11.dat
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/circles/circles5.png
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/circles/circles_corners9.dat
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/circles/circles_corners7.dat
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/circles/circles_corners12.dat
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/circles/circles2.png
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/circles/circles_corners8.dat
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/circles/circles13.png
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/circles/circles_corners4.dat
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/circles/circles_corners5.dat
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/circles/circles_corners14.dat
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/circles/circles7.png
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/circles/circles_corners1.dat
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/circles/circles_list.dat
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/circles/circles_corners13.dat
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/circles/circles1.png
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/circles/circles10.png
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/circles/circles_corners3.dat
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/circles/circles4.png
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/circles/circles14.png
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/circles/circles11.png
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/circles/circles_corners10.dat
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/circles/circles12.png
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/circles/circles_corners2.dat
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/circles/circles6.png
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/circles/circles8.png
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/circles/circles3.png
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/chess_corners9.dat
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/negative_1.png
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/chess_corners2.dat
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/BoardStereoL5.png
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/chess_corners4.dat
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/BoardStereoR4.png
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/chess_corners1.dat
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/subpixel
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/subpixel/m-0-capt0044.yml
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/subpixel/m-0-capt0033.yml
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/subpixel/m-0-capt0028.yml
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/subpixel/m-0-capt0031.png
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/subpixel/m-0-capt0042.yml
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/subpixel/m-1-capt0059.yml
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/subpixel/m-0-capt0030.png
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/subpixel/m-1-capt0032.yml
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/subpixel/m-0-capt0041.png
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/subpixel/m-0-capt0045.png
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/subpixel/m-0-capt0040.png
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/subpixel/m-1-capt0043.png
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/subpixel/m-1-capt0026.yml
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/subpixel/m-1-capt0030.yml
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/subpixel/m-1-capt0045.yml
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/subpixel/m-0-capt0025.png
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/subpixel/m-1-capt0028.yml
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/subpixel/m-0-capt0027.yml
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/subpixel/m-0-capt0029.yml
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/subpixel/m-1-capt0045.png
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/subpixel/m-0-capt0072.yml
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/subpixel/m-1-capt0032.png
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/subpixel/m-0-capt0028.png
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/subpixel/m-1-capt0027.png
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/subpixel/m-0-capt0031.yml
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/subpixel/m-0-capt0040.yml
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/subpixel/m-0-capt0041.yml
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/subpixel/m-0-capt0047.png
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/subpixel/m-1-capt0058.yml
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/subpixel/m-1-capt0033.yml
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/subpixel/m-1-capt0029.png
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/subpixel/m-0-capt0046.yml
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/subpixel/m-1-capt0034.png
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/subpixel/m-0-capt0043.yml
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/subpixel/m-1-capt0044.png
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/subpixel/m-0-capt0042.png
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/subpixel/m-1-capt0046.yml
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/subpixel/m-1-capt0047.png
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/subpixel/m-1-capt0046.png
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/subpixel/m-1-capt0041.png
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/subpixel/m-1-capt0029.yml
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/subpixel/m-0-capt0032.yml
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/subpixel/m-1-capt0034.yml
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/subpixel/m-0-capt0043.png
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/subpixel/m-0-capt0025.yml
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/subpixel/m-1-capt0027.yml
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/subpixel/m-0-capt0029.png
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/subpixel/m-0-capt0045.yml
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/subpixel/m-1-capt0047.yml
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/subpixel/m-1-capt0042.yml
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/subpixel/m-1-capt0044.yml
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/subpixel/m-1-capt0043.yml
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/subpixel/m-0-capt0047.yml
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/subpixel/m-0-capt0046.png
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/subpixel/m-0-capt0027.png
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/subpixel/m-0-capt0030.yml
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/subpixel/m-0-capt0026.png
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/subpixel/m-1-capt0030.png
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/subpixel/m-0-capt0033.png
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/subpixel/m-1-capt0041.yml
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/subpixel/m-0-capt0032.png
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/subpixel/m-1-capt0042.png
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/subpixel/m-0-capt0044.png
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/subpixel/m-1-capt0033.png
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/subpixel/m-1-capt0028.png
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/subpixel/m-1-capt0031.yml
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/subpixel/m-1-capt0031.png
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/subpixel/m-0-capt0026.yml
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/subpixel/m-1-capt0026.png
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/BoardStereoL1.png
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/multi_cameras
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/multi_cameras/multi_camera_omnidir.xml
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/multi_cameras/images_omnidir
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/multi_cameras/images_omnidir/1-232.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/multi_cameras/images_omnidir/3-104.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/multi_cameras/images_omnidir/3-103.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/multi_cameras/images_omnidir/1-187.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/multi_cameras/images_omnidir/0-129.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/multi_cameras/images_omnidir/4-22.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/multi_cameras/images_omnidir/0-156.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/multi_cameras/images_omnidir/4-34.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/multi_cameras/images_omnidir/0-188.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/multi_cameras/images_omnidir/2-25.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/multi_cameras/images_omnidir/3-101.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/multi_cameras/images_omnidir/4-232.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/multi_cameras/images_omnidir/0-182.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/multi_cameras/images_omnidir/3-96.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/multi_cameras/images_omnidir/0-158.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/multi_cameras/images_omnidir/2-64.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/multi_cameras/images_omnidir/4-24.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/multi_cameras/images_omnidir/0-140.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/multi_cameras/images_omnidir/3-132.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/multi_cameras/images_omnidir/1-244.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/multi_cameras/images_omnidir/3-85.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/multi_cameras/images_omnidir/2-19.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/multi_cameras/images_omnidir/2-96.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/multi_cameras/images_omnidir/4-233.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/multi_cameras/images_omnidir/0-195.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/multi_cameras/images_omnidir/3-93.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/multi_cameras/images_omnidir/2-67.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/multi_cameras/images_omnidir/3-141.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/multi_cameras/images_omnidir/4-245.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/multi_cameras/images_omnidir/0-159.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/multi_cameras/images_omnidir/2-68.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/multi_cameras/images_omnidir/2-63.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/multi_cameras/images_omnidir/0-187.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/multi_cameras/images_omnidir/4-19.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/multi_cameras/images_omnidir/2-85.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/multi_cameras/images_omnidir/4-32.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/multi_cameras/images_omnidir/2-84.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/multi_cameras/images_omnidir/3-129.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/multi_cameras/images_omnidir/0-179.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/multi_cameras/images_omnidir/1-179.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/multi_cameras/images_omnidir/1-203.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/multi_cameras/images_omnidir/3-37.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/multi_cameras/images_omnidir/3-94.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/multi_cameras/images_omnidir/3-142.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/multi_cameras/images_omnidir/4-25.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/multi_cameras/images_omnidir/0-155.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/multi_cameras/images_omnidir/2-21.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/multi_cameras/images_omnidir/2-94.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/multi_cameras/images_omnidir/3-112.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/multi_cameras/images_omnidir/1-205.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/multi_cameras/images_omnidir/2-61.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/multi_cameras/images_omnidir/4-21.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/multi_cameras/images_omnidir/2-24.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/multi_cameras/images_omnidir/0-132.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/multi_cameras/images_omnidir/3-3.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/multi_cameras/images_omnidir/4-244.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/multi_cameras/images_omnidir/1-182.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/multi_cameras/images_omnidir/4-36.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/multi_cameras/images_omnidir/4-231.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/multi_cameras/images_omnidir/3-84.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/multi_cameras/images_omnidir/pattern_small.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/multi_cameras/images_omnidir/3-140.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/multi_cameras/images_omnidir/1-231.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/multi_cameras/images_omnidir/1-245.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/multi_cameras/images_omnidir/2-93.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/multi_cameras/images_omnidir/0-142.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/multi_cameras/images_omnidir/1-204.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/multi_cameras/images_omnidir/2-22.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/multi_cameras/images_omnidir/2-104.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/multi_cameras/images_omnidir/4-28.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/multi_cameras/images_omnidir/1-195.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/multi_cameras/images_omnidir/1-188.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/multi_cameras/images_omnidir/1-233.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/multi_cameras/images_omnidir/0-141.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/multi_cameras/images_omnidir/0-160.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/multi_cameras/images_omnidir/1-211.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/BoardStereoL4.png
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/datafiles.txt
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/small_chessboard2.dat
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/BoardStereoR5.png
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/BoardStereoR6.png
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/chessboard_list_subpixel.dat
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/chessboard_list.dat
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/BoardStereoR1.png
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/calib1.dat
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/chessboard_hires.dat
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/small_chessboard1.png
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/chessboard-artificial2.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/negative_list.dat
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/BoardStereoL6.png
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/BoardStereoL3.png
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/small_chessboard2.png
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/chess_corners7.dat
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/negative_1.dat
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/chess_corners6.dat
-- Installing: /usr/share/OpenCV/testdata/cv/cameracalibration/chess8.png
-- Installing: /usr/share/OpenCV/testdata/cv/dpm
-- Installing: /usr/share/OpenCV/testdata/cv/dpm/cars.png
-- Installing: /usr/share/OpenCV/testdata/cv/dpm/convert_models_voc2007.m
-- Installing: /usr/share/OpenCV/testdata/cv/dpm/cat.png
-- Installing: /usr/share/OpenCV/testdata/cv/dpm/VOC2007_Cascade
-- Installing: /usr/share/OpenCV/testdata/cv/dpm/VOC2007_Cascade/bird.xml
-- Installing: /usr/share/OpenCV/testdata/cv/dpm/VOC2007_Cascade/bus.xml
-- Installing: /usr/share/OpenCV/testdata/cv/dpm/VOC2007_Cascade/chair.xml
-- Installing: /usr/share/OpenCV/testdata/cv/dpm/VOC2007_Cascade/sheep.xml
-- Installing: /usr/share/OpenCV/testdata/cv/dpm/VOC2007_Cascade/sofa.xml
-- Installing: /usr/share/OpenCV/testdata/cv/dpm/VOC2007_Cascade/bicycle.xml
-- Installing: /usr/share/OpenCV/testdata/cv/dpm/VOC2007_Cascade/cat.xml
-- Installing: /usr/share/OpenCV/testdata/cv/dpm/VOC2007_Cascade/motorbike.xml
-- Installing: /usr/share/OpenCV/testdata/cv/dpm/VOC2007_Cascade/horse.xml
-- Installing: /usr/share/OpenCV/testdata/cv/dpm/VOC2007_Cascade/inriaperson.xml
-- Installing: /usr/share/OpenCV/testdata/cv/dpm/VOC2007_Cascade/tvmonitor.xml
-- Installing: /usr/share/OpenCV/testdata/cv/dpm/VOC2007_Cascade/aeroplane.xml
-- Installing: /usr/share/OpenCV/testdata/cv/dpm/VOC2007_Cascade/diningtable.xml
-- Installing: /usr/share/OpenCV/testdata/cv/dpm/VOC2007_Cascade/train.xml
-- Installing: /usr/share/OpenCV/testdata/cv/dpm/VOC2007_Cascade/car.xml
-- Installing: /usr/share/OpenCV/testdata/cv/dpm/VOC2007_Cascade/boat.xml
-- Installing: /usr/share/OpenCV/testdata/cv/dpm/VOC2007_Cascade/dog.xml
-- Installing: /usr/share/OpenCV/testdata/cv/dpm/VOC2007_Cascade/cow.xml
-- Installing: /usr/share/OpenCV/testdata/cv/dpm/VOC2007_Cascade/pottedplant.xml
-- Installing: /usr/share/OpenCV/testdata/cv/dpm/VOC2007_Cascade/bottle.xml
-- Installing: /usr/share/OpenCV/testdata/cv/dpm/VOC2007_Cascade/person.xml
-- Installing: /usr/share/OpenCV/testdata/cv/dpm/mat2opencvxml.m
-- Installing: /usr/share/OpenCV/testdata/cv/optflow
-- Installing: /usr/share/OpenCV/testdata/cv/optflow/rock_1.bmp
-- Installing: /usr/share/OpenCV/testdata/cv/optflow/image2.png
-- Installing: /usr/share/OpenCV/testdata/cv/optflow/lk_next.dat
-- Installing: /usr/share/OpenCV/testdata/cv/optflow/frames
-- Installing: /usr/share/OpenCV/testdata/cv/optflow/frames/720p_01.png
-- Installing: /usr/share/OpenCV/testdata/cv/optflow/frames/VGA_01.png
-- Installing: /usr/share/OpenCV/testdata/cv/optflow/frames/VGA_03.png
-- Installing: /usr/share/OpenCV/testdata/cv/optflow/frames/720p_04.png
-- Installing: /usr/share/OpenCV/testdata/cv/optflow/frames/1080p_03.png
-- Installing: /usr/share/OpenCV/testdata/cv/optflow/frames/720p_00.png
-- Installing: /usr/share/OpenCV/testdata/cv/optflow/frames/1080p_01.png
-- Installing: /usr/share/OpenCV/testdata/cv/optflow/frames/720p_03.png
-- Installing: /usr/share/OpenCV/testdata/cv/optflow/frames/VGA_02.png
-- Installing: /usr/share/OpenCV/testdata/cv/optflow/frames/720p_05.png
-- Installing: /usr/share/OpenCV/testdata/cv/optflow/frames/VGA_04.png
-- Installing: /usr/share/OpenCV/testdata/cv/optflow/frames/1080p_02.png
-- Installing: /usr/share/OpenCV/testdata/cv/optflow/frames/1080p_00.png
-- Installing: /usr/share/OpenCV/testdata/cv/optflow/frames/720p_02.png
-- Installing: /usr/share/OpenCV/testdata/cv/optflow/frames/VGA_00.png
-- Installing: /usr/share/OpenCV/testdata/cv/optflow/frames/1080p_04.png
-- Installing: /usr/share/OpenCV/testdata/cv/optflow/image1.png
-- Installing: /usr/share/OpenCV/testdata/cv/optflow/RubberWhale1.png
-- Installing: /usr/share/OpenCV/testdata/cv/optflow/RubberWhale.flo
-- Installing: /usr/share/OpenCV/testdata/cv/optflow/lk_prev.dat
-- Installing: /usr/share/OpenCV/testdata/cv/optflow/rock_2.bmp
-- Installing: /usr/share/OpenCV/testdata/cv/optflow/RubberWhale2.png
-- Installing: /usr/share/OpenCV/testdata/cv/optflow/tvl1_flow.flo
-- Installing: /usr/share/OpenCV/testdata/cv/fast
-- Installing: /usr/share/OpenCV/testdata/cv/fast/result2.xml
-- Installing: /usr/share/OpenCV/testdata/cv/fast/result1.xml
-- Installing: /usr/share/OpenCV/testdata/cv/fast/result0.xml
-- Installing: /usr/share/OpenCV/testdata/cv/cvtcolor
-- Installing: /usr/share/OpenCV/testdata/cv/cvtcolor/bayer_gold.png
-- Installing: /usr/share/OpenCV/testdata/cv/cvtcolor/bayerVNG_gold.png
-- Installing: /usr/share/OpenCV/testdata/cv/cvtcolor/bayer_input.png
-- Installing: /usr/share/OpenCV/testdata/cv/stereo
-- Installing: /usr/share/OpenCV/testdata/cv/stereo/case1
-- Installing: /usr/share/OpenCV/testdata/cv/stereo/case1/left02.png
-- Installing: /usr/share/OpenCV/testdata/cv/stereo/case1/left11.png
-- Installing: /usr/share/OpenCV/testdata/cv/stereo/case1/left09.png
-- Installing: /usr/share/OpenCV/testdata/cv/stereo/case1/right07.png
-- Installing: /usr/share/OpenCV/testdata/cv/stereo/case1/right03.png
-- Installing: /usr/share/OpenCV/testdata/cv/stereo/case1/left01.png
-- Installing: /usr/share/OpenCV/testdata/cv/stereo/case1/left03.png
-- Installing: /usr/share/OpenCV/testdata/cv/stereo/case1/right13.png
-- Installing: /usr/share/OpenCV/testdata/cv/stereo/case1/right12.png
-- Installing: /usr/share/OpenCV/testdata/cv/stereo/case1/right06.png
-- Installing: /usr/share/OpenCV/testdata/cv/stereo/case1/right04.png
-- Installing: /usr/share/OpenCV/testdata/cv/stereo/case1/left04.png
-- Installing: /usr/share/OpenCV/testdata/cv/stereo/case1/right08.png
-- Installing: /usr/share/OpenCV/testdata/cv/stereo/case1/right01.png
-- Installing: /usr/share/OpenCV/testdata/cv/stereo/case1/right02.png
-- Installing: /usr/share/OpenCV/testdata/cv/stereo/case1/stereo_calib.txt
-- Installing: /usr/share/OpenCV/testdata/cv/stereo/case1/left14.png
-- Installing: /usr/share/OpenCV/testdata/cv/stereo/case1/left05.png
-- Installing: /usr/share/OpenCV/testdata/cv/stereo/case1/right09.png
-- Installing: /usr/share/OpenCV/testdata/cv/stereo/case1/left06.png
-- Installing: /usr/share/OpenCV/testdata/cv/stereo/case1/left13.png
-- Installing: /usr/share/OpenCV/testdata/cv/stereo/case1/right05.png
-- Installing: /usr/share/OpenCV/testdata/cv/stereo/case1/right14.png
-- Installing: /usr/share/OpenCV/testdata/cv/stereo/case1/left08.png
-- Installing: /usr/share/OpenCV/testdata/cv/stereo/case1/left12.png
-- Installing: /usr/share/OpenCV/testdata/cv/stereo/case1/left07.png
-- Installing: /usr/share/OpenCV/testdata/cv/stereo/case1/right11.png
-- Installing: /usr/share/OpenCV/testdata/cv/agast
-- Installing: /usr/share/OpenCV/testdata/cv/agast/result2.xml
-- Installing: /usr/share/OpenCV/testdata/cv/agast/result1.xml
-- Installing: /usr/share/OpenCV/testdata/cv/agast/result0.xml
-- Installing: /usr/share/OpenCV/testdata/cv/connectedcomponents
-- Installing: /usr/share/OpenCV/testdata/cv/connectedcomponents/ccomp_exp.png
-- Installing: /usr/share/OpenCV/testdata/cv/connectedcomponents/concentric_circles.png
-- Installing: /usr/share/OpenCV/testdata/cv/sfm
-- Installing: /usr/share/OpenCV/testdata/cv/sfm/backyard_tracks.txt
-- Installing: /usr/share/OpenCV/testdata/cv/sfm/backyard.blend
-- Installing: /usr/share/OpenCV/testdata/cv/features2d
-- Installing: /usr/share/OpenCV/testdata/cv/features2d/descriptor_extractors
-- Installing: /usr/share/OpenCV/testdata/cv/features2d/descriptor_extractors/descriptor-latch
-- Installing: /usr/share/OpenCV/testdata/cv/features2d/descriptor_extractors/descriptor-kaze_keypoints.xml.gz
-- Installing: /usr/share/OpenCV/testdata/cv/features2d/descriptor_extractors/descriptor-orb
-- Installing: /usr/share/OpenCV/testdata/cv/features2d/descriptor_extractors/descriptor-boostdesc-lbgm
-- Installing: /usr/share/OpenCV/testdata/cv/features2d/descriptor_extractors/descriptor-boostdesc-bgm_hard
-- Installing: /usr/share/OpenCV/testdata/cv/features2d/descriptor_extractors/descriptor-brief
-- Installing: /usr/share/OpenCV/testdata/cv/features2d/descriptor_extractors/descriptor-boostdesc-bgm_bilinear
-- Installing: /usr/share/OpenCV/testdata/cv/features2d/descriptor_extractors/descriptor-boostdesc-binboost_64
-- Installing: /usr/share/OpenCV/testdata/cv/features2d/descriptor_extractors/descriptor-brisk
-- Installing: /usr/share/OpenCV/testdata/cv/features2d/descriptor_extractors/descriptor-opponent-surf
-- Installing: /usr/share/OpenCV/testdata/cv/features2d/descriptor_extractors/descriptor-sift
-- Installing: /usr/share/OpenCV/testdata/cv/features2d/descriptor_extractors/descriptor-boostdesc-binboost_256
-- Installing: /usr/share/OpenCV/testdata/cv/features2d/descriptor_extractors/descriptor-akaze-with-kaze-desc
-- Installing: /usr/share/OpenCV/testdata/cv/features2d/descriptor_extractors/descriptor-opponent-sift
-- Installing: /usr/share/OpenCV/testdata/cv/features2d/descriptor_extractors/descriptor-surf
-- Installing: /usr/share/OpenCV/testdata/cv/features2d/descriptor_extractors/descriptor-boostdesc-bgm
-- Installing: /usr/share/OpenCV/testdata/cv/features2d/descriptor_extractors/descriptor-lucid
-- Installing: /usr/share/OpenCV/testdata/cv/features2d/descriptor_extractors/descriptor-akaze-with-kaze-desc_keypoints.xml.gz
-- Installing: /usr/share/OpenCV/testdata/cv/features2d/descriptor_extractors/descriptor-boostdesc-binboost_128
-- Installing: /usr/share/OpenCV/testdata/cv/features2d/descriptor_extractors/descriptor-akaze_keypoints.xml.gz
-- Installing: /usr/share/OpenCV/testdata/cv/features2d/descriptor_extractors/descriptor-daisy
-- Installing: /usr/share/OpenCV/testdata/cv/features2d/descriptor_extractors/descriptor-freak
-- Installing: /usr/share/OpenCV/testdata/cv/features2d/descriptor_extractors/descriptor-akaze
-- Installing: /usr/share/OpenCV/testdata/cv/features2d/descriptor_extractors/descriptor-calonder-uchar
-- Installing: /usr/share/OpenCV/testdata/cv/features2d/descriptor_extractors/descriptor-calonder-float
-- Installing: /usr/share/OpenCV/testdata/cv/features2d/descriptor_extractors/descriptor-opponent-brief
-- Installing: /usr/share/OpenCV/testdata/cv/features2d/descriptor_extractors/descriptor-kaze
-- Installing: /usr/share/OpenCV/testdata/cv/features2d/descriptor_extractors/descriptor-vgg
-- Installing: /usr/share/OpenCV/testdata/cv/features2d/feature_detectors
-- Installing: /usr/share/OpenCV/testdata/cv/features2d/feature_detectors/detector-agast.xml.gz
-- Installing: /usr/share/OpenCV/testdata/cv/features2d/feature_detectors/detector-akaze-with-kaze-desc.xml.gz
-- Installing: /usr/share/OpenCV/testdata/cv/features2d/feature_detectors/detector-akaze.xml.gz
-- Installing: /usr/share/OpenCV/testdata/cv/features2d/feature_detectors/detector-star.xml.gz
-- Installing: /usr/share/OpenCV/testdata/cv/features2d/feature_detectors/detector-harris.xml.gz
-- Installing: /usr/share/OpenCV/testdata/cv/features2d/feature_detectors/detector-sift.xml.gz
-- Installing: /usr/share/OpenCV/testdata/cv/features2d/feature_detectors/detector-kaze.xml.gz
-- Installing: /usr/share/OpenCV/testdata/cv/features2d/feature_detectors/detector-orb.xml.gz
-- Installing: /usr/share/OpenCV/testdata/cv/features2d/feature_detectors/detector-pyramid-fast.xml.gz
-- Installing: /usr/share/OpenCV/testdata/cv/features2d/feature_detectors/detector-grid-fast.xml.gz
-- Installing: /usr/share/OpenCV/testdata/cv/features2d/feature_detectors/detector-mser.xml.gz
-- Installing: /usr/share/OpenCV/testdata/cv/features2d/feature_detectors/detector-brisk.xml.gz
-- Installing: /usr/share/OpenCV/testdata/cv/features2d/feature_detectors/detector-gftt.xml.gz
-- Installing: /usr/share/OpenCV/testdata/cv/features2d/feature_detectors/detector-surf.xml.gz
-- Installing: /usr/share/OpenCV/testdata/cv/features2d/feature_detectors/detector-fast.xml.gz
-- Installing: /usr/share/OpenCV/testdata/cv/features2d/tsukuba.png
-- Installing: /usr/share/OpenCV/testdata/cv/features2d/calonder_classifier.rtc
-- Installing: /usr/share/OpenCV/testdata/cv/features2d/keypoints.xml.gz
-- Installing: /usr/share/OpenCV/testdata/cv/npr
-- Installing: /usr/share/OpenCV/testdata/cv/npr/pencil_sketch_reference.png
-- Installing: /usr/share/OpenCV/testdata/cv/npr/smooth_NCF.png
-- Installing: /usr/share/OpenCV/testdata/cv/npr/stylized_reference.png
-- Installing: /usr/share/OpenCV/testdata/cv/npr/detail_enhanced_reference.png
-- Installing: /usr/share/OpenCV/testdata/cv/npr/test1.png
-- Installing: /usr/share/OpenCV/testdata/cv/npr/test3.png
-- Installing: /usr/share/OpenCV/testdata/cv/npr/test4.png
-- Installing: /usr/share/OpenCV/testdata/cv/npr/smooth_RF.png
-- Installing: /usr/share/OpenCV/testdata/cv/npr/smoothened_NCF_reference.png
-- Installing: /usr/share/OpenCV/testdata/cv/npr/color_pencil_sketch_reference.png
-- Installing: /usr/share/OpenCV/testdata/cv/npr/smoothened_RF_reference.png
-- Installing: /usr/share/OpenCV/testdata/cv/npr/test2.png
-- Installing: /usr/share/OpenCV/testdata/cv/sparse_match_interpolator
-- Installing: /usr/share/OpenCV/testdata/cv/sparse_match_interpolator/RubberWhale_reference_result.flo
-- Installing: /usr/share/OpenCV/testdata/cv/sparse_match_interpolator/RubberWhale_sparse_matches.txt
-- Installing: /usr/share/OpenCV/testdata/cv/fuzzy
-- Installing: /usr/share/OpenCV/testdata/cv/fuzzy/exp1.png
-- Installing: /usr/share/OpenCV/testdata/cv/fuzzy/mask1.png
-- Installing: /usr/share/OpenCV/testdata/cv/fuzzy/exp5.png
-- Installing: /usr/share/OpenCV/testdata/cv/fuzzy/exp6.png
-- Installing: /usr/share/OpenCV/testdata/cv/fuzzy/mask2.png
-- Installing: /usr/share/OpenCV/testdata/cv/fuzzy/exp3.png
-- Installing: /usr/share/OpenCV/testdata/cv/fuzzy/orig.png
-- Installing: /usr/share/OpenCV/testdata/cv/fuzzy/exp2.png
-- Installing: /usr/share/OpenCV/testdata/cv/fuzzy/exp4.png
-- Installing: /usr/share/OpenCV/testdata/cv/mser
-- Installing: /usr/share/OpenCV/testdata/cv/mser/mser_test.png
-- Installing: /usr/share/OpenCV/testdata/cv/mser/mser_test2.png
-- Installing: /usr/share/OpenCV/testdata/cv/mser/boxes.txt
-- Installing: /usr/share/OpenCV/testdata/cv/mser/puzzle.png
-- Installing: /usr/share/OpenCV/testdata/cv/watershed
-- Installing: /usr/share/OpenCV/testdata/cv/watershed/wshed_exp.png
-- Installing: /usr/share/OpenCV/testdata/cv/watershed/comp.xml
-- Installing: /usr/share/OpenCV/testdata/cv/watershed/wshed_segments.png
-- Installing: /usr/share/OpenCV/testdata/cv/reg
-- Installing: /usr/share/OpenCV/testdata/cv/reg/home.png
-- Installing: /usr/share/OpenCV/testdata/cv/imgproc
-- Installing: /usr/share/OpenCV/testdata/cv/imgproc/HoughLines.xml
-- Installing: /usr/share/OpenCV/testdata/cv/imgproc/HoughLinesP.xml
-- Installing: /usr/share/OpenCV/testdata/cv/detectors
-- Installing: /usr/share/OpenCV/testdata/cv/detectors/star.xml
-- Installing: /usr/share/OpenCV/testdata/cv/detectors/surf.xml
-- Installing: /usr/share/OpenCV/testdata/cv/video
-- Installing: /usr/share/OpenCV/testdata/cv/video/768x576.avi
-- Installing: /usr/share/OpenCV/testdata/cv/video/1920x1080.avi
-- Installing: /usr/share/OpenCV/testdata/cv/snakes
-- Installing: /usr/share/OpenCV/testdata/cv/snakes/ring.bmp
-- Installing: /usr/share/OpenCV/testdata/cv/snakes/square.bmp
-- Installing: /usr/share/OpenCV/testdata/cv/snakes/ring.txt
-- Installing: /usr/share/OpenCV/testdata/cv/snakes/square.txt
-- Installing: /usr/share/OpenCV/testdata/cv/vstab
-- Installing: /usr/share/OpenCV/testdata/cv/vstab/map_world.jpg
-- Installing: /usr/share/OpenCV/testdata/cv/inpaint
-- Installing: /usr/share/OpenCV/testdata/cv/inpaint/exp1.png
-- Installing: /usr/share/OpenCV/testdata/cv/inpaint/mask.png
-- Installing: /usr/share/OpenCV/testdata/cv/inpaint/orig.png
-- Installing: /usr/share/OpenCV/testdata/cv/inpaint/exp2.png
-- Installing: /usr/share/OpenCV/testdata/superres
-- Installing: /usr/share/OpenCV/testdata/superres/car.avi
-- Installing: /usr/share/OpenCV/testdata/python
-- Installing: /usr/share/OpenCV/testdata/python/images
-- Installing: /usr/share/OpenCV/testdata/python/images/cvCreateTrackbar.jpg
-- Installing: /usr/share/OpenCV/testdata/python/images/QCIF_28.bmp
-- Installing: /usr/share/OpenCV/testdata/python/images/QCIF_12.bmp
-- Installing: /usr/share/OpenCV/testdata/python/images/QCIF_24.bmp
-- Installing: /usr/share/OpenCV/testdata/python/images/QCIF_06.bmp
-- Installing: /usr/share/OpenCV/testdata/python/images/QCIF_10.bmp
-- Installing: /usr/share/OpenCV/testdata/python/images/baboon.bmp
-- Installing: /usr/share/OpenCV/testdata/python/images/QCIF_16.bmp
-- Installing: /usr/share/OpenCV/testdata/python/images/QCIF_15.bmp
-- Installing: /usr/share/OpenCV/testdata/python/images/QCIF_19.bmp
-- Installing: /usr/share/OpenCV/testdata/python/images/baboon.png
-- Installing: /usr/share/OpenCV/testdata/python/images/cvWaitKey.jpg
-- Installing: /usr/share/OpenCV/testdata/python/images/QCIF_14.bmp
-- Installing: /usr/share/OpenCV/testdata/python/images/cvShowImage.jpg
-- Installing: /usr/share/OpenCV/testdata/python/images/QCIF_11.bmp
-- Installing: /usr/share/OpenCV/testdata/python/images/QCIF_25.bmp
-- Installing: /usr/share/OpenCV/testdata/python/images/baboon_256x256.sr
-- Installing: /usr/share/OpenCV/testdata/python/images/QCIF_17.bmp
-- Installing: /usr/share/OpenCV/testdata/python/images/baboon.jpg
-- Installing: /usr/share/OpenCV/testdata/python/images/QCIF_02.bmp
-- Installing: /usr/share/OpenCV/testdata/python/images/cvSetMouseCallback.jpg
-- Installing: /usr/share/OpenCV/testdata/python/images/baboon_256x256.tiff
-- Installing: /usr/share/OpenCV/testdata/python/images/baboon_256x256.bmp
-- Installing: /usr/share/OpenCV/testdata/python/images/QCIF_18.bmp
-- Installing: /usr/share/OpenCV/testdata/python/images/QCIF_27.bmp
-- Installing: /usr/share/OpenCV/testdata/python/images/QCIF_22.bmp
-- Installing: /usr/share/OpenCV/testdata/python/images/baboon_256x256.jpg
-- Installing: /usr/share/OpenCV/testdata/python/images/QCIF_20.bmp
-- Installing: /usr/share/OpenCV/testdata/python/images/QCIF_01.bmp
-- Installing: /usr/share/OpenCV/testdata/python/images/QCIF_03.bmp
-- Installing: /usr/share/OpenCV/testdata/python/images/baboon.gif
-- Installing: /usr/share/OpenCV/testdata/python/images/baboon.tiff
-- Installing: /usr/share/OpenCV/testdata/python/images/QCIF_00.bmp
-- Installing: /usr/share/OpenCV/testdata/python/images/baboon_256x256.tif
-- Installing: /usr/share/OpenCV/testdata/python/images/QCIF_13.bmp
-- Installing: /usr/share/OpenCV/testdata/python/images/baboon.ppm
-- Installing: /usr/share/OpenCV/testdata/python/images/QCIF_26.bmp
-- Installing: /usr/share/OpenCV/testdata/python/images/baboon_256x256.png
-- Installing: /usr/share/OpenCV/testdata/python/images/baboon_256x256.gif
-- Installing: /usr/share/OpenCV/testdata/python/images/QCIF_07.bmp
-- Installing: /usr/share/OpenCV/testdata/python/images/baboon_256x256.ppm
-- Installing: /usr/share/OpenCV/testdata/python/images/QCIF_29.bmp
-- Installing: /usr/share/OpenCV/testdata/python/images/QCIF_05.bmp
-- Installing: /usr/share/OpenCV/testdata/python/images/QCIF_09.bmp
-- Installing: /usr/share/OpenCV/testdata/python/images/QCIF_23.bmp
-- Installing: /usr/share/OpenCV/testdata/python/images/QCIF_08.bmp
-- Installing: /usr/share/OpenCV/testdata/python/images/QCIF_21.bmp
-- Installing: /usr/share/OpenCV/testdata/python/images/QCIF_04.bmp
-- Installing: /usr/share/OpenCV/testdata/python/videos
-- Installing: /usr/share/OpenCV/testdata/python/videos/dv_pal_progressive.dv
-- Installing: /usr/share/OpenCV/testdata/python/videos/qcif_RGBA.avi
-- Installing: /usr/share/OpenCV/testdata/python/videos/uncompressed.avi
-- Installing: /usr/share/OpenCV/testdata/python/videos/qcif_YVU9.avi
-- Installing: /usr/share/OpenCV/testdata/python/videos/qcif_Y8.avi
-- Installing: /usr/share/OpenCV/testdata/python/videos/3gp.3gp
-- Installing: /usr/share/OpenCV/testdata/python/videos/qcif_YUY2.avi
-- Installing: /usr/share/OpenCV/testdata/python/videos/huffyuv.avi
-- Installing: /usr/share/OpenCV/testdata/python/videos/bmp32.avi
-- Installing: /usr/share/OpenCV/testdata/python/videos/cinepak.avi
-- Installing: /usr/share/OpenCV/testdata/python/videos/qcif_YV16.avi
-- Installing: /usr/share/OpenCV/testdata/python/videos/qcif_RGB.avi
-- Installing: /usr/share/OpenCV/testdata/python/videos/divx.avi
-- Installing: /usr/share/OpenCV/testdata/python/videos/mpeg4.mp4
-- Installing: /usr/share/OpenCV/testdata/python/videos/qcif_YV12.avi
-- Installing: /usr/share/OpenCV/testdata/python/videos/qcif_UYVY.avi
-- Installing: /usr/share/OpenCV/testdata/python/videos/indeo.avi
-- Installing: /usr/share/OpenCV/testdata/python/videos/wmv9.avi
-- Installing: /usr/share/OpenCV/testdata/python/videos/dv_pal_progressive.avi
-- Installing: /usr/share/OpenCV/testdata/python/videos/bmp24.avi
-- Installing: /usr/share/OpenCV/testdata/viz
-- Installing: /usr/share/OpenCV/testdata/viz/dragon.ply
-- Installing: /usr/share/OpenCV/testdata/viz/lena.png
-- Installing: /usr/share/OpenCV/testdata/dnn
-- Installing: /usr/share/OpenCV/testdata/dnn/halide_scheduler_squeezenet_v1_1.yml
-- Installing: /usr/share/OpenCV/testdata/dnn/gtsrb.prototxt
-- Installing: /usr/share/OpenCV/testdata/dnn/street.png
-- Installing: /usr/share/OpenCV/testdata/dnn/bvlc_alexnet.prototxt
-- Installing: /usr/share/OpenCV/testdata/dnn/ssd_vgg16.prototxt
-- Installing: /usr/share/OpenCV/testdata/dnn/halide_scheduler_opencl_resnet_50.yml
-- Installing: /usr/share/OpenCV/testdata/dnn/tf_inception_prob.npy
-- Installing: /usr/share/OpenCV/testdata/dnn/torch_enet_prob.npy
-- Installing: /usr/share/OpenCV/testdata/dnn/ResNet-50-deploy.prototxt
-- Installing: /usr/share/OpenCV/testdata/dnn/.gitignore
-- Installing: /usr/share/OpenCV/testdata/dnn/halide_scheduler_alexnet.yml
-- Installing: /usr/share/OpenCV/testdata/dnn/img_classes_inception.txt
-- Installing: /usr/share/OpenCV/testdata/dnn/caffe_fcn8s_prob.npy
-- Installing: /usr/share/OpenCV/testdata/dnn/halide_scheduler_opencl_alexnet.yml
-- Installing: /usr/share/OpenCV/testdata/dnn/squeezenet_v1.1.prototxt
-- Installing: /usr/share/OpenCV/testdata/dnn/torch
-- Installing: /usr/share/OpenCV/testdata/dnn/torch/net_reshape_single_sample_net.txt
-- Installing: /usr/share/OpenCV/testdata/dnn/torch/net_deconv_input.txt
-- Installing: /usr/share/OpenCV/testdata/dnn/torch/net_linear_2d_output.txt
-- Installing: /usr/share/OpenCV/testdata/dnn/torch/net_cadd_table_input.txt
-- Installing: /usr/share/OpenCV/testdata/dnn/torch/net_logsoftmax_input.txt
-- Installing: /usr/share/OpenCV/testdata/dnn/torch/net_linear_2d_net.txt
-- Installing: /usr/share/OpenCV/testdata/dnn/torch/net_reshape_output.txt
-- Installing: /usr/share/OpenCV/testdata/dnn/torch/torch_gen_test_data.lua
-- Installing: /usr/share/OpenCV/testdata/dnn/torch/net_prelu_net.txt
-- Installing: /usr/share/OpenCV/testdata/dnn/torch/net_softmax_spatial_output.txt
-- Installing: /usr/share/OpenCV/testdata/dnn/torch/net_reshape_batch_input.txt
-- Installing: /usr/share/OpenCV/testdata/dnn/torch/torch_nn_echo.lua
-- Installing: /usr/share/OpenCV/testdata/dnn/torch/net_softmax_output.txt
-- Installing: /usr/share/OpenCV/testdata/dnn/torch/net_reshape_net.txt
-- Installing: /usr/share/OpenCV/testdata/dnn/torch/net_prelu_output.txt
-- Installing: /usr/share/OpenCV/testdata/dnn/torch/net_pool_max_output.txt
-- Installing: /usr/share/OpenCV/testdata/dnn/torch/net_softmax_input.txt
-- Installing: /usr/share/OpenCV/testdata/dnn/torch/net_concat_output.txt
-- Installing: /usr/share/OpenCV/testdata/dnn/torch/net_pool_ave_input.txt
-- Installing: /usr/share/OpenCV/testdata/dnn/torch/net_batch_norm_net.txt
-- Installing: /usr/share/OpenCV/testdata/dnn/torch/net_pool_ave_output.txt
-- Installing: /usr/share/OpenCV/testdata/dnn/torch/net_parallel_output.txt
-- Installing: /usr/share/OpenCV/testdata/dnn/torch/net_simple_net.txt
-- Installing: /usr/share/OpenCV/testdata/dnn/torch/net_simple_output.txt
-- Installing: /usr/share/OpenCV/testdata/dnn/torch/net_concat_input.txt
-- Installing: /usr/share/OpenCV/testdata/dnn/torch/net_reshape_single_sample_input.txt
-- Installing: /usr/share/OpenCV/testdata/dnn/torch/net_batch_norm_output.txt
-- Installing: /usr/share/OpenCV/testdata/dnn/torch/net_simple_input.txt
-- Installing: /usr/share/OpenCV/testdata/dnn/torch/net_prelu_input.txt
-- Installing: /usr/share/OpenCV/testdata/dnn/torch/net_conv_net.txt
-- Installing: /usr/share/OpenCV/testdata/dnn/torch/net_logsoftmax_spatial_output.txt
-- Installing: /usr/share/OpenCV/testdata/dnn/torch/net_parallel_input.txt
-- Installing: /usr/share/OpenCV/testdata/dnn/torch/net_logsoftmax_net.txt
-- Installing: /usr/share/OpenCV/testdata/dnn/torch/net_pool_max_output_2.txt
-- Installing: /usr/share/OpenCV/testdata/dnn/torch/net_reshape_batch_net.txt
-- Installing: /usr/share/OpenCV/testdata/dnn/torch/net_pool_max_net.txt
-- Installing: /usr/share/OpenCV/testdata/dnn/torch/net_pool_max_input.txt
-- Installing: /usr/share/OpenCV/testdata/dnn/torch/net_softmax_net.txt
-- Installing: /usr/share/OpenCV/testdata/dnn/torch/net_cadd_table_output.txt
-- Installing: /usr/share/OpenCV/testdata/dnn/torch/net_cadd_table_net.txt
-- Installing: /usr/share/OpenCV/testdata/dnn/torch/net_logsoftmax_spatial_net.txt
-- Installing: /usr/share/OpenCV/testdata/dnn/torch/net_reshape_input.txt
-- Installing: /usr/share/OpenCV/testdata/dnn/torch/net_concat_net.txt
-- Installing: /usr/share/OpenCV/testdata/dnn/torch/net_pool_ave_net.txt
-- Installing: /usr/share/OpenCV/testdata/dnn/torch/net_conv_output.txt
-- Installing: /usr/share/OpenCV/testdata/dnn/torch/net_reshape_single_sample_output.txt
-- Installing: /usr/share/OpenCV/testdata/dnn/torch/net_logsoftmax_output.txt
-- Installing: /usr/share/OpenCV/testdata/dnn/torch/net_batch_norm_input.txt
-- Installing: /usr/share/OpenCV/testdata/dnn/torch/net_softmax_spatial_net.txt
-- Installing: /usr/share/OpenCV/testdata/dnn/torch/net_parallel_net.txt
-- Installing: /usr/share/OpenCV/testdata/dnn/torch/net_deconv_net.txt
-- Installing: /usr/share/OpenCV/testdata/dnn/torch/net_conv_input.txt
-- Installing: /usr/share/OpenCV/testdata/dnn/torch/net_logsoftmax_spatial_input.txt
-- Installing: /usr/share/OpenCV/testdata/dnn/torch/net_linear_2d_input.txt
-- Installing: /usr/share/OpenCV/testdata/dnn/torch/net_reshape_batch_output.txt
-- Installing: /usr/share/OpenCV/testdata/dnn/torch/net_softmax_spatial_input.txt
-- Installing: /usr/share/OpenCV/testdata/dnn/torch/net_deconv_output.txt
-- Installing: /usr/share/OpenCV/testdata/dnn/googlenet_0.png
-- Installing: /usr/share/OpenCV/testdata/dnn/layers
-- Installing: /usr/share/OpenCV/testdata/dnn/layers/layer_mvn.prototxt
-- Installing: /usr/share/OpenCV/testdata/dnn/layers/layer_deconvolution.caffemodel
-- Installing: /usr/share/OpenCV/testdata/dnn/layers/layer_dropout.prototxt
-- Installing: /usr/share/OpenCV/testdata/dnn/layers/layer_inner_product.prototxt
-- Installing: /usr/share/OpenCV/testdata/dnn/layers/layer_lrn_channels.npy
-- Installing: /usr/share/OpenCV/testdata/dnn/layers/rnn.prototxt.w_0.npy
-- Installing: /usr/share/OpenCV/testdata/dnn/layers/rnn.input.npy
-- Installing: /usr/share/OpenCV/testdata/dnn/layers/layer_dropout.npy
-- Installing: /usr/share/OpenCV/testdata/dnn/layers/layer_lrn_channels.prototxt
-- Installing: /usr/share/OpenCV/testdata/dnn/layers/layer_relu.prototxt
-- Installing: /usr/share/OpenCV/testdata/dnn/layers/rnn.prototxt.w_4.npy
-- Installing: /usr/share/OpenCV/testdata/dnn/layers/layer_concat.prototxt
-- Installing: /usr/share/OpenCV/testdata/dnn/layers/layer_inner_product.npy
-- Installing: /usr/share/OpenCV/testdata/dnn/layers/layer_elu_model.pb
-- Installing: /usr/share/OpenCV/testdata/dnn/layers/layer_inner_product.caffemodel
-- Installing: /usr/share/OpenCV/testdata/dnn/layers/rnn.prototxt.w_1.npy
-- Installing: /usr/share/OpenCV/testdata/dnn/layers/layer_convolution.npy
-- Installing: /usr/share/OpenCV/testdata/dnn/layers/layer_softmax.npy
-- Installing: /usr/share/OpenCV/testdata/dnn/layers/layer_lrn_spatial.npy
-- Installing: /usr/share/OpenCV/testdata/dnn/layers/layer_elu_in.npy
-- Installing: /usr/share/OpenCV/testdata/dnn/layers/layer_batch_norm.prototxt
-- Installing: /usr/share/OpenCV/testdata/dnn/layers/layer_pooling_max.prototxt
-- Installing: /usr/share/OpenCV/testdata/dnn/layers/rnn.prototxt.h_1.npy
-- Installing: /usr/share/OpenCV/testdata/dnn/layers/layer_elu_out.npy
-- Installing: /usr/share/OpenCV/testdata/dnn/layers/layer_deconvolution.input.npy
-- Installing: /usr/share/OpenCV/testdata/dnn/layers/lstm.prototxt.w_0.npy
-- Installing: /usr/share/OpenCV/testdata/dnn/layers/layer_concat.npy
-- Installing: /usr/share/OpenCV/testdata/dnn/layers/rnn.prototxt.w_3.npy
-- Installing: /usr/share/OpenCV/testdata/dnn/layers/lstm.prototxt.w_2.npy
-- Installing: /usr/share/OpenCV/testdata/dnn/layers/layer_deconvolution.npy
-- Installing: /usr/share/OpenCV/testdata/dnn/layers/layer_batch_norm.caffemodel
-- Installing: /usr/share/OpenCV/testdata/dnn/layers/run.py
-- Installing: /usr/share/OpenCV/testdata/dnn/layers/lstm.prototxt.h_1.npy
-- Installing: /usr/share/OpenCV/testdata/dnn/layers/recurrent.input.npy
-- Installing: /usr/share/OpenCV/testdata/dnn/layers/layer_convolution.caffemodel
-- Installing: /usr/share/OpenCV/testdata/dnn/layers/blob.npy
-- Installing: /usr/share/OpenCV/testdata/dnn/layers/layer_pooling_max.npy
-- Installing: /usr/share/OpenCV/testdata/dnn/layers/layer_pooling_ave.prototxt
-- Installing: /usr/share/OpenCV/testdata/dnn/layers/layer_pooling_ave.npy
-- Installing: /usr/share/OpenCV/testdata/dnn/layers/layer_relu.npy
-- Installing: /usr/share/OpenCV/testdata/dnn/layers/lstm.prototxt.w_1.npy
-- Installing: /usr/share/OpenCV/testdata/dnn/layers/layer_batch_norm.npy
-- Installing: /usr/share/OpenCV/testdata/dnn/layers/layer_deconvolution.prototxt
-- Installing: /usr/share/OpenCV/testdata/dnn/layers/reshape_and_slice_routines.prototxt
-- Installing: /usr/share/OpenCV/testdata/dnn/layers/rnn.prototxt.w_2.npy
-- Installing: /usr/share/OpenCV/testdata/dnn/layers/layer_softmax.prototxt
-- Installing: /usr/share/OpenCV/testdata/dnn/layers/layer_mvn.npy
-- Installing: /usr/share/OpenCV/testdata/dnn/layers/layer_lrn_spatial.prototxt
-- Installing: /usr/share/OpenCV/testdata/dnn/layers/layer_convolution.prototxt
-- Installing: /usr/share/OpenCV/testdata/dnn/googlenet_inception_4c#1x1.npy
-- Installing: /usr/share/OpenCV/testdata/dnn/halide_scheduler_opencl_inception_5h.yml
-- Installing: /usr/share/OpenCV/testdata/dnn/halide_scheduler_opencl_enet.yml
-- Installing: /usr/share/OpenCV/testdata/dnn/caffe_alexnet_prob.npy
-- Installing: /usr/share/OpenCV/testdata/dnn/resnet50_prob.npy
-- Installing: /usr/share/OpenCV/testdata/dnn/fcn8s-heavy-pascal.prototxt
-- Installing: /usr/share/OpenCV/testdata/dnn/tensorflow
-- Installing: /usr/share/OpenCV/testdata/dnn/tensorflow/max_pool_even_in.npy
-- Installing: /usr/share/OpenCV/testdata/dnn/tensorflow/eltwise_add_mul_out.npy
-- Installing: /usr/share/OpenCV/testdata/dnn/tensorflow/max_pool_odd_same_in.npy
-- Installing: /usr/share/OpenCV/testdata/dnn/tensorflow/padding_same_out.npy
-- Installing: /usr/share/OpenCV/testdata/dnn/tensorflow/padding_same_in.npy
-- Installing: /usr/share/OpenCV/testdata/dnn/tensorflow/max_pool_odd_same_net.pb
-- Installing: /usr/share/OpenCV/testdata/dnn/tensorflow/max_pool_even_out.npy
-- Installing: /usr/share/OpenCV/testdata/dnn/tensorflow/fused_batch_norm_net.pb
-- Installing: /usr/share/OpenCV/testdata/dnn/tensorflow/fused_batch_norm_out.npy
-- Installing: /usr/share/OpenCV/testdata/dnn/tensorflow/eltwise_add_mul_in.npy
-- Installing: /usr/share/OpenCV/testdata/dnn/tensorflow/padding_valid_out.npy
-- Installing: /usr/share/OpenCV/testdata/dnn/tensorflow/max_pool_even_net.pb
-- Installing: /usr/share/OpenCV/testdata/dnn/tensorflow/pad_and_concat_in.npy
-- Installing: /usr/share/OpenCV/testdata/dnn/tensorflow/padding_same_net.pb
-- Installing: /usr/share/OpenCV/testdata/dnn/tensorflow/pad_and_concat_net.pb
-- Installing: /usr/share/OpenCV/testdata/dnn/tensorflow/generate_tf_models.py
-- Installing: /usr/share/OpenCV/testdata/dnn/tensorflow/padding_valid_in.npy
-- Installing: /usr/share/OpenCV/testdata/dnn/tensorflow/max_pool_odd_same_out.npy
-- Installing: /usr/share/OpenCV/testdata/dnn/tensorflow/max_pool_odd_valid_out.npy
-- Installing: /usr/share/OpenCV/testdata/dnn/tensorflow/single_conv_net.pb
-- Installing: /usr/share/OpenCV/testdata/dnn/tensorflow/padding_valid_net.pb
-- Installing: /usr/share/OpenCV/testdata/dnn/tensorflow/max_pool_odd_valid_net.pb
-- Installing: /usr/share/OpenCV/testdata/dnn/tensorflow/max_pool_odd_valid_in.npy
-- Installing: /usr/share/OpenCV/testdata/dnn/tensorflow/fused_batch_norm_in.npy
-- Installing: /usr/share/OpenCV/testdata/dnn/tensorflow/single_conv_in.npy
-- Installing: /usr/share/OpenCV/testdata/dnn/tensorflow/single_conv_out.npy
-- Installing: /usr/share/OpenCV/testdata/dnn/tensorflow/eltwise_add_mul_net.pb
-- Installing: /usr/share/OpenCV/testdata/dnn/tensorflow/pad_and_concat_out.npy
-- Installing: /usr/share/OpenCV/testdata/dnn/googlenet_conv1#7x7_s2.npy
-- Installing: /usr/share/OpenCV/testdata/dnn/bvlc_googlenet.prototxt
-- Installing: /usr/share/OpenCV/testdata/dnn/generate_torch_models.py
-- Installing: /usr/share/OpenCV/testdata/dnn/download_models.py
-- Installing: /usr/share/OpenCV/testdata/dnn/halide_scheduler_opencl_squeezenet_v1_1.yml
-- Installing: /usr/share/OpenCV/testdata/dnn/squeezenet_v1.1_prob.npy
-- Installing: /usr/share/OpenCV/testdata/dnn/grace_hopper_227.png
-- Installing: /usr/share/OpenCV/testdata/dnn/space_shuttle.jpg
-- Installing: /usr/share/OpenCV/testdata/dnn/halide_scheduler_enet.yml
-- Installing: /usr/share/OpenCV/testdata/dnn/googlenet_conv1#relu_7x7.npy
-- Installing: /usr/share/OpenCV/testdata/dnn/halide_scheduler_resnet_50.yml
-- Installing: /usr/share/OpenCV/testdata/dnn/ssd_out.npy
-- Installing: /usr/share/OpenCV/testdata/dnn/googlenet_prob.npy
-- Installing: /usr/share/OpenCV/testdata/dnn/googlenet_1.png
-- Installing: /usr/share/OpenCV/testdata/dnn/halide_scheduler_inception_5h.yml
-- Installing: /usr/share/OpenCV/testdata/dnn/googlenet_inception_4c#relu_1x1.npy
-- Installing: /usr/share/OpenCV/testdata/stitching
-- Installing: /usr/share/OpenCV/testdata/stitching/a3.png
-- Installing: /usr/share/OpenCV/testdata/stitching/b1.png
-- Installing: /usr/share/OpenCV/testdata/stitching/newspaper1.jpg
-- Installing: /usr/share/OpenCV/testdata/stitching/budapest3.jpg
-- Installing: /usr/share/OpenCV/testdata/stitching/newspaper3.jpg
-- Installing: /usr/share/OpenCV/testdata/stitching/newspaper4.jpg
-- Installing: /usr/share/OpenCV/testdata/stitching/prague1.jpg
-- Installing: /usr/share/OpenCV/testdata/stitching/budapest5.jpg
-- Installing: /usr/share/OpenCV/testdata/stitching/boat3.jpg
-- Installing: /usr/share/OpenCV/testdata/stitching/boat4.jpg
-- Installing: /usr/share/OpenCV/testdata/stitching/boat2.jpg
-- Installing: /usr/share/OpenCV/testdata/stitching/boat5.jpg
-- Installing: /usr/share/OpenCV/testdata/stitching/warp_tst0.png
-- Installing: /usr/share/OpenCV/testdata/stitching/budapest6.jpg
-- Installing: /usr/share/OpenCV/testdata/stitching/s1.jpg
-- Installing: /usr/share/OpenCV/testdata/stitching/a_result.png
-- Installing: /usr/share/OpenCV/testdata/stitching/baboon_lena.png
-- Installing: /usr/share/OpenCV/testdata/stitching/boat6.jpg
-- Installing: /usr/share/OpenCV/testdata/stitching/budapest4.jpg
-- Installing: /usr/share/OpenCV/testdata/stitching/a2.png
-- Installing: /usr/share/OpenCV/testdata/stitching/prague2.jpg
-- Installing: /usr/share/OpenCV/testdata/stitching/b2.png
-- Installing: /usr/share/OpenCV/testdata/stitching/newspaper2.jpg
-- Installing: /usr/share/OpenCV/testdata/stitching/budapest2.jpg
-- Installing: /usr/share/OpenCV/testdata/stitching/s2.jpg
-- Installing: /usr/share/OpenCV/testdata/stitching/budapest1.jpg
-- Installing: /usr/share/OpenCV/testdata/stitching/a1.png
-- Installing: /usr/share/OpenCV/testdata/stitching/boat1.jpg
-- Installing: /usr/share/OpenCV/testdata/stitching/b_result.png
-- Installing: /usr/bin/opencv_traincascade
-- Set runtime path of "/usr/bin/opencv_traincascade" to "/usr/lib:/usr/local/cuda-8.0/lib64"
-- Installing: /usr/bin/opencv_createsamples
-- Set runtime path of "/usr/bin/opencv_createsamples" to "/usr/lib:/usr/local/cuda-8.0/lib64"
-- Installing: /usr/bin/opencv_annotation
-- Set runtime path of "/usr/bin/opencv_annotation" to "/usr/lib:/usr/local/cuda-8.0/lib64"
-- Installing: /usr/bin/opencv_visualisation
-- Set runtime path of "/usr/bin/opencv_visualisation" to "/usr/lib:/usr/local/cuda-8.0/lib64"
-- Installing: /usr/bin/opencv_interactive-calibration
-- Set runtime path of "/usr/bin/opencv_interactive-calibration" to "/usr/lib:/usr/local/cuda-8.0/lib64"
-- Installing: /usr/bin/opencv_version
-- Set runtime path of "/usr/bin/opencv_version" to "/usr/lib:/usr/local/cuda-8.0/lib64"
-- Installing: /usr/share/OpenCV/samples/cpp/phase_corr.cpp
-- Installing: /usr/share/OpenCV/samples/cpp/videocapture_starter.cpp
-- Installing: /usr/share/OpenCV/samples/cpp/openni_capture.cpp
-- Installing: /usr/share/OpenCV/samples/cpp/cloning_gui.cpp
-- Installing: /usr/share/OpenCV/samples/cpp/falsecolor.cpp
-- Installing: /usr/share/OpenCV/samples/cpp/ffilldemo.cpp
-- Installing: /usr/share/OpenCV/samples/cpp/facedetect.cpp
-- Installing: /usr/share/OpenCV/samples/cpp/inpaint.cpp
-- Installing: /usr/share/OpenCV/samples/cpp/connected_components.cpp
-- Installing: /usr/share/OpenCV/samples/cpp/autofocus.cpp
-- Installing: /usr/share/OpenCV/samples/cpp/detect_blob.cpp
-- Installing: /usr/share/OpenCV/samples/cpp/drawing.cpp
-- Installing: /usr/share/OpenCV/samples/cpp/opencv_version.cpp
-- Installing: /usr/share/OpenCV/samples/cpp/fback.cpp
-- Installing: /usr/share/OpenCV/samples/cpp/convexhull.cpp
-- Installing: /usr/share/OpenCV/samples/cpp/polar_transforms.cpp
-- Installing: /usr/share/OpenCV/samples/cpp/stereo_match.cpp
-- Installing: /usr/share/OpenCV/samples/cpp/videowriter_basic.cpp
-- Installing: /usr/share/OpenCV/samples/cpp/neural_network.cpp
-- Installing: /usr/share/OpenCV/samples/cpp/contours2.cpp
-- Installing: /usr/share/OpenCV/samples/cpp/houghcircles.cpp
-- Installing: /usr/share/OpenCV/samples/cpp/edge.cpp
-- Installing: /usr/share/OpenCV/samples/cpp/segment_objects.cpp
-- Installing: /usr/share/OpenCV/samples/cpp/distrans.cpp
-- Installing: /usr/share/OpenCV/samples/cpp/image_alignment.cpp
-- Installing: /usr/share/OpenCV/samples/cpp/lkdemo.cpp
-- Installing: /usr/share/OpenCV/samples/cpp/morphology2.cpp
-- Installing: /usr/share/OpenCV/samples/cpp/camshiftdemo.cpp
-- Installing: /usr/share/OpenCV/samples/cpp/train_HOG.cpp
-- Installing: /usr/share/OpenCV/samples/cpp/videostab.cpp
-- Installing: /usr/share/OpenCV/samples/cpp/image.cpp
-- Installing: /usr/share/OpenCV/samples/cpp/filestorage_base64.cpp
-- Installing: /usr/share/OpenCV/samples/cpp/dbt_face_detection.cpp
-- Installing: /usr/share/OpenCV/samples/cpp/filestorage.cpp
-- Installing: /usr/share/OpenCV/samples/cpp/detect_mser.cpp
-- Installing: /usr/share/OpenCV/samples/cpp/3calibration.cpp
-- Installing: /usr/share/OpenCV/samples/cpp/laplace.cpp
-- Installing: /usr/share/OpenCV/samples/cpp/pca.cpp
-- Installing: /usr/share/OpenCV/samples/cpp/select3dobj.cpp
-- Installing: /usr/share/OpenCV/samples/cpp/matchmethod_orb_akaze_brisk.cpp
-- Installing: /usr/share/OpenCV/samples/cpp/image_sequence.cpp
-- Installing: /usr/share/OpenCV/samples/cpp/kalman.cpp
-- Installing: /usr/share/OpenCV/samples/cpp/imagelist_creator.cpp
-- Installing: /usr/share/OpenCV/samples/cpp/starter_imagelist.cpp
-- Installing: /usr/share/OpenCV/samples/cpp/cloning_demo.cpp
-- Installing: /usr/share/OpenCV/samples/cpp/intelperc_capture.cpp
-- Installing: /usr/share/OpenCV/samples/cpp/stitching_detailed.cpp
-- Installing: /usr/share/OpenCV/samples/cpp/stereo_calib.cpp
-- Installing: /usr/share/OpenCV/samples/cpp/watershed.cpp
-- Installing: /usr/share/OpenCV/samples/cpp/squares.cpp
-- Installing: /usr/share/OpenCV/samples/cpp/tvl1_optical_flow.cpp
-- Installing: /usr/share/OpenCV/samples/cpp/cout_mat.cpp
-- Installing: /usr/share/OpenCV/samples/cpp/calibration.cpp
-- Installing: /usr/share/OpenCV/samples/cpp/shape_example.cpp
-- Installing: /usr/share/OpenCV/samples/cpp/lsd_lines.cpp
-- Installing: /usr/share/OpenCV/samples/cpp/kmeans.cpp
-- Installing: /usr/share/OpenCV/samples/cpp/create_mask.cpp
-- Installing: /usr/share/OpenCV/samples/cpp/logistic_regression.cpp
-- Installing: /usr/share/OpenCV/samples/cpp/em.cpp
-- Installing: /usr/share/OpenCV/samples/cpp/grabcut.cpp
-- Installing: /usr/share/OpenCV/samples/cpp/fitellipse.cpp
-- Installing: /usr/share/OpenCV/samples/cpp/application_trace.cpp
-- Installing: /usr/share/OpenCV/samples/cpp/peopledetect.cpp
-- Installing: /usr/share/OpenCV/samples/cpp/bgfg_segm.cpp
-- Installing: /usr/share/OpenCV/samples/cpp/tree_engine.cpp
-- Installing: /usr/share/OpenCV/samples/cpp/letter_recog.cpp
-- Installing: /usr/share/OpenCV/samples/cpp/train_svmsgd.cpp
-- Installing: /usr/share/OpenCV/samples/cpp/dft.cpp
-- Installing: /usr/share/OpenCV/samples/cpp/npr_demo.cpp
-- Installing: /usr/share/OpenCV/samples/cpp/mask_tmpl.cpp
-- Installing: /usr/share/OpenCV/samples/cpp/facial_features.cpp
-- Installing: /usr/share/OpenCV/samples/cpp/points_classifier.cpp
-- Installing: /usr/share/OpenCV/samples/cpp/demhist.cpp
-- Installing: /usr/share/OpenCV/samples/cpp/houghlines.cpp
-- Installing: /usr/share/OpenCV/samples/cpp/videocapture_basic.cpp
-- Installing: /usr/share/OpenCV/samples/cpp/stitching.cpp
-- Installing: /usr/share/OpenCV/samples/cpp/smiledetect.cpp
-- Installing: /usr/share/OpenCV/samples/cpp/delaunay2.cpp
-- Installing: /usr/share/OpenCV/samples/cpp/minarea.cpp
-- Installing: /usr/share/OpenCV/samples/dnn/fcn_semsegm.cpp
-- Installing: /usr/share/OpenCV/samples/dnn/ssd_mobilenet_object_detection.cpp
-- Installing: /usr/share/OpenCV/samples/dnn/caffe_googlenet.cpp
-- Installing: /usr/share/OpenCV/samples/dnn/squeezenet_halide.cpp
-- Installing: /usr/share/OpenCV/samples/dnn/ssd_object_detection.cpp
-- Installing: /usr/share/OpenCV/samples/dnn/torch_enet.cpp
-- Installing: /usr/share/OpenCV/samples/dnn/tf_inception.cpp
-- Installing: /usr/share/OpenCV/samples/gpu/performance/performance.cpp
-- Installing: /usr/share/OpenCV/samples/gpu/performance/tests.cpp
-- Installing: /usr/share/OpenCV/samples/gpu/performance/performance.h
-- Installing: /usr/share/OpenCV/samples/gpu/video_reader.cpp
-- Installing: /usr/share/OpenCV/samples/gpu/cascadeclassifier.cpp
-- Installing: /usr/share/OpenCV/samples/gpu/stereo_match.cpp
-- Installing: /usr/share/OpenCV/samples/gpu/super_resolution.cpp
-- Installing: /usr/share/OpenCV/samples/gpu/generalized_hough.cpp
-- Installing: /usr/share/OpenCV/samples/gpu/surf_keypoint_matcher.cpp
-- Installing: /usr/share/OpenCV/samples/gpu/hog.cpp
-- Installing: /usr/share/OpenCV/samples/gpu/optical_flow.cpp
-- Installing: /usr/share/OpenCV/samples/gpu/cascadeclassifier_nvidia_api.cpp
-- Installing: /usr/share/OpenCV/samples/gpu/farneback_optical_flow.cpp
-- Installing: /usr/share/OpenCV/samples/gpu/alpha_comp.cpp
-- Installing: /usr/share/OpenCV/samples/gpu/stereo_multi.cpp
-- Installing: /usr/share/OpenCV/samples/gpu/driver_api_stereo_multi.cpp
-- Installing: /usr/share/OpenCV/samples/gpu/pyrlk_optical_flow.cpp
-- Installing: /usr/share/OpenCV/samples/gpu/bgfg_segm.cpp
-- Installing: /usr/share/OpenCV/samples/gpu/multi.cpp
-- Installing: /usr/share/OpenCV/samples/gpu/driver_api_multi.cpp
-- Installing: /usr/share/OpenCV/samples/gpu/video_writer.cpp
-- Installing: /usr/share/OpenCV/samples/gpu/houghlines.cpp
-- Installing: /usr/share/OpenCV/samples/gpu/morphology.cpp
-- Installing: /usr/share/OpenCV/samples/gpu/opticalflow_nvidia_api.cpp
-- Installing: /usr/share/OpenCV/samples/gpu/opengl.cpp
-- Installing: /usr/share/OpenCV/samples/tapi/ufacedetect.cpp
-- Installing: /usr/share/OpenCV/samples/tapi/clahe.cpp
-- Installing: /usr/share/OpenCV/samples/tapi/hog.cpp
-- Installing: /usr/share/OpenCV/samples/tapi/squares.cpp
-- Installing: /usr/share/OpenCV/samples/tapi/tvl1_optical_flow.cpp
-- Installing: /usr/share/OpenCV/samples/tapi/camshift.cpp
-- Installing: /usr/share/OpenCV/samples/tapi/pyrlk_optical_flow.cpp
-- Installing: /usr/share/OpenCV/samples/tapi/bgfg_segm.cpp
nvidia@gpu:~/opencv/build$ sudo ldconfig
nvidia@gpu:~/opencv/build$ ls /usr/local/lib/python3.5/
dist-packages
nvidia@gpu:~/opencv/build$ ls /usr/local/lib/python3.5/dist-packages/
nvidia@gpu:~/opencv/build$ ls /usr/local/lib/python
python2.7/ python3.5/ 
nvidia@gpu:~/opencv/build$ ls /usr/local/lib/python2.7/
dist-packages/ site-packages/ 
nvidia@gpu:~/opencv/build$ ls /usr/local/lib/python2.7/
dist-packages/ site-packages/ 
nvidia@gpu:~/opencv/build$ ls /usr/local/lib/python2.7/site-packages/
nvidia@gpu:~/opencv/build$ 

```