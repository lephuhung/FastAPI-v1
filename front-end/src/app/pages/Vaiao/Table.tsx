/* eslint-disable jsx-a11y/anchor-is-valid */
import React, {useState} from 'react'
import {KTSVG, toAbsoluteUrl} from '../../../_metronic/helpers'

import {useQuery} from 'react-query'
import axios from 'axios'
import {IVaiaoResponse} from './Vaiao'
import {ToastContainer} from 'react-toastify'
import Avatar from 'react-avatar'
import {CreateAppModal} from './CreateAppModal'
import {ModalViewItemVaiao} from './ModalViewItemVaiao'
import {useNavigate} from 'react-router-dom'
const URL = process.env.REACT_APP_API_URL
type Props = {
  className: string
}
const PUBLIC_URL = process.env.PUBLIC_URL
const Table: React.FC<Props> = ({className}) => {
  const [showCreateAppModal, setShowCreateAppModal] = useState<boolean>(false)
  const [showModalItemVaiao, setShowModalItemVaiao] = useState<boolean>(false)
  const [id, setid] = useState<string>('')
  const [name, setname] = useState<string>('')
  const [loading, setloading] = useState<boolean>(false)
  const [showModelItem, setModelItem] = useState<boolean>(false)
  const navigate = useNavigate()
  const {isLoading, data, error} = useQuery({
    queryKey: ['vaiao', loading],
    queryFn: async () => {
      setloading(false)
      const respone = await axios.get(`${URL}/vaiao`)
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
  return (
    <div className={`card ${className}`}>
      {/* begin::Header */}
      <div className='card-header border-0 pt-5'>
        <h3 className='card-title align-items-start flex-column'>
          <span className='card-label fw-bold fs-3 mb-1'>
            DANH SÁCH VAI ẢO ĐANG BỐ TRÍ TRONG HỘI NHÓM
          </span>
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
            Thêm Vai ảo mới
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
                <th className='ps-4 min-w-200px rounded-start'>TÊN VAI ẢO</th>
                <th className='min-w-150px'>HỘI NHÓM</th>
                <th className='min-w-100px'>TRẠNG THÁI</th>
                <th className='min-w-100px text-center'>ĐƠN VỊ QUẢN LÝ</th>
                <th className='min-w-100px text-center'>CTNV</th>
                {/* <th className='min-w-150px'>CẬP NHẬT CUỐI</th> */}
                <th className='min-w-200px text-center'>HÀNH ĐỘNG</th>
              </tr>
            </thead>
            {/* end::Table head */}
            {/* begin::Table body */}
            <tbody>
              {data &&
                data.map((el: IVaiaoResponse, index: number) => (
                  <tr key={index}>
                    <td>
                      <div className='d-flex align-items-center'>
                        <div className='symbol symbol-50px me-5'>
                          <Avatar name={el.vaiao_name} round={true} size='50' />
                        </div>
                        <div className='d-flex justify-content-start flex-column'>
                          <a href='#' className='text-dark fw-bold text-hover-primary mb-1 fs-6'>
                            {el.vaiao_name.toUpperCase()}
                          </a>
                          <span className='text-muted fw-semibold text-muted d-block fs-7'>
                            {`UID: ${el.uid_vaiao}`}
                          </span>
                        </div>
                      </div>
                    </td>

                    <td>
                      <div className='d-flex justify-content-start flex-column'>
                        <a href='#' className='text-dark fw-bold text-hover-primary mb-1 fs-6'>
                          {el.hoinhom_name.toUpperCase()}
                        </a>
                        <span className='text-muted fw-semibold text-muted d-block fs-7'>
                          {`UID: ${el.uid_hoinhom}`}
                        </span>
                      </div>
                    </td>
                    <td>
                      {el.active === true ? (
                        <span className='badge badge-primary fs-7 fw-semibold fw-semibold'>
                          HOẠT ĐỘNG
                        </span>
                      ) : (
                        <span className='badge badge-danger fs-7 fw-semibold fw-semibold'>
                          ĐANG DỪNG
                        </span>
                      )}
                    </td>
                    <td className='text-center'>
                      {/* <a
                        href='#'
                        className='text-dark fw-bold text-hover-primary d-block mb-1 fs-6'
                      ></a> */}
                      <span className='badge badge-danger fs-7 fw-semibold fw-semibold text-center'>
                        {el.unit_name}
                      </span>
                    </td>
                    <td className='text-center'>
                      <span className='badge badge-warning fs-7 fw-semibold fw-semibold text-center'>
                        {el.task_name.toUpperCase()}
                      </span>
                    </td>
                    {/* <td>
                      <span className='text-muted fw-semibold text-muted d-block fs-7'>
                        {el.updated_at.split('.')[0]}
                      </span>
                    </td> */}
                    <td className='text-center'>
                      <span
                        className='btn btn-bg-light btn-color-muted btn-active-color-primary btn-sm px-4 me-1'
                        onClick={(e) => {
                          navigate(`${PUBLIC_URL}/trichtin/${el?.uid_hoinhom}`)
                        }}
                      >
                        Trích tin hội nhóm
                      </span>

                      <span
                        className='btn btn-bg-light btn-color-muted btn-active-color-primary btn-sm px-4 me-1'
                        onClick={() => {
                          setShowModalItemVaiao(true)
                          setid(el.uid_vaiao)
                          setname(el.vaiao_name)
                        }}
                      >
                        Lịch sử trích tin
                      </span>
                      <a
                        href='#'
                        className='btn btn-icon btn-bg-light btn-active-color-primary btn-sm'
                        onClick={() => {
                          navigate(`${PUBLIC_URL}/trichtinvaiao/${el?.uid_vaiao}`)
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
        title='THÊM VAI ẢO MỚI THEO DÕI HỘI NHÓM'
      />
      <ModalViewItemVaiao
        show={showModalItemVaiao}
        handleClose={() => setShowModalItemVaiao(false)}
        title={`LỊCH SỬ TRÍCH TIN VAI ẢO: ${name}`}
        id={id}
      />
    </div>
  )
}

export {Table}
