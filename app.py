from flask import Flask, render_template, request
from process_data import read_data_from_db
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

# Define route for the index page
@app.route("/")
def index():
    # Get the selected chart column from the form data, or use the default values
    selected_column = request.args.get("columns", "open")
    chart_data = read_data_from_db(selected_column)
    
    return render_template(
        "index.html",
        labels=chart_data["labels"],
        values=chart_data["values"],
        selected_column=selected_column,
        columns=chart_data["columns"],
    )

if __name__ == "__main__":
    app.run(debug=True)
