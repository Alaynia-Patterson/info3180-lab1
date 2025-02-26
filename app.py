from flask import Flask, render_template

app = Flask(__name__)

'''
# Routing for your application.
# Put your routes below this comment
'''
'''
# Home Route
'''
@app.route('/')
def home():
    return render_template('index.html')

'''
# About Route
'''
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/not_found')
def not_found():
    return render_template('404.html')

@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)
