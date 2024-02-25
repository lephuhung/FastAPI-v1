from app import crud, schemas, models
from app.schemas.user_donvi import UserDonviCreate
from app.core.sercurity import get_salt, get_password_hash
from app.constants.role import Role
from app.schemas.role import RoleCreate
from app.schemas.role_has_permission import Role_has_PermissionCreate
from app.schemas.permission import PermissionCreate
from app.schemas.user_has_role import User_has_RoleCreate
from app.core.config import settings
from sqlalchemy.orm import Session
from datetime import datetime
from app.schemas.color import colorcreate
from app.schemas.moiquanhe import moiquanhecreate
from app.schemas.tinhchat import tinhchatcreate
from app.schemas.tags import tagscreate
from app.schemas.ctnv import ctnvcreate
from app.schemas.type import typecreate
from app.schemas.trangthai import trangthaicreate
from app.core.Utils import random_hex_color
def init_db(db: Session)-> None:

    # Create donvi
    donvi_list= ["PA05", "PA02", "PA03", "PA04", "PA06", "PA09", "PA08", "PA01"]
    donvi= crud.crud_donvi.get_donvi_by_name(db=db, name="PA05")
    if donvi is None:
        for item in donvi_list:
            donviinDB= schemas.donvi.DonviCreate(name= item)
            crud.crud_donvi.create(db, obj_in=donviinDB)

    donvi_PA05= crud.crud_donvi.get_donvi_by_name(db=db, name="PA05")
    # Create superadmin PA05
    username_pao5=["Luongvinhlong", "Nguyendangphi", "Dangdonthang"]
    user = crud.crud_user.get_by_name(db=db, username=settings.FIRST_SUPER_ADMIN_ACCOUNT_NAME)
    salt= get_salt()
    if user is None:
        model_user_admin= schemas.user.UserCreate(
            username= settings.FIRST_SUPER_ADMIN_ACCOUNT_NAME,
            active= True,
            salt= salt,
            donvi_id = donvi_PA05.id,
            password= get_password_hash(f'lph77{salt}'),
        )
        crud.crud_user.create(db, obj_in=model_user_admin) 
        for item in username_pao5:
            user_pa05= schemas.user.UserCreate(
                username= item,
                active= True,
                salt= get_salt(),
                password= get_password_hash(f'123456{salt}'),
                donvi_id=donvi_PA05.id
            )
            crud.crud_user.create(db, obj_in= user_pa05)

            
    # Create user for Phong PA05 

    user_admin = crud.crud_user.get_multi(db)
    for item in user_admin:
        user_item = UserDonviCreate(
            user_id= item.id,
            donvi_id=donvi_PA05.id
        )
        crud.crud_user_donvi.create(db, obj_in=user_item)

    # Create Role
    roles= ["superadmin", "admin", "Phong", "CAH", "DOI" ]
    roloutDB= crud.CURD_Role.get_roleid_by_name(name="superadmin", db=db)
    if roloutDB is None:
        for item in roles:
            role = RoleCreate(name=item)
            crud.CURD_Role.create(db, obj_in=role)


    # Create Permission
    permissions= ["user.all","user.read", "user.update", "user.delete", "user.create", "role.all","role.read", "role.update", "role.delete", "role.create", 
                    "ctnv.all","ctnv.read", "ctnv.update", "ctnv.delete", "ctnv.create", "doituong.all","doituong.create", "doituong.update", "doituong.delete", "doituong.read"
                    "tags.read", "tags.update", "tags.delete", "tags.create", "tags.all", "tinhchat.all","tinhchat.create", "tinhchat.update", "tinhchat.delete", "tinhchat.create"
                   "trangthai.all", "trangthai.read", "trangthai.update", "trangthai.delete", "trangthai.create", "trichtin.all", "trichtin.create", "trichtin.update", "trichtin.delete", "trichtin.read",
                   "uid.all", "uid.read", "uid.delete", "uid.create", "uid.update"
                     ]
    peroutDB= crud.CURD_Permission.get_permission_by_name(name="user.all", db=db)
    if peroutDB is None:
        for item in permissions:
            per = PermissionCreate(name=item)
            crud.CURD_Permission.create(db, obj_in=per)


    # Create permissions of role
    roleinDB= crud.CURD_Role.get_roleid_by_name(name="superadmin", db=db)
    if roleinDB is None:
        for i in range(1, 50):
            data = Role_has_PermissionCreate(
                role_id=roleinDB.id,
                permission_id= i
            )
            crud.CrudRole_has_Permission.create(db, obj_in= data)
    
    #create user has role superadmin

    user_superadmin = crud.crud_user.get_by_name(db=db, username=settings.FIRST_SUPER_ADMIN_ACCOUNT_NAME)
    roleoutDB= crud.CURD_Role.get_roleid_by_name(name="superadmin", db=db)
    user_has_role = crud.crud_user_has_role.get_user_has_role_by_userid(user_id=user_superadmin.id, db=db)
    if user_has_role is None:
        user_has_role_instance = User_has_RoleCreate(
            user_id=user_superadmin.id,
            role_id= roleoutDB.id
        )
        crud.crud_user_has_role.create(db, obj_in=user_has_role_instance)


    # create color table
    color_name_array=['red', 'blue', 'green', 'yellow']
    color_hex_array = ['#CB1D1D', '#3C14C9', '#37C914',  "#FFFA91"]
    color_db = crud.crud_color.get_color_by_name(db= db, name="red")
    if color_db is None:
        for i in range (0, len(color_name_array)):
            item = colorcreate(name=color_name_array[i], color=color_hex_array[i])
            crud.crud_color.create(db=db, obj_in= item)


    # create  tags, tinhchat, type, moiquanhe
    moiquanhe_array= ['quản trị viên', 'kiểm duyệt viên', 'nghi ngờ có liên quan']
    moiquanhe_db = crud.crud_moiquanhe.get_name_by_id(db= db, id=1)
    if moiquanhe_db is None:
        for item in moiquanhe_array:
            mqh = moiquanhecreate(name=item)
            crud.crud_moiquanhe.create(db= db, obj_in=mqh)

    #  tinhchat
    tinhchat_array = ['công giáo', 'đông thành viên', 'phản động', 'thông tin', 'tích cực', "tiêu cực"]
    tinhchat_db = crud.crud_tinhchat.find_tinhchat_byid(db=db, id=1)
    if tinhchat_db is None:
        for item in tinhchat_array:
            tchat = tinhchatcreate(name=item, color=random_hex_color())
            crud.crud_tinhchat.create(db=db, obj_in= tchat)

    #  tags
    tags_array = ['tài khoản mới tạo', 'KOL mới nổi', 'đăng tải hoạt động từ thiện']
    tags_db= crud.crud_tags.get_tags_by_id(db=db, id=1)
    if tags_db is None:
        for item in tags_array:
            tags_in_db = tagscreate(name=item, color=random_hex_color())
            crud.crud_tags.create(db=db, obj_in=tags_in_db)

    # CTNV
    ctnv_array = ['ĐTCB', 'Theo dõi', 'Gọi hỏi răn đe', 'QLNV']
    ctnv_db= crud.crud_ctnv.get_ctnv_by_id(db=db, id=1)
    if ctnv_db is None:
        for item in ctnv_array:
            ctnv_in_db = ctnvcreate(name=item)
            crud.crud_ctnv.create(db=db, obj_in=ctnv_in_db)

    # type
    type_array= ['Nhóm Facebook', "Facebook cá nhân", "Trang Facebook", "Tài khoản TikTok", "Tài khoản Zalo"]
    type_db= crud.crud_type.get_type_by_id(db=db, id=1)
    if type_db is None:
        for item in type_array:
            type_in_db= typecreate(name=item)
            crud.crud_type.create(db=db, obj_in=type_in_db)


    # trangthai
    trangthai_array =['Chỉ hiện thị bạn bè', 'Nhóm riêng tư', "Nhóm bí mật","Nhóm công khai", "Chỉ hiện thị với bạn bè"]
    trangthai_db = crud.crud_trangthai.get_trangthai_by_id(db=db, id=1)
    if trangthai_db is None:
        for item in trangthai_array:
            trangthai_in_db = trangthaicreate(name=item, color=random_hex_color())
            crud.crud_trangthai.create(db=db, obj_in=trangthai_in_db)
