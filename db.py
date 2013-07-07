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


def add_address_data(address_data):
    old_address_data = database.address_settings.find_one()
    if old_address_data:
        database.address_settings.remove({})
    address_data['updated'] = datetime.datetime.now()
    database.address_settings.insert(address_data)
    return address_data

def get_address_settings():
    return database.address_settings.find_one()


def add_map_data(map_data):
    old_map_data = database.map_settings.find_one()
    if old_map_data:
        database.map_settings.remove({})
    map_data['updated'] = datetime.datetime.now()
    database.map_settings.save(map_data)
    return map_data

def get_map_data():
    data = database.map_settings.find_one()
    mapdata = {}
    if data:
        mapdata = data['loc'] # [{"latitude": "37.50209991181568"}, {"longitude": "126.77947998046875"}]
    return mapdata

def add_social_data(data):
    social_data = database.social_settings.find_one()
    if social_data:
        database.social_settings.remove({})
    data['updated'] = datetime.datetime.now()
    database.social_settings.insert(data)
    return data

def get_social_settings():
    return database.social_settings.find_one()


def add_analytics(data):
    data['updated'] = datetime.datetime.now()
    database.analytics.insert(data)
    return 
