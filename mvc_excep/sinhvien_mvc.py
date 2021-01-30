import db_exceptions
import sinhvien_view, sinhvien_controller
from MVC_Python import sinhvien_model


def start():
    try:
        # Khởi tạo đối tượng model
        model = sinhvien_model.SinhVienModel("localhost", "root", "123456789", "python_mvc")
        #model = sinhvien_model.SinhVienModel("localhost", "root", ""123456789", "python_mvc")
        # Khởi tạo đối tượng view
        view = sinhvien_view.SinhVienView()
        # Khởi tạo controller
        controller = sinhvien_controller.SinhvienController(model, view)

        # Hiển thị tất cả dữ liệu của bảng sinhvien
        #controller.show_all_sinhvien1()
        controller.them_sinhvien("Tuan Anh")
        # Hiển thị tất cả dữ liệu của bảng sinh

        #controller.show_all_sinhvien()
    except db_exceptions.DatabaseConnection as err:
        print(err)

if __name__ == "__main__":
    start()
