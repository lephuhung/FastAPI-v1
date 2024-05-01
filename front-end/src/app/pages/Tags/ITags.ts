export interface ITags{
    name:string
    color:string
}
export interface IResponseTags extends ITags{
    id: number
    created_at:string,
    updated_at:string
}