from google.appengine.ext import db

class User(db.Model):
    full_name = db.StringProperty()
    email = db.StringProperty()
    nickname = db.StringProperty()
    openid = db.StringProperty()

