

from flask import Flask

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/')
def index():
    return render_template("main_page.html")

