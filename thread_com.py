import threading
import Queue
import time


class ChildThread(threading.Thread):
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue

    def run(self):
        a = [1, 2, 3, 4, 5]
        for message in a:
            self.queue.put(message)
            time.sleep(1)


class MainThread(object):
    def __init__(self):
        self.message = "helloworld"
        self.queue = Queue.Queue()

    def spawn_thread(self):
        child_thread = ChildThread(self.queue)
        child_thread.start()

    def fetch_message(self):
        return self.queue.get(block=True)

main_thread = MainThread()
main_thread.spawn_thread()
while True:
    print "message: " + str(main_thread.fetch_message())
