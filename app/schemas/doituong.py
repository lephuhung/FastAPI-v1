from pydantic import UUID4, BaseModel
from typing import Optional
from datetime import datetime, date


class doituong(BaseModel):

    client_name: Optional[str]
    CMND: Optional[str]
    CCCD: Optional[str]
    Ngaysinh: Optional[date]
    # True is Nam, False is Nu
    Gioitinh: bool
    Quequan: Optional[str]
    Thongtinbosung: Optional[str]
    SDT: Optional[str]
    KOL: bool
    Image: Optional[str]


class doituongcreate(doituong):
    ctnv_id: Optional[int]
    donvi_id: Optional[UUID4]

    def get_doituong_instance(self) -> doituong:
        return doituong(
            client_name= self.client_name,
            CMND = self.CMND,
            CCCD = self.CCCD,
            Ngaysinh= self.Ngaysinh,
            # True is Nam, False is Nu
            Gioitinh=self.Gioitinh,
            Quequan = self.Quequan,
            Thongtinbosung= self.Thongtinbosung,
            SDT= self.SDT,
            KOL = self.KOL,
            Image= self.Image
        )


class doituongupdate(doituongcreate):
    id: UUID4
    pass


class doituongoutDB(doituong):
    created_at: datetime
    updated_at: datetime
