from flask import Flask, request, jsonify
import math
import json
import os


app = Flask(__name__)

history_file = 'history.json'
if os.path.exists(history_file):
    with open(history_file, 'r') as f:
        operations_history = json.load(f)
else:
    operations_history = []

def save_history():
    with open(history_file, 'w') as f:
        json.dump(operations_history, f, indent=2)


def evaluate_operation(operation_str):
    operation_str = operation_str.replace('plus', '+').replace('minus', '-').replace('into', '*').replace('by', '/')
    try:
        result = eval(operation_str)
        return result, True
    except Exception as e:
        return None, False

def calculate_factorial(n):
    return math.factorial(int(n))

@app.route('/')
def hello():
    return "Type the Math Operations in URL"

@app.route('/<path:operation>')
def calculate(operation):
    operation = operation.replace('/', ' ')
    
    
    
    if operation.lower() == 'history':
        return jsonify({'history': operations_history})
    
    if 'powerof' in operation:
        nums = operation.split('powerof')
        if len(nums) == 2:
            result = float(nums[0]) ** float(nums[1])
            question = operation
            answer = result
            operations_history.append({'question': question, 'answer': answer})
            if len(operations_history) > 20:
                operations_history.pop(0)
            return jsonify({'question': question, 'answer': answer})
    
    if 'rootof' in operation:
        nums = operation.split('rootof')
        if len(nums) == 2:
            result = float(nums[0]) ** (1.0 / float(nums[1]))
            question = operation
            answer = result
            operations_history.append({'question': question, 'answer': answer})
            if len(operations_history) > 20:
                operations_history.pop(0)
            return jsonify({'question': question, 'answer': answer})
    
    if 'factorial' in operation:
        num = operation.replace('factorial', '').strip()
        try:
            result = calculate_factorial(num)
            
            answer = result
            question = operation
            operations_history.append({'question': question, 'answer': answer})
            if len(operations_history) > 20:
                operations_history.pop(0)
            return jsonify({'question': question, 'answer': answer})
        except:
            return jsonify({'error': 'Invalid operation'})
    
    result, success = evaluate_operation(operation)
    if success:
        question = operation
        question = question.replace('powerof', '^').replace('rootof', '√').replace('factorial', '!')
            
        question = (
            question
            .replace('plus', '+')
            .replace('minus', '-')
            .replace('into', '*')
            .replace('by', '/')
        )
        
        answer = result
        operations_history.append ({'question': question, 'answer': answer})
        if len(operations_history) > 20:
            operations_history.pop(0)
        save_history()
        return jsonify({'question': question, 'answer': answer})
    else:
        return jsonify({'error': 'Invalid operation'})
if __name__ == '__main__':
    app.run(debug=True)
