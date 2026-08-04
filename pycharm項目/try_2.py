#BMI
user_weight = float(input("輸入您的體重 (kg):"))
user_height = float(input("請輸入您的身高 (m):"))
user_BMI = user_weight / user_height ** 2
print("您的BMI值為:" + str(int(user_BMI)))