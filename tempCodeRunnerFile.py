from flask import Flask,jsonify,request
import run_test

app = Flask(__name__)#创建一个服务，赋值给APP

@app.route('/get_file',methods=['post'])#指定接口访问的路径，支持什么请求方式get，post

#json方式传参
def get_ss():
    file = request.json.get('file1')#获取带json串请求的username参数传入的值
    return jsonify(run_test.get_score(file))

#如果不在的话，返回err对应key的value转成的json串信息

app.run(host="192.168.43.49",port=8080,debug=True)