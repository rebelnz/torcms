#db file
import pymongo
import unicodedata
import re
import os
import time
import bson
import datetime

from pprint import pprint

connection = pymongo.Connection("localhost",27017)
database = connection.torcms

def add_site_data(site_data):

    settings_data = database.site_settings.find_one()

    if settings_data:
        database.site_settings.remove({})        
    site_data['updated'] = datetime.datetime.now()
    database.site_settings.insert(site_data)
    return site_data

def get_site_settings():
    return database.site_settings.find_one()


def add_map_data(map_data):
    old_map_data = database.map_settings.find_one()
    if old_map_data:
        database.map_settings.remove({})        
    map_data['updated'] = datetime.datetime.now()
    database.map_settings.save(map_data)
    return map_data
