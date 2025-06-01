import axios from 'axios'

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
export interface Report {
  id: number;
  social_account_uid: string;
  content_note: string;
  comment: string;
  action: string;
  linked_social_account_uid: string;
  created_at: string;
  updated_at: string;
  user: {
    id: string;
    name: string;
  } | null;
}
export interface individual {
  full_name: string
  national_id: string | null
  citizen_id: string | null
  image_url: string | null
  date_of_birth: string | null
  is_male: boolean | null
  hometown: string | null
  additional_info: string | null
  phone_number: string | null
  is_kol: boolean
  unit_id?: string
  task_id?: number
}

export interface individualResponse extends individual {
  id: string
  created_at: string
  updated_at: string
  individual_units: any[]
  unit?: {
    id: number
    name: string
  }
  task?: {
    id: number
    name: string
  }
}

export interface statuses {
    created_at: string,
    id: number,
    name: string,
    color: string,
    updated_at: string
}

export interface units {
    id: string
    name: string
}

export interface account_types extends units{

}

export interface tasks {
  id: number
  name: string
}

export interface relationship {
  id: number
  name: string
}
export interface ResponseSocialAccounts {
  id: number
  uid: string
  name: string
}
export interface report {
  id: number
  social_account_uid: string
  content_note: string
  comment: string
  action: string
  related_social_account_uid: string
  created_at: string;
  updated_at: string;
  user: {
      id: string
      name: string
  } | null
}