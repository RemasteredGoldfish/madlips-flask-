from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit_form():
    examplequestion1 = request.form.get('examplequestion1')
    examplequestion2 = request.form.get('examplequestion2')
    examplequestion3 = request.form.get('examplequestion3')
    examplequestion4 = request.form.get('examplequestion4')
    examplequestion5 = request.form.get('examplequestion5')
    examplequestion6 = request.form.get('examplequestion6')
    examplequestion7 = request.form.get('examplequestion7')

    # Do some processing with the form data
    result = f"The result of the form submission is: {examplequestion1}, {examplequestion2}, {examplequestion3}, {examplequestion4}, {examplequestion5}, {examplequestion6}, {examplequestion7}."

    return render_template('result_form.html', result=result)
app.run(debug=True)