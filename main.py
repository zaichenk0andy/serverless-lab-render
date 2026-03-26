<<<<<<< HEAD
from flask import Flask, request, jsonify
=======
from flask import Flask
>>>>>>> a150c1aba46fd7cc38af5d16c448f4de401806fd

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, Serverless! 🚀\n", 200, {'Content-Type': 'text/plain'}

<<<<<<< HEAD
@app.route('/echo', methods=['POST'])
def echo():
    data = request.get_json()
    return jsonify({
        "status": "received",
        "you_sent": data,
        "length": len(str(data)) if data else 0
    })
=======
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

>>>>>>> a150c1aba46fd7cc38af5d16c448f4de401806fd
