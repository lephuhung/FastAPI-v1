import axios from 'axios'
import { donvi } from '../Group/Group'

const URL = process.env.REACT_APP_API_URL

export const getIndividuals = async (params: any) => {
  const response = await axios.get(`${URL}/individuals`, { params })
  return response.data
}

export const getIndividual = async (id: number) => {
  const response = await axios.get(`${URL}/individuals/${id}`)
  return response.data
}

export const createIndividual = async (data: any) => {
  const response = await axios.post(`${URL}/individuals`, data)
  return response.data
}

export const updateIndividual = async (id: number, data: any) => {
  const response = await axios.put(`${URL}/individuals/${id}`, data)
  return response.data
}

export const deleteIndividual = async (id: number) => {
  const response = await axios.delete(`${URL}/individuals/${id}`)
  return response.data
}

export interface individual{
    client_name: string,
    CMND: string,
    CCCD: string,
    Image:string,
    Ngaysinh: string,
    Gioitinh: boolean,
    Quequan: string,
    Thongtinbosung: string,
    SDT: string,
    KOL: boolean,
}
export interface individualResponse extends individual{
    id: string,
    ctnv_id?: number,
    donvi_id?: string,
    donvi_name?: string,
    ctnv_name?: string,
    created_at: string,
    updated_at: string,
}
export interface statuses {
    created_at: string,
    id: number,
    name: string,
    color: string,
    updated_at: string
}
export interface units {
    created_at:string,
    id: string,
    name:string,
    updated_at:string
}
export interface account_types extends donvi{

}
export interface tasks extends donvi{

}