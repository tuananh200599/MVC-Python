import db_exceptions
import sinhvien_db

class SinhvienController(object):
    #Phương thức khởi tạo
    def __init__(self, model, view):
        self.model = model
        self.view = view

    #Phương thức hiển thị tất cả dữ liệu của bảng person
    def show_all_sinhvien(self):
        try:
            items = self.model.get_all_sinhvien()
            self.view.display_all_sinhvien(items)
        except db_exceptions.SelectError as err_msg:
            self.view.thong_bao_loi(err_msg)

    #Phương thức insert
    def them_sinhvien(self, hoten):
        try:
            resultID = self.model.them_sinhvien(hoten)
            self.view.ket_qua_insert(resultID)
        except db_exceptions.InsertError as err:
            self.view.thong_bao_loi(err)

    #Phương thức update


    #Phương thức delete