import random
import discord
import json
import sys
import asyncio
from replit import db
from discord.ext import commands, tasks
from os import listdir
from itertools import cycle
import datetime as dt
import pymongo
from os import system as sys

statuses = cycle([
    discord.Activity(type=discord.ActivityType.competing, name="A Hypixel Tournament"),
    discord.Activity(type=discord.ActivityType.competing, name="A Box"),
    discord.Activity(type=discord.ActivityType.watching, name="hanime.tv"),
    discord.Activity(type=discord.ActivityType.watching, name="4anime.to"),
    discord.Activity(type=discord.ActivityType.watching, name="9anime.live"),
    discord.Activity(type=discord.ActivityType.watching, name="hentaihaven.xxx"),
    discord.Activity(type=discord.ActivityType.listening, name="MC Virgins"),
    discord.Activity(type=discord.ActivityType.watching, name="Pokimane Fart Compilation 4k HDR Dolby Digital"),
    discord.Activity(type=discord.ActivityType.watching, name="xvideos.com"),
    discord.Game(name="Naruto Storm 4"),
    discord.Game(name=".help"),
    discord.Activity(type=discord.ActivityType.streaming, name="epic memes"),
    discord.Activity(type=discord.ActivityType.listening, name="MC Virgins"),
    discord.Activity(type=discord.ActivityType.listening, name=".help"),
    discord.Activity(type=discord.ActivityType.watching, name="hanime.tv"), 
    discord.Game(name='With your dads pp'),
    discord.Activity(type=discord.ActivityType.playing, name="Undertale"),
    discord.Activity(type=discord.ActivityType.custom, name="Coding"),
    ])