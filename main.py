numPlate = str(input("ป้อนเลขทะเบียนรถยนต์: "))
hours = int(input("ชั่วโมงการจอดรถยนต์: "))
buyChoice = str(input("ได้ซื้อของหรือไม่ (หากใช่ให้พิมพ์ yes หรือ y หากไม่ได้ซื้อให้พิมพ์ no หรือ n): "))

# Configuration
promotion = 20
discount = 0
receipt = 0

if buyChoice == "yes" or buyChoice == "y":
    receipt = float(input("กรุณาป้อนยอดใบเสร็จของคุณ: "))
    if hours <= 3:
        discount = 0
        price = promotion
    elif hours <= 24:
        discount = receipt*0.05
        hoursMinus = hours-3
        price = promotion + (hoursMinus*20) - discount
    else:
        discount = receipt*0.05
        hoursMinus = hours-24
        price = (promotion + (21*20) + (hoursMinus*10)) - discount

elif buyChoice == "no" or buyChoice == "n":
    if hours <= 3:
        price = 20
    elif hours <= 24:
        hoursMinus = hours-3
        price = 20 + (hoursMinus*20)
    else:
        hoursMinus = hours-24
        price = promotion + (21*20) + (hoursMinus*10)

print(f"\n*********ใบเสร็จ*********")
print(f"ทะเบียนรถยนต์: {numPlate}\nส่วนลดที่ได้รับ: {discount} บาท\nค่าใช้จ่ายที่ต้องชำระ: {price} บาท")
print("************************")