#Tạo 3 random số nguyên từ 100 tới 999 những số đó chia hết cho 5
import random
print("Generating 3 random integer number between 100 and 999 divisible by 5")
for num in range(3):
    print(random.randrange(100,999,5),end=", ")
