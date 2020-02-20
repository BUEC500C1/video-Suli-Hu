import os
import tw2video as twt


def tweet2video(username, picpath, numOfTweets):
    # get tweets and make pics and make them to a video
    if not os.path.exists(picpath):
        os.mkdir(picpath)

    tweet1 = twt.get_all_tweets(username, numOfTweets)

    for i in range(len(tweet1)):
        twt.textToImg(twt.deEmojify(tweet1[i]), username, i)

    if os.path.exists(f'{picpath}.DS_Store'):
        os.remove(f'{picpath}.DS_Store')

    twt.makevideo(picpath, f'v_{username}')
    os.rmdir(picpath)

# tweet2video('@Shakespeare','./pic/',5)
# name = '@Shakespeare'
# name = '@realDonaldTrump'
