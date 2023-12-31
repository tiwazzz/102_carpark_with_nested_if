# Configuration
promotion = 20
discount = 0

# Input
numPlate = str(input("ป้อนเลขทะเบียนรถยนต์: "))
hours = int(input("ชั่วโมงการจอดรถยนต์: "))
receipt = float(input("กรุณาป้อนยอดใบเสร็จของคุณ (ค่าเริ่มต้น: 0): ")) 

# Checking
if receipt > 0:
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
elif receipt == "" or receipt == 0:
    receipt = 0
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