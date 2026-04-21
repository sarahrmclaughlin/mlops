# Run this query using DUCKDB
# ```bash uv run python src/pipelines/mrr_buggy.py```

import duckdb

mrr_query = """
SELECT
    customer_id,
    SUM(revenue) AS total_revenue,
    COUNT(subscription_id) AS subscriptions
FROM subscriptions
WHERE status = 'active'
GROUP BY customer
ORDER BY total_revenue DESC;
"""


def run():
    con = duckdb.connect()

    con.execute(
        """
    CREATE TABLE subscriptions AS
    SELECT 1 AS customer_id, 100 AS revenue, 'active' AS status
    , 10 AS subscription_id
    UNION ALL
    SELECT 1, 200, 'active', 11
    """
    )

    query = mrr_query
    print(con.execute(query).df())


if __name__ == "__main__":
    run()
