from flask import Blueprint, render_template, request, redirect
import datetime
from collections import Counter

from metode.sheets import plahte

dodaj_dan = Blueprint('dodaj_dan', __name__,
                      template_folder='templates')

worksheet = plahte()
trenutni_datum = datetime.date.today()

datum = datetime.datetime.strptime(str(trenutni_datum), '%Y-%m-%d')
formatiran_datum = datum.strftime('%d.%m.%Y')

@dodaj_dan.route('/novi_dan/', methods=['get', 'post'])
def novi_dan():
    
    stupac_redni_broj = [value for value in worksheet.get_col(1) if value]
    posljednja_vrijednost = stupac_redni_broj[-1]
    redni_broj = int(posljednja_vrijednost) + 1 
    
    stupac_dorucci = [value for value in worksheet.get_col(3) if value]
    dorucci = set(stupac_dorucci[2:])   
    dorucci = sorted(dorucci)
    
    stupac_orasi = [value for value in worksheet.get_col(5) if value]     
    stupac_orasi = set(stupac_orasi[2:])   
    stupac_orasi = {int(element) for element in stupac_orasi} # pretvaranje elemenata iz str u int 
    stupac_orasi = sorted(stupac_orasi)
    
    dane = ['Da', 'Ne']    
    
    # Treći stupac (stupac C) - pronađite zadnji popunjeni redak
    col_values = worksheet.get_col(3, include_tailing_empty=False)  # Broj 3 označava treći stupac (C)
    last_row = len(col_values)  # Zadnji popunjeni redak
    
    print(last_row)
    okini=''
    
    if (last_row - 2) % 14 == 0:
        print('okini nokte')
        okini = 'okini nokte na šakama'
    else:
        print('Ne treba kidati nokte')
        okini = 'ne treba okiniti nokte na šakama'
    
    if (last_row - 2) % 28 == 0:
        print('okini nokte')
        stopala = 'okini nokte na stopalima'
    else:
        print('Ne treba kidati nokte')
        stopala = 'ne treba okiniti nokte na stopalima'

    
    if request.method == 'POST':
        
        dorucak = request.form['dorucak']
        orasi = request.form['orasi']
        bioaktiv = request.form['bioaktiv']    
        trbusnjaci = request.form['trbusnjaci']      
        nokti_sake = request.form['nokti_sake']
        
        def new_value(new_value, col):
            col_values = worksheet.get_col(3, include_tailing_empty=False)  # Broj 3 označava treći stupac (C)
            last_row = len(col_values)
            
            new_value = new_value
            worksheet.update_value((last_row, col), new_value)  
        
      
            
     
         
           
            
       
        
        otvori ='Otvori za odabir'           
    
        if dorucak != otvori:        
            novi_red = [redni_broj, formatiran_datum, dorucak]
            worksheet.insert_rows(row=redni_broj + 1, values=[novi_red])        
        elif dorucak == otvori and orasi != otvori:          
            new_value(orasi, 5)
        elif dorucak == otvori and orasi == otvori and bioaktiv != otvori:           
            new_value(bioaktiv, 6)
        elif dorucak == otvori and orasi == otvori and bioaktiv == otvori and trbusnjaci != '':        
            new_value(trbusnjaci, 7)  
        elif dorucak == otvori and orasi == otvori and bioaktiv == otvori and trbusnjaci == '':        
            new_value(nokti_sake, 8)       
        else:
            print(otvori)        
    
        # Da ne radi dupli POST prilikom osvježavanja stranice
        return redirect('/novi_dan')

    return render_template('novi_dan.html',
                           redni_broj=redni_broj,
                           dorucci=dorucci,
                           stupac_orasi=stupac_orasi,
                           dane=dane,
                           okini=okini,
                           stopala=stopala
                           )