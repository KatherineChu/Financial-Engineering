import math
import matplotlib.pyplot as plt
import numpy as np

# 計算 Present Value
def PV(ParValue, Coupon, Period, CouponRate):
	PresentValue = 0
	for i in range (1, Period + 1) :
		PresentValue += Coupon / math.pow((1 + CouponRate), i)
	PresentValue += ParValue / math.pow((1 + CouponRate), Period)
	return PresentValue

# 資料輸入
CurrentPrice = float(input('Current Bond Price: '))
ParValue = float(input('Bond Par Value: '))
CouponRate = float(input('Bond Coupon Rate (% p.a.): '))
YearsToMaturity = int(input('Years to Maturity: '))
Payment = int(input('Payment (Enter 1 for Annually, 2 for Semi-annually, 4 for quarterly) : '))

# 資料型別轉換
Period = YearsToMaturity * Payment
CouponRate = CouponRate / 100
Coupon = ParValue * CouponRate

# 資料宣告
ytm = CouponRate
flag = True

# 利用反覆試驗來趨近 ytm 的值
while flag:
	if CurrentPrice < ParValue:
		ytm += 0.00001
	else:
		ytm -= 0.00001

	PresentValue = PV(ParValue, Coupon/Payment, Period, ytm/Payment)

	if CurrentPrice < ParValue:
		flag = PresentValue > CurrentPrice
	else:
		flag = PresentValue < CurrentPrice
print("\nYield to Maturity:  ", '%.3f' % ((ytm/Payment)*100), "%")

# 計算 Spot Rate
SpotRate = math.pow(CurrentPrice/ParValue, -1/Period) - 1
print("\nSpot Rate:  ", '%.3f' % (SpotRate*100), "%")

# 宣告 Forward Table
ForwardTable = [[0 for _ in range(Period+1)] for _ in range(Period+1)]

# 計算 Forward Rate
AllCurrentPrice = []
AllCurrentPrice.append(CurrentPrice)
for i in range (1, Period+1):
	print("Please enter the current price of year", i, ":")
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