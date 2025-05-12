

export interface ReportDataSchema {
  id: number;
  social_account_uid: string | null;
  content_note: string | null;
  comment: string | null;
  action: string | null;
  related_social_account_uid: string | null;
  user_id: string | null; 
  created_at: string; // Kiểu string cho ISO date
  updated_at: string; // Kiểu string cho ISO date
}


export interface uid {
    uid: string,
    name: string,
    SDT?: string,
    trangthai_id: number,
    type_id: number,
    ghichu: string,
    reaction: number,
    Vaiao: Boolean,

}
export interface uidsearch {
    _index: string,
    _id: string,
    _score: string,
    _source: uid,
    sort: number[]
}
export interface trichtin {
    id: number,
    uid : string
    ghichu_noidung : string
    nhanxet : string
    xuly: string
    uid_vaiao : string
    hoinhom_name?: string
    user: string
    created_at : string
    updated_at : string
}
export interface individual{
    id: string,
    client_name: string,
    CMND: string,
    CCCD: string,
    Image:string,
    Ngaysinh: string,
    Gioitinh: boolean,
    Quequan: string,
    Thongtinbosung: string,
    SDT: string,
    KOL: boolean,
}
export interface individualsearch {
    _index: string,
    _id: string,
    _score: string,
    _source: individual,
    sort: number[]
}
export interface trichtinsearch {
    _index: string,
    _id: string,
    _score: string,
    _source: trichtin,
    sort: number[]
}