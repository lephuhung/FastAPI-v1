import React, {FC, useState, useEffect} from 'react'
import {useIntl} from 'react-intl'
import {PageTitle} from '../../../_metronic/layout/core'
import {KTSVG} from '../../../_metronic/helpers'
import {Formik, Form, Field} from 'formik'
import {donvi, type, tinhchat, ctnv} from '../Facebook/IFacebook'
import {individualsearch} from './search'
import axios from 'axios'
import instance from '../../modules/axiosInstance'
import {toAbsoluteUrl} from '../../../_metronic/helpers'
import {statuses, individual} from '../Individual/individual'
import {toast} from 'react-toastify'
import Avatar from 'react-avatar';
const GroupWrap: FC = () => {
  return <Table className='mb-5 mb-xl-8' />
}
const URL = process.env.REACT_APP_API_URL
type Props = {
  className: string
}
const PUBLIC_URL = process.env.PUBLIC_URL
const DoituongSearch: FC = () => {
  const intl = useIntl()
  return (
    <>
      <PageTitle breadcrumbs={[]}>{'TÌM KIẾM THÔNG TIN TRONG THÔNG TIN ĐỐI TƯỢNG'}</PageTitle>
      <GroupWrap />
    </>
  )
}
const containerStyle = {
  display: 'flex',
  flexDirection: 'column',
  alignItems: 'center',
  justifyContent: 'center',
  height: '100vh', // Adjust to center vertically
}

const formStyle = {
  display: 'flex',
  alignItems: 'center',
  maxWidth: '300px',
}

const inputStyle = {
  padding: '10px',
  marginRight: '10px',
  border: '1px solid #ccc',
  borderRadius: '5px',
  flex: '1',
}

const buttonStyle = {
  padding: '10px 20px',
  backgroundColor: '#007bff',
  color: '#fff',
  border: 'none',
  borderRadius: '5px',
  cursor: 'pointer',
}

