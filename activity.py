import time

class Activity:
    """Common base class for all activities.
    An activity is considered to be anything you schedule to do.

    :ivar str name: a name or phrase that describes the activity.
    :ivar int duration: the amount of minutes this activity requires.
    :ivar array days: which days will the activity occur during one
        period.
    :ivar Period period: the time period during which the activity will happen
        at least once.
    """

    def __init__(self, name, duration, days, period):
        self.name = name

        # duration is multiplied by 60 to get minutes
        self.duration = duration*60
        self.days = days
        self.period = period

        # time left is initially the same as activity duration
        self.time_left = self.duration
        self.time_stamp = None
        self.is_running = False

        # ended means the activity is now completed and won't run again
        self.ended = False

    # updates time left for the activity
    def update_time(self):

        # if first update renew time_stamp
        if self.is_running is False:
            self.time_stamp = int(time.time())
            self.is_running = True
            print("starting time is "+str(self.time_stamp))

        # t is seconds from epoch
        t = int(time.time())
        dt = t - self.time_stamp

        self.time_left -= dt

        # time_stamp is renewed
        self.time_stamp = t

        # if time_left is negative, end the activity
        if self.time_left < 0:
            self.time_left = 0
            self.end()

            print("time left: "+str(self.time_left))

    def stop_time_update(self):
        self.is_running = False

    def return_hour_minute_format(self):
        hours = int(self.time_left / 3600)
        hours_string = str(hours)+"h " if hours != 0 else ""
        minutes = int(self.time_left % 3600 / 60)
        minutes_string = str(minutes)+"min " if minutes != 0 else ""
        seconds = int(self.time_left % 3600 % 60)
        seconds_string = str(seconds)+"s " if seconds != 0 else ""
        return hours_string+minutes_string+seconds_string

    def end(self):
        self.is_running = False
        self.ended = True

    def reset(self):
        self.time_left = self.duration
        self.ended = False

    def __str__(self):
        return "%s, %s, %s, %s" % (
                self.name, self.duration, self.days, self.period)


class Period:
    Weekly, once = range(2)
    # Weekly, Monthly, Yearly, once = range(4)


class Days:
    Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday = range(7)
