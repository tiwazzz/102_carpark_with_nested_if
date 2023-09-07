numPlate = str(input("ป้อนเลขทะเบียนรถยนต์: "))
hour = int(input("ชั่วโมงการจอดรถยนต์: "))
buyChoice = str(input("ได้ซื้อของหรือไม่ (หากใช่ให้พิมพ์ yes หรือ y หากไม่ได้ซื้อให้พิมพ์ no หรือ n): "))

# Configuration
promotion = 20
discount = 0
receipt = 0

if buyChoice == "yes" or buyChoice == "y":
    receipt = float(input("กรุณาป้อนยอดใบเสร็จของคุณ: "))
    if hour <= 3:
        discount = 0
        price = promotion
    elif hour <= 24:
        discount = receipt*0.05
        hourMinus = hour-3
        price = promotion + (hourMinus*20) - discount
    else:
        discount = receipt*0.05
        hourMinus = hour-24
        price = (promotion + (21*20) + (hourMinus*10)) - discount

elif buyChoice == "no" or buyChoice == "n":
    if hour <= 3:
        price = 20
    elif hour <= 24:
        hourMinus = hour-3
        price = 20 + (hourMinus*20)
    else:
        hourMinus = hour-24
        price = promotion + (21*20) + (hourMinus*10)

print(f"\n*********ใบเสร็จ*********")
print(f"ทะเบียนรถยนต์: {numPlate}\nส่วนลดที่ได้รับ: {discount} บาท\nค่าใช้จ่ายที่ต้องชำระ: {price} บาท")
print("************************")