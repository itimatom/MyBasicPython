tilecolor = {'red':100, 'gold':200, 'white':90, 'gray':30}


print('-----ราคากระเบื้อง-----')
for c,t in tilecolor.items():
    print( 'สี:  {}  ราคา:  {}  บาท' .format(c,t))


print('------Tiles calculation program------')
try:
    tiles = int(input('ต้องการปูกี่แผ่น: '))
    row = int(input('1 แถวปูกี่แผ่น: '))
    color = input('กระเบื้องสีอะไร? [red/gold/white/gray] : ')
except:
    print('กรอกเป็นตัวเลขเท่านั้น!')
    tiles = int(input('ต้องการปูกี่แผ่น: '))
    row = int(input('1 แถวปูกี่แผ่น: '))

print('------Calculate------')
total_row = tiles // row
remain_tiles = tiles % row

buy_more = row - remain_tiles

print(f'มีกระเบื้องทั้งหมด: {tiles} แผ่น')
print(f'1 แถวปูกระเบื้องได้: {row} แผ่น')
print('-----คำนวน------')
print(f'ต้องปูกระเบื้องทั้งหมด {total_row} แถว')
print(f'เหลือกระเบื้อง {remain_tiles} แผ่น')
print(f'ซื้อเพื่ม {buy_more} แผ่น')
print(f'ราคาซื้อเพิ่ม {buy_more * tilecolor[color]} บาท')

print('--------The End--------')