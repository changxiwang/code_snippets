from flask import Flask, render_template

app = Flask(__name__)

posts =[
    {
        'author': 'Changxi',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'June 7, 2018'
    },

    {
        'author': 'Ting',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'June 8, 2020'
    }



]

@app.route('/')
@app.route('/home')
def hello():
    #name = request.args.get("name", "World")
    return render_template('home.html',posts=posts)

@app.route('/about')
def about():
    #name = request.args.get("name", "World")
    return render_template('about.html',title='About')

if __name__ == '__main__':
    app.run(debug=True)