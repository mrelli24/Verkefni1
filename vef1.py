from sys import argv

import bottle
from bottle import *

bottle.debug(True)


@route("/")
def index():
    return """
    <h2>Verkefni 1</h2>
    <a href="/about">Um okkur</a></p>
    <a href="/bio">Ferilskrá</a></p>
    <a href="/pics">Myndir</a></p>
    """


@route("/about")
def jobbi():
    return "Hér eru upplýsingar"

@route("/bio")
def jobbi():
    return "Hér ferilskrá"

@route("/pics")
def jobbi():
    return "Hér eru myndir"

bottle.run(host="0,0,0,0", port=argv[1])


#run(host='localhost', port=5000)
