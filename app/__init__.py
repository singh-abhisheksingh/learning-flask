from flask import Flask, render_template, flash

from contentManagement import Content

app = Flask(__name__)
app.secret_key = "super secret key"

########### INDEX #######################

@app.route('/')
def index():
	return render_template("index.html", TOPIC_LIST=TOPIC_LIST)

############ FLASH MESSAGING #############

@app.route('/nextpage/')
def nextpage():
	flash("flash test !!!")
	flash("flashing it again !!!")
	flash("flash once more :-p")
	return render_template("nextpage.html")

############# ERROR HANDLING #############

@app.route('/main/')
def main():
	try:
		return render_template("index.html", TOPIC_LIST=UNDEFINED_TOPIC_LIST)
	except Exception as e:
		return str(e)

######## PAGE NOT FOUND ERROR #############
	
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

######## METHOD NOT FOUND ERROR ############

@app.errorhandler(405)
def method_not_found(e):
    return render_template("405.html")

############# TEMPLATE PAGE ################

@app.route('/template/')
def template():
	return render_template("template.html")


if __name__ == "__main__":
	app.run()