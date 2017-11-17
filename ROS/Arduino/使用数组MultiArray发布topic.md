## 使用数组MultiArray发布topic

- 参考
    - https://answers.ros.org/question/223565/array-data-from-arduino/

```
#include <ros.h>
#include <std_msgs/Int16MultiArray.h>


ros::NodeHandle  nh;
std_msgs::Int16MultiArray multiarray ;
ros::Publisher pub_array("multiarray", &multiarray);
int length = 10;
int counter = 0;
void setup() {
  pinMode(13, OUTPUT);
  // put your setup code here, to run once:
  nh.initNode();
  multiarray.data_length = length;
  nh.advertise(pub_array);
}

void loop() {
  digitalWrite(13, HIGH-digitalRead(13));   // blink the led
  
  // put your main code here, to run repeatedly:
  for (int i = 1; i < length + 1; i++) {
    multiarray.data[i - 1] = i * counter+3;
  }
  pub_array.publish(&multiarray);
  if (counter < 100) {
    counter++;
  } else {
    counter = 0;
  }
  
  nh.spinOnce();
  delay(1000);
}
```

- 问题
    - LED 13 不发光，不工作
    - 发布的数据，列表有问题
        - 参考：https://github.com/ros-drivers/rosserial/issues/45
```bash
layout: 
  dim: []
  data_offset: 0
data: [242, 201, 300, 399, 498, 597, 10, 0, 1371, 4626]
```
    
-     