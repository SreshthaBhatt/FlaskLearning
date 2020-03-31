import pymysql
from app import app
from flask import jsonify
from flask import flash, request

@app.route('/')
@app.route('/test')
def test():
    conn=pymysql.connect(db='test', user='root', passwd='Yashbhatt@123', host='localhost')
    cur=conn.cursor(pymysql.cursors.DictCursor)
    cur.execute("select * from CAN_AB_GLCA;")
    rows=cur.fetchall()
    resp=jsonify(rows)
    resp.status_code=200
    return resp
    cur.close()
    conn.close()

@app.errorhandler(404)
def not_found(error=None):
    message={
        'status':404,
        'message': 'Not Found'+ request.url,
    }
    resp=jsonify(message)
    resp.status_code=404
    return resp

if __name__=="__main__":
    app.run()

