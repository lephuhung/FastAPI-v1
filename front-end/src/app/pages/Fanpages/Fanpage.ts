
export interface IFanpage{
    uid: string,
    name:string,
    phone_number?: string,
    status:number,
    account_type_id: number,
    note:string,
    reaction:number,
    Vaiao: Boolean,

}
export interface IFanpageModal extends IFanpage{
    status_name:string,
    task_id: number,
    unit_id: string
}
export interface IResponseFanpage{
    id: number,
    uid: string,
    name:string,
    phone_number?: string,
    status:number,
    account_type_id: number,
    note:string,
    reaction:number,
    Vaiao: Boolean,
    created_at:string,
    updated_at:string,
    status_name:string,
    status_color:string,
    task_name: string,
    characteristic_id:number,
    unit_name:string,
    unit_id?: string,
    task_id?: number,
    id_hoinhomunit?: number,
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
export interface characteristic extends unit{
    color:string
}