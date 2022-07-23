#Thay thế tất cả các giá trị cột chứa ?, n.a hoặc NaN.
import pandas as pd
df = pd.read_csv("Automobile_data.csv", na_values={
'price':["?","n.a"],
'stroke':["?","n.a"],
'horsepower':["?","n.a"],
'peak-rpm':["?","n.a"],
'average-mileage':["?","n.a"]})
print (df)
df.to_csv("Automobile_data.csv")