from flask import Flask, render_template, request, json, jsonify
app = Flask(__name__)
# from flask_socketio import SocketIO
from flask_cors import CORS
# socketio = SocketIO(app, cors_allowed_origins='*')
CORS(app, resources={r"/.*": {"origins": ["http://43.254.19.106:8080/","https://bluewhale-stock.tw"]}})



@app.route('/')
def index_page():
  return render_template("index.html")

#run server
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True,ssl_context='adhoc')