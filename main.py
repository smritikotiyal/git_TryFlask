from flask import Flask, flash, redirect, render_template, request, url_for


app = Flask(__name__)


@app.route('/')
def schema():
    return render_template('/schemaExp.html', the_title='Schema')


if __name__ == '__main__':
    app.run(debug=True)