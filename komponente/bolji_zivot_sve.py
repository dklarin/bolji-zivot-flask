from flask import Blueprint, render_template
import pygsheets

from metode.sheets import plahte

pregled_bolji_zivot = Blueprint('pregled_bolji_zivot', __name__,
                                template_folder='templates')

wks = plahte()

@pregled_bolji_zivot.route('/bolji-zivot/', methods=['get', 'post'])
def sve_bolji_zivot():

    svi_retci = wks.get_all_records()  

    return render_template('bolji-zivoti.html', svi_retci=svi_retci)
