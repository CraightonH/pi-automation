from gpiozero import LED

class StopLight(object):
    def __init__(self):
        self.red = LED(17)
        self.yellow = LED(27)
        self.green = LED(22)

    def enable_red(self):
        self.red.on()

    def disable_red(self):
        self.red.off()

    def enable_yellow(self):
        self.yellow.on()

    def disable_yellow(self):
        self.yellow.off()

    def enable_green(self):
        self.green.on()

    def disable_green(self):
        self.green.off()

    def disable_all(self):
        self.disable_red()
        self.disable_yellow()
        self.disable_green()

    def enable_light(self, color):
        self.disable_all()
        method_name = 'enable_' + str(color)
        method = getattr(self, method_name)
        method()
