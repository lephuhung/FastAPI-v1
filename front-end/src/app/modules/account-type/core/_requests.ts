import axios from 'axios'
import { AccountTypeModel } from './_models'
const API_URL = process.env.REACT_APP_API_URL

export const GET_ACCOUNT_TYPES_URL = `${API_URL}/account-types/public`

export function getAccountTypes() {
  return axios.get<AccountTypeModel[]>(GET_ACCOUNT_TYPES_URL)
} 