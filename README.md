# macropad
A basic macropad using CircuitPython

## Setup

[Configuration for Ubuntu](https://learn.adafruit.com/adafruit-arduino-ide-setup/linux-setup#udev-rules)

[HID library for CircuitPython](https://github.com/adafruit/Adafruit_CircuitPython_Bundle/releases/tag/20181102)

## Debugging

List connected devices:

```bash
ls /dev/ttyACM*
```

Connect to device output:

```bash
screen /dev/ttyACM0
```

To exit screen `ctrl + a + d`

