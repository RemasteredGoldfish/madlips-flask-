from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

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
    result = f"Er zijn veel mensen die niet kunnen {examplequestion1}. Neem nou {examplequestion2}. Zelfs met de hulp van een {examplequestion3} of zelfs {examplequestion4} kan {examplequestion2} niet {examplequestion1}. Dat heeft niet te maken met een gebrek aan {examplequestion5}, maar met een te veel aan {examplequestion6}. Te veel {examplequestion6} leidt tot {examplequestion7} en dat is niet goed als je wilt {examplequestion1}. Helaas voor {examplequestion2}."

    return render_template('result_form.html', result=result)

@app.route('/submitTwo', methods=['POST'])
def submit_formTwo():
    question1 = request.form.get('question1')
    question2 = request.form.get('question2')
    question3 = request.form.get('question3')
    question4 = request.form.get('question4')
    question5 = request.form.get('question5')
    question6 = request.form.get('question6')
    question7 = request.form.get('question7')
    question8 = request.form.get('question8')

    result = f"Er heerst paniek in het koninkrijk {question1}. Koning Egmond is ten einde raad en als koning {question6} ten einde raad is, dan roept hij zijn ten-einde-raadsheer {question2}.\n'{question2}! Het is een ramp! Het is een schande!'\n'Sire, Majesteit, Uwe Luidruchtigheid, wat is er aan de hand?'\n'Mijn {question1} is verdwenen! Zo maar, zonder waarschuwing. En ik had net {question5} voor hem gekocht!'\n'Majesteit, uw {question5} komt vast vanzelf weer terug?'\n'Ja da's leuk en aardig maar hoe moet ik in de tussentijd {question8} leren?'\n'Maar Sire, daar kunt u toch uw {question7} gebruiken.'\n'{question2}, je hebt helemaal gelijk! Wat zou ik doen als ik jou niet had.'\n'{question4}, Sire.'"

    return render_template('result_formtwo.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
