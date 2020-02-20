# to grab tweets and write words into pics
# Copyright Suli Hu sulihu@bu.edu
import tweepy
import json
import os
import cv2
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
# Twitter API credentials
consumer_key = 'qiylvzRnR4B9qcwL8KuDb5jLF'
consumer_secret = 'exFrXCwnmfc8s0W8GdmvEH6dza1PDU1kjE3eqvwJA46q9Fn1Hl'
access_key = '1171124944215740416-12P7GVnhdXYblB2Xj8s2MDWGh9wcNR'
access_secret = 'sloUYZYFBjmLSYZvL7AxjSvRJQryj5Hn6jtawyVV4oPGV'

def deEmojify(inputString):
    # If you meet trouble with emoji
    return inputString.encode('ascii', 'ignore').decode('ascii')

def textToImg(text,user,num):
    ft = ImageFont.truetype('./font2.ttf' ,20)
    img = Image.new('RGB',(1600,500),color = (255,255,224))
    d = ImageDraw.Draw(img)
    d.text((5,100), text, font = ft,fill=(0,0,0))
    filename = 'pic_'+user+'/' + 'v'+ str(num) + user +'.png'
    img.save(filename)

def get_all_tweets(name, numOfTweets):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
    alltweets = []
    new_tweets = api.user_timeline(screen_name = name, count = numOfTweets)
    for tweet in new_tweets:
        alltweets = alltweets + [tweet.text]
    return alltweets

# to make pics into videos
def makevideo(filepath,videoname):
    file_dir = (f'{filepath}')
    list=[]
    for root,dirs,files in os.walk(file_dir):
        for file in files:
           list.append(file)  
    print(len(list))
    list.sort()
    video=cv2.VideoWriter(f'./{videoname}.avi',cv2.VideoWriter_fourcc(*'MJPG'),0.333,(1600,500))
    for i in range(1,len(list)+1):
        img=cv2.imread(f'{filepath}'+list[i-1])
        img=cv2.resize(img,(1600,500)) 
        video.write(img)   
    for e in list:
        print(e)
        os.remove(f'{filepath}{e}')
    #video.release()
# makevideo('./pic/','aaa') # this is a test




