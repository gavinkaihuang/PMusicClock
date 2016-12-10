#coding=utf-8
import time, datetime
import logging
class Clock:

    week = []
    hour = 0
    minute = 0
    def __init__(self, line_set):
        # print "init clock %s " % line_set
        array = str(line_set).split("|")
        self.week = array[0].split(",")
        self.hour = int(array[1].strip())
        self.minute = int(array[2].strip())

    def print_target(self):
        print "week %s " % self.week
        print "hour %s " % self.hour
        print "minute %s" % self.minute

    def is_alert(self):
        week_value = self.is_week_checked()
        time_value = self.is_time_checked()
        if (week_value and time_value):
            return True
        else:
            log_value = "Target: %s %s %s ; Now : %s ; week=%s time=%s" % (self.week, self.hour, self.minute, time.localtime(), week_value, time_value)
            logging.info(log_value)
            return False

    def is_week_checked(self):
        now_weekday = datetime.datetime.now().weekday()
        # print datetime.datetime.now()
        for week_value in self.week:
            # print "for week_value % s now_weekday %s" % (week_value, now_weekday)
            if (week_value.strip() == '*'):
                return True
            elif (week_value.strip() == str(now_weekday)):
                # print "true for week_value % s now_weekday %s" % (week_value, now_weekday)
                return True
        return False

    def is_time_checked(self):
        now = time.localtime()
        # print now
        now_hour = int(now[3])
        now_minute = int(now[4])
        if (self.hour == now_hour and self.minute == now_minute):
            # print "true for hour % s minute %s" % (now_hour, now_minute)
            return True
        else:
            return False

