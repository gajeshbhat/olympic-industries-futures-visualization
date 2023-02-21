import sqlite3
import os
import pandas as pd

# Check if the database already exists, otherwise create it
def create_db_if_not_exists():
    if not os.path.exists("futures_data.db"):
        conn = sqlite3.connect("futures_data.db")
        c = conn.cursor()

        # Create table to store the futures data
        c.execute(
            """CREATE TABLE futures_data
                    (date text, open real, high real, low real, close real, adj_close real, volume real)"""
        )
        futures_data = read_data_from_excel()

        futures_data.to_sql("futures_data", conn, if_exists="replace", index=False)

        # Close the database connection
        conn.close()


# Open the database connection and read the data to plot
def read_data_from_db(column):
    # Create the database if it doesn't exist
    create_db_if_not_exists()

    # Connect to the database and fetch the data to plot
    conn = sqlite3.connect("futures_data.db")

    query = "SELECT date, {0} FROM futures_data".format(column)
    data = pd.read_sql(query, conn)

    # Close the database connection
    conn.close()

    # Generate the chart
    labels = data["date"].tolist()
    values = data[column].tolist()
    columns = ['open', 'high', 'low', 'close', 'adj_close', 'volume']

    # List of supported chart types for the data

    chart_data = {
        "labels": labels,
        "values": values,
        "columns": columns,
    }
    return chart_data


def clean_data(futures_data):
    # Drop the rows with missing or duplicate data
    futures_data = futures_data.dropna()
    # Drop the rows with duplicate dates but keep the row with volume > 0
    futures_data = futures_data.drop_duplicates(subset="date", keep="last")
    # Remove the rows with any column containing a value '-'
    futures_data = futures_data[~futures_data.applymap(lambda x: x == "-").any(1)]

    return futures_data

# Read the futures data from the Excel file and store it in the database
def read_data_from_excel():
    futures_data = pd.read_excel("futures_data.xlsx")
    futures_data.columns = [
        column.lower().strip().replace("*", "").replace("**", "").replace(" ", "_")
        for column in futures_data.columns
    ]
    futures_data = clean_data(futures_data)
    return futures_data