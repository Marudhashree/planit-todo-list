from flask import Flask, request, redirect, url_for, render_template_string

app = Flask(__name__)

# Task list (stores tasks and their completion status)
tasks = []

# HTML Template inside Python
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PlanIt - To-Do List</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            margin: 50px;
            background: linear-gradient(to right, #6dd5fa, #2980b9);
            color: white;
        }
        h2 {
            font-size: 28px;
        }
        form {
            margin-bottom: 20px;
        }
        input {
            padding: 10px;
            width: 250px;
            border-radius: 5px;
            border: none;
        }
        button {
            padding: 10px 15px;
            background: #ffcc00;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-weight: bold;
        }
        button:hover {
            background: #ffdb4d;
        }
        ul {
            list-style-type: none;
            padding: 0;
        }
        li {
            font-size: 18px;
            margin: 10px 0;
            background: rgba(255, 255, 255, 0.2);
            padding: 10px;
            border-radius: 5px;
            display: flex;
            justify-content: center;
            align-items: center;
            gap: 10px;
        }
        .completed {
            text-decoration: line-through;
            color: lightgray;
        }
        .task-container {
            display: flex;
            gap: 10px;
            align-items: center;
        }
        a {
            text-decoration: none;
            font-weight: bold;
            color: #ffcc00;
        }
        a:hover {
            color: #ffdb4d;
        }
    </style>
</head>
<body>
    <h2>PlanIt - Simple To-Do List</h2>
    
    <form action="/add" method="post">
        <input type="text" name="task" placeholder="Enter a task" required>
        <button type="submit">Add Task</button>
    </form>

    <ul>
        {% for task in tasks %}
            <li>
                <span class="{% if task.completed %}completed{% endif %}">{{ task.text }}</span>
                <a href="{{ url_for('toggle_task', task_id=loop.index0) }}">✅</a>
                <a href="{{ url_for('delete_task', task_id=loop.index0) }}">❌</a>
            </li>
        {% endfor %}
    </ul>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE, tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    task_text = request.form.get('task')
    if task_text:
        tasks.append({"text": task_text, "completed": False})  # Store task with completion status
    return redirect(url_for('index'))

@app.route('/toggle/<int:task_id>')
def toggle_task(task_id):
    if 0 <= task_id < len(tasks):
        tasks[task_id]["completed"] = not tasks[task_id]["completed"]
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
