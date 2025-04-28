import React, {FC, useState, useEffect} from 'react'
import {useIntl} from 'react-intl'
import {PageTitle} from '../../../_metronic/layout/core'
import {KTSVG} from '../../../_metronic/helpers'
import {Formik, Form, Field} from 'formik'
import { unit, type, characteristic, task } from '../Facebook/IFacebook'
import {uidsearch} from './search'
import axios from 'axios'
import instance from '../../modules/axiosInstance'
import { toAbsoluteUrl } from '../../../_metronic/helpers'
import { status } from '../Individual/individual';
const GroupWrap: FC = () => {
  return <Table className='mb-5 mb-xl-8' />
}
const URL = process.env.REACT_APP_API_URL
type Props = {
  className: string
}
const PUBLIC_URL = process.env.PUBLIC_URL
const UIDSearch: FC = () => {
  const intl = useIntl()
  return (
    <>
      <PageTitle breadcrumbs={[]}>{'TÌM KIẾM THÔNG TIN TRONG HỘI NHÓM'}</PageTitle>
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
  const [data, setData] = useState<uidsearch[]>([])
//   const [phanloai, setPhanloai] = useState<status[]>([])
  const [loading, setloading] = useState<boolean>(false)
  const [showModelItem, setModelItem] = useState<boolean>(false)
  const typeString = localStorage.getItem('type')
  const type: type[] = typeof typeString === 'string' ? JSON.parse(typeString) : []
  const phanloaiString = localStorage.getItem('phanloai')
  const phanloai: status[] = typeof phanloaiString=== 'string' ? JSON.parse(phanloaiString) : []
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
                  .post(`${URL}/search/uid?keyword=${values.keyword}`)
                  .then((response:any) => {setData(response.data)})
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

          <table className='table align-middle gs-0 gy-4'>
            {/* begin::Table head */}
            <thead>
              <tr className='fw-bold text-muted'>
                <th className='min-w-50px text-center'>STT</th>
                <th className='ps-4 min-w-250px rounded-start'>TÊN</th>
                {/* <th className='min-w-150px'>CẬP NHẬT</th> */}
                <th className='min-w-150px'>PHÂN LOẠI</th>
                <th className='min-w-100px'>SĐT</th>
                <th className='min-w-100px'>VAI ẢO</th>
                <th className='min-w-100px'>LOẠI TÀI KHOẢN</th>
                <th className='min-w-100px text-center'>BẠN BÈ</th>
                <th className='min-w-200px text-center'>HÀNH ĐỘNG</th>
              </tr>
            </thead>
            {/* end::Table head */}
            {/* begin::Table body */}
            <tbody>
              {data &&
                data.map((el: uidsearch, index: number) => (
                  <tr key={index} className='fw-bold fs-6 text-gray-800 border-bottom border-gray-200'>
                    <td className='text-center'>
                      <span className='text-muted fw-semibold text-muted d-block fs-7'>
                        {index + 1}
                      </span>
                    </td>
                    <td>
                      <div className='d-flex align-items-center'>
                        <div className='symbol symbol-50px me-5'>
                          <img src={toAbsoluteUrl('/media/facebook.png')} className='' alt='' />
                        </div>
                        <div className='d-flex justify-content-start flex-column'>
                          <span className='text-dark fw-bold text-hover-primary mb-1 fs-6'>
                            {el._source.name.toUpperCase()}
                          </span>
                          <span className='text-muted fw-semibold text-muted d-block fs-7'>
                            {`UID: ${el._source.uid}`}
                          </span>
                        </div>
                      </div>
                    </td>
                    <td>
                      <span className='badge badge-primary fs-7 fw-semibold'>
                        {phanloai[el._source.status-1].name}
                      </span>
                    </td>
                    <td>
                      <span className='badge badge-primary fs-7 fw-semibold'>{el._source.phone_number}</span>
                    </td>
                    <td>
                      {el._source.Vaiao ? (
                        <span className='badge badge-primary fs-7 fw-semibold'>
                          VAI ẢO
                        </span>
                      ) : (
                        <span className='badge badge-warning fs-7 fw-semibold'>
                           KHÔNG
                        </span>
                      )}
                    </td>
                    <td>
                      <span className='badge badge-danger fs-7 fw-semibold'>{type[el._source.account_type_id].name}</span>
                    </td>
                    <td className='text-center'>
                      <span className='badge badge-success fs-7 fw-semibold'>
                        {el._source.reaction}
                      </span>
                    </td>
                    <td className='text-center'>
                      <span
                        className='btn btn-bg-light btn-color-muted btn-active-color-primary btn-sm px-4 me-1'
                        onClick={() => {
                         
                        }}
                      >
                        Hiện thị
                      </span>

                      <a
                        href='#'
                        className='btn btn-icon btn-bg-light btn-active-color-primary btn-sm me-1'
                        onClick={() => {
                         
                        }}
                      >
                        <KTSVG path='/media/icons/duotune/art/art005.svg' className='svg-icon-3' />
                      </a>
                      <a
                        href='#'
                        className='btn btn-icon btn-bg-light btn-active-color-primary btn-sm'

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

export {UIDSearch}
