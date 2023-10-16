# -*- coding: utf-8 -*-

from twocaptcha import TwoCaptcha
import os
import sys


import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait,Select
from selenium.webdriver.support import expected_conditions as EC 

import discord
from discord.ext import commands
import asyncio
import requests
import random
import datetime
from bs4 import BeautifulSoup
import re
import json
from pathlib import Path

sys.path.append(os.path.abspath(".."))
from attend_program import *


prefix_json="json/prefix.json"


class Attend(commands.Cog):
    def __init__(self,bot:commands.Bot):
        self.bot=bot



    async def cog_command_error(self, ctx: commands.Context, error: commands.CommandError):
        await ctx.send('An error occurred: {}'.format(str(error)))


    @commands.command(name='attend') 
    async def _attend(self, ctx: commands.Context, course_name: str = "None" , pwd: str= "None"):
        """點名"""
        if(course_name=="None" or pwd=="None"):
            await ctx.send("輸入錯誤，請重新輸入")
            return
        await ctx.send("點名中...")
        result=attend_main(course_name,pwd)
        await ctx.send(result)


    @commands.command(name='prefix')
    @commands.guild_only()
    async def setprefix(self, ctx, *, prefixes=""):
        """設定前綴"""
        
        if(prefixes==""):
            await ctx.send("please enter the prefix.")
            return


        with open(prefix_json,"rb") as f:
            custom_prefixes = json.load(f)
            custom_prefixes[ctx.guild.id] = prefixes
            dict=custom_prefixes
        f.close()
        with open(prefix_json,"w") as r:
            json.dump(dict,r)
        r.close()
        await ctx.send("Prefix was set to {} ".format(prefixes))
    

async def setup(bot):
    await bot.add_cog(Attend(bot))

    
    