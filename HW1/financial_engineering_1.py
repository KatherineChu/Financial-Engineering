import math

print("本金平均攤還試算\n")

# 輸入
principal = float(input('本金(萬元)： '))
period = int(input('期數(年)   : '))
interest_rate = float(input('年利率(%)  : '))

# 轉換
principal *= 10000
original_principal = principal
interest_rate /= 100
total_month = period * 12
interest_rate_month = interest_rate / 12

# 計算每月應攤還本金（無條件進位法）
amortized_principal = math.ceil(principal / total_month)


original_amortized_principal = amortized_principal
current_interest = 0
accumulated_interest = 0

print("\n本金(元)      利息(元)        本金利息累計(元)")

# 計算每月應付利息、每月應付本息金額
for i in range (total_month):
	amortized_interest = round(principal * interest_rate_month)
	principal = principal - amortized_principal
	if i == total_month-1:
		amortized_principal = int(original_principal - (amortized_principal * (total_month - 1)))
	current_interest = amortized_principal + amortized_interest
	accumulated_interest += current_interest
	print('%-15s%-15s%-15s' %((amortized_principal, amortized_interest, accumulated_interest)))

# 輸出統整表格
print("\n")
print("本金             : ", int(original_principal))
print("期數(年)         : ", period)
print("年利率           : ", interest_rate*100, "%")
print("平均每月攤還本金 : ", original_amortized_principal)
print("平均每月攤還利息 :  請參考上表")
print("全部利息         : ", int(accumulated_interest - original_principal))