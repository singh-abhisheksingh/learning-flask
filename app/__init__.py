from flask import Flask, render_template, flash
from flask import request, url_for, redirect

from contentManagement import Content

TOPIC_LIST = Content()

app = Flask(__name__)
app.secret_key = "super secret key"

########### INDEX #######################

@app.route('/')
def index():
	return render_template("index.html", TOPIC_LIST=TOPIC_LIST)

############ LOGIN ######################

@app.route('/login/', methods = ['GET','POST'])
def loginpage():
	error = None
	try:
		print ("in try")
		if request.method == "POST":
			attempted_username = request.form['username']
			attempted_password = request.form['password']
			
			# attempted_username = request.form.get('username')
			# attempted_password = request.form.get('password')

			print("in POST")
			flash(attempted_username)
			flash(attempted_password)
			print(attempted_username)
			print(attempted_password)

			if attempted_username == "admin" and attempted_password == "password":
				return redirect(url_for("template"))
			else:
				error = "Invalid Credentials. Try Again."
		else:
			attempted_username = request.args.get('username')
			attempted_password = request.args.get('password')

			print("in POST else")
			flash(attempted_username)
			flash(attempted_password)
			print(attempted_username)
			print(attempted_password)

			if attempted_username == "admin" and attempted_password == "password":
				return redirect(url_for("template"))
			else:
				error = "Invalid Credentials. Try Again."
				
		return render_template("login.html", error=error)

	except Exception as e:
		flash(e)
		print("in except")
		return render_template("login.html", error=error)

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