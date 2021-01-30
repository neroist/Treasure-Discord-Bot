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

MClient = pymongo.MongoClient(f"mongodb+srv://{db['mongodb_username']}:{db['mongodb_password']}@{db['mongodb_cluster']}/Discord?retryWrites=true&w=majority")
Mdb = MClient.Discord
econ = Mdb.economy

class EconUser(discord.Member, object):
    def __init__(self, money=100, items: dict = DefaultItems, pet = None, health = 150, **options):
        self.money = money
        self.items = items
        self.weapons = items['weapons']
        self.food = items['food']
        self.pet_food = items['pet_food']
        self.options = options

    def create(self, user: discord.Member):
        """Creates and Adds EconUser to db, 
        creates the connection between the cog and the db. 
        For now uses the synchronous pymongo"""

        omlet = {'_id': user.id, 'items': self.items}

        econ.insert_one(omlet)
        print('Successfully created EconUser')

def setup(bot):
    pass