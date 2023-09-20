#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage
import os


hb_storage = os.environ.get('HBNB_TYPE_STORAGE')
if hb_storage == 'db':
    storage = DBStorage()
else:
    storage = FileStorage()
storage.reload()
