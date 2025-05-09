export interface uid {
    uid: string,
    name: string,
    phone_number?: string,
    status: number,
    account_type_id: number,
    note: string,
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
    full_name: string,
    national_id: string,
    citizen_id: string,
    image_url:string,
    date_of_birth: string,
    is_male: boolean,
    hometown: string,
    additional_info: string,
    phone_number: string,
    is_kol: boolean,
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