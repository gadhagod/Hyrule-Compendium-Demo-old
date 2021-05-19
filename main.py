import flask
from pyrule_compendium import compendium

app = flask.Flask(__name__)
comp = compendium()

@app.route("/")
def home():
    res = comp.get_all()
    entries = sorted((res["creatures"]["food"] + res["creatures"]["non_food"] + res["equipment"] + res["monsters"] + res["materials"] + res["treasure"]), key=(lambda a: a["id"]))
    return(flask.render_template("index.html", entries=entries))

@app.route("/<entry>")
def entry(entry):
    res = comp.get_entry(entry)
    return flask.render_template("entry.html", entry=res)

if __name__ == "__main__": app.run()