from flask import Flask, render_template
from flask_bootstrap import Bootstrap

from komponente.bolji_zivot_sve import pregled_bolji_zivot
from komponente.bolji_zivot_jedan import pregled_boljeg_zivota
from komponente.bolji_zivot_dodaj import dodaj_dan

app = Flask(__name__)
bootstrap = Bootstrap(app)

app.register_blueprint(pregled_bolji_zivot)
app.register_blueprint(pregled_boljeg_zivota)
app.register_blueprint(dodaj_dan)

@app.route('/')
def index():
    return render_template('index.html')
