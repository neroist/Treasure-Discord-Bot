#WIP

import discord 
from discord.ext import commands
import asyncio
import pymongo
from replit import db


DefaultItems = {
    'weapons' :[
        'pistol', 
        'knife'
    ],

    'food':[
        'bread',
        'raw chicken', 
        'apples'
    ],

    'pet_food':[
        None
    ]

}

class EconUser(discord.Member, object):
    def __init__(self, money=100, items: dict = DefaultItems, pet = None, health = 150, **options):
        self.money = money
        self.items = items
        self.weapons = items['weapons']
        self.food = items['food']
        self.pet_food = items['pet_food']
        self.options = options

    def create(self, user: discord.Member):
        pass

def setup(bot):
    pass
