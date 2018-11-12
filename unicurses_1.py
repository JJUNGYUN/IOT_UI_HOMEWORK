import json
import pandas as pd

Room = pd.read_json('project.json')

print(Room["Inner Room"].Value)
