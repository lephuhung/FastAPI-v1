export interface ITinhchat{
    name: string,
    color: string
}
export interface ITinhchatResponse extends ITinhchat{
    id: number,
    created_at: string,
    updated_at: string
}