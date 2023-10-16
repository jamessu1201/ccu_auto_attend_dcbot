# -*- coding: utf-8 -*-
import os
import discord
from discord.ext.commands.core import command
from discord.ext import commands


default_prefixes = "!"            #default prefixes


try:
    with open('secret/token.txt','r') as bot_token:
        token=bot_token.read()
except:
    print("token does not exist,please create a bot")
    os._exit(0)

def main():
    owners=[]  #可以填自己的id，可控制admin.py的指令
    try:
        with open("private/owners.txt","r") as r:
            raw=r.read()
            for owner in raw.split(","):
                owners.append(int(owner))
        r.close()
        print(owners)
    except:
        pass
    bot = commands.Bot(command_prefix="!",owner_ids=set(owners), description='james的點名機器人',intents=discord.Intents.all())

    
    @bot.event
    async def on_ready():
        intents = discord.Intents().default()
        intents.message_content = True
        for file in os.listdir("cogs"):
            if(file.endswith(".py") and not file.startswith("_")):
                print(f"cogs.{file[:-3]}")
                await bot.load_extension(f"cogs.{file[:-3]}")
        print('Logged in as:\n{0.user.name}\n{0.user.id}'.format(bot))

    bot.run(token)
    

if(__name__=='__main__'):         
    main()
    