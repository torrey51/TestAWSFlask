from flask import Flask, render_template, request
app= Flask(__name__)

#route 1 (page 1) #Home
from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('home.html')

#route 2 (page 2) #contact
@app.route('/contact')
def contact():
    contact = request.args.get('contact')
    return render_template('contact.html', contact=contact)

#route 3 (page 3) #about
@app.route('/abouts')
def abouts():
    abouts = ['Seth Torrey', 'IFT 401 Capstone']
    return render_template('about.html', abouts=abouts)

#route 34 (page 4) #test
@app.route('/test')
def test():
    tests = ['']
    return render_template('test.html', tests=tests)
