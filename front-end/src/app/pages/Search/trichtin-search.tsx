import React, {FC, useState, useEffect} from 'react'
import {useIntl} from 'react-intl'
import {PageTitle} from '../../../_metronic/layout/core'
import {KTSVG} from '../../../_metronic/helpers'
import {Formik, Form, Field} from 'formik'
import {unit, type, characteristic, task} from '../Facebook/IFacebook'
import {trichtinsearch} from './search'
import axios from 'axios'
import instance from '../../modules/axiosInstance'
import {toAbsoluteUrl} from '../../../_metronic/helpers'
import {status} from '../Individual/individual'
const GroupWrap: FC = () => {
  return <Table className='mb-5 mb-xl-8' />
}
const URL = process.env.REACT_APP_API_URL
type Props = {
  className: string
}
const PUBLIC_URL = process.env.PUBLIC_URL
const TrichinSearch: FC = () => {
  const intl = useIntl()
  return (
    <>
      <PageTitle breadcrumbs={[]}>{'TÌM KIẾM THÔNG TIN TRONG TRÍCH TIN'}</PageTitle>
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
  const [data, setData] = useState<trichtinsearch[]>([])
  //   const [phanloai, setPhanloai] = useState<status[]>([])
  const [loading, setloading] = useState<boolean>(false)
  const [showModelItem, setModelItem] = useState<boolean>(false)
  const typeString = localStorage.getItem('type')
  const type: type[] = typeof typeString === 'string' ? JSON.parse(typeString) : []
  const phanloaiString = localStorage.getItem('phanloai')
  const phanloai: status[] = typeof phanloaiString === 'string' ? JSON.parse(phanloaiString) : []
  console.log(phanloai)
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
                  .post(`${URL}/search/trichtin?keyword=${values.keyword}`)
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

          <table className='table align-middle '>
            {/* begin::Table head */}
            <thead>
              <tr className='fw-bold text-muted bg-light'>
                <th className='min-w-40px text-center'>STT</th>
                <th className='ps-4 min-w-200px rounded-start'>VAI ẢO</th>
                <th className='min-w-300px'>NỘI DUNG</th>
                <th className='min-w-300px'>Nhận xét</th>
                <th className='min-w-100px'>Hành động </th>
              </tr>
            </thead>
            {/* end::Table head */}
            {/* begin::Table body */}
            <tbody>
              {data &&
                data.map((el: trichtinsearch, index: number) => (
                  <tr key={index}>
                    <td>
                      <span className='text-muted fw-semibold text-muted d-block fs-7 text-center'>
                        {index + 1}
                      </span>
                    </td>
                    <td>
                      <div className='d-flex align-items-center'>
                        <div className='d-flex justify-content-start flex-column'>
                          <a href='#' className='text-dark fw-bold text-hover-primary mb-1 fs-6'>
                            {el._source.uid_vaiao}
                          </a>
                          <span className='text-muted fw-semibold text-muted d-block fs-7'>
                            {`${el._source.updated_at.split('.')[0]}`}
                          </span>
                        </div>
                      </div>
                    </td>
                    <td>
                      <span
                        className='text-muted fw-semibold text-muted d-block fs-7'
                        style={{whiteSpace: 'pre-wrap'}}
                      >
                        {el._source.ghichu_noidung.slice(0, 200)}
                      </span>
                    </td>
                    <td>
                      <span
                        className='text-muted fw-semibold text-muted d-block fs-7'
                        style={{whiteSpace: 'pre-wrap'}}
                      >
                        {el._source.nhanxet.slice(0, 200)}
                      </span>
                    </td>
                    <td className='text-canter'>
                      <span
                        className='btn btn-bg-light btn-color-muted btn-active-color-primary btn-sm px-4'
                        onClick={() => {
                          // settrichtin(el)
                          // setshowModalIndividual(true)
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
    </div>
  )
}

export {TrichinSearch}
