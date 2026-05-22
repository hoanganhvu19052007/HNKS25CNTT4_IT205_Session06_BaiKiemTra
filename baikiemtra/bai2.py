password_error = 0


while password_error != 4 :
    password = input("Nhập mật khẩu để đăng nhập: ")
    if password == "123456" :
        print("Đăng nhập thành công!")
        break
    else :
        print("Mật khẩu sai, vui lòng nhập lại!")
        password_error += 1
        continue
if password_error == 4 :
    print("Tài khoản đã bị khóa!")