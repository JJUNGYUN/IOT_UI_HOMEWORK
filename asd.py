import pandas as pd

json = pd.read_json('project.json')
list = json.to_dict()

