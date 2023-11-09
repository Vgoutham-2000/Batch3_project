from flask import Flask #import flask

app = Flask(__name__) # init app 

@app.route('/') # url mapping
def home():
    return 'Hello, World! This is my Flask App.'

if __name__ == '__main__':
    app.run(debug=True)    
