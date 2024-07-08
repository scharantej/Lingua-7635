
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    lessons = ['Lesson 1: Greetings', 'Lesson 2: Pronunciation', 'Lesson 3: Basic Grammar']
    exercises = ['Exercise 1: Write a short self-introduction', 'Exercise 2: Translate some simple phrases']
    grammar = ['Nouns', 'Verbs', 'Adjectives']
    return render_template('index.html', lessons=lessons, exercises=exercises, grammar=grammar)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
