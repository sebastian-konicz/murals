from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def render_the_map():
    return render_template('mural_map.html')

if __name__ == '__main__':
    app.run(debug=True)