"""A simple Flask app."""

from flask import Flask, render_template, session, request, redirect

app = Flask(__name__)
app.secret_key = "RANDOM SECRET KEY"

@app.route('/')
def show_homepage():
    """Show homepage."""
    return render_template('homepage.html')

###############################
#                             #
# 1) Finish the routes below. #
#                             #
###############################


@app.route('/form')
def show_form():
    """Show form with message options."""
    pass

@app.route('/results')
def show_results():
    """Show resulting message."""
    pass


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
