import React, {FC, useState, useEffect} from 'react'
import {useIntl} from 'react-intl'
import {PageTitle} from '../../../_metronic/layout/core'
import {KTSVG} from '../../../_metronic/helpers'
import {Formik, Form, Field} from 'formik'
import {account_type, status} from '../SocialAccount/SocialAccount'
import {ReportDataSchema} from './search-schemas'
import axios from 'axios'
import instance from '../../modules/axiosInstance'
import {toAbsoluteUrl} from '../../../_metronic/helpers'
const GroupWrap: FC = () => {
  return <Table className='mb-5 mb-xl-8' />
}
const URL = process.env.REACT_APP_API_URL

type Props = {
  className: string
}

const PUBLIC_URL = process.env.PUBLIC_URL

const TrichTinSearch: FC = () => {
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
  maxWidth: '400px', // Tăng chiều rộng xíu
  width: '100%', // Để form co giãn tốt hơn
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
  // const [showCreateAppModal, setShowCreateAppModal] = useState<boolean>(false)
  // const [showModalItemVaiao, setShowModalItemVaiao] = useState<boolean>(false)
  // const [showModelItem, setModelItem] = useState<boolean>(false)
  const [data, setData] = useState<ReportDataSchema[]>([])
  const [loading, setLoading] = useState<boolean>(false)

  // Lấy type và statuses từ localStorage (có thể dùng cho filter sau này)
  // const typeString = localStorage.getItem('type')
  // const type: account_type[] = typeof typeString === 'string' ? JSON.parse(typeString) : []
  // const statusesString = localStorage.getItem('statuses')
  // const statuses: status[] = typeof statusesString === 'string' ? JSON.parse(statusesString) : []
  // console.log(statuses)

  console.log('data', data)

  return (
    <div className={`card ${className}`}>
      {/* begin::Header */}
      <div className='card-header border-0 pt-5'>
        <h3 className='card-title align-items-start flex-column'>
          <span className='card-label fw-bold fs-3 mb-1'>Kết quả tìm kiếm</span>
        </h3>
        <div className='card-toolbar'>
          <div
            style={{
              display: 'flex',
              flexDirection: 'column',
              alignItems: 'center',
              justifyContent: 'center',
              width: '100%'
            }}
          >
            <Formik
              initialValues={{keyword: ''}} // keyword để nhập liệu
              onSubmit={async (values, {setSubmitting}) => {
                if (!values.keyword.trim()) {
                  setData([]); // Xóa kết quả nếu keyword rỗng
                  setSubmitting(false);
                  return;
                }
                setLoading(true)
                try {
                  // Sửa API call: method GET, truyền keyword qua params
                  const response = await instance.get(`${URL}/search/report`, {
                    params: {
                      query: values.keyword, // Backend API mong muốn param là 'query'
                      // limit: 20 // Có thể thêm các params khác nếu cần
                    }
                  })
                  setData(response.data) // response.data đã là List[ReportData]
                } catch (error) {
                  console.error("Lỗi khi tìm kiếm trích tin:", error)
                  setData([]) // Xóa kết quả nếu có lỗi
                } finally {
                  setLoading(false)
                  setSubmitting(false)
                }
              }}
            >
              {({isSubmitting}) => (
                <Form style={formStyle}>
                  <Field
                    type='text'
                    name='keyword' // Đổi name thành keyword để khớp initialValues
                    placeholder='Nhập nội dung, UID vai ảo...'
                    style={inputStyle}
                  />
                  <button type='submit' style={buttonStyle} disabled={isSubmitting || loading}>
                    {loading ? 'Đang tìm...' : 'Tìm kiếm'}
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
                <th className='min-w-150px text-center rounded-end'>NGÀY CẬP NHẬT</th>
              </tr>
            </thead>
            {/* end::Table head */}
            {/* begin::Table body */}
            <tbody>
              {/* Nếu đang tải dữ liệu, hiển thị dòng thông báo */}
            {loading && (
                <tr>
                  <td colSpan={6} className='text-center py-5'>
                    Đang tải dữ liệu...
                  </td>
                </tr>
              )}
              {!loading && data.length === 0 && (
                 <tr>
                  <td colSpan={6} className='text-center py-5'>
                    Không tìm thấy dữ liệu phù hợp.
                  </td>
                </tr>
              )}
              {!loading && data.map((el: ReportDataSchema, index: number) => (
                <tr key={el.id}> {/* Sử dụng el.id là khóa duy nhất */}
                  <td className='text-center'>
                    <span className='text-muted fw-semibold d-block fs-7'>
                      {index + 1}
                    </span>
                  </td>
                  <td>
                    <div className='d-flex align-items-center'>
                      <div className='d-flex justify-content-start flex-column'>
                        <span className='text-dark fw-bold text-hover-primary mb-1 fs-6'>
                          {el.social_account_uid || 'N/A'}
                        </span>
                        {/* <span className='text-muted fw-semibold d-block fs-7'>
                          Ngày tạo: {new Date(el.created_at).toLocaleDateString()}
                        </span> */}
                      </div>
                    </div>
                  </td>
                  <td>
                    <span
                      className='text-dark fw-semibold d-block fs-7' // Đổi text-muted thành text-dark
                      style={{whiteSpace: 'pre-wrap'}}
                      title={el.content_note || ''} // Thêm tooltip để xem đầy đủ
                    >
                      {(el.content_note || '').slice(0, 150)}
                      {(el.content_note || '').length > 150 ? '...' : ''}
                    </span>
                  </td>
                  <td>
                    <span
                      className='text-dark fw-semibold d-block fs-7'
                      style={{whiteSpace: 'pre-wrap'}}
                      title={el.comment || ''}
                    >
                      {(el.comment || '').slice(0, 150)}
                      {(el.comment || '').length > 150 ? '...' : ''}
                    </span>
                  </td>
                  <td>
                     <span
                      className='text-dark fw-semibold d-block fs-7'
                      style={{whiteSpace: 'pre-wrap'}}
                      title={el.action || ''}
                    >
                      {(el.action || '').slice(0, 100)}
                       {(el.action || '').length > 100 ? '...' : ''}
                    </span>
                  </td>
                   <td className='text-center'>
                     <span className='text-muted fw-semibold d-block fs-7'>
                       {el.updated_at ? new Date(el.updated_at).toLocaleDateString() : 'N/A'}
                     </span>
                   </td>
                  {/* <td className='text-center'>
                    <button // Đổi thành button để có hành động rõ ràng
                      className='btn btn-sm btn-light-primary' // Class Metronic
                      onClick={() => {
                        // Xử lý khi click xem chi tiết, ví dụ mở modal
                        // setCurrentReport(el)
                        // setShowReportModal(true)
                        console.log("Xem chi tiết report:", el);
                      }}
                    >
                      Xem
                    </button>
                  </td> */}
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

export {TrichTinSearch}
