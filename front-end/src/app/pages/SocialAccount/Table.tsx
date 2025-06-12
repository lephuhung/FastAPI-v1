/* eslint-disable jsx-a11y/anchor-is-valid */
import React, { useState, FC, useEffect } from 'react'
import { KTSVG, toAbsoluteUrl } from '../../../_metronic/helpers'
import { CreateSocialAccountModal } from './CreateSocialAccountModal'
import { useQuery } from 'react-query'
import axios from 'axios'
import { UpdateModal } from './UpdateAppModal'
import { CreateModelMLH } from './CreateAppModalMLH'
import { useNavigate } from 'react-router-dom'
import { ToastContainer, toast } from 'react-toastify'
import { SocialAccountResponse, SocialAccountListResponse } from './SocialAccount'
import { ModalViewItem } from './ModalViewItem'
const URL = process.env.REACT_APP_API_URL

interface Props {
  className: string
  socialAccount?: SocialAccountListResponse
  typeId: string
}

const exampleData = {
  id: 0,
  uid: '',
  name: '',
  reaction_count: 0,
  phone_number: '',
  status_id: 0,
  type_id: 0,
  note: '',
  is_active: false,
  created_at: '',
  updated_at: '',
  unit: {
    id: '',
    name: ''
  },
  task: {
    id: 0,
    name: ''
  }
}