const Table: React.FC<Props> = ({className}) => {
  const [showCreateAppModal, setShowCreateAppModal] = useState<boolean>(false)
  const [showModalItemVaiao, setShowModalItemVaiao] = useState<boolean>(false)
  const [data, setData] = useState<individualsearch[]>([])
  //   const [phanloai, setPhanloai] = useState<trangthai[]>([])
  const [loading, setloading] = useState<boolean>(false)
  const [showModelItem, setModelItem] = useState<boolean>(false)
  const typeString = localStorage.getItem('type')
  const type: type[] = typeof typeString === 'string' ? JSON.parse(typeString) : []
  const statusesString = localStorage.getItem('statuses')
  const statuses: statuses[] = typeof statusesString === 'string' ? JSON.parse(statusesString) : []
  return (
    <div className={`card ${className}`}>
      {/* begin::Header */}
      <div className='card-header border-0 pt-5'>
        <h3 className='card-title align-items-start flex-column'>
          <span className='card-label fw-bold fs-3 mb-1'></span>
        </h3>
        <div className='card-toolbar'>
          <div
            style={{
              display: 'flex',
              flexDirection: 'column',
              alignItems: 'center',
              justifyContent: 'center',
            }}
          >
            <Formik
              initialValues={{keyword: ''}}
              onSubmit={(values) => {
                instance
                  .post(`${URL}/search/doituong?keyword=${values.keyword}`)
                  .then((response: any) => {
                    setData(response.data)
                  })
                  .catch((error) => {})
              }}
            >
              {({isSubmitting}) => (
                <Form style={formStyle}>
                  <Field type='text' name='keyword' placeholder='Search' style={inputStyle} />
                  <button type='submit' style={buttonStyle}>
                    Search
                  </button>
                </Form>
              )}
            </Formik>
          </div>
        </div>
      </div>
      {/* end::Header */}
      {/* begin::Body */}
      <div className='card-body py-3'>
        {/* begin::Table container */}
        <div className='table-responsive'>
          {/* begin::Table */}

          <table className='table border gy-3 gs-3'>
            {/* begin::Table head */}
            <thead>
              <tr className='fw-bold fs-6 text-gray-800 border-bottom border-gray-200'>
                {/* <th className='ps-4 min-w-5px rounded-start text-center'>STT</th> */}
                <th className='min-w-150px text-center'>THÔNG TIN</th>
                <th className='min-w-100px text-center'>SĐT</th>
                <th className='min-w-150px text-center'>QUÊ QUÁN</th>
                <th className='min-w-100px text-center'>ĐƠN VỊ</th>
                <th className='min-w-100px text-center'>CTNV</th>
                <th className='min-w-50px text-center'>KOL</th>
                <th className='min-w-150px text-center'>HÀNH ĐỘNG</th>
              </tr>
            </thead>
            <tbody>
              {data &&
                data.map((el: individualsearch, index: number) => (
                  <tr
                    key={index}
                    className='fw-bold fs-6 text-gray-800 border-bottom border-gray-200'
                  >
                    {/* <td className='text-center'>
                      <span className='text-muted fw-semibold text-muted d-block fs-7'>
                        {index + 1}
                      </span>
                    </td> */}
                    <td>
                      <div className='d-flex align-items-center'>
                        <div className='symbol symbol-50px me-5'>
                          {el._source.Image ? (
                            <img src={el._source.Image} className='' alt='' />
                          ) : (
                            <Avatar name={el._source.client_name} round={true} size='50' />
                          )}
                        </div>
                        <div className='d-flex justify-content-start flex-column'>
                          <a href='#' className='text-dark fw-bold text-hover-primary mb-1 fs-6'>
                            {el._source.client_name.toUpperCase()}
                          </a>
                          <span className='text-muted fw-semibold text-muted d-block fs-7'>
                            {`CCCD/CMND: ${el._source.CCCD}/${el._source.CMND}`}
                          </span>
                        </div>
                      </div>
                    </td>
                    <td>
                      <span className='badge badge-light-primary fs-7 fw-semibold'>{el._source.SDT}</span>
                    </td>
                    <td>
                      <span className='badge badge-light-success fs-7 fw-semibold'>
                        {el._source.Quequan.slice(0, 30)}
                      </span>
                    </td>
                    <td>
                      <span className='badge badge-primary fs-7 fw-semibold fw-semibold'>
                        {/* {el._source.donvi_name} */}
                      </span>
                    </td>
                    <td>
                      <span className='badge badge-success fs-7 fw-semibold fw-semibold'>
                        {/* {el.ctnv_name} */}
                      </span>
                    </td>
                    <td className='text-center'>
                      {el._source.KOL === true ? (
                        <span className='badge badge-primary fs-7 fw-semibold fw-semibold'>
                          KOL
                        </span>
                      ) : (
                        <span className='badge badge-danger fs-7 fw-semibold fw-semibold'>
                          KHÔNG
                        </span>
                      )}
                    </td>
                    <td>
                      <span
                        className='btn btn-bg-light btn-color-muted btn-active-color-primary btn-sm px-4 me-1'
                        onClick={() => {
                          // setdoituongItem(el)
                          // setshowModalDoituong(true)
                        }}
                      >
                        Chi tiết
                      </span>

                      <a
                        href='#'
                        className='btn btn-icon btn-bg-light btn-active-color-primary btn-sm me-1'
                        onClick={() => {
                          // setdoituongItemUpdate(el)
                          // setshowModalDoituongupdate(true)
                        }}
                      >
                        <KTSVG path='/media/icons/duotune/art/art005.svg' className='svg-icon-3' />
                      </a>
                      <a
                        href=''
                        className='btn btn-icon btn-bg-light btn-active-color-primary btn-sm'
                        onClick={() => {
                          axios
                            .delete(`${URL}/doituong/delete/${el._source.id}`)
                            .then((res) => {
                              if (res.status === 200) {
                                toast.success('Xóa thành công', {
                                  position: 'bottom-right',
                                  autoClose: 5000,
                                  hideProgressBar: false,
                                  closeOnClick: true,
                                  pauseOnHover: true,
                                  draggable: true,
                                  progress: undefined,
                                  theme: 'light',
                                })
                              }
                            })
                            .catch((e) => {
                              toast.warning(e, {
                                position: 'top-center',
                                autoClose: 5000,
                                type: 'error',
                                hideProgressBar: false,
                                closeOnClick: true,
                                pauseOnHover: true,
                                draggable: true,
                                progress: undefined,
                                theme: 'light',
                              })
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
    </div>
  )
}

export {DoituongSearch}
