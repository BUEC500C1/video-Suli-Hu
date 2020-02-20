# video-Suli-Hu
1. Implemented python threading to put a finite number of tasks in the pool, the extra numbers of tasks will be put in a queue as a waiting list.
2. Used Twitter API and python CV and PIL tools to grab the target user timeline tweets and draw them into pictures, then make video for each users. This is the single task as one thread in the threads pool.
3. Used `flake8` to do some simple syntax checking and test. 

## Committed files
- `video.py`
This is the main program. You can change the userlist like adding new twitter user's screen names or change the number of tweets. During the run time, program will create a temp directaries to store pictures for diffent users, after that program will delete them. The only out put is the videos.

- `compress.py` 
This is the interface of a single tweets to video task.

- `tw2video.py` 
This is the kernel part of the program, includes all the details.

- `defult.ttf` and `font2.ttf`
These are fonts that are used to make the video.

- `.avi` files
These are the example out puts of the program.
