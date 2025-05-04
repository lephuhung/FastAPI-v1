export interface SocialAccountModal {
    uid: string,
    name: string,
    phone_number?: string,
    status_id: number,
    type_id: number,
    note: string,
    reaction_number: number,
    characteristics_id: number,
    unit_id: string,
    task_id: number,
    is_active: Boolean,
}
export interface SocialAccount extends SocialAccountModal {
    trangthai_name: string,
    ctnv_id: number,
    donvi_id: string
}
export interface SocialAccountResponse {
    id: number
    uid: string
    name: string
    reaction_count: number
    phone_number: string
    status_id: number
    status_name?: string
    type_id: number
    note: string
    is_active: boolean
    created_at: string
    updated_at: string
    unit?: {
        id: string
        name: string
    }
    task?: {
        id: number
        name: string
    }
}

export interface SocialAccountSimple {
    uid: string
    name: string
}

export interface SocialAccountTypeGroup {
    type_id: number
    type_name: string
    data: SocialAccountSimple[]
}

export interface SocialAccountTypeResponse {
    data: SocialAccountTypeGroup[]
}

export interface SocialAccountListResponse {
    account_type_name: string
    data: SocialAccountResponse[]
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
export interface account_type extends unit{

}
export interface task extends unit{

}
export interface relationship extends unit{

}
export interface characteristics extends unit{

}
