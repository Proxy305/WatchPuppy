# Function for the daemon process of Watchdog
import os
import time

# Define the life span of the video file. 
# For instance, if 'lifeSpan = 12', video files that were created 12 hours ago or earlier will be removed from the file system. 
#lifeSpan = 8  

def generate_time():
    return time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time()))

# timeStr sample: 2015-01=01-00-00-00
def get_min_between(timeStr1,timeStr2):
    day1 = int(timeStr1[8:10])
    day2 = int(timeStr2[8:10])
    hour1 = int(timeStr1[11:13])
    hour2 = int(timeStr2[11:13])
    min1 = int(timeStr1[14:16])
    min2 = int(timeStr2[14:16])
    
    deltaMin = min2 - min1    
    deltaHour = hour2 - hour1
    deltaDay = day2 - day1
    
    if deltaMin < 0:
        deltaHour -= 1
        deltaMin += 60
        
    if deltaHour < 0:
        deltaDay -= 1
        deltaHour += 24
        
    minutesInBetween = deltaDay*1440 + deltaHour*60 + deltaMin
    
    return minutesInBetween

def free_disk_space(lifeSpan,currentTimeStr):
    fileList = os.listdir(os.getcwd());
    lifeSpanMin = lifeSpan*60
    #print(fileList)
    for i in fileList:
        if i.find('h264') > 0:
            if get_min_between(i[0:19], currentTimeStr) > lifeSpanMin:
                os.remove(os.path.join(os.getcwd(),i))
    
def daemon(lifeSpan):
    while(True):
        free_disk_space(lifeSpan, generate_time())
        time.sleep(600)     
