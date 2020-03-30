import math
import matplotlib.pyplot as plt
import numpy as np

# 資料輸入
CurrentPrice = float(input('Please enter the current price: '))
ParValue = float(input('Please enter par value: '))
Period = int(input('Please enter total period: '))

# 宣告 Forward Table
ForwardTable = [[0 for _ in range(Period+1)] for _ in range(Period+1)]

# 計算 Forward Rate
AllCurrentPrice = []
AllCurrentPrice.append(CurrentPrice)
for i in range (1, Period+1):
	print("Please enter the current price of Period", i, ":")
	AllCurrentPrice.append(int(input('-> ')))

for i in range(1, Period+2):
	for j in range(i, Period+2):
		if i == j or i == (Period+2) or j == (Period+2):
			continue
		NearSpotRate = math.pow(AllCurrentPrice[i-1]/ParValue, -1/i) - 1
		FarSpotRate = math.pow(AllCurrentPrice[j-1]/ParValue, -1/j) - 1
		ForwardRate = (math.pow((1 + FarSpotRate),j)/math.pow((1 + NearSpotRate),i))**(1/(j-i))-1
		print("The forward rate from", i-1, "th year to", j-1, "th year is", ForwardRate)
		# 將 Forward Rate 放入對應 Forward Table 中
		ForwardTable[i-1][j-1] = '%.3f' % ForwardRate

# Forward Table 處理
for i in range (Period+1):
	for j in range (Period+1):
		if i == j:
			ForwardTable[i-1][j-1] = 0
		elif ForwardTable[i-1][j-1] == 0:
			ForwardTable[i-1][j-1] = "-"

# 繪製 Forward Table
table = plt.table(cellText=ForwardTable, colWidths = [0.1]*6, rowLabels = np.arange(Period+1)
				 ,colLabels = np.arange(Period+1),loc='center')
plt.axis('off')
plt.show()