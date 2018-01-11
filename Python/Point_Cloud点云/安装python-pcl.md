## 安装python-pcl

- 在macOS安装
```bash
brew tap homebrew/science
brew install pcl
sudo cp travisCI/pcl_2d-1.8.pc  /usr/local/lib/pkgconfig/

git clone https://github.com/strawlab/python-pcl.git
cd python-pcl/
ls
pip install --upgrade pip
pip install cython
pip install numpy
python setup.py build_ext -i
python setup.py install

```