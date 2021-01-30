import db_exceptions
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

    def thong_bao_loi(self, err_msg):
        print('-' * 30)
        print(err_msg)
        print('-' * 30)