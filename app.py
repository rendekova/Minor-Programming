from flask import Flask, render_template, request
import re
import string

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        plate = request.form['plate']
        if is_valid(plate):
            return render_template('valid.html', plate=plate)
        else:
            return render_template('invalid.html')

    return render_template('index.html', plates=[])

@app.route('/projects')
def projects():
    return render_template('myprojects.html')

@app.route('/about')
def about():
    return render_template('learnaboutme.html')

if __name__ == '__main__':
    app.run(debug=True)
