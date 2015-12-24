import asyncio
import aiohttp
import asyncio_redis
from config import LOG_INTERVAL,REQ_KEY,KILL_KEY

class Child(object):

    """

    wrapping all the child process feature in this class
    """

    def __init__(self,id,url):
        self.id = id+"-"+REQ_KEY
        # print(self.id)
        # self.connection = redis.Connection()
        self.url = url
        self.loop = asyncio.get_event_loop()
        self.client = aiohttp.ClientSession(loop=self.loop)
        self.count = 0 # total request/s


    async def init(self):
        self.redis_connection = await asyncio_redis.Pool.create(poolsize=2)



    async def hammer(self):
        while True:

            connection = await self.client.get(self.url)
            self.count+=1
            await connection.release()

    async def send_stats(self):

        while True:
            await self.redis_connection.set(self.id,str(self.count//LOG_INTERVAL))
            self.count=0
            await asyncio.sleep(LOG_INTERVAL)

    def clean_up(self):
        pass

    async def listen_for_close(self):
        subscriber = await self.redis_connection.start_subscribe()
        await subscriber.subscribe([KILL_KEY])
        reply =await subscriber.next_published()

        # above will block until something is published

        self.clean_up()





    def start(self,*funcs):
        self.loop.run_until_complete(self.init())

        asyncio.ensure_future(self.send_stats())
        asyncio.ensure_future(self.hammer())
        asyncio.ensure_future(self.listen_for_close())

        if funcs:
            for func in funcs:
                asyncio.ensure_future(func)
        self.loop.run_forever()
    


