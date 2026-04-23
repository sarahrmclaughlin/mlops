### MLOps Monitoring

### Setup
uv venv
source .venv/bin/activate
uv sync

#### Step 1
- Create a training dataset and save as an artifact
``` bash uv run src/train.py 
```

#### Step 1
- Create a training dataset and save as an artifact
- This is saved as an artifact & we will use it as a baseline
``` bash uv run src/train.py 
```

#### Step 2
- Create a daily inference dataset as incoming batch
- Save it as a CSV in data
``` bash uv run src/generate_inference.py 
```

#### Step 3
- Create a daily drift check
- This is saved as an artifact for monitoring
``` bash uv run src/check_for_daily_drift.py
```
#### Step 4
- Simulate multiple days 
``` bash    
        for i in {1..5}
        do
        uv run src/generate_inference.py
        uv run src/check_for_daily_drift.py
        done
```
#### Step 4 Set-up DAG
- drift_dag.py script for monitoring
- Update docker-compose which will run airflow dag
- create airflow user id/pw, save in .env, CLI run once.
```bash docker exec airflow-webserver airflow users list
```








