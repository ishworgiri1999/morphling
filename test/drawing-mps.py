import pandas as pd
import json
csv = pd.read_csv('rntt1mps-pytorch.csv')
quota=[]
sm=[]
key=[]
for index, row in csv.iterrows():
    limit_json = json.loads(row["limitations"])
    metrics_json = json.loads(row["other_metrics"])

    quota.append(float(limit_json['GPU_QUOTA']))
    sm.append(int(limit_json['GPU_SM']))
    key.append(float(row["value"]))


import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.interpolate import griddata
dfdata = pd.DataFrame({'x':quota, 'y':sm, 'z':key})
print(dfdata)
df = dfdata.groupby(['x', 'y']).agg({'z': 'max'}).reset_index()
df = df[df.z != -1]
#sns.scatterplot(x='x', y='y', hue='z', data=df)
#plt.savefig('scatterplot.png')

#sns.kdeplot(x='x', y='y', hue='z', data=df)
#plt.savefig('kdeplot.png')

plt.xlabel('Time Quota')
plt.ylabel('Throughput(req/s)')
palette = sns.color_palette("mako_r", 5)

g = sns.lineplot(x='x', y='z', hue='y', data=df, style="y",
     markers=True, dashes=False,
     palette=palette
     )

plt.legend(title="Partition(%)")
#plt.savefig('lineplot.png')
g.figure.savefig('rntt1mps.pdf')
