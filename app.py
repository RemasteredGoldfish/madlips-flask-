from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/paniek')
def paniek():
    return render_template('paniek.html')

@app.route('/sumbit', methods=['POST'])
def submit_form():
    examplequestion1 = request.form.get('examplequestion1')
    examplequestion2 = request.form.get('examplequestion2')
    examplequestion3 = request.form.get('examplequestion3')
    examplequestion4 = request.form.get('examplequestion4')
    examplequestion5 = request.form.get('examplequestion5')
    examplequestion6 = request.form.get('examplequestion6')
    examplequestion7 = request.form.get('examplequestion7')

    # Do some processing with the form data
    result = f"Er zijn veel mensen die niet kunnen {examplequestion1}. Neem nou {examplequestion2}. Zelfs met de hulp van een {examplequestion3} of zelfs {examplequestion4} kan {examplequestion2} niet {examplequestion1}. Dat heeft niet te maken met een gebrek aan {examplequestion5}, maar met een te veel aan {examplequestion6}. Te veel {examplequestion6} leidt tot {examplequestion7} en dat is niet goed als je wilt {examplequestion1}. Helaas voor {examplequestion2}"

    return render_template('result_form.html', result=result)

@app.route('/sumbitTwo', methods=['POST'])
def sumbit_formTwo():
    question1 = request.form.get('question1')
    question2 = request.form.get('question2')
    question3 = request.form.get('question3')
    question4 = request.form.get('question4')
    question5 = request.form.get('question5')
    question6 = request.form.get('question6')
    question7 = request.form.get('question7')

    result = f"Er zijn veel mensen die niet kunnen {question1}. Neem nou {question2}. Zelfs met de hulp van een {question3} of zelfs {question4} kan {question2} niet {question1}. Dat heeft niet te maken met een gebrek aan {question5}, maar met een te veel aan {question6}. Te veel {question6} leidt tot {question7} en dat is niet goed als je wilt {question1}. Helaas voor {question2}"

    return render_template('result_formtwo.html', result=result)
app.run()