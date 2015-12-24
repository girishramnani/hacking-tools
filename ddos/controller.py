from multiprocessing import Process
from uuid import uuid4
from child import Child
import asyncio_redis
import asyncio
from config import KILL_KEY, REQ_KEY, LOG_INTERVAL
import redis
import time
import threading

class Controller(object):

    def __init__(self,auto=True,**kwargs):
        if not auto:
            try:

                self.no_c = kwargs.get("clients")
            except KeyError:
                print("number of clients not specified")
                exit(-1)
        self.auto=auto
        self.childs = dict()


        # loop.run_until_complete(self.init())






    async def init(self):
        self.redis = await asyncio_redis.Connection.create()


    def auto_balance(self):
        pass

    def fork_child(self,url):
        id =uuid4()
        child = Child(str(id),url)
        process = Process(target=lambda : child.start())
        self.childs[str(id)] = (child,process)


    def start(self):
        for _,process in self.childs.values():
            process.start()


    def show_messages(self):
        #so that the message has been published
        time.sleep(LOG_INTERVAL//2)
        self.redis = redis.Redis()
        while True:
            message =[]
            for keys in self.childs:

                out =self.redis.get(keys+"-"+REQ_KEY)
                if out:
                    message.append(" ".join([out.decode(),"req/s"]))
            mess = " | ".join(message)
            print(mess+"\r",end="")
            time.sleep(LOG_INTERVAL)



    def kill_all(self):
        for key in self.childs.keys():
            self.redis.publish(key+"-"+KILL_KEY,"KILL")





if __name__ == '__main__':
    controller = Controller(False,clients=5)
    controller.fork_child("http://google.com")
    controller.fork_child("http://google.com")
    controller.fork_child("http://google.com")
    controller.fork_child("http://google.com")
    controller.fork_child("http://google.com")
    controller.fork_child("http://google.com")
    controller.fork_child("http://google.com")
    controller.fork_child("http://google.com")
    controller.fork_child("http://google.com")


    thread = threading.Thread(target=lambda :controller.show_messages())
    thread.start()
    controller.start()



