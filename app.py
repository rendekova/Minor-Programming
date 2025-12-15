from flask import Flask, render_template, request
import re
import string
# from database import Database # 

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True


# db = Database('vanity.db') 
# db.init_db() 

# ... (all your functions)

@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        plate = request.form['plate']
        # db.add_numberPlates(plate) 
        if is_valid(plate):
            return render_template('valid.html', plate=plate)
        else:
            return render_template('invalid.html')

    # plates = db.get_numberPlates()
    return render_template('index.html', plates=[]) # App now returns an empty list


