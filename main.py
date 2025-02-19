from flask import Flask, render_template, request, redirect
from pymongo import MongoClient
import os

# Get MongoDB URI from environment variable
MONGODB_URI = os.environ.get('MONGODB_URI', 'mongodb://localhost:27017/')
client = MongoClient(MONGODB_URI)
db = client['Portfolio']

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contactus', methods=['POST'])
def contactus():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']
    
    doc = {
        'name': name,
        'email': email,
        'message': message
    }
    
    db.contactus.insert_one(doc)
    
    return redirect('/')

if __name__ == '__main__':
    # Get port from environment variable with a fallback
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)