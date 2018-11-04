import time

from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode

from events import ContinuousCapacitiveEvent, SingleCapacitiveEvent


def main():
    mute = 0xE2

    buttons = [
        SingleCapacitiveEvent('touch_A1', ConsumerControlCode.PLAY_PAUSE),
        SingleCapacitiveEvent('touch_A2', ConsumerControlCode.SCAN_NEXT_TRACK),
        SingleCapacitiveEvent('touch_A3', ConsumerControlCode.SCAN_PREVIOUS_TRACK),
        SingleCapacitiveEvent('touch_A6', mute),
        ContinuousCapacitiveEvent('touch_A5', ConsumerControlCode.VOLUME_DECREMENT),
        ContinuousCapacitiveEvent('touch_A4', ConsumerControlCode.VOLUME_INCREMENT),
    ]

    media_control = ConsumerControl()


    time.sleep(1)

    for button in cycle(buttons):
        if button.is_pressed(): 
            media_control.send(button.output_control)

        time.sleep(0.025)


def cycle(iterable):
    saved = []
    for element in iterable:
        yield element
        saved.append(element)
    while saved:
        for element in saved:
              yield element


if __name__ == '__main__':
    main()