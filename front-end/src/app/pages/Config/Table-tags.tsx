/* eslint-disable jsx-a11y/anchor-is-valid */
import React, {useState} from 'react'
import {KTSVG, toAbsoluteUrl} from '../../../_metronic/helpers'
import {useQuery} from 'react-query'
import {ITrangthaiResponse} from './trangthai'
import Avatar from 'react-avatar'
import instance from '../../modules/axiosInstance'
import {CreateAppModal} from './CreateAppModal'
import {useSearchParams} from 'react-router-dom'
import { ToastContainer } from 'react-toastify'
const URL = process.env.REACT_APP_API_URL
type Props = {
  className: string
}

export interface reaction {
  react: number
  shares: number
}

const TableTags: React.FC<Props> = ({className}) => {
  const [showCreateAppModal, setShowCreateAppModal] = useState<boolean>(false)
  const [UID, setUID] = useState<string>('')
  const [page] = useSearchParams()
  const [content, setContent] = useState<string>('')
  const [loading, setLoading] = useState<boolean>(false)
  const {isLoading, data, error} = useQuery({
    queryKey: ['post'],
    queryFn: async () => {
      const respone = await instance.get(`${URL}/tags`)
      const {data} = respone
      return data
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
          <span className='card-label fw-bold fs-3 mb-1'>DANH SÁCH PHÂN LOẠI HỘI NHÓM </span>
        </h3>
        <div className='card-toolbar'>
          <a
            href='#'
            className='btn btn-sm btn-light-primary'
            onClick={() => {
              setShowCreateAppModal(true)
            }}
          >
            <KTSVG path='/media/icons/duotune/arrows/arr075.svg' className='svg-icon-2' />
            Thêm mới phân loại
          </a>
        </div>
      </div>
      {/* end::Header */}
      {/* begin::Body */}
      <div className='card-body py-3'>
        {/* begin::Table container */}
        <div className='table-responsive'>
          {/* begin::Table */}
          <table className='table align-middle gs-0 gy-4 table-row-dashed table-row-gray-300'>
            {/* begin::Table head */}
            <thead>
              <tr className='fw-bold text-muted bg-light'>
                <th className='ps-4 min-w-625px rounded-start'>TÊN</th>
                {/* <th className='min-w-125px'>UID</th> */}
                <th className='min-w-150px'>THỜI GIAN</th>
                <th className='min-w-100px'>MÀU SẮC</th>
                <th className='min-w-100px'>HIỆN THỊ MÀU</th>
                {/* <th className='min-w-150px'>Anh bai viet</th> */}
                <th className='min-w-100px text-center rounded-end'>HÀNH ĐỘNG</th>
              </tr>
            </thead>
            <tbody>
              {data &&
                data.map((el: ITrangthaiResponse, index: number) => (
                  <tr className='fw-bolder fs-6 text-gray-800' key={index}>
                    <td>
                      <div className='d-flex align-items-center'>
                        <div className='symbol symbol-50px me-5'>
                          <Avatar name={el.name} size='50px' round={true} />
                        </div>
                        <div className='d-flex justify-content-start flex-column'>
                          <a href='#' className='text-dark fw-bold text-hover-primary mb-1 fs-6'>
                            {el.name.toUpperCase()}
                            <span className='text-muted fw-semibold text-muted d-block fs-7'>
                              {`ID: ${el.id}`}
                            </span>
                          </a>
                        </div>
                      </div>
                    </td>
                    <td>
                      <span className='text-muted fw-semibold text-muted d-block fs-7'>
                        {el.created_at}
                      </span>
                    </td>
                    <td style={{color: `${el.color}`}}>
                      <span className='text-muted fw-semibold text-muted d-block fs-7'>
                        {el.color}
                      </span>
                    </td>
                    <td>
                      <Avatar color={el.color} name='' round={true} size='50px' />
                    </td>
                    <td className='text-canter'>
                      <span
                        className='btn btn-bg-light btn-color-muted btn-active-color-primary btn-sm px-4'
                        onClick={() => {
                          // setShowCreateAppModal(true)
                          // setUID(el.uid)
                          // setContent(cutString(el.message, 200))
                          // setPost(el)
                        }}
                      >
                        Hiện thị
                      </span>
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

      <CreateAppModal
        show={showCreateAppModal}
        handleClose={() => setShowCreateAppModal(false)}
        handleLoading={() => setLoading(true)}
        title='CẬP NHẬT THÔNG TIN'
        // dataModal={ifacebookupdate}
      />
      <ToastContainer
        position='bottom-right'
        autoClose={5000}
        hideProgressBar={false}
        newestOnTop={false}
        closeOnClick
        rtl={false}
        pauseOnFocusLoss
        draggable
        pauseOnHover
        theme='light'
      />
    </div>
  )
}
export function cutString(string: string, maxLength: number): string {
  if (string != null && string.length > maxLength) {
    string = string.substring(0, maxLength)
  }
  return string
}
export {TableTags}
