from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('paniek.html')

@app.route('/sumbit', methods=['POST'])
def sumbit_form2():
    question1 = request.form.get('question1')
    question2 = request.form.get('question2')
    question3 = request.form.get('question3')
    question4 = request.form.get('question4')
    question5 = request.form.get('question5')
    question6 = request.form.get('question6')
    question7 = request.form.get('question7')

    result2 = f"Er zijn veel mensen die niet kunnen {question1}. Neem nou {question2}. Zelfs met de hulp van een {question3} of zelfs {question4} kan {question2} niet {question1}. Dat heeft niet te maken met een gebrek aan {question5}, maar met een te veel aan {question6}. Te veel {question6} leidt tot {question7} en dat is niet goed als je wilt {question1}. Helaas voor {question2}"

    return render_template('result_form2.html', result2=result2)
app.run(debug=True)