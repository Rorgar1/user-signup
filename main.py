from flask import Flask, request

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!doctype html>
<html>
    <body> 
        <form action="/username" method = "POST">
            <label for="user_name">Username: </label>
            <input id="user_name" type="text" name="user_name" />
            <input type="submit" />
        </form>
    </body>
</html>
"""



@app.route("/")
def index():
    return form

@app.route ("/username", methods=["POST"])
def username():
    user_name = request.form["user_name"]
    return "<h1> Welcome, " + user_name + "</h1>"

app.run()
