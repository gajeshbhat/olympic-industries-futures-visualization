from flask import Flask, render_template, request
from process_data import read_data_from_db

app = Flask(__name__)

# Define route for the chart page
@app.route("/")
def chart():

    # Get the selected chart column from the form data, or use the default values
    selected_column = request.args.get("columns", "open")

    chart_data = read_data_from_db(selected_column)
    print(chart_data["labels"])
    print(type(chart_data["labels"]))

    return render_template(
        "index.html",
        labels=chart_data["labels"],
        values=chart_data["values"],
        selected_column=selected_column,
        columns=chart_data["columns"],
    )

if __name__ == "__main__":
    app.run(debug=True)
