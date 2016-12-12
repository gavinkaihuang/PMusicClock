#coding=utf-8
import subprocess
import random, os, glob, time, platform
import logging
from clock import Clock

# 播放mp3文件 OSX
def play_mp3(file_path):
    if (platform.system() == 'Darwin'):
        return_code = subprocess.call(["afplay", file_path])
    elif (platform.system() == 'Linux'):
        os.system('omxplayer ' + file_path)

def get_random_file_no(file_no):
    return int(random.uniform(0, file_no))

# 随机取得某目录中的一个mp3文件
def get_one_file(folder_path):
    files_path = os.path.join(folder_path, "*.mp3")
    files = glob.glob(files_path)
    file_no = len(files)
    return files[get_random_file_no(file_no)]

def read_alert_clock():
    clock_array = []
    f = open('clock.properties', 'r')
    one_line =  f.readline()
    while (one_line != ''):
        # print one_line
        if (one_line.startswith("#") or one_line.strip() == ''):
            pass
        else:
            # print one_line.strip() , " to append"
            # alert_array.append(one_line.strip())
            clock = Clock(one_line)
            clock_array.append(clock)
        one_line = f.readline()
    f.close()
    return clock_array

#扫描是否需要闹铃
def check_if_alert_now(alert_array):
    for one_clock in alert_array:
        if (one_clock.is_alert() == True):
            return True
        else:
            continue
    return False

# alert_time = "22:30"

if __name__ == '__main__':
    logging.basicConfig(filename='logger.log', level=logging.INFO)
    while 1:
        #read clock time from properties
        clock_array = read_alert_clock()

        if (check_if_alert_now(clock_array)):
            music_file = get_one_file('./music')
            log_value = str(time.localtime()) + ': now play music %s ' % music_file
            logging.info(log_value)
            # print log
            play_mp3(music_file)
        else:
            #TODO caculate sleep time space
            time.sleep(5)

