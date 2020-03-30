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
