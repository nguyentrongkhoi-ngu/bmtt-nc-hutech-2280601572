from SinhVien import SinhVien

class QuanLySinhVien:
    listSinhVien = []
    def generateId(self):
        maxId = 1
        if(self.soLuongSinhVien() > 0):
            maxId = self.listSinhVien[0]._id
            for i in range(1, self.soLuongSinhVien()):
                if(maxId < self.listSinhVien[i]._id):
                    maxId = self.listSinhVien[i]._id
        return maxId 
    
    def soLuongSinhVien(self):
        return self.listSinhVien.__len__()
    
    def nhapSinhVien(self):
        svId = self.generateId()
        name = input("Nhập tên sinh viên: ")
        sex = input ("Nhập giới tính sinh viên: ")
        major = input("Nhập chuyên ngành sinh viên: ")
        diemTB = float(input("Nhập điểm trung bình sinh viên: "))
        sv = SinhVien(svId, name, sex, major, diemTB)
        self.listSinhVien.append(sv)
        self.xepLoaiHocLuc(sv)
    def updateSinhVien(self, ID):
        sv:SinhVien = self.findByID(ID)
        if(sv != None):
            name = input("Nhập tên sinh viên: ")
            sex = input ("Nhập giới tính sinh viên: ")
            major = input("Nhập chuyên ngành sinh viên: ")
            diemTB = float(input("Nhập điểm trung bình sinh viên: "))
            sv._name = name
            sv._sex = sex
            sv._major = major
            sv._diemTB = diemTB
            self.xepLoaiHocLuc(sv)
        else:
                print("Sinh viên có ID= {} không tồn tại." .format(ID))
    def sortByID(self):
        self.listSinhVien.sort(key=lambda x: x._id, reverse=False)
    def sortByName(self):
        self.listSinhVien.sort(key=lambda x: x._name, reverse=False)
    def sortByDiemTB(self):
        self.listSinhVien.sort(key=lambda x: x._diemTB, reverse=False)
                
    def findByID(self, ID):
        searcgResult = None
        if(self.soLuongSinhVien() > 0):
            for sv in self.listSInhVIen:
                if(sv._id == ID):
                    searcgResult = sv
        return searcgResult
    def findByName(self, keyword):
        listSV = []
        if(self.soLuongSinhVien() > 0):
            for sv in self.listSinhVien:
                if(keyword.upper() in sv._name.upper()):
                    listSV.append(sv)
        return listSV
    def deleteById(self, ID):
        isDeleted = False
        sv = self.findByID(ID)
        if(sv != None):
            self.listSinhVien.remove(sv)
            isDeleted = True
        return isDeleted 
       
    def xepLoaiHocLuc(self, sv):
        if(sv._diemTB >= 8):
            sv._hocluc = "Giỏi"
        elif(sv._diemTB >= 6.5):
            sv._hocluc = "Khá"
        elif(sv._diemTB >= 5):
            sv._hocluc = "Trung bình"
        else:
            sv._hocluc = "Yếu"
    def showSinhVien(self, listSV):
        print(("{:<8} {:<18} {:<8} {:<18} {:<8} {:<8}").format("ID", "Tên", "Giới tính", "Chuyên ngành", "Điểm TB", "Học lực"))
        if listSV.__len__() > 0:
            for sv in listSV:
                print(("{:<8} {:<18} {:<8} {:<18} {:<8} {:<8}").format(sv._id, sv._name, sv._sex, sv._major, sv._diemTB, sv._hocluc))
        print ("\n")
    def getListSinhVien(self):
        return self.listSinhVien
