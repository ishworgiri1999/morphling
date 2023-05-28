import mysql.connector
import pandas as pd

cnx = mysql.connector.connect(
  host="10.244.0.89",
  user="root",
  password="morphling",
  database="morphling"
)

df = pd.read_sql("SELECT * FROM trial_result_info WHERE trial_name like 'rnnt%'", cnx)
print(df)
df.to_csv("rnnt-pytorch.csv", index=False)
