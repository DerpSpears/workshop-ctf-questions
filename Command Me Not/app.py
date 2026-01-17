from flask import Flask, render_template, request, jsonify
import subprocess
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html', title="Home Page")
@app.route('/process-input', methods=['POST'])
def process_input():
    data = request.get_json()
    user_input = data.get('input_value')
    command = f"whois {user_input}"
    output = subprocess.getoutput(command)
    return jsonify({'result': output})
    
if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
