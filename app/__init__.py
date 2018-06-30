from flask import Flask, render_template

app = Flask(__name__)

########### INDEX #######################

@app.route('/')
def index():
	return render_template("index.html")

######## PAGE NOT FOUND ERROR #############
	
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")


if __name__ == "__main__":
	app.run()