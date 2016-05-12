from datetime import timedelta
import re
import time


def longer_time_string(run_time_in_seconds):
    time_delta = timedelta(seconds=run_time_in_seconds)
    timedelta_string = str(time_delta)

    m = re.search('(\d* (days|day), )?(\d*):(\d*):(\d*)', timedelta_string)
    days_string = m.group(1)
    hours = int(m.group(3))
    minutes = int(m.group(4))
    seconds = int(m.group(5))

    if days_string:
        days_string = days_string[:-2]
        return "{}, {} hours, {} minutes, {} seconds".format(days_string, hours, minutes, seconds)
    elif hours:
        return "{} hours, {} minutes, {} seconds".format(hours, minutes, seconds)
    elif minutes:
        return "{} minutes, {} seconds".format(minutes, seconds)
    else:
        return "{} seconds".format(seconds)


def get_time_string(time):
    if time > 1:
        time_string = "{0:.1f} seconds".format(time)
        if time > 60:
            time_string = longer_time_string(time)
    else:
        time *= 1000
        if time > 1:
            time_string = "{0:.0f} milliseconds".format(time)
        else:
            time *= 1000
            time_string = "{0:.0f} microseconds".format(time)

    return time_string


def timeit(method):
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()
        time_ = te - ts

        print("{}: {}".format(method.__name__, get_time_string(time_)))
        return result

    return timed
