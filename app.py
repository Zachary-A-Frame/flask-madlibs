from flask import Flask, request, render_template
from stories import Story
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY'] = "chickieslayeggs213123123"
app.debug = True

debug = DebugToolbarExtension(app)

@app.route('/')
def home():
    """ Shows home page """
    return render_template("/home.html")

@app.route('/story')
def story():
    """ Shows our story """
    text = story.generate(request.args)
    return render_template("/story.html", text=text)
