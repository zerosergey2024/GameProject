from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/gamecat')
def change_name():
    return render_template('gamecat.html')

@app.route('/change_email')
def change_email():
    return render_template('change_email.html')

@app.route('/change_avatar')
def change_avatar():
    return render_template('change_avatar.html')

if __name__ == '__main__':
    app.run(debug=True)