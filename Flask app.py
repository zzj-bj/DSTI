# You cannot run this in jupyter, instead you have to convert it into a script adn launch it from terminal

from flask import Flask
import uuid

# Create a new flask application
app = Flask(__name__)

# Create a id
id = str(uuid.uuid4())

# Create the root route
@app.route("/")
def hello_world():
    return "<p>Hello, World! "+id+" </p>"

# Create another route
@app.route("/bye")
def bye():
    return "<p>Bye, World!</p>"

# Run the flask server on port 5000 in debug mode
app.run(debug=True,port=5000,host='0.0.0.0')