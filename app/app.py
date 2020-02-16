from flask import Flask, request,jsonify

from random import randrange

app=Flask(__name__)


@app.route('/echo', methods=["POST"])
def response():
	try:
		if(request.is_json):
			data = request.get_json()
			if(data):
				return jsonify({"status": "OK", "msg":data})
			else:
				return jsonify({"status":"Error"})
		else:
			return jsonify({"status":"Error"})
	except:
		return jsonify({"status":"Error"})

@app.route('/random', methods=["GET"])
def random():
	return jsonify({"status":"ok","number": randrange(1,100)})


if __name__ == '__main__':
	app.run(debug=True, host = '0.0.0.0')

	#curl -X POST -H 'Content-Type: application/json' http://127.0.0.1:5000/echo -d '{"name":"Sealia"}'
