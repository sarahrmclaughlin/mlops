"""Check for data drift by comparing latest inference data to baseline stats."""
import json
import sys
import pandas as pd
import numpy as np
import glob
from scipy.stats import ks_2samp
import os
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

date_str = sys.argv[1]

airflow_path = "/opt/airflow"
os.makedirs(f"{airflow_path}/artifacts", exist_ok=True)

    
# load baseline
with open(f"{airflow_path}/artifacts/baseline_stats.json") as f:
    baseline = json.load(f)

# get latest inference file
files = sorted(glob.glob(f"{airflow_path}/data/inference_*.csv"))
latest_file = files[-1]

df = pd.read_csv(latest_file)

results = {}

for col in df.columns:
    # simulate baseline distribution from stats
    baseline_sample = np.random.normal(
        baseline[col]["mean"],
        baseline[col]["std"],
        1000
    )

    stat, p_value = ks_2samp(baseline_sample, df[col])

    results[col] = {
        "p_value": float(p_value),
        "drift_detected": int(p_value < 0.05)
    }

with open(f"{airflow_path}/artifacts/drift_report.json", "w") as f:
    json.dump(results, f, indent=2)

logging.info(f"✅ Drift check complete on {latest_file}")
logging.info(f"Drift results:\n{json.dumps(results, indent=2)}")

logging.info("Working on drift history file...")
history_file = f"{airflow_path}/artifacts/drift_history.csv"

rows = []

for feature, vals in results.items():
    rows.append({
        "date": date_str,
        "feature": feature,
        "p_value": vals["p_value"],
        "drift_detected": vals["drift_detected"]
    })

if any(v["drift_detected"] for v in results.values()):
    logging.info("🚨 DRIFT DETECTED!")
else:
    logging.info("✅ No drift detected.")

df_new = pd.DataFrame(rows)

# append or create
if os.path.exists(history_file):
    logging.info(f"Existing history found. Appending new results to {history_file}")
    df_existing = pd.read_csv(history_file)
    df_final = pd.concat([df_existing, df_new], ignore_index=True)
else:
    logging.info(f"No existing history found. Creating new file {history_file}")
    df_final = df_new

df_final.to_csv(history_file, index=False)

logging.info(f"✅ Drift history updated: {history_file}")
