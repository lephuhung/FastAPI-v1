/* eslint-disable jsx-a11y/anchor-is-valid */
import React, {useState} from 'react'
import {KTSVG, toAbsoluteUrl} from '../../../_metronic/helpers'
import {CreateAppModal} from './CreateAppModal'
import {useQuery} from 'react-query'
import axios from 'axios'
import {IResponseFacebook} from './IFacebook'
import {ModalViewGroup} from './ModalViewGroup'
import {UpdateModal} from './UpdateAppModal'
import { CreateModelMLH } from './CreateAppModalMLH'
import {useNavigate} from 'react-router-dom'
import {ToastContainer, toast} from 'react-toastify'
const URL = process.env.REACT_APP_API_URL
type Props = {
  className: string
}
const exampleData = {
  id: 0,
  uid: '',
  name: '',
  phone_number: '',
  status: 1,
  status_id: 0,
  account_type_id: 0,
  note: '',
  reaction: 0,
  Vaiao: false,
  created_at: '',
  updated_at: '',
  status_name: '',
  status_color: '',
  task_name: '',
  unit_name: '',
  id_hoinhomunit: 0,
}
const Table: React.FC<Props> = ({className}) => {
  const PUBLIC_URL = process.env.PUBLIC_URL
  const [showCreateAppModal, setShowCreateAppModal] = useState<boolean>(false)
  const [showModalGroup, setShowModalGroup] = useState<boolean>(false)
  const [showModalupdate, setShowModalUpdate] = useState<boolean>(false)
  const [showModalMLH, setShowModalMLH] = useState<boolean>(false)
  const [ifacebook, setIfacebook] = useState<IResponseFacebook>()
  const navigate = useNavigate()
  const [ifacebookupdate, setIfacebookupdate] = useState<IResponseFacebook>(exampleData)
  const [loading, setloading] = useState<boolean>(false)
  
  const {isLoading, data, error} = useQuery({
    queryKey: ['facebook', loading],
    queryFn: async () => {
      setloading(false)
      const respone = await axios.get(`${URL}/social-accounts`)
      if(respone.status===200){
        const {data} = respone
        console.log(data)
        return data
      }else if(respone.status===403){
        
      }
    },
    onError: (error: any) => {
      if (error.response && error.response.status === 403) {
        // Handle 403 error here
        navigate(`${PUBLIC_URL}/auth`)
        // You can show a message to the user, redirect them, or perform any other action
      }
    }
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
          <span className='card-label fw-bold fs-3 mb-1'>DANH SÁCH TÀI KHOẢN FACEBOOK</span>
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
            Thêm mới Facebook
          </a>
          <a
            href='#'
            className='btn btn-sm btn-light-primary'
            onClick={() => {
              setShowModalMLH(true)
            }}
            style={{marginLeft:'30px'}}
          >
            <KTSVG path='/media/icons/duotune/arrows/arr075.svg' className='svg-icon-2' />
            Tạo mối liên hệ
          </a>
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
                {/* <th className='min-w-150px'>CẬP NHẬT</th> */}
                <th className='min-w-100px text-center'>PHÂN LOẠI</th>
                <th className='min-w-100px text-center'>SĐT</th>
                <th className='min-w-100px'>VAI ẢO</th>
                <th className='min-w-100px'>ĐƠN VỊ</th>
                <th className='min-w-100px text-center'>CTNV</th>
                <th className='min-w-200px text-center'>HOẠT ĐỘNG</th>
              </tr>
            </thead>
            {/* end::Table head */}
            {/* begin::Table body */}
            <tbody>
              {data &&
                data.map((el: IResponseFacebook, index: number) => (
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
                            {el.name.toUpperCase()}
                          </span>
                          <span className='text-muted fw-semibold text-muted d-block fs-7'>
                            {`UID: ${el.uid}`}
                          </span>
                        </div>
                      </div>
                    </td>
                    <td className='text-center'>
                      <span className='badge badge-primary fs-7 fw-semibold'>
                        {/* {el?.status_name.toUpperCase()} */}
                        {el?.status_id}
                      </span>
                    </td>
                    <td className='text-center'> 
                      <span className='badge badge-primary fs-7 fw-semibold'>{el?.phone_number==='0' ? 'Chưa có': el.phone_number}</span>
                    </td>
                    <td>
                      {el.Vaiao ? (
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
                      <span className='badge badge-danger fs-7 fw-semibold'>{el.unit_name}</span>
                    </td>
                    <td className='text-center'>
                      <span className='badge badge-success fs-7 fw-semibold'>
                        {/* {el.task_name.toUpperCase()} */}
                        {el.name.toUpperCase()}
                      </span>
                    </td>
                    <td className='text-center'>
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
                            .delete(`${URL}/uid/delete/${el.uid}`)
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
      <CreateAppModal
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
      <ModalViewGroup
        show={showModalGroup}
        handleClose={() => setShowModalGroup(false)}
        title='THÔNG TIN CỤ THỂ TÀI KHOẢN'
        ifacebook={ifacebook}
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
export {Table}
