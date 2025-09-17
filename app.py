from flask import Flask, render_template, request, redirect, url_for, session
import json

app = Flask(__name__)
app.secret_key = "secret"

# Load questions
with open("questions.json") as f:
    questions = json.load(f)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/quiz", methods=["GET", "POST"])
def quiz():
    if request.method == "POST":
        score = 0
        for i, q in enumerate(questions):
            selected = request.form.get(f"q{i}")
            if selected == q["answer"]:
                score += 1
        return redirect(url_for("result", score=score))
    return render_template("quiz.html", questions=questions, enumerate=enumerate)

@app.route("/result/<int:score>")
def result(score):
    return render_template("result.html", score=score, total=len(questions))

if __name__ == "__main__":
    app.run(debug=True)
