from flask import Blueprint, render_template

from metode.sheets import plahte

pregled_boljeg_zivota = Blueprint('pregled_boljeg_zivota', __name__,
                                  template_folder='templates')

worksheet = plahte()

@pregled_boljeg_zivota.route('/dan/<broj>', methods=['get', 'post'])
def jedan_dan(broj):

    svi_retci = worksheet.get_all_records()

    trazeni_redak = None
    for redak in svi_retci:
        if redak['redni_broj'] == int(broj):
            trazeni_redak = redak
            break

    return render_template('bolji-zivot.html',
                           trazeni_redak=trazeni_redak 
                           )