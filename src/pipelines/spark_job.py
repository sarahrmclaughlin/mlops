from pyspark.sql import SparkSession


# ```bash uv run python src/pipelines/spark_job.py```
# TODO: FIX PYSPARK CLI JAVA ERROR
def run():
    spark = SparkSession.builder.appName("spark_sql_example").getOrCreate()

    data = [(1, "100"), (2, "200"), (3, None)]
    df = spark.createDataFrame(data, ["id", "revenue"])

    # BUG 1: treating string as numeric
    # df = df.withColumn("revenue", df["revenue"] * 2)

    # # BUG 2: null handling
    # df = df.filter(df["revenue"] > 100)

    df.show()

    spark.stop()


if __name__ == "__main__":
    run()
