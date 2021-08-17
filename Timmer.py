# This is the stopwatch for the packs.

import time


def time_convert(sec):
    mint = sec // 60
    sec = sec % 60
    hours = mint // 60
    mint = mint % 60
    print("Time Lapsed = {0}:{1}:{2}".format(int(hours), int(mint), sec))


input("Press Enter to start")
start_time = time.time()

input("Press Enter to stop")
end_time = time.time()

time_lapsed = end_time - start_time
time_convert(time_lapsed)
