from flask import Flask

import settings

app = Flask('idtest')
app.config.from_object('idtest.settings')

import testapp


