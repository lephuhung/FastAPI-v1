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
export interface Task {
    id: number,
    name: string,
    created_at: string,
    updated_at: string
}
export interface Characteristic {
    id: number,
    name: string,
    color: string,
    created_at: string,
    updated_at: string
}
export interface Tag {
    id: number,
    name: string,
    color: string,
    created_at: string,
    updated_at: string
}