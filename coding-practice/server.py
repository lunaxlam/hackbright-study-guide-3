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

@app.route('/save-name')
def save_name():
    """Save the name into the 'name' session key."""

    name = request.args.get("name")

    session["name"] = name

    return redirect('/')


@app.route('/form')
def show_form():
    """Show form with message options."""
    return render_template('form.html')

@app.route('/results')
def show_results():
    """Show resulting message."""

    message = request.args.get("message")

    return render_template('results.html', message=message)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
