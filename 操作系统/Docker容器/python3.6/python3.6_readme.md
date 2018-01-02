- 获取
    - docker pull python:3.6
        - 基于Debian8
    - docker pull python:3.6.4-stretch
        - 基于Debian9
- 运行
    - docker run -it python:3.6 bash
    - docker run -it --rm python:3.6 bash
        - exit 退出删除掉
```bash
root@94a707e49f1c:/# cat /etc/os-release
PRETTY_NAME="Debian GNU/Linux 8 (jessie)"
NAME="Debian GNU/Linux"
VERSION_ID="8"
VERSION="8 (jessie)"
ID=debian
HOME_URL="http://www.debian.org/"
SUPPORT_URL="http://www.debian.org/support"
BUG_REPORT_URL="https://bugs.debian.org/"
```