
from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return 'Windy Lodge Inventory System is ready for deployment'

if __name__ == '__main__':
    app.run()
