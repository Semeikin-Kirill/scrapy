import pandas as pd
import json


def get_counts():
    with open('os.json', 'r') as f:
        data = json.load(f)
    counts = pd.Index(data)
    return counts
