from flask import Flask
from flask import render_template, url_for, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chatbot', methods = ['GET', 'POST'])
def form():
    if request.method == 'POST':
        username = request.form['username']
        return render_template('chatbot.html', username=username)

# @app.route('/return_form/<glon>', methods = ['GET', 'POST'])
# def return_form(glon):
#     return render_template('return_form.html', glon=glon)

if __name__ == '__main__':
    app.debug = True
    app.run()