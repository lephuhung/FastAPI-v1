export interface individual{
    full_name: string,
    id_number: string,
    kols_type: string,
    image_url:string,
    date_of_birth: string,
    is_male: boolean,
    hometown: string,
    additional_info: string,
    phone_number: string,
    is_kol: boolean,
}
export interface individualResponse extends individual{
    id: string,
    task_id?: number,
    unit_id?: string,
    unit_name?: string,
    task_name?: string,
    created_at: string,
    updated_at: string,
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