import video

def test_normal():
    u1 = ['@Shakespeare','@realDonaldTrump', '@Literature', '@langston_poems']
    u2 = ['@langston_poems']
    u3 = ['@Shakespeare','@realDonaldTrump']
    assert compressVideo(u1,10) == 0
    assert compressVideo(u2,10) == 0
    assert compressVideo(u3,10) == 0

def test_more_users():
    u1 = ['@Shakespeare','@realDonaldTrump', '@Literature', '@langston_poems']
    assert compressVideo(u1,3) == 0

def main():
    pass

if __name__ == "__main__":
    main()

