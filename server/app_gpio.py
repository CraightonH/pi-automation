from gpiozero import LED

class StopLight(object):
    red = LED(17)
    yellow = LED(27)
    green = LED(22)

    def enable_light(self, color):
        disable_all()
        method_name = 'enable_' + str(color)
        method = getattr(self, method_name)
        method()

    def enable_red():
        red.on()

    def disable_red():
        red.off()

    def enable_yellow():
        yellow.on()

    def disable_yellow():
        yellow.off()

    def enable_green():
        green.on()

    def disable_green():
        green.off()

    def disable_all():
        disable_red()
        disable_yellow()
        disable_green()
