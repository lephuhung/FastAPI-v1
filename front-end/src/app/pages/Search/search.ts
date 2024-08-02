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
export interface doituong{
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
export interface doituongsearch {
    _index: string,
    _id: string,
    _score: string,
    _source: doituong,
    sort: number[]
}
export interface trichtinsearch {
    _index: string,
    _id: string,
    _score: string,
    _source: trichtin,
    sort: number[]
}