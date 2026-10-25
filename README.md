# Project Structure

## Main file
The main file serves as the entry point of the application. 
Instead of reloading the main file after each change, it automatically uploads its own copy into the `datasets` folder under the name `processing.py` after the processing is completed.

## Dataset directory
The `datasets` directory is automatically created after the main process finishes.
This directory stores information about the dataset and its processing.

## Data input
To begin processing a dataset, place it in the `data/input` directory.
The datasets to be processed must be stored here.

## Processing class (`ProjectParsetron`)
Processing parameters are set within a class inherited from `Parsetron`. Example:

```python
class ProjectParsetron(Parsetron):
    test_mode: bool = True
    dataset_code_name: str = 'index_0001'
```

The `dataset_code_name` represents the code name of the dataset index (e.g., `'index_0001'`), which uniquely identifies the dataset for processing.

## How to run locally?

```
uv sync --group dev
uv run python3 main.py
```

## How to run in cluster-mode\Add machine to existing cluster?
1.Install Parsetron fro latest local pip package (if you didn't have it on machine yet)
To build local pip package do following:
- Change version in setup.py
- Run locally: 
``` pip install build
    python -m build
```
This creates a dist/ directory with .tar.gz and .whl files.
- Copy .whl file to machine which you want to add to cluster and run:
```pip install .parsetron-0.2.3-py3-none-any.whl```

2.Set environment variables: 
- MINIO_HOSTS 
- MINIO_ACCESS_KEY 
- MINIO_SECRET_KEY 
- MINIO_MEDIA_FILES_BUCKET_NAME
- GEO_API_HOSTS
- ANALYZER_API_HOSTS
- SPARK_MASTER_ENDPOINT
- SPARK_S3A_ENDPOINT
- SPARK_S3A_ACCESS_KEY
- SPARK_S3A_SECRET_KEY

3.At machine, where you want to run master node, execute:

```$SPARK_HOME/sbin/start-master.sh```

4.At machine where you want to run worker nodes, execute:

```$SPARK_HOME/sbin/start-slave.sh {IP ADDRESS OF MACHINE WITH MASTER NODE}```

5.To be able to set Instances and Cores number for worker nodes set following variables in spark-env:

```nano $SPARK_HONE/conf/spark-env.sh```

- SPARK_WORKER_INSTANCES
- SPARK_WORKER_CORES

6.You can check Worker status at port 8081, master status at port 8080 and check SparkUI of cluster at port 4040 on master node
