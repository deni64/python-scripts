import time
index =0
def func(grow):
    index = int(input())
    if index == 0:
        print('netu')
    if index == 1:
        print('cvetet')
    if index == 2:
        print('zeleniy')
    if index == 3:
        print('krasniy')
    time.sleep(2)
    index +=1
    
    if index == 0:
        print('netu')
    if index == 1:
        print('он вырос теперь он cvetet')
    if index == 2:
        print('он вырос теперь он zeleniy')
    if index == 3:
        print('он вырос теперь он krasniy')
    if index>=4:
        print('он вырос теперь он сгнил')
    return index
func(index)