from flask import Flask, render_template
app= Flask(__name__)

 
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about us')
def about():
    return render_template('/about.html')

@app.route('/Membership')
def membership():
    return render_template('membership.html')

@app.route('/Contact')
def contact():
    return render_template('contactus.html')

if __name__=='__main__':
    app.run(debug=True)