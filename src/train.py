"""Simulate a training process and save baseline statistics for monitoring."""
import numpy as np
import json
import os
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
os.makedirs("artifacts", exist_ok=True)

# simulate "training data"
np.random.seed(42)
feature_1 = np.random.normal(10, 2, 1000)
feature_2 = np.random.normal(50, 5, 1000)

baseline = {
    "feature_1": {
        "mean": float(np.mean(feature_1)),
        "std": float(np.std(feature_1))
    },
    "feature_2": {
        "mean": float(np.mean(feature_2)),
        "std": float(np.std(feature_2))
    }
}

logging.info(f"✅ Baseline stats calculated: {baseline}")
with open("artifacts/baseline_stats.json", "w") as f:
    json.dump(baseline, f, indent=2)

logging.info("✅ Baseline stats saved")