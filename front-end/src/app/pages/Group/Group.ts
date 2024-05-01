export interface IGroup {
    uid: string,
    name: string,
    SDT?: string,
    trangthai_id: number,
    type_id: number,
    ghichu: string,
    reaction: number,
    Vaiao: Boolean,

}
export interface IGroupModal extends IGroup {
    trangthai_name: string,
    ctnv_id: number,
    donvi_id: string,
}
export interface IResponseGroup {
    uid: string,
    name: string,
    SDT?: string,
    trangthai_id: number,
    type_id: number,
    ghichu: string,
    reaction: number,
    Vaiao: Boolean,
    created_at: string,
    updated_at: string,
    trangthai_name: string,
    trangthai_color: string,
    ctnv_name: string,
    donvi_name: string,
    donvi_id?: string,
    ctnv_id?: number,
    id_hoinhomdonvi?: number,
}
export interface trangthai {
    created_at: string,
    id: number,
    name: string,
    color: string,
    updated_at: string
}
export interface donvi {
    created_at: string,
    id: string,
    name: string,
    updated_at: string
}
export interface type extends donvi {

}
export interface ctnv extends donvi {

}