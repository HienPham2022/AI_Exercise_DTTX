#Đọc dữ liệu bán hàng kem đánh răng của mỗi tháng và hiển thị dữ liệu đó bằng cách sử dụng biểu đồ phân tán
import pandas as pd
import matplotlib.pyplot as plt  

df = pd.read_csv("company_sales_data.csv")
monthList  = df ['month_number'].tolist()
toothPasteSalesData = df ['toothpaste'].tolist()
plt.scatter(monthList, toothPasteSalesData, label = 'Tooth paste Sales data')
plt.xlabel('Month Number')
plt.ylabel('Number of units Sold')
plt.legend(loc='upper left')
plt.title(' Tooth paste Sales data')
plt.xticks(monthList)
plt.grid(True, linewidth= 1, linestyle="--")
plt.show()