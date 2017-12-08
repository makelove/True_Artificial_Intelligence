## TensorFlow_debug调试

- 错误
```bash
2017-12-08 10:53:13.362783: I tensorflow/stream_executor/dso_loader.cc:129] Couldn't open CUDA library libcupti.so.8.0. LD_LIBRARY_PATH: /usr/local/cuda-8.0/lib64:
2017-12-08 10:53:13.362976: F ./tensorflow/stream_executor/lib/statusor.h:212] Non-OK-status: status_ status: Failed precondition: could not dlopen DSO: libcupti.so.8.0; dlerror: libcupti.so.8.0: cannot open shared object file: No such file or directory
[I 10:53:14.610 NotebookApp] KernelRestarter: restarting kernel (1/5)
WARNING:root:kernel 48eb1627-8e5e-43ad-8835-c25a6c306dd4 restarted
```
- 解决
    - nano .bashrc
        - export LD_LIBRARY_PATH=/usr/local/cuda/extras/CUPTI/lib64:$LD_LIBRARY_PATH