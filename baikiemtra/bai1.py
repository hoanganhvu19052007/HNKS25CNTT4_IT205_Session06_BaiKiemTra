price = int(input("Nhập vào số đơn giá của sản phẩm: "))
quantity = int(input("Nhập vào số lượng của sản phẩm: "))

total_price = price * quantity
total_sale = total_price
if total_price >= 1000000 :
    total_sale = total_sale * 0.1
    total_price -= total_sale
    print("Khách hàng được giảm giá 10%")
    print("Tổng số tiền phải thanh toán là: ", total_price)
else :
    print("Khách hàng không được giảm giá")
    print("Tổng số tiền phải thanh toán là: ", total_price)