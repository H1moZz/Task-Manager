from flask import Flask, request, jsonify

app = Flask(__name__)

tasks = []

@app.route("/")
def Home():
    return "Hello this is Task Manager"

@app.route("/tasks", methods=["POST"])
def add_task():
    data = request.get_json()

    if not data or not data.get("title"):
        return jsonify({"err":"Title is required data"}), 400

    task = {
        "id": len(tasks) + 1,
        "title": data["title"],
        "done": False 
    }
    tasks.append(task)
    return jsonify(task), 201

@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify(tasks), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)