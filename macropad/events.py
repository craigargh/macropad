from digitalio import DigitalInOut, Direction, Pull
from adafruit_circuitplayground.express import cpx


class ContinuousMixin:
    def is_pressed(self):
        return self.button_value()


class SingleMixin:
    prev_state = False

    def is_pressed(self):
        pressed = not self.prev_state and self.button_value()
        released = self.prev_state and not self.button_value()

        if pressed:
            self.prev_state = True
            return True

        if released:
            self.prev_state = False
            return False

        return False


class DigitalButtonMixin:
    def setup_input(self, input_pin):
        self.button = DigitalInOut(input_pin)
        self.button.direction = Direction.INPUT
        self.button.pull = Pull.DOWN

    def button_value(self):
        return self.button.value


class CapacitiveTouchMixin:
    def setup_input(self, input_pin):
        self.button = input_pin

    def button_value(self):
        return getattr(cpx, self.button)


class ContinuousButtonEvent(ContinuousMixin, DigitalButtonMixin):
    def __init__(self, input_pin, output_control):
        self.setup_input(input_pin)

        self.output_control = output_control


class SingleButtonEvent(SingleMixin, DigitalButtonMixin):
    def __init__(self, input_pin, output_control):
        self.setup_input(input_pin)

        self.output_control = output_control


class ContinuousCapacitiveEvent(ContinuousMixin, CapacitiveTouchMixin):
    def __init__(self, input_pin, output_control):
        self.setup_input(input_pin)

        self.output_control = output_control


class SingleCapacitiveEvent(SingleMixin, CapacitiveTouchMixin):
    def __init__(self, input_pin, output_control):
        self.setup_input(input_pin)

        self.output_control = output_control
