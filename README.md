# Futures Data Flask Web Application

This is a Flask web application that displays futures data for Lumbers. The application reads data from an Excel file, cleans it up, and stores it in a SQLite database. The user can select a column to display in a line chart using a form on the index page.

The application uses the following technologies:

1. Python
2. Flask
3. SQLite
4. Pandas
5. Chart.js

## Getting Started
To run this application, you need to have Python 3 on your system. You can download Python 3 from https://www.python.org/downloads/.

## Installation
1. Initalize the environment `python3 -m venv venv`
2. Activate the environment `source venv/bin/activate`
3. Install the required packages `pip install -r requirements.txt`
## Run the application:
`python app.py`

Open your web browser and go to http://127.0.0.1:5000/ to view the application.

## Usage
On the index page, select a column from the dropdown list to display the corresponding data in a line chart.
