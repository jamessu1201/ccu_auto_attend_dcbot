# -*- coding: utf-8 -*-
import re
import string
import discord
from discord.ext import commands,tasks
import random
import json
import utils
import time
import datetime

utc = datetime.timezone.utc

happy_birthday_time = datetime.time(hour=0, minute=0, tzinfo=datetime.timezone(datetime.timedelta(hours=8)))

curr_dt = datetime.datetime.now()

print(happy_birthday_time)
print("Current datetime: ", curr_dt)

class Auto(commands.Cog):
    
    def __init__(self,bot:commands.Bot):
        self.bot=bot
        self.happy_birthday.start()

    @tasks.loop(time=happy_birthday_time)
    async def happy_birthday(self):
        channel = await self.bot.fetch_channel('1056547645499379753')
        await channel.send('<@&1104820254145790133>')
        await channel.send('<@&1148518925496225803>')
        await channel.send('<@&1151170809457541282>')
        await channel.send('<@&1153019088252186734>')
        await channel.send('https://giphy.com/gifs/xTcnSSsbe4hhZBvV6M')
    

        


async def setup(bot):
    await bot.add_cog(Auto(bot))