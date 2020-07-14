from flask import Flask


app = Flask(__name__)
app.config["SECRET_KEY"] = "helloworld"
app.config["DEBUG"] = True



from app import routes, forms