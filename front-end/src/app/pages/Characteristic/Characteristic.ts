export interface ICharacteristic{
    name: string,
    color: string
}
export interface ICharacteristicResponse extends ICharacteristic{
    id: number,
    created_at: string,
    updated_at: string
}