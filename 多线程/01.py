import threading

def func():
    print("woshifunc")

if __name__ == '__main__':
    t1=threading.Thread(target=func)
    t1.start()
    t1.join()
    print("woshimain")


