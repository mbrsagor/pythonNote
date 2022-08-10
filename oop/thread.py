from time import sleep
from threading import Thread


class Download(Thread):

    def run(self):
        for download in range(10):
            print(f"Downloading {download} %")
            sleep(1)


d1 = Download()
d1.run()
