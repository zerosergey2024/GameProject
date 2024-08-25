from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/change_name')
def change_name():
    return render_template('change_name.html')

if __name__ == '__main__':
    app.run(debug=True)