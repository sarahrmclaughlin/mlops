import pandas as pd
import requests


def run():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    data = response.json()

    df = pd.DataFrame(data)

    # BUG 1: wrong column name
    # df["created_at"] = pd.to_datetime(df["createdAt"])

    # BUG 2: filtering wrong type
    # df = df[df["userId"] == "1"]

    print(df.head())


if __name__ == "__main__":
    run()
