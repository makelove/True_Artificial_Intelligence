## libfreenect测试工具
- 'w' - tilt up, 's' - level, 'x' - tilt down
- '0'-'6' - select LED mode, 
- '+' & '-' - change IR intensity
- 'f' - change video format, 'm' - mirror video, 'o' - rotate video with accelerometer
- 'e' - auto exposure, 'b' - white balance, 'r' - raw color, 
- 'n' - near mode (K4W only)

```bash
freenect-glview
#
Kinect camera test
Number of devices found: 1
Found sibling device [single on same bus]
GL thread
[Stream 70] Negotiated packet size 1920
write_register: 0x0105 <= 0x00
write_register: 0x0006 <= 0x00
write_register: 0x0012 <= 0x03
write_register: 0x0013 <= 0x01
write_register: 0x0014 <= 0x1e
write_register: 0x0006 <= 0x02
write_register: 0x0017 <= 0x00
[Stream 80] Negotiated packet size 1920
write_register: 0x000c <= 0x00
write_register: 0x000d <= 0x01
write_register: 0x000e <= 0x1e
write_register: 0x0005 <= 0x01
[Stream 70] Lost 159 total packets in 0 frames (inf lppf)
[Stream 70] Lost 171 total packets in 0 frames (inf lppf)
write_register: 0x0047 <= 0x00
'w' - tilt up, 's' - level, 'x' - tilt down, '0'-'6' - select LED mode, '+' & '-' - change IR intensity
'f' - change video format, 'm' - mirror video, 'o' - rotate video with accelerometer
'e' - auto exposure, 'b' - white balance, 'r' - raw color, 'n' - near mode (K4W only)
```