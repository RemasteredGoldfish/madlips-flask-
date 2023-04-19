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
    result = f"Er zijn veel mensen die niet kunnen {examplequestion1}. Neem nou {examplequestion2}. Zelfs met de hulp van een {examplequestion3} of zelfs {examplequestion4} kan {examplequestion2} niet {examplequestion1}. Dat heeft niet te maken met een gebrek aan {examplequestion5}, maar met een te veel aan {examplequestion6}. Te veel {examplequestion6} leidt tot {examplequestion7} en dat is niet goed als je wilt {examplequestion1}. Helaas voor {examplequestion2}"

    return render_template('result_form.html', result=result)
app.run(debug=True)