from flask import Flask, request, jsonify, render_template
from student import will_pass

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/result', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        result_dict = request.form
        first_sem_num = int(result_dict['first_sem'])
        second_sem_num = int(result_dict['second_sem'])
        pass_or_not = will_pass(first_sem_num, second_sem_num)
        return pass_or_not


if __name__ == '__main__':
    app.run()
