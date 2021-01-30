import sinhvien_db

class SinhVienView(object):

    #Hàm hiển thị tất cả dữ liệu về sinhvien
    def display_all_sinhvien(self, items):
        print("Dữ liệu về các sinhvien thu được như sau:")
        for item in items:
            print("ID: {}, họ và tên: {}".format(item.idSINHVIEN, item.hoten))
        print("-----Kết thúc hiển thị dữ liệu------")

    def ket_qua_insert(self, resultID):
        id = resultID[0]
        if id > 0:
                print("Insert thanh cong")
        else:
                print("Fail")

    def ket_qua_update(self):
        print("Update thanh cong")

    def ket_qua_delete(self):
        print("Delete thanh cong")