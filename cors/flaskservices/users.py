from flask import Flask,jsonify
from flask_cors import CORS

users = {"name":["burak","emre","efe","doruk"]}
app = Flask(__name__)
CORS(app)

@app.route("/get-users")
def get_users():
    return jsonify(users)

if __name__ == "__main__":
    app.run(debug=True,host='localhost',port=8001)
