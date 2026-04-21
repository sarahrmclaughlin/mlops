import duckdb
import requests


def run():
    url = "https://jsonplaceholder.typicode.com/posts"
    data = requests.get(url).json()

    con = duckdb.connect("data.db")
    con.register("data", data)
    con.execute("CREATE TABLE IF NOT EXISTS posts AS SELECT * FROM data")

    print("Loaded data into DuckDB")
