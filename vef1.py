from bottle import route, run, template

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




run(host='localhost', port=5000)
