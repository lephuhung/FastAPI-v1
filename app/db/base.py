# Import all the models, so that Base has them before being
# imported by Alembic
from app.db.base_class import Base  # noqa
# from app.models.account import Account  # noqa
# from app.models.role import Role  # noqa
from app.models.user import User  # noqa
from app.models.unit import Unit  # noqa
from app.models.user_unit import UserUnit  # noqa
from app.models.role import Role  # noqa
from app.models.permission import Permission  # noqa
from app.models.user_role import UserRole  # noqa
from app.models.role_permission import RolePermission  # noqa
from app.models.user_permission import UserPermission  # noqa
from app.models.individual import Individual  # noqa
from app.models.social_account import SocialAccount  # noqa
from app.models.individual_social_account import IndividualSocialAccount  # noqa
from app.models.individual_unit import IndividualUnit  # noqa
from app.models.unit_group import UnitGroup  # noqa
from app.models.task import Task  # noqa
from app.models.status import Status  # noqa
from app.models.characteristic import Characteristic  # noqa
from app.models.tag import Tag  # noqa
from app.models.individual_tag import IndividualTag  # noqa
from app.models.account_type import AccountType  # noqa
from app.models.relationship import Relationship  # noqa
from app.models.report import Report  # noqa
from app.models.administrator import Administrator  # noqa
from app.models.group_status import GroupStatus  # noqa
from app.models.group_characteristic import GroupCharacteristic  # noqa
from app.models.social_account_link import SocialAccountLink  # noqa
