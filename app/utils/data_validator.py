import pandas as pd

# file is CSV file path


def validate_csv(file):
    try:
        df = pd.read_csv(file)
        return True, df
    except Exception as e:
        return False, str(e)