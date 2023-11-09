from flask import Flask, render_template, request
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB configuration (local)
client = MongoClient('mongodb://localhost:27017/')
db = client["signup_app"]
collection = db["users"]

@app.route('/')
def index():
    return render_template('signup.html')

@app.route('/signup', methods=['POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        # Add additional fields as needed

        # Insert user data into the database
        user_data = {
            "username": username,
            "email": email,
            # Add additional fields as needed
        }
        collection.insert_one(user_data)
        
        return "Signup successful! Thank you for registering."

if __name__ == '__main__':
    app.run(debug=True)
