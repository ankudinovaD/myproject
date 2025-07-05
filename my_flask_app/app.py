from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__) #Створення Flask-додатку.
app.config['SECRET_KEY'] = 'daria' #дуже секретний ключ
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///MiniPlanner.db'#Вказуємо шлях до SQLite-бази.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #Вимикаємо відстеження змін — щоб уникнути зайвих попереджень.

db = SQLAlchemy(app) #Ініціалізація БД


# Розписуємо структуру БД?
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    priority = db.Column(db.String(10), default='low')
    done = db.Column(db.Boolean, default=False)


    def __repr__(self):
        return f'<Task {self.title}>'

with app.app_context():
        db.create_all()  # створюємо таблиці за моделями, якщо вони ще не існують

@app.route("/") #Моя головна сторінка
def index():
    tasks = Task.query.order_by(Task.done.asc(), Task.priority.desc()).all()
    return render_template("index.html", tasks=tasks)

# Те що додає задачі
@app.route("/add", methods=["POST"])
def add():
    title = request.form["title"]
    priority = request.form.get("priority", "low")
    if title:
        task = Task(title=title, priority=priority)
        db.session.add(task)
        db.session.commit()
    return redirect(url_for("index"))

# Те що маркує їх як виконані
@app.route("/done/<int:task_id>")
def done(task_id):
    task = Task.query.get_or_404(task_id)
    task.done = True
    db.session.commit()
    return redirect(url_for("index"))

# Видалення задачі
@app.route("/delete/<int:task_id>")
def delete(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for("index"))

# ---------------------
if __name__ == "__main__":
    app.run(debug=True)
    