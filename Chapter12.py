from flask import Flask, request
import pymysql
app = Flask(__name__)
def getConnection():
  return pymysql.connect(host='localhost', user='dream', password='hack', db='dreamhack', charset='utf8')
@app.route('/' , methods=['GET'])
def index():
  username = request.args.get('username')
  sql = "select username from users where username='%s'" %username
  conn = getConnection()
  curs = conn.cursor(pymysql.cursors.DictCursor)
  curs.execute(sql)
  rows = curs.fetchall()
  conn.close()
  if(rows[0]['username'] == "admin"):
    return "True"
  else:
    return "False"
app.run(host='0.0.0.0', port=8000)