from flask import Flask, render_template

# Making our app
app = Flask(__name__)

# Make the home page 
@app.route("/")
def home():
    return render_template("home_page.html")

# Making the about page 
@app.route('/about')
def about_page():
    return render_template("about_page.html")

# Make the neural network page
@app.route("/nnpage")
def neural_network_page():
    return render_template("nn_page.html")

# Make the pygame page 
@app.route("/pygamepage")
def pygame_page():
    return render_template("pygame_page.html")

# Running our app
if __name__ == "__main__":
    app.run(debug=True)