"""Check for data drift by comparing latest inference data to baseline stats."""
import json
import pandas as pd
import numpy as np
import glob
from scipy.stats import ks_2samp
import os
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
os.makedirs("artifacts", exist_ok=True)

    
# load baseline
with open("artifacts/baseline_stats.json") as f:
    baseline = json.load(f)

# get latest inference file
files = sorted(glob.glob("data/inference_*.csv"))
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

with open("artifacts/drift_report.json", "w") as f:
    json.dump(results, f, indent=2)

logging.info(f"✅ Drift check complete on {latest_file}")
logging.info(f"Drift results:\n{json.dumps(results, indent=2)}")
