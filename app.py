from flask import Flask 

app = Flask( __name__)

@app.route("/<string:operation>/<int:num1>/<int:num2>")
def calculate(operation, num1, num2):
    try:
        if operation == "add":
            return str(num1 + num2)
        elif operation == "sub":
            return str(num1 - num2)
        elif operation == "mul":
            return str(num1 * num2)
        elif operation == "div":
            return str(num1 / num2)
    except ZeroDivisionError:
        return "Division by zero is not allowed"
    
if __name__ == "__main__":
    app.run(host="0.0.0.0")