import asyncio
import aiohttp
import redis
from config import LOG_INTERVAL

class Child(object):

    """

    wrapping all the child process feature in this class
    """

    def __init__(self,id,url):
        self.id = id
        # self.connection = redis.Connection()
        self.url = url
        self.loop = asyncio.get_event_loop()
        self.client = aiohttp.ClientSession(loop=self.loop)
        self.count = 0 # total request/s



    async def hammer(self):
        while True:

            connection = await self.client.get(self.url)
            self.count+=1
            await connection.release()

    async def send_stats(self):
        while True:
            print("Count : ",self.count,"\r",end="")
            self.count=0
            await asyncio.sleep(LOG_INTERVAL)



    def start(self,*funcs):
        asyncio.ensure_future(self.send_stats())
        asyncio.ensure_future(self.hammer())
        if funcs:
            for func in funcs:
                asyncio.ensure_future(func)
        self.loop.run_forever()
    


