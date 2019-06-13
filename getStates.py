import pandas as pd

df = pd.read_csv("preprocR1/arrDel_cancelled_diverted_onTime_Huston/FeaturesLabels201001.csv")

states = set()

for index, row in df.iterrows():
    states.add(row['DEST_STATE_ABR'])

print(states)
