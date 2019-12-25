from flask import render_template
from app import app

@app.route("/")
def index():
    """
    view root paage that returns back the index page and its data
    """
    title='cat-co-news see headline news'
    return render_template('index.html',title=title)

