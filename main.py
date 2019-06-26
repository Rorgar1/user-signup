from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)
app.config['DEBUG'] = True




@app.route("/",  methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")

    if request.method == "POST":
        user_name = str(request.form["user_name"])
        user_password = str(request.form["user_password"])
        v_password = str(request.form["v_password"])
        user_email = str(request.form["user_email"])

        if user_name == '' or len(user_name) < 3 or len(user_name) > 20 or ' ' in user_name:
            user_name_error = "Invalid username. Length must be 3-20 characters."
        else:
            user_name_error = ""

        if user_password == '' or len(user_password) < 3 or len(user_password) > 20 or ' ' in user_password:
            password_error = "Invalid password. Length must be 3-20 characters."
        else:
            password_error = ""

        if v_password != user_password:
            v_password_error = "Passwords do not match."
        else:
            v_password_error = ""

        if user_email == '' or len(user_email) < 3 or len(user_email) > 20 or ' ' in user_email or '@' not in user_email:
            email_error = "Invalid email."
        else:
            email_error = ""


        if len(user_name_error) > 0 or len(password_error) > 0 or len(v_password_error) > 0 or len(email_error) > 0:
            return render_template("index.html", user_name_error=user_name_error,
                                    password_error=password_error,
                                    v_password_error=v_password_error,
                                    email_error=email_error,
                                    user_name=user_name,
                                    user_email=user_email)
 
        else:  
            return render_template("welcome.html",user_name=user_name) #redirect("/welcome")

@app.route("/welcome", methods=['GET'])
def welcome_page():
    return render_template("welcome.html")
       




app.run()
