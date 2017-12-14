## wemos_mega_wifi_r3上手指南
双11在淘宝买了这个板子，感觉很厉害，其实很麻烦。
- https://s.taobao.com/search?q=wemos+mega+wifi+r3
- 参考链接
    - 俄国网站http://www.sysengineering.ru/blog/%D1%8D%D0%BB%D0%B5%D0%BA%D1%82%D1%80%D0%BE%D0%BD%D0%B8%D0%BA%D0%B0-%D0%BA%D0%BE%D0%BD%D1%82%D1%80%D0%BE%D0%BB%D0%BB%D0%B5%D1%80-arduino-mega-%D1%81-esp8266/
    - 中文翻译，请看PDF附件
    
- 总结
    - Mega2560+ESP8266组装在一起，可以分别使用Mega2560或ESP8266。也可以通过Mega2560调用ESP8266的WIFI功能
    - 板子上有9个开关和1个RX/TX开关，通过这些开关的组合，决定使用哪个芯片。
    - 如果通过Mega2560调用ESP8266的WIFI功能，则需要分别写好2份Arduino代码。
    
- 还不如购买：
    - 1个国产的Mega2560 [mega2560 r3 改进版](https://s.taobao.com/search?q=mega2560+r3+%E6%94%B9%E8%BF%9B%E7%89%88)
    - 带WIFI的shield [mega2560+wifi](https://s.taobao.com/search?q=mega2560+wifi)