#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'


@app.route('/print/<string:New>')
def print_string(New):
    print(New)
    return New

@app.route('/count/<int:numbers>')
def count(numbers):
    num_list = [str(i) for i in range(numbers)]
    return '\n'.join(num_list) + '\n'

@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1, operation, num2):
    result = 0
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        if num2 != 0:
            result = num1 / num2
        else:
            return 'Error: Division by zero!'
    elif operation == '%':
        result = num1 % num2
    else:
        return 'Error: Invalid operation!'
    return str(result)




if __name__ == '__main__':
    app.run(port=5555, debug=True)
