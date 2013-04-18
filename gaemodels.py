
from google.appengine.ext import db

class Association(db.Model):
    """
    An association with another OpenID server, either a consumer or a provider.
    """
    url         = db.LinkProperty()
    handle      = db.StringProperty()
    association = db.TextProperty()
    created     = db.DateTimeProperty(auto_now_add=True)


class UsedNonce(db.Model):
    """
    An OpenID nonce that has been used.
    """
    server_url  = db.LinkProperty()
    timestamp   = db.DateTimeProperty()
    salt        = db.StringProperty()

