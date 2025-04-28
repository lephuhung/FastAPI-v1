/* eslint-disable jsx-a11y/anchor-is-valid */
import React, { useState } from 'react'
import { KTSVG, toAbsoluteUrl } from '../../../_metronic/helpers'
import { useQuery } from 'react-query'
import instance from '../../modules/axiosInstance'
import { ICharacteristicResponse } from './Characteristic'
import { CreateAppModal } from './CreateAppModal'
import { useSearchParams } from 'react-router-dom'
import { ToastContainer, toast } from 'react-toastify';

import Avatar from 'react-avatar'
const URL = process.env.REACT_APP_API_URL
type Props = {
  className: string
}

const Table: React.FC<Props> = ({ className }) => {
  const [showCreateAppModal, setShowCreateAppModal] = useState<boolean>(false)
  const [loading, setloading] = useState<boolean>(false)
  const [page] = useSearchParams()
  const { isLoading, data, error } = useQuery({
    queryKey: ['characteristic', page.get('characteristic')],
    queryFn: async () => {
      const respone = await instance.get(`${URL}/characteristic/getAll`)
      const { data } = respone
      return data
    },
  })
  if (isLoading) {
    <div>Loading</div>
  }
  if (error) {
    console.log(error)
  }

  return (
    <div className={`card ${className}`}>
      {/* begin::Header */}
      <div className='card-header border-0 pt-5'>
        <h3 className='card-title align-items-start flex-column'>
          <span className='card-label fw-bold fs-3 mb-1'>DANH SÁCH TÍNH CHẤT ĐỐI TƯỢNG</span>
          {/* <span className='text-muted mt-1 fw-semibold fs-7'>Over 500 new products</span> */}
        </h3>
        <div className='card-toolbar'>
          <a
            href='#'
            className='btn btn-sm btn-light-primary'
            onClick={() => {
              setShowCreateAppModal(true)
              setloading(true)
            }}
          >
            <KTSVG path='/media/icons/duotune/arrows/arr075.svg' className='svg-icon-2' />
            Thêm mới Client
          </a>
        </div>
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
                <th className='ps-4 min-w-300px rounded-start'>TÊN TAGS</th>
                <th className='min-w-150px'>THỜI GIAN TẠO</th>
                <th className='min-w-150px'>COlOR HEX</th>
                <th className='min-w-250px'>HIỆN THỊ MÀU</th>
                <th className='min-w-200px text-center '>HÀNH ĐỘNG</th>
              </tr>
            </thead>
            {/* end::Table head */}
            {/* begin::Table body */}
            <tbody>
              {data &&
                data.map((el: ICharacteristicResponse, index: number) => (
                  <tr key={index}>
                    <td>
                      <div className='d-flex align-items-center'>
                        <div className='symbol symbol-50px me-5'>
                          <Avatar name={el.name} size='50px' round={true}/>
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
                        {el.updated_at.split('.')[0]}
                      </span>
                    </td>
                    <td>
                      <span className='text-muted fw-semibold text-muted d-block fs-7'>
                        {el.color}
                      </span>
                    </td>
                    <td>
                      <Avatar name='' size='50px' color={el.color} round={true}/>
                    </td>
                    <td className='text-center'>
                      <a
                        href='#'
                        className='btn btn-icon btn-bg-light btn-active-color-primary btn-sm me-1'
                      >
                        <KTSVG
                          path='/media/icons/duotune/general/gen019.svg'
                          className='svg-icon-3'
                        />
                      </a>
                      <a
                        href='#'
                        className='btn btn-icon btn-bg-light btn-active-color-primary btn-sm me-1'
                      >
                        <KTSVG path='/media/icons/duotune/art/art005.svg' className='svg-icon-3' />
                      </a>
                      <a
                        href='#'
                        className='btn btn-icon btn-bg-light btn-active-color-primary btn-sm'
                        onClick={() => {
                          instance
                            .delete(`${URL}/tags/${el.id}`)
                            .then((res) => {
                              console.log(res.data);
                            })
                            .catch((e) => {
 
                            })
                        }}
                      >
                        <KTSVG
                          path='/media/icons/duotune/general/gen027.svg'
                          className='svg-icon-3'
                        />
                      </a>
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
      <CreateAppModal
        show={showCreateAppModal}
        handleClose={() => setShowCreateAppModal(false)}
        handleLoading={() => setloading(true)}
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

export { Table }
