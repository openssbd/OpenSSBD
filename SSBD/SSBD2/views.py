# -*- coding: utf-8 -*-

myDebug=True

MIDDLEWARE_CLASSES = (
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.transaction.TransactionMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
)

from models import *

from xml.dom import minidom    # needed by generateDS
from xml.dom import Node       # needed by generateDS
import bdmllib    # generateDS generated bdml interface

#TODO create level to control the necessary print statement
def debugPrint(string):
#   if __debug__:
   if myDebug==True:
       print string
   else:
       return
