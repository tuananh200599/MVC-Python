import sqlalchemy as db
import db_exceptions

#Xây dựng hàm thiết lập kết nối đến csdl
#Trả về đối tượng là connection, metadata và engine
def ket_noi_den_csdl(database_server, username, password, database):
    try:
        connection_str = "mysql://{}:{}@{}/{}".format(username, password, database_server, database)
        engine = db.create_engine(connection_str)
        connection = engine.connect()
        metadata = db.MetaData()
        return connection, metadata, engine
    except:
        raise db_exceptions.DatabaseConnection("Thông tin kết nối username = {}, pass = {}, "
                                               "database = {} hoặc server ={} không đúng".format(username,
                                                                                                 password,
                                                                                                 database,
                                                                                                 database_server))


#Xây dựng hàm lấy tất cả dữ liệu của bảng sinhvien
def lay_tat_ca_du_lieu_bang_sinhvien(connection, metadata, engine):
    # Lấy đối tượng SinhVien trong csdl
    try:
        sinhvien = db.Table('sinhvien', metadata, autoload=True, autoload_with=engine)

    # Lấy tất cả dữ liệu của bảng sinhvien - tương đương câu lênh SELECT * FROM sinhvien
        query = db.select([sinhvien])

        ResultProxy = connection.execute(query)
        ResultSet = ResultProxy.fetchall()
        return ResultSet
    except:
        raise db_exceptions.SelectError("Xảy ra lỗi trong quá trình thực hiện lấy dữ liệu")

    #Hàm insert
def them_sinhvien(connection, metadata, engine,
                hoten):
    try:
        # Lấy đối tượng person từ bảng person trong csdl
        sinhvien = db.Table('sinhvienx', metadata, autoload=True, autoload_with=engine)
        # Chèn 1 dòng vào bảng sinhvien
        query = db.insert(sinhvien).values(hoten=hoten)
        ResultProxy = connection.execute(query)
        # Trả về giá trị id vừa được sinh
        return ResultProxy.inserted_primary_key
    except:
        raise db_exceptions.InsertError("Xảy ra lỗi  trong quá trình Insert")

#Hàm update


#Hàm delete

