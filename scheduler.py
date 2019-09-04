#integrating with django

#import os

#os.environ.setdefault("DJANGO_SETTINGS_MODULE", "wordcloud.settings")

# your imports, e.g. Django models
#from movie.models import *

import schedule 
import time 
from twitter import func_twitter
#import twitter

global val

val=0

def update_word_cloud():
    global val
    print("hiiiii")
    val=val+1
    func_twitter()
    if(val==2):
        schedule.clear()

#schedule.every(6).hours.do(update_word_cloud) 

schedule.every(1).minutes.do(update_word_cloud) 

# Loop so that the scheduling task 
# keeps on running all time. 
while True: 
  
    # Checks whether a scheduled task  
    # is pending to run or not 
    schedule.run_pending() 
    time.sleep(1)
    if(val==2):
        break
    


