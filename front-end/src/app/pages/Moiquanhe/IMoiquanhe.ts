export interface Irelationship{
    name:string
}
export interface IResponserelationship extends Irelationship{
    id: number
    created_at:string,
    updated_at:string
}