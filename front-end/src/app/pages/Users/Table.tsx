/* eslint-disable jsx-a11y/anchor-is-valid */
import React from 'react'
import {useQuery} from 'react-query'
import axios from 'axios'
import { iResponeDonvi } from './Donvi'
const URL = process.env.REACT_APP_API_URL
type Props = {
  className: string
}

export interface Tele {
  id: number
  content: string,
  status: boolean,
  created_at: string,
  updated_at: string
}
const Table: React.FC<Props> = ({className}) => {
  const {isLoading, data, error} = useQuery({
    queryKey: ['tele'],
    queryFn: async () => {
      const respone = await axios.get(`${URL}/donvi`)
      const {data} = respone
      return data.DATA
    },
  })
  if (isLoading) {
    <div>Loading</div>
  }
  if (error) {
    console.log(error)
  }
  console.log(data)
  return (
    <div className={`card ${className}`}>
      {/* begin::Header */}
      <div className='card-header border-0 pt-5'>
        <h3 className='card-title align-items-start flex-column'>
          <span className='card-label fw-bold fs-3 mb-1'>DANH SÁCH ĐƠN VỊ SỬ DỤNG PHẦN MỀM </span>
          {/* <span className='text-muted mt-1 fw-semibold fs-7'>Over 500 new products</span> */}
        </h3>
      </div>
      {/* end::Header */}
      {/* begin::Body */}
      <div className='card-body py-3'>
        {/* begin::Table container */}
        <div className='table-responsive'>
          {/* begin::Table */}
          <table className='table align-middle gs-0 gy-4'>
            {/* begin::Table head */}
            <thead>
              <tr className='fw-bold text-muted bg-light'>
                <th className='ps-4 min-w-625px rounded-start text-center'>STT</th>
                <th className='min-w-150px'>TÊN ĐƠN VỊ</th>
                <th className='min-w-100px'>THỜI GIAN</th>
                <th className='min-w-150px'>PHÂN LOẠI</th>
                <th className='min-w-150px'>SỐ LƯỢNG TÀI KHOẢN</th>
              </tr>
            </thead>
            <tbody>
              {data &&
                data.map((el: iResponeDonvi, index: number) => (
                  <tr key={index}>
                    <td className='text-center'>
                      <span className='badge badge-light-primary fs-7 fw-semibold'>{index+1}</span>
                    </td>
                    <td>
                      <div className='d-flex align-items-center'>
                        <div className='d-flex justify-content-start flex-column'>
                          <a
                            href='#'
                            className='text-dark fw-light text-hover-primary mb-1 fs-6'
                          >
                            {el.name}
                          </a>
                        </div>
                      </div>
                    </td>
                    <td>
                      {/* <a href='#' className='text-dark fw-bold text-hover-primary d-block mb-1 fs-6'>
                      
                    </a> */}
                      <span className='text-muted fw-semibold text-muted d-block fs-7'>
                        {el.created_at}
                      </span>
                    </td>
                    <td>
                     <span className='badge badge-primary fs-7 fw-semibold fw-semibold'>Hoạt động</span>
                    </td>
                    <td> 
                    <span className='badge badge-primary fs-7 fw-semibold fw-semibold'>0 tài khoản</span>
                    </td>
                  </tr>
                ))}
            </tbody>
            {/* end::Table body */}
          </table>
          {/* end::Table */}
        </div>
        {/* end::Table container */}
      </div>
      {/* begin::Body */}
    </div>
  )
}
export function cutString(string: string, maxLength: number): string {
  if (string != null && string.length > maxLength) {
    string = string.substring(0, maxLength)
  }
  return string
}
export {Table}