from flask import Flask, render_template, request
from analyzer import analyze_code

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    result = None

    if request.method == "POST":
        code = request.form.get("code", "")
        error_message = request.form.get("error", "")

        result = analyze_code(code, error_message)

    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)
