product = {'ดินสอกดpentel':{'ราคา':50,'สี':'แดง'},
         'ยางลบ':{'ราคา':3,'สี':'เขียว'},
         'ดินสอสี':{'ราคา':100,'สี':'ส้ม'}}


while True:
    print('-----กรุณากรอกชื่อสินค้า-----')
    p = input('ชื่อสินค้า: ')
    q = int(input('จำนวน: '))
    print('------')
    if p in product:
        print(f'สินค้า: {p}  \nราคา: {product[p]['ราคา']} บาท  \nสี: {product[p]['สี']}')
        print(f'จำนวน: {q} ชิ้น \nรวมทั้งหมด: {product[p]['ราคา'] * q} บาท')
    else:
        print('ไม่มีสินค้าในระบบ')
    # ออกจากลูปโดยการกด control+c (ตอนที่ run แล้ว)