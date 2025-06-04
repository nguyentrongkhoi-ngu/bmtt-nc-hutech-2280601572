from QuanLySinhVien import QuanLySinhVien

qlsv = QuanLySinhVien()
while (1==1):
    print("\nCHUONG TRINH QUAN LY SINH VIEN")
    print("***********************************MENU***********************************")
    print("** 1. Them sinh vien.                                                   **")
    print("** 2. Cap nhat thong tin sinh vien boi ID.                              **")
    print("** 3. Xoa sinh vien boi ID.                                             **")
    print("** 4. Tim kiem sinh vien theo ten.                                      **")
    print("** 5. Sap xep danh sach sinh vien theo diem trung binh.                 **")
    print("** 6. Sap xep danh sach sinh vien theo ten chuyen nganh.                **")
    print("** 7. Hien thi danh sach sinh vien.                                     **")
    print("** 0. Thoat chuong trinh.                                               **")
    print("**************************************************************************")
    key = int(input("Nhap lua chon: "))
    if key == 1:
        print("1. Them sinh vien")
        qlsv.nhapSinhVien()
        print("Da them sinh vien thanh cong.")
    elif key == 2:
        if qlsv.soLuongSinhVien() > 0:
            print("2. Cap nhat thong tin sinh vien boi ID")
            ID = input("Nhap ID sinh vien: ")
            qlsv.updateSinhVien(ID)
            print("Da cap nhat thong tin sinh vien thanh cong.")
        else:
            print("\nSanh sach sinh vien trong!.")
    elif key == 3:
        if qlsv.soLuongSinhVien() > 0:
            print("3. Xoa sinh vien boi ID")
            ID = input("Nhap ID sinh vien: ")
            isDeleted = qlsv.deleteById(ID)
            if isDeleted:
                print("Da xoa sinh vien thanh cong.")
            else:
                print("Khong tim thay sinh vien co ID = {}." .format(ID))
        else:
            print("\nSanh sach sinh vien trong!.")
    elif key == 4:
        if qlsv.soLuongSinhVien() > 0:
            print("4. Tim kiem sinh vien theo ten")
            keyword = input("Nhap ten sinh vien: ")
            listSV = qlsv.findByName(keyword)
            if len(listSV) > 0:
                print("Danh sach sinh vien tim kiem duoc:")
                for sv in listSV:
                    print(sv)
            else:
                print("Khong tim thay sinh vien co ten = {}." .format(keyword))
        else:
            print("\nSanh sach sinh vien trong!.")
    elif key == 5:
        if qlsv.soLuongSinhVien() > 0:
            print("5. Sap xep danh sach sinh vien theo diem trung binh")
            qlsv.sortByDiemTB()
            qlsv.showSinhVien(qlsv.getListSinhVien())
            
        else:
            print("\nSanh sach sinh vien trong!.")
    elif key == 6:
        if qlsv.soLuongSinhVien() > 0:
            print("6. Sap xep danh sach sinh vien theo ten chuyen nganh")
            qlsv.sortByName()
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else:
            print("\nSanh sach sinh vien trong!.")
    elif key == 7:
        if qlsv.soLuongSinhVien() > 0:
            print("7. Hien thi danh sach sinh vien")
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else:
            print("\nSanh sach sinh vien trong!.")
    elif key == 0:
        print(" Thoat chuong trinh")
        break
    else: 
        print("\n Khong co lua chon nay trong menu")
        print("\nHay chon chuc nang trong hop menu" )
            
            