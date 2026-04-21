import duckdb


def run():
    print(duckdb.query("SELECT 1 AS id").df())
