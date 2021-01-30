import sinhvien_model, sinhvien_view, sinhvien_controller

def start():
    model = sinhvien_model.SinhVienModel("localhost", "root", "123456789", "python_mvc")
    view = sinhvien_view.SinhVienView()
    controller = sinhvien_controller.SinhvienController(model, view)
    item = menu()
    while item in ["1", "2", "3", "4"]:
        if item == "1":
            controller.show_all_sinhvien()
        elif item == "2":
            hoten = input("Nhập họ tên: ")
            controller.them_sinhvien(hoten)
        elif item == "3":
            hoten = input("Nhập họ tên: ")
            id = input("Nhập Id:")
            controller.update_sinhvien(hoten,id)
        elif item == "4":
            id = input("Nhập Id: ")
            controller.delete_sinhvien(id)

        item = menu()
def menu():
    print("1: Hiển thị tất cả Sinh viên")
    print("2: Thêm mới Sinh viên")
    print("3: Cập nhật Sinh viên")
    print("4: Xóa Sinh viên")
    choice = input("Bạn hãy chọn các số từ 1 đến 4. Chọn sai thoát khỏi chương trình.")
    return choice

if __name__ == "__main__":
    start()
