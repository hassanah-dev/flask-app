from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template(template_name_or_list='index.html', active='home')


@app.route("/about")
def about():
    return render_template(template_name_or_list='about.html', title="About", active='about')


if __name__ == "__main__":
    app.run(debug=True)
