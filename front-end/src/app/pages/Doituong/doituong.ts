export interface doituong{
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
export interface doituongResponse extends doituong{
    id: string,
    ctnv_id?: number,
    donvi_id?: string,
    donvi_name?: string,
    ctnv_name?: string,
    created_at: string,
    updated_at: string,
}
export interface trangthai {
    created_at: string,
    id: number,
    name: string,
    color: string,
    updated_at: string
}
export interface donvi {
    created_at:string,
    id: string,
    name:string,
    updated_at:string
}
export interface type extends donvi{

}
export interface ctnv extends donvi{

}