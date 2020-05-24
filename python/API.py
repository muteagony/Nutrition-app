import flask
import database_connection
from flask_cors import CORS
import json


app = flask.Flask(__name__)
app.config["DEBUG"] = True


CORS(app)


@app.route("/", methods=["GET"])
def home():
    return json.dumps(
        database_connection.db_query("SELECT * FROM ingredient_schema LIMIT 3")
    )


app.run()
