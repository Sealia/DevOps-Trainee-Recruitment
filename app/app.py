from flask import Flask, request,jsonify

from random import randrange

app=Flask(__name__)


@app.route('/echo', methods=["GET","POST"])
def response():
	try:
		if(request.is_json):
			data = request.get_json()
			if(data):
				return jsonify({"status": "OK", "msg":data})
			else:
				return jsonify({"status":"Error empty"})
		else:
			return jsonify({"status":"Error2"})
	except:
		return jsonify({"status":"Error"})

@app.route('/random', methods=["GET"])
def random():
	return jsonify({"status":"ok","number": randrange(1,100)})



if __name__ == '__main__':
	app.run()

	#curl -X POST -H 'Content-Type: application/json' http://127.0.0.1:5000/echo -d '{"name":"Sealia"}'
