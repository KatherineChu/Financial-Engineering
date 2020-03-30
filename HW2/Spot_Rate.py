import math

ParValue = float(input('Bond Par Value: '))
CurrentPrice = float(input('Current Bond Price: '))
Duration = int(input('Duration of SpotRate: '))

# 計算 Spot Rate
SpotRate = math.pow(CurrentPrice/ParValue, -1/Duration) - 1
print("\nSpot Rate:  ", '%.3f' % (SpotRate*100), "%")