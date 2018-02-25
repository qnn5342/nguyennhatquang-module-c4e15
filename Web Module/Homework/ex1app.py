from flask import Flask, render_template, redirect
app = Flask(__name__)


@app.route('/about-me')
def aboutme():
    aboutme= "About me - Nguyen Nhat Quang"
    content= [
    {"name": "Nguyen Nhat Quang",
    "Work": "Ad-analyst at Coc Coc",
    "School": "Truman State University - USA",
    "Hobbies": "Soccer, reading, discussion",
    "Crush": "Top secret ^^",
    },
    ]

    return render_template('aboutme.html', aboutme=aboutme, content=content)

@app.route('/school')
def index():
    return redirect("http://techkids.vn")
if __name__ == '__main__':
  app.run(debug=True)
