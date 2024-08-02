from typing import Any, Optional
from app.crud.base import CRUDBase
from app.models.user_donvi import user_donvi
from app.models.user import User
from app.models.donvi import Donvi
from sqlalchemy.orm import Session, joinedload, aliased
from sqlalchemy import func
from app.schemas.user_donvi import UserDonviCreate, UserDonviUpdate
from pydantic import UUID4
from app import crud
import json
class crud_user_donvi(CRUDBase[user_donvi, UserDonviCreate, UserDonviUpdate]):
    # View detail user in Donvi
    def get_user_by_uid_donvi(self, uid_donvi: UUID4 ,db: Session)->Optional[list[User]]:
        user_alias = aliased(User)
        donvi_alias = aliased(Donvi)
        users_with_donvi_names = (db.query(user_alias.id.label('user_uid'),user_alias.username.label('user_name'), donvi_alias.name.label('donvi_name'))
                .join(user_donvi, user_alias.id == user_donvi.user_id)
                .join(donvi_alias, donvi_alias.id == user_donvi.donvi_id)
                .filter(donvi_alias.id == uid_donvi)
                .all())
        result_dict_list = [{'user_uid': user_uid ,'username': user_name, 'donvi_name': donvi_name} for user_uid,user_name, donvi_name in users_with_donvi_names]
        return result_dict_list

    # Get donvi of user ID
    def get_donvi_by_user_id(self, user_id: UUID4, db: Session):
        donvi_alias = aliased(Donvi)
        user_data = db.query(donvi_alias.id.label('id'), donvi_alias.name.label('name')).join(user_donvi, user_donvi.donvi_id==donvi_alias.id).filter(user_donvi.user_id == user_id).first()
        result_dict_list = [{'donvi_id': user_data.id, 'donvi_name': user_data.name}]
        return result_dict_list
    # Count user on donvi ID
    def count_users_in_donvi(self, donvi_id: UUID4, db: Session):
        user_count_by_donvi = db.query(Donvi.name, func.count(user_donvi.user_id).label('user_count')).join(user_donvi).group_by(Donvi.name).filter(user_donvi.donvi_id==donvi_id).all()
        result_dict_list = [{'Donvi': name ,'Number_account': user_count} for name,user_count in user_count_by_donvi]
        return result_dict_list
    #  Count all users in all donvi
    def count_all_user_in_donvi(self,db:Session):
        user_count_by_donvi = db.query(Donvi.name, func.count(user_donvi.user_id).label('user_count')).join(user_donvi).group_by(Donvi.name).all()
        result_dict_list = [{'Donvi': name ,'Number_User': user_count} for name,user_count in user_count_by_donvi]
        return result_dict_list
    #Create test
    def create_user(self, data: UserDonviCreate, db: Session):
        return crud.crud_user_donvi.create(db, obj_in= data)
    
crud_user_donvi = crud_user_donvi(user_donvi) 
