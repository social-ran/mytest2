import socket
import asyncio
import time
import random
import json

from walkoff_app_sdk.app_base import AppBase

class HelloWorld(AppBase):
    __version__ = "1.0.0"
    app_name = "hello_world"  # this needs to match "name" in api.yaml

    def __init__(self, redis, logger, console_logger=None):

        super().__init__(redis, logger, console_logger)

    async def hello_world(self):
        message = f"Hello World from {socket.gethostname()} in workflow {self.current_execution_id}!"
        #加f表示格式化字符串，可以用花括号！！
        # This logs to the docker logs
        self.logger.info(message)

        return message

    async def repeat_back_to_me(self, call):
        return call

    async def return_plus_one(self, number):
        return str(number + 1)

    async def pause(self, seconds):
        time.sleep(seconds)
        return "Waited %d seconds" % seconds

    async def get_type(self, value):
        return "Type: %s" % type(value)
    async def return_plus_two(self, number):
        return str(number + 2)


if __name__ == "__main__":
    asyncio.run(HelloWorld.run(), debug=True)
