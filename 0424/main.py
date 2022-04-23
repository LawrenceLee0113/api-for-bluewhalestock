from flask import Flask, render_template, request, json, jsonify
app = Flask(__name__)
# from flask_socketio import SocketIO
from flask_cors import CORS
# socketio = SocketIO(app, cors_allowed_origins='*')
CORS(app, resources={r"/.*": {"origins": ["http://43.254.19.106:8080/","https://bluewhale-stock.tw"]}})
import DBManager as DB
newStock_DB = DB.DBManager("localhost","bluewhal_yih","r0g{bYg+([jd","bluewhal_NewStock")



@app.route('/')
def index_page():
  return render_template("index.html")

@app.route('/get_data_base',methods=['GET', 'POST'])
def get_data_base():
  if request.method == 'GET':
    print("get")
  elif request.method == 'POST':
    account_id = request.form.get('account_id')
    database_name = request.form.get("database_name")
    table_name = request.form.get("table_name")
    column_name = request.form.get("column_name")
    values = newStock_DB.get_data("newstock_otc",["公司代號","公司名稱","承銷商"])
    return jsonify({"values":values})




#run server
if __name__ == "__main__":
  app.run(host='0.0.0.0', port=8080, debug=True,ssl_context='adhoc')