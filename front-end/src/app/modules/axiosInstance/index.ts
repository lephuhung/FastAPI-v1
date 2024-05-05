import axios from 'axios'

const API_URL = process.env.REACT_APP_API_URL
const instance = axios.create({
    baseURL: API_URL,
    timeout: 1000,
    headers: {
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Headers":
        "Access-Control-Allow-Headers, Content-Type, Authorization",
        "Access-Control-Allow-Methods": "*",
        "Content-Type": "application/json",
    }
});
export default instance