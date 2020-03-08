# to grab tweets and write words into pics
# Copyright Suli Hu sulihu@bu.edu
import tweepy
import os
import cv2
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import configparser


class Tweet2Video:
    def __init__(self, username, num_tweets, key_filename='./keys'):
        self.username = username
        self.picpath = f'./pic_{username}'
        self.num_tweets = num_tweets
        config = configparser.ConfigParser()
        config.read(key_filename)
        self.consumer_key = config.get('auth', 'consumer_key').strip()
        self.consumer_secret = config.get('auth', 'consumer_secret').strip()
        self.access_key = config.get('auth', 'access_token').strip()
        self.access_secret = config.get('auth', 'access_secret').strip()

    def get_all_tweets(self):
        auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        auth.set_access_token(self.access_key, self.access_secret)
        api = tweepy.API(auth)
        all_tweets = []
        new_tweets = api.user_timeline(
            screen_name=self.username, count=self.num_tweets)
        for tweet in new_tweets:
            all_tweets = all_tweets + [tweet.text]
        return all_tweets

    def de_emojify(self, input_string):
        # If you meet trouble with emoji
        return input_string.encode('ascii', 'ignore').decode('ascii')

    def text2img(self, text, num):
        ft = ImageFont.truetype('./font2.ttf', 20)
        img = Image.new('RGB', (1600, 500), color=(255, 255, 224))
        d = ImageDraw.Draw(img)
        d.text((5, 100), text, font=ft, fill=(0, 0, 0))
        filename = f'{self.picpath}/v{num}{self.username}.png'
        img.save(filename)

    # to make pics into videos
    def make_video(self, videoname):
        """
        Example:
            makevideo('./pic/','aaa') # this is a test
        """
        if os.path.exists(f'{self.picpath}/.DS_Store'):
            os.remove(f'{self.picpath}/.DS_Store')
        pic_filenames = []
        for root, dirs, files in os.walk(self.picpath):
            for file in files:
                pic_filenames.append(file)
        pic_filenames.sort()
        video = cv2.VideoWriter(
            f'./video/{videoname}.avi',
            cv2.VideoWriter_fourcc(*'MJPG'),
            0.333,
            (1600, 500))
        for i in range(1, len(pic_filenames)+1):
            img = cv2.imread(f'{self.picpath}/{pic_filenames[i-1]}')
            img = cv2.resize(img, (1600, 500))
            video.write(img)
        for picname in pic_filenames:
            os.remove(f'{self.picpath}/{picname}')
        # video.release()

    def run(self):
        # Fetch tweet texts from twitter
        tweet_list = self.get_all_tweets()

        # Make tweets to images
        if not os.path.exists(self.picpath):
            os.mkdir(self.picpath)
        for i in range(len(tweet_list)):
            self.text2img(self.de_emojify(tweet_list[i]), i)

        # Concatenate images to a video
        self.make_video(f'v_{self.username}')
        os.rmdir(self.picpath)


def main():
    username = '@Shakespeare'
    num_tweets = 5
    auth_key_filename = 'keys'
    t2v = Tweet2Video(username, num_tweets, auth_key_filename)
    t2v.run()


if __name__ == '__main__':
    main()
