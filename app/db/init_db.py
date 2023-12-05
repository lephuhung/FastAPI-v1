from app import crud, schemas, models
from app.schemas.user_donvi import UserDonviCreate
from app.core.sercurity import get_salt, get_password_hash
from app.constants.role import Role
from app.schemas.role import RoleCreate, RoleUpdate
from app.schemas.permission import PermissionCreate, PermissionUpdate
from app.core.config import settings
from sqlalchemy.orm import Session
from datetime import datetime

def init_db(db: Session)-> None:

    # Create donvi
    donvi_list= ["PA05", "PA02", "PA03", "PA04", "PA06", "PA09", "PA08", "PA01"]
    donvi= crud.crud_donvi.get_donvi_by_name(db=db, name="PA05")
    if donvi is None:
        for item in donvi_list:
            donviinDB= schemas.donvi.DonviCreate(name= item)
            crud.crud_donvi.create(db, obj_in=donviinDB)

    
    # Create superadmin PA05
    username_pao5=["Luongvinhlong", "Nguyendangphi", "Dangdonthang"]
    user = crud.crud_user.get_by_name(db=db, username=settings.FIRST_SUPER_ADMIN_ACCOUNT_NAME)
    salt= get_salt()
    if user is None:
        model_user_admin= schemas.user.UserCreate(
            username= settings.FIRST_SUPER_ADMIN_ACCOUNT_NAME,
            active= True,
            salt= salt,
            password= get_password_hash(f'lph77{salt}'),
        )
        crud.crud_user.create(db, obj_in=model_user_admin) 
        for item in username_pao5:
            user_pa05= schemas.user.UserCreate(
                username= item,
                active= True,
                salt= get_salt(),
                password= get_password_hash(f'123456{salt}')
            )
            crud.crud_user.create(db, obj_in= user_pa05)
    # Create user for Phong PA05 
    pa05 = crud.crud_donvi.get_donvi_by_name(name="PA05", db=db)
    user_admin = crud.crud_user.get_multi(db)
    for item in user_admin:
        user_item = UserDonviCreate(
            user_id= item.id,
            donvi_id=pa05.id
        )
        crud.CRUDUser_donvi.create(db, obj_in=user_item)

    # Create Role
    roles= ["superadmin", "admin", "Phong", "CAH", "DOI" ]
    for item in roles:
        role = RoleCreate(name=item)
        crud.CURD_Role.create(db, obj_in=role)
    # Create Permission
    permissions= ["user.read", "user.update", "user.delete", "user.create", "role.read", "role.update", "role.delete", "role.create", 
                    "ctnv.read", "ctnv.update", "ctnv.delete", "ctnv.create", "doituong.create", "doituong.update", "doituong.delete", "doituong.read"
                    "tags.read", "tags.update", "tags.delete", "tags.create", "tinhchat.create", "tinhchat.update", "tinhchat.delete", "tinhchat.create"
                    "trangthai.read", "trangthai.update", "trangthai.delete", "trangthai.create", "trichtin.create", "trichtin.update", "trichtin.delete", "trichtin.read",
                    "uid.read", "uid.delete", "uid.create", "uid.update"
                     ]
    for item in permissions:
        per = PermissionCreate(name=item)
        crud.CURD_Permission.create(db, obj_in=per)
    # Create permissions of role
    roleinDB= crud.CURD_Role.get_roleid_by_name(name="superadmin", db=db)