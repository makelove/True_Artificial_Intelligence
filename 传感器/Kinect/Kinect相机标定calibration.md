## 相机标定

- 参考
    - http://wiki.ros.org/openni_launch/Tutorials/IntrinsicCalibration
    - http://wiki.ros.org/camera_calibration/Tutorials/MonocularCalibration
    - ORB_SLAM实战-（rosindigo） http://www.jianshu.com/p/c3e8c88edb64

- 准备标准黑白棋格盘
    - 下载[黑白棋盘](http://wiki.ros.org/camera_calibration/Tutorials/MonocularCalibration?action=AttachFile&do=view&target=check-108.pdf) 来源：http://wiki.ros.org/camera_calibration/Tutorials/MonocularCalibration
    - 打印棋盘（可以A4纸打印，粘贴在硬纸板上）
    - 测量棋盘单元(黑色或白色正方形)边长（A4纸的在0.025 m 左右）(实际边长？)
    
- 步骤
    - 启动openni驱动
        - roslaunch openni_launch openni.launch
    - 进行校准，RGB相机
        - rosrun camera_calibration cameracalibrator.py image:=/camera/rgb/image_raw camera:=/camera/rgb --size 5x4 --square 0.0245
        -  size是黑白格的横纵点数，square是黑白格边长，image是图像节点名称，camera是相机名称
        - 标定界面出现后，按照x（左右）、y（上下）、size（前后）、skew（倾斜）等方式移动棋盘，知道x,y,size,skew的进度条都变成绿色位置，此时可以按下CALIBRATE按钮，等一段时间就可以完成标定。
        - 然后 commit 。成功
    - IR（深度）相机
        - rosrun camera_calibration cameracalibrator.py --size 8x6 --square 0.025  image:=/camera/ir/image_raw camera:=/camera/ir
        - 然后 commit 。/camera/ir/image_raw 没数据？
        