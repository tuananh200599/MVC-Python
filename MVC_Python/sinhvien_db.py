import sqlalchemy as db

#Xây dựng hàm thiết lập kết nối đến csdl
#Trả về đối tượng là connection, metadata và engine
def ket_noi_den_csdl(database_server, username, password, database):
    connection_str = "mysql://{}:{}@{}/{}".format(username, password, database_server, database)
    engine = db.create_engine(connection_str)
    connection = engine.connect()
    metadata = db.MetaData()
    return connection, metadata, engine

#Xây dựng hàm lấy tất cả dữ liệu của bảng sinhvien
def lay_tat_ca_du_lieu_bang_sinhvien(connection, metadata, engine):
    # Lấy đối tượng SinhVien trong csdl
    sinhvien = db.Table('sinhvien', metadata, autoload=True, autoload_with=engine)

    # Lấy tất cả dữ liệu của bảng sinhvien - tương đương câu lênh SELECT * FROM sinhvien
    query = db.select([sinhvien])

    ResultProxy = connection.execute(query)
    ResultSet = ResultProxy.fetchall()

    return ResultSet

#Hàm insert
def them_sinhvien(connection, metadata, engine,
                hoten):
    # Lấy đối tượng person từ bảng person trong csdl
    sinhvien = db.Table('sinhvien', metadata, autoload=True, autoload_with=engine)
    # Chèn 1 dòng vào bảng sinhvien
    query = db.insert(sinhvien).values(hoten=hoten)
    ResultProxy = connection.execute(query)
    # Trả về giá trị id vừa được sinh
    return ResultProxy.inserted_primary_key

#Hàm update
def update_sv(connection,metadata, engine,hoten,idSINHVIEN):
    sinhvien = db.Table('sinhvien', metadata, autoload=True, autoload_with=engine)
    query_insert = db.update(sinhvien).values(hoten=hoten).where(sinhvien.columns.idSINHVIEN == idSINHVIEN)
    ResultProxy = connection.execute(query_insert)
    return ResultProxy

#Hàm delete
def delete_sv(connection,metadata, engine,idSINHVIEN):
    sinhvien = db.Table('sinhvien', metadata, autoload=True, autoload_with=engine)
    query_delete = db.delete(sinhvien).where(sinhvien.columns.idSINHVIEN == idSINHVIEN)
    ResultProxy = connection.execute(query_delete)
    return ResultProxy