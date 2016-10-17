
import math
import time

class Clock():

    def __init__(self, hr, minutes):
        self.hr = hr
        self.minutes = minutes
        self.timeInSeconds = None
        self.time = None

    def calcTime(self):
        hr = self.hr
        minutes = self.minutes
        hourAdjustment = 0

        while minutes < 0:
            hourAdjustment -= 1
            minutes = minutes + 60

        if minutes >= 60:
            hourAdjustment = int(math.floor(minutes/60))
            minutes = minutes % 60

        hr += hourAdjustment

        while hr < 0:
            hr = hr + 24

        if hr >= 24:
            hr = hr % 24

        seconds = hr * 60 * 60
        seconds += minutes * 60
        self.timeInSeconds = seconds


    def add(self, minutes):
        self.minutes += minutes
        self.calcTime()
        return time.strftime("%H:%M", time.gmtime(self.timeInSeconds))

    def __eq__(self, other):
        if self.timeInSeconds == other.timeInSeconds:
            return True
        else:
            return False

    def __repr__(self):
        self.calcTime()
        return time.strftime("%H:%M", time.gmtime(self.timeInSeconds))
