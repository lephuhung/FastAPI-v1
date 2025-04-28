from app import crud, schemas, models
from app.core.security import get_salt, get_password_hash
from app.core.config import settings
from sqlalchemy.orm import Session
from datetime import datetime


def init_db(db: Session) -> None:
    # Create units
    unit_list = [
        "PA01", "PA02", "PA03", "PA04", "PA05", "PA06", "PA08", "PA09",
        "PC01", "PC02", "PC03", "PC04", "PC06", "PC07", "PC08", "PC09",
        "PC10", "PC11", "PK02", "Thành phố Hà Tĩnh", "Thị xã Hồng Lĩnh",
        "Thị xã Kỳ Anh", "Huyện Nghi Xuân", "Huyện Đức Thọ", "Huyện Hương Sơn",
        "Huyện Hương Khê", "Huyện Vũ Quang", "Huyện Can Lộc", "Huyện Thạch Hà",
        "Huyện Lộc Hà", "Huyện Cẩm Xuyên", "Huyện Kỳ Anh", "Đơn vị khác"
    ]
    
    unit_pa05 = crud.unit.get_by_name(db=db, name="PA05")
    if unit_pa05 is None:
        for item in unit_list:
            unit_in_db = schemas.unit.UnitCreate(name=item)
            crud.unit.create(db, obj_in=unit_in_db)

    unit_pa05 = crud.unit.get_by_name(db=db, name="PA05")
    
    # Create superadmin PA05
    username_pa05 = ["Luongvinhlong", "Nguyendangphi", "Dangdonthang", "Tranquangphat", "Levantu"]
    user = crud.user.get_by_username(db=db, username=settings.FIRST_SUPER_ADMIN_ACCOUNT_NAME)
    salt = get_salt()
    
    if user is None:
        model_user_admin = schemas.user.UserCreate(
            username=settings.FIRST_SUPER_ADMIN_ACCOUNT_NAME,
            is_active=True,
            salt=salt,
            unit_id=unit_pa05.id,
            password=get_password_hash(f'lph77{salt}'),
        )
        crud.user.create(db, obj_in=model_user_admin)
        
        for item in username_pa05:
            user_pa05 = schemas.user.UserCreate(
                username=item,
                is_active=True,
                salt=get_salt(),
                password=get_password_hash(f'123456{salt}'),
                unit_id=unit_pa05.id
            )
            crud.user.create(db, obj_in=user_pa05)

    # Create roles
    roles = ["superadmin", "admin", "Phong", "CAH", "DOI"]
    role_superadmin = crud.role.get_by_name(db=db, name="superadmin")
    
    if role_superadmin is None:
        for item in roles:
            role = schemas.role.RoleCreate(name=item)
            crud.role.create(db, obj_in=role)

    # Create permissions
    permissions = [
        "user.all", "user.read", "user.update", "user.delete", "user.create",
        "role.all", "role.read", "role.update", "role.delete", "role.create",
        "task.all", "task.read", "task.update", "task.delete", "task.create",
        "individual.all", "individual.create", "individual.update", "individual.delete", "individual.read",
        "tags.read", "tags.update", "tags.delete", "tags.create", "tags.all",
        "characteristic.all", "characteristic.create", "characteristic.update", "characteristic.delete", "characteristic.create",
        "status.all", "status.read", "status.update", "status.delete", "status.create",
        "trichtin.all", "trichtin.create", "trichtin.update", "trichtin.delete", "trichtin.read",
        "uid.all", "uid.read", "uid.delete", "uid.create", "uid.update",
        "unit.all", "unit.read", "unit.create", "unit.update", "unit.delete"
    ]
    
    permission_user_all = crud.permission.get_by_name(db=db, name="user.all")
    if permission_user_all is None:
        for item in permissions:
            per = schemas.permission.PermissionCreate(name=item)
            crud.permission.create(db, obj_in=per)

    # Create role permissions for superadmin
    role_superadmin = crud.role.get_by_name(db=db, name="superadmin")
    if role_superadmin:
        for i in range(1, len(permissions) + 1):
            data = schemas.role_permission.RolePermissionCreate(
                role_id=role_superadmin.id,
                permission_id=i
            )
            crud.role_permission.create(db, obj_in=data)

    # Create user role for superadmin
    user_superadmin = crud.user.get_by_username(db=db, username=settings.FIRST_SUPER_ADMIN_ACCOUNT_NAME)
    role_superadmin = crud.role.get_by_name(db=db, name="superadmin")
    
    if user_superadmin and role_superadmin:
        user_role = crud.user_role.get_by_user_and_role(
            db=db, user_id=user_superadmin.id, role_id=role_superadmin.id
        )
        if user_role is None:
            user_role_instance = schemas.user_role.UserRoleCreate(
                user_id=user_superadmin.id,
                role_id=role_superadmin.id
            )
            crud.user_role.create(db, obj_in=user_role_instance)
