export interface IStatus{
    name: string,
    color: string
}
export interface IStatusResponse extends IStatus{
    id: number,
    created_at:string,
    updated_at:string
}
