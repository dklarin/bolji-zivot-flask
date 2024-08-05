from flask import Blueprint, render_template, request, redirect

from metode.sheets import plahte

dodaj_dan = Blueprint('dodaj_dan', __name__,
                      template_folder='templates')

worksheet = plahte()

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
    
    bioaktiv = ['Da', 'Ne']    
  
    
    if request.method == 'POST':
        
        dorucak = request.form['dorucak']
        orasi = request.form['orasi']
        bioaktiv = request.form['bioaktiv']        

        if orasi == 'Otvori za odabir':
            orasi = 0    
        else:
            orasi = orasi    
    
        if dorucak != 'Otvori za odabir':        
            novi_red = [redni_broj, '05.08.2024', dorucak]
            worksheet.insert_rows(row=redni_broj + 1, values=[novi_red])
    
        
        elif dorucak == 'Otvori za odabir' and orasi != 0:
            col_values = worksheet.get_col(3, include_tailing_empty=False)  # Broj 3 označava treći stupac (C)
            last_row = len(col_values)
            
            new_value = orasi
            worksheet.update_value((last_row, 5), new_value)
        elif dorucak == 'Otvori za odabir' and orasi == 0:
            col_values = worksheet.get_col(3, include_tailing_empty=False)  # Broj 3 označava treći stupac (C)
            last_row = len(col_values)
            
            new_value = bioaktiv
            worksheet.update_value((last_row, 6), new_value)   
        
        else:
            print('Hi')
      
             
        
    
        # Da ne radi dupli POST prilikom osvježavanja stranice
        return redirect('/novi_dan')

    return render_template('novi_dan.html',
                           redni_broj=redni_broj,
                           dorucci=dorucci,
                           stupac_orasi=stupac_orasi,
                           bioaktiv=bioaktiv)