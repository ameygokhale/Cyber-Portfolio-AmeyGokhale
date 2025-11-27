from flask import Flask, request, render_template

app = Flask(__name__)

# Hard-coded "correct" credentials for the lab
CORRECT_USERNAME = "securityadmin"
CORRECT_PASSWORD = "SuperSecure123"

@app.route("/", methods=["GET"])
def index():
    return render_template("login.html", error=None)

@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username", "")
    password = request.form.get("password", "")

    if username == CORRECT_USERNAME and password == CORRECT_PASSWORD:
        # SUCCESS RESPONSE – no failure string here
        return "Login successful! Welcome, {}.".format(username)
    else:
        # FAILURE RESPONSE – this text is what Hydra will look for
        error_message = "Login failed"
        return render_template("login.html", error=error_message)

if __name__ == "__main__":
    # Run on port 8080 to match our Hydra config
    app.run(host="0.0.0.0", port=8080, debug=True)
