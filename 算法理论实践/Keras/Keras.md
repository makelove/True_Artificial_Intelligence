# Keras

-参考
    - https://morvanzhou.github.io/tutorials/machine-learning/keras/1-3-backend/
    - [Keras:基于Python的深度学习库](https://keras-cn.readthedocs.io/en/latest/)

- 安装
    - pip install keras
    - 修改Backend
        - vi ~/.keras/keras.json
```json
{
    "epsilon": 1e-07,
    "image_data_format": "channels_last",
    "backend": "tensorflow",
    "floatx": "float32"
}
```        
