"""Simulate daily inference process with drift for baseline comparison."""

import sys
import numpy as np
import pandas as pd
import os
from datetime import datetime
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

airflow_path = "/opt/airflow"
os.makedirs(f"{airflow_path}/data", exist_ok=True)

ds = sys.argv[1]  # <-- from Airflow

# simulate drift toggle
DRIFT = True

np.random.seed()

if DRIFT:
    f1 = np.random.normal(15, 3, 500)  # shifted mean
    f2 = np.random.normal(60, 7, 500)
else:
    f1 = np.random.normal(10, 2, 500)
    f2 = np.random.normal(50, 5, 500)

df = pd.DataFrame({
    "feature_1": f1,
    "feature_2": f2
})

logging.info(f"✅ Inference data generated with drift={DRIFT}")
logging.info(f"df.head():\n{df.head()}")
filename = f"{airflow_path}/data/inference_{ds}.csv"
df.to_csv(filename, index=False)

logging.info(f"✅ Inference data saved: {filename}")