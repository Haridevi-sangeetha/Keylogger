from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/clear")
def clear_logs():
    open("log.txt", "w").close()
    return "Cleared"

@app.route("/logs")
def get_logs():
    with open("log.txt", "r") as file:
        data = file.read()
    return jsonify({"logs": data})

if __name__ == "__main__":
    app.run(debug=True)