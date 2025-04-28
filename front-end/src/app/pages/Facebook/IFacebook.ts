
export interface IFacebookModal {
    uid: string,
    name: string,
    phone_number?: string,
    status_id: number,
    account_type_id: number,
    note: string,
    reaction: number,
    Vaiao: Boolean,
}
export interface IFacebook extends IFacebookModal {
    status_name: string,
    task_id: number,
    unit_id: string
}
export interface IResponseFacebook {
    id: number,
    uid: string,
    name: string,
    phone_number?: string,
    status_id: number,
    status: number,
    account_type_id: number,
    note: string,
    reaction: number,
    Vaiao: Boolean,
    created_at: string,
    updated_at: string,
    status_name: string,
    status_color: string,
    task_name: string,
    unit_name: string,
    unit_id?: string,
    task_id?: number,
    id_hoinhomunit?: number,
    characteristic_id?: number,
}
export interface status {
    created_at: string,
    id: number,
    name: string,
    color: string,
    updated_at: string
}
export interface unit {
    created_at:string,
    id: string,
    name:string,
    updated_at:string
}
export interface type extends unit{

}
export interface task extends unit{

}
export interface relationship extends unit{

}
export interface characteristic extends unit{
    color: string
}
