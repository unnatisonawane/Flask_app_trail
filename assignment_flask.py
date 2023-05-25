from flask import Flask

app = Flask(__name__)

@app.route('/welcome')
def welcome_func():
    return "Welcome to ABC Corporation"

@app.route('/')
def details():
    return '''Company Name: ABC Corporation
    Location: India
    Contact Detail: 999-999-9999'''

if __name__=="__main__":
    app.run(host="0.0.0.0")


from flask import Flask, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return 'Home Page'

@app.route('/about')
def about():
    return 'About Page'

@app.route('/user/<username>')
def user_profile(username):
    return f'User Profile: {username}'

if __name__ == '__main__':
    with app.test_request_context():
        # Generating URLs using url_for()
        home_url = url_for('home')
        about_url = url_for('about')
        user_profile_url = url_for('user_profile', username='pwskill')

        # Printing the generated URLs
        print(f'Home URL: {home_url}')
        print(f'About URL: {about_url}')
        print(f'User Profile URL: {user_profile_url}')


