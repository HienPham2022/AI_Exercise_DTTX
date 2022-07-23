#dựa vào file csv tìm xe mắc nhất
import pandas as pd
df = pd.read_csv("Automobile_data.csv")
df = df [['company','price']][df.price==df['price'].max()]
print(df)