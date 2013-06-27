#db file
import pymongo
import unicodedata
import re
import os
import time
import bson

from pprint import pprint

connection = pymongo.Connection("localhost",27017)
database = connection.torcms
