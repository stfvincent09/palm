from flask import Flask, request, render_template
import google.generativeai as palm
palm.configure(api_key="AIzaSyAEGxZJcd5ArXxuQqgLKz1Mah7a9v9jV6s")
model = {"model": "models/chat-bison-001"}
app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"])
def index():
    if request.method == "POST":
        q = request.form.get("q")
        r = palm.chat(
            **model,
            messages = q                
        )
        return(render_template("index.html", r = palm.chat(**model,messages = q).last))
    else:
        return(render_template("index.html", result ="Waiting for query..........."))

if __name__== "__main__":
    app.run()
