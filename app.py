from flask import Flask, render_template
from flask_bootstrap import Bootstrap

from komponente.bolji_zivot_sve import pregled_bolji_zivot

app = Flask(__name__)
bootstrap = Bootstrap(app)

app.register_blueprint(pregled_bolji_zivot)

@app.route('/')
def index():
    return render_template('index.html')
