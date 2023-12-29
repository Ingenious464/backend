from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/about', methods=['GET'])
def about():
    data = {
        "name": "Adetunji Fatai",
        "gender": "Male",
        "github_url": "https://github.com/Ingenious464/",
        "framework": "Flask",
        "location": "Nigeria"
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