export const Table: FC<Props> = ({ className, socialAccount, typeId }) => {
  const PUBLIC_URL = process.env.PUBLIC_URL
  const [showCreateAppModal, setShowCreateAppModal] = useState<boolean>(false)
  const [showModalGroup, setShowModalGroup] = useState<boolean>(false)
  const [showModalupdate, setShowModalUpdate] = useState<boolean>(false)
  const [showModalMLH, setShowModalMLH] = useState<boolean>(false)
  const [searchValue, setSearchValue] = useState<string>('')
  const [ifacebook, setIfacebook] = useState<SocialAccountResponse>()
  const navigate = useNavigate()
  const [ifacebookupdate, setIfacebookupdate] = useState<SocialAccountResponse>(exampleData)
  const [loading, setloading] = useState<boolean>(false)
  const [tableData, setTableData] = useState<SocialAccountResponse[]>([])
  const [accountTypeName, setAccountTypeName] = useState<string>('')

  // Fetch data by type ID
  const { isLoading, data, error } = useQuery({
    queryKey: ['social-accounts', typeId],
    queryFn: async () => {
      const response = await axios.get(`${URL}/social-accounts/type/${typeId}`)
      return response.data
    },
    onError: (error: any) => {
      if (error.response && error.response.status === 403) {
        navigate(`${PUBLIC_URL}/auth`)
      }
    }
  })

  useEffect(() => {
    if (data) {
      setTableData(data.data || [])
      setAccountTypeName(data.account_type_name || '')
    }
  }, [data])

  const handleSearch = async () => {
    if (!searchValue.trim()) return

    try {
      setloading(true)
      const response = await axios.get(`${URL}/social-accounts/search/${typeId}/${searchValue.trim()}`)
      setTableData(response.data.data || [])
      setAccountTypeName(response.data.account_type_name || '')
    } catch (error) {
      console.error('Error searching accounts:', error)
      toast.error('Có lỗi xảy ra khi tìm kiếm tài khoản')
    } finally {
      setloading(false)
    }
  }

  const handleKeyPress = (e: React.KeyboardEvent<HTMLInputElement>) => {
    if (e.key === 'Enter') {
      handleSearch()
    }
  }

  if (isLoading) {
    return (
      <div className='d-flex justify-content-center align-items-center' style={{minHeight: '400px'}}>
        <div className='spinner-border text-primary' role='status' style={{width: '3rem', height: '3rem'}}>
          <span className='visually-hidden'>Loading...</span>
        </div>
      </div>
    )
  }

  if (error) {
    console.log(error)
    window.location.reload()
  }

  return (
    <div className={`card ${className}`}>
      {/* begin::Header */}
      <div className='card-header border-0 pt-5'>

        <div className='card-toolbar'>
          <div className='d-flex align-items-center position-relative'>
            <KTSVG
              path='/media/icons/duotune/general/gen021.svg'
              className='svg-icon-1 position-absolute ms-6'
            />
            <input
              type='text'
              className='form-control form-control-solid w-250px ps-12'
              placeholder='Tìm kiếm theo UID ...'
              value={searchValue}
              onChange={(e) => setSearchValue(e.target.value)}
              onKeyPress={handleKeyPress}
            />
          </div>
          <button
            type='button'
            className='btn btn-sm btn-light-primary ms-3'
            onClick={() => {
              setShowCreateAppModal(true)
            }}
          >
            <KTSVG path='/media/icons/duotune/arrows/arr075.svg' className='svg-icon-2' />
            Thêm mới tài khoản
          </button>
          <button
            type='button'
            className='btn btn-sm btn-light-primary ms-3'
            onClick={() => {
              setShowModalMLH(true)
            }}
          >
            <KTSVG path='/media/icons/duotune/arrows/arr075.svg' className='svg-icon-2' />
            Thêm mối liên hệ
          </button>
        </div>
      </div>
      {/* end::Header */}
      {/* begin::Body */}
      <div className='card-body py-3'>
        {/* begin::Table container */}
        <div className='table-responsive'>
          {/* begin::Table */}
          <table className='table table-row-dashed table-row-gray-200 gy-4'>
            {/* begin::Table head */}
            <thead>
              <tr className='fw-bold text-muted'>
                <th className='min-w-50px text-center'>STT</th>
                <th className='ps-4 min-w-250px rounded-start text-center'>TÊN</th>
                <th className='min-w-100px text-center'>TRẠNG THÁI</th>
                <th className='min-w-100px text-center'>SĐT</th>
                <th className='min-w-100px text-center'>HOẠT ĐỘNG</th>
                <th className='min-w-100px text-center'>ĐƠN VỊ</th>
                <th className='min-w-100px text-center'>CTNV</th>
                <th className='min-w-200px text-center'>HOẠT ĐỘNG</th>
              </tr>
            </thead>
            {/* end::Table head */}
            {/* begin::Table body */}
            <tbody>
              {tableData.map((el: SocialAccountResponse, index: number) => (
                <tr key={index} className='fw-bold fs-6 text-gray-800 border-bottom border-gray-200'>
                  <td className='text-center align-middle'>
                    <span className='text-muted fw-semibold text-muted d-block fs-7'>
                      {index + 1}
                    </span>
                  </td>
                  <td className='align-middle'>
                    <div className='d-flex align-items-center'>
                      <div className='symbol symbol-50px me-5'>
                        <img src={toAbsoluteUrl('/media/facebook.png')} className='' alt='' />
                      </div>
                      <div className='d-flex justify-content-start flex-column'>
                        <span className='text-dark fw-bold text-hover-primary mb-1 fs-6'>
                          {el.name.toUpperCase()}
                        </span>
                        <span className='text-muted fw-semibold text-muted d-block fs-7'>
                          {`UID: ${el.uid}`}
                        </span>
                      </div>
                    </div>
                  </td>
                  <td className='text-center align-middle'>
                    <span className='badge badge-primary fs-7 fw-semibold' style={{width: '150px', display: 'inline-block', overflow: 'hidden', textOverflow: 'ellipsis', whiteSpace: 'nowrap'}}>
                      {el.status_name?.toUpperCase()}
                    </span>
                  </td>
                  <td className='text-center align-middle'>
                    <span className='badge badge-primary fs-7 fw-semibold' style={{ display: 'inline-block', overflow: 'hidden', textOverflow: 'ellipsis', whiteSpace: 'nowrap'}} >
                      {el.phone_number === '0' ? 'Chưa có' : el.phone_number}
                    </span>
                  </td>
                  <td className='align-middle'>
                    {el.is_active ? (
                      <span className='badge badge-primary fs-7 fw-semibold' style={{width: '150px', display: 'inline-block', overflow: 'hidden', textOverflow: 'ellipsis', whiteSpace: 'nowrap'}}>
                        HOẠT ĐỘNG
                      </span>
                    ) : (
                      <span className='badge badge-warning fs-7 fw-semibold' style={{width: '150px', display: 'inline-block', overflow: 'hidden', textOverflow: 'ellipsis', whiteSpace: 'nowrap'}}>
                        KHÔNG HOẠT ĐỘNG
                      </span>
                    )}
                  </td>
                  <td className='align-middle'> 
                    {el.unit?.name ? (
                      <span className='badge badge-primary fs-7 fw-semibold' style={{width: '80px', display: 'inline-block', overflow: 'hidden', textOverflow: 'ellipsis', whiteSpace: 'nowrap'}}>
                        {el.unit?.name}
                      </span>
                    ) : (
                      <span className='badge badge-danger fs-7 fw-semibold' style={{width: '80px', display: 'inline-block', overflow: 'hidden', textOverflow: 'ellipsis', whiteSpace: 'nowrap'}}>
                        KHÔNG
                      </span>
                    )}
                  </td>
                  <td className='text-center align-middle'>
                    {el.task?.name ? (
                      <span className='badge badge-success fs-7 fw-semibold' style={{width: '150px', display: 'inline-block', overflow: 'hidden', textOverflow: 'ellipsis', whiteSpace: 'nowrap'}}>
                        {el.task?.name}
                      </span>
                    ) : (
                      <span className='badge badge-danger fs-7 fw-semibold' style={{width: '150px', display: 'inline-block', overflow: 'hidden', textOverflow: 'ellipsis', whiteSpace: 'nowrap'}}>
                        CHƯA PHÂN CÔNG
                      </span>
                    )}
                  </td>
                  <td className='text-center align-middle'>
                    <span
                      className='btn btn-bg-light btn-secondary btn-active-color-primary btn-sm px-4 me-1'
                      onClick={() => {
                        setIfacebook(el)
                        setShowModalGroup(true)
                      }}
                    >
                      Hiện thị
                    </span>
                    <a
                      href='#'
                      className='btn btn-icon btn-bg-light btn-secondary btn-active-color-primary btn-sm me-1'
                      onClick={() => {
                        setIfacebookupdate(el)
                        setShowModalUpdate(true)
                      }}
                    >
                      <KTSVG path='/media/icons/duotune/art/art005.svg' className='svg-icon-3' />
                    </a>
                    <a
                      href='#'
                      className='btn btn-icon btn-bg-light btn-secondary btn-active-color-primary btn-sm'
                      onClick={() => {
                        axios
                          .delete(`${URL}/social-accounts/${el.uid}`)
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
                            if (res.status === 400) {
                              toast.warning('Xóa không thành công', {
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
                            toast.warning('Xóa không thành công', {
                              position: 'bottom-right',
                              autoClose: 5000,
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
      {/* begin::Body */}
      <CreateSocialAccountModal
        show={showCreateAppModal}
        handleClose={() => setShowCreateAppModal(false)}
        handleLoading={() => setloading(true)}
        title='THÊM TÀI KHOẢN FACEBOOK MỚI'
      />
      <UpdateModal
        show={showModalupdate}
        handleClose={() => setShowModalUpdate(false)}
        handleLoading={() => setloading(true)}
        title='CẬP NHẬT THÔNG TIN'
        dataModal={ifacebookupdate}
      />
      <CreateModelMLH
        show={showModalMLH}
        handleClose={() => setShowModalMLH(false)}
        handleLoading={() => setloading(true)}
        title='CẬP NHẬT MỐI LIÊN HỆ GIỮA TÀI KHOẢN FACEBOOK'
      />
      <ModalViewItem
        show={showModalGroup}
        handleClose={() => setShowModalGroup(false)}
        title='THÔNG TIN CỤ THỂ TÀI KHOẢN'
        item={ifacebook}
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

// export async function get_user_groups(user_id: string, access_token: string) {
//   const url = 'https://graph.facebook.com/graphql'
//   const params = {
//     access_token: access_token,
//     q: `nodes(${user_id}){groups{nodes{id,name,viewer_post_status,visibility,group_member_profiles{count}}}}`,
//   }
//   const config = {
//     headers: {
//       'Access-Control-Allow-Origin': '*',
//     },
//     params: params,
//   }
//   const response = await axios.get(url, config)
//   const data = response.data

//   if ('error' in data) {
//     const error_message = data.error.message
//     throw new Error(`GraphQL query failed: ${error_message}`)
//   }

//   const groups = data[user_id].groups.nodes
//   console.log(JSON.stringify(groups))
//   return groups
// }
