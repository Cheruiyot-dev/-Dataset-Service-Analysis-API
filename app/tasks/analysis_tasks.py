from config import celery_app
import pandas as pd
import asyncio
import time


@celery_app.task
def analyze_dataset(df):
    # Simulate a long running analysis task
    # asyncio.sleep(10)
    time.sleep(10)

    # perform data analysis
    summary = df.describe()

    #  store the results in the database

    return summary.to_dict()
