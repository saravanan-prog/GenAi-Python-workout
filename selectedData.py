import pandas as pd


df = pd.read_excel(r"./file/demo.xlsx")

filterData = df[["candidateName","Result"]]

print(filterData)