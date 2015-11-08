import time


class ExecTimer():

    start_time = 0

    def __init__(self):
        self.reset()

    def getvalue(self):
        return time.time() - self.start_time

    def reset(self):
        self.start_time = time.time()