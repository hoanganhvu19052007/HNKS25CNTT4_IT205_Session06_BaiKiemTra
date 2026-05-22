box_count = 0

quantity_count = 0
while True :    
    total_quantity = int(input("Nhập vào tổng số lượng sản phẩm: "))

    if total_quantity < 0 :
        print("Số lượng không hợp lệ, bỏ qua thùng này!")
        continue
    elif total_quantity == 0 :
        print("Đã kiểm đếm xong")
        break
    else :
        quantity_count += total_quantity
        box_count += 1

print("Tổng số thùng hàng hợp lệ: ", box_count)
print("Tổng số lượng sản phẩm thu được: ", quantity_count)
