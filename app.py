from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

tasks = ['Pick kids from school', 'Do the dishes', 'Walk the dog']

@app.route("/")
@app.route("/index")
def index():
    return render_template('index.html')

@app.route("/tasks")
def task_list():
    return render_template("tasks.html", tasks=tasks)

@app.route("/addtask", methods=['GET'])
def add_task_get():
    return render_template("addtask.html")

@app.route("/addtask", methods=['POST'])
def add_task():
    task = request.form.get('task')
    tasks.append(task)
    print(tasks)
    return redirect(url_for("task_list"))

@app.route("/deletetask/<int:task_id>")
def delete_task(task_id):
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)
    return redirect(url_for('task_list'))
