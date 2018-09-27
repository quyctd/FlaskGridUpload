from mongoengine import *
from datetime import datetime

class Image(Document):
    data = ImageField()
    time_stamp = DateTimeField(default = datetime.now())
    