from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy
from flask_scss import Scss
from datetime import datetime

#my app setup
app = Flask(__name__)
Scss(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Mytask(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Boolean, default=False)
    started = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Task {self.id}>"
    
with app.app_context():
    db.create_all()
    

# Route setup
@app.route("/", methods=["GET","POST"])
def index():
    # Add a task
    if request.method == "POST":
        current_task = request.form["content"]
        new_task = Mytask(content=current_task)
        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect("/")
        except Exception as e:
            print(f"Error{e}")
            return f"Error adding task: {e}"
    # See all tasks
    else:
        tasks = Mytask.query.order_by(Mytask.started).all()
        return render_template("index.html", tasks=tasks)

# Delete an Item
@app.route("/delete/<int:id>")
def delete(id:int):
    delete_task = Mytask.query.get_or_404(id)
    try:
        db.session.delete(delete_task)
        db.session.commit()
        return redirect("/")
    except Exception as e:
        return f"Error deleting task: {e}"

# Edit an Item
@app.route("/edit/<int:id>", methods=["GET","POST"])
def edit(id:int):
    edit_task = Mytask.query.get_or_404(id)
    if request.method == "POST":
        edit_task.content = request.form["content"]
        edit_task.completed = True if 'completed' in request.form else False
        try:
            db.session.commit()
            return redirect("/")
        except Exception as e:
            return f"Error updating task: {e}"
    else:
        return render_template("edit.html", task=edit_task)

#run and debug
if __name__ == "__main__":
   app.run(debug=True)
