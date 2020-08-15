from threading import Thread
from time import sleep


class MyThread(Thread):

    def run(self):
        for number in range(10):
            print(f"Downloading {number} %")
            sleep(1)


thread_instance = MyThread()
thread_instance.start()
thread_instance.join()

print("The end")
