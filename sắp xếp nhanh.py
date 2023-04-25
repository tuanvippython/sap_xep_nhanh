# Tạo hàm sắp xếp nhanh 
def quick_sort(x):
    # Nếu danh sách x có số phần tử bé hơn hoặc bằng 1 thì sẽ trả về danh sách x vì nó đã được sắp xếp
    if len(x) <= 1:
        return x
    # Ngược lại ta sẽ chọn phần tử chốt là phần tử đầu tiên của danh sách và chia danh sách thành 2 dãy con
    else:
        phan_tu_chot = x[0]
        # Tạo dãy số bên trái
        day_so_trai = []
        # tạo dãy số bên phải
        day_so_phai = []
        # Sử dụng vòng lặp để duyệt từ phần tử thứ 2 đến hết danh sách vì chúng ta đã chọn phần tử đầu tiên làm chốt
        for i in x[1:]:
            # Nếu i bé hơn phần tử chốt thì sẽ thêm vào dãy số bên trái
            if i < x[0]:
                day_so_trai.append(i)
            # Nếu i lớn hơn phần tử chốt thì sẽ thêm vào dãy số bên phải
            else:
                day_so_phai.append(i)
        # Gọi đệ quy để sắp xếp dãy số bên trái và bên phải
        return quick_sort(day_so_trai) + [phan_tu_chot] + quick_sort(day_so_phai)
    
x = [3, 7, 2, 8, 1, 9, 4, 6, 5]
print(quick_sort(x))


        
