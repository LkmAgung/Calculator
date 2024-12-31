from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/calculate", methods=["POST"])
def calculate():
    try:
        num1 = float(request.form["num1"])
        num2 = float(request.form["num2"])
        operator = request.form["operator"]
        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            result = num1 / num2
        else:
            result = "Invalid Operator"
        return render_template("index.html", result=result)
    except Exception as e:
        return render_template("index.html", result="Error: " + str(e))

if __name__ == "__main__":
    app.run(debug=True)
