from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {
        'author': "haha",
        'title': "hahaha",
        "content": "hahahashhfk",
        'date_posted': "212121"
    },
    {
        'author': "haha",
        'title': "hahaha",
        "content": "hahahashhfk",
        'date_posted': "212121"
    },
    {
        'author': "haha",
        'title': "hahaha",
        "content": "hahahashhfk",
        'date_posted': "212121"
    }
]


@app.route('/home')
@app.route('/')
def home():
    return render_template("home.html", posts=posts)


@app.route('/about')
def about():
    return render_template("about.html", title="About")


if __name__ == "__main__":
    app.run(debug=True)
