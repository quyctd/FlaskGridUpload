import mongoengine

# mongodb://<dbuser>:<dbpassword>@ds163382.mlab.com:63382/flaskgrid
host = "ds163382.mlab.com"
port = 63382
db_name = "flaskgrid"
user_name = "admin"
password = "admin123"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())