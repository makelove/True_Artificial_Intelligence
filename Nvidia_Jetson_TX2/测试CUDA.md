## 测试CUDA

- 参考
    - [使用Python写CUDA程序](http://blog.csdn.net/taonull/article/details/52673864)
- 对比

    - numba使用一些指令标记某些函数进行加速（也可以使用Python编写内核函数），这一点类似于OpenACC，而PyCUDA需要自己写kernel，在运行时进行编译，底层是基于C/C++实现的。通过测试，这两种方式的加速比基本差不多。但是，numba更像是一个黑盒，不知道内部到底做了什么，而PyCUDA就显得很直观。因此，这两种方式具有不同的应用： 
        * 如果只是为了加速自己的算法而不关心CUDA编程，那么直接使用numba会更好。 
        * 如果为了学习、研究CUDA编程或者实验某一个算法在CUDA下的可行性，那么使用PyCUDA。 
        * 如果写的程序将来要移植到C/C++，那么就一定要使用PyCUDA了，因为使用PyCUDA写的kernel本身就是用CUDA C/C++写的。    

- numba https://pypi.python.org/pypi/numba
    - conda install numba 应该可以
    - 在jetson tx2安装conda https://github.com/thomasantony/constructor/tree/master/examples/jetsonconda
```bash
sudo apt-get install build-essential
sudo apt-get install llvm
pip install llvmpy#安装失败
pip install cython
pip install numba
```
    


- pycuda
    - pip install pycuda
    - 测试
```bash
(.py3) nvidia@gpu:~/WORK$ py test_pyCuda.py
------------1---------------
N = 10485760
gpu run time 0.089287 seconds
cpu run time 0.280304 seconds
-0.00146484 0.000976562
------------2---------------
N = 20971520
gpu run time 0.168097 seconds
cpu run time 0.556074 seconds
-0.00146484 0.000976562
------------3---------------
N = 31457280
gpu run time 0.243027 seconds
cpu run time 0.833326 seconds
-0.00146484 0.00146484
------------4---------------
N = 41943040
gpu run time 0.319355 seconds
cpu run time 1.111787 seconds
-0.00146484 0.00146484
------------5---------------
N = 52428800
gpu run time 0.396374 seconds
cpu run time 1.383929 seconds
-0.00146484 0.00146484
------------6---------------
N = 62914560
gpu run time 0.459795 seconds
cpu run time 1.675015 seconds
-0.00195312 0.00146484
------------7---------------
N = 73400320
gpu run time 0.526261 seconds
cpu run time 1.996370 seconds
-0.00195312 0.00146484
------------8---------------
N = 83886080
gpu run time 0.695422 seconds
cpu run time 2.235510 seconds
-0.00195312 0.00146484
------------9---------------
N = 94371840
gpu run time 0.787763 seconds
cpu run time 2.500583 seconds
-0.00195312 0.00146484
```    