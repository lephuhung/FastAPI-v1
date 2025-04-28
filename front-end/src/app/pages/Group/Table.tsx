/* eslint-disable jsx-a11y/anchor-is-valid */
import React, {useState} from 'react'
import {KTSVG, toAbsoluteUrl} from '../../../_metronic/helpers'
import {CreateAppModal} from './CreateAppModal'
import {ModalViewItem} from './ModalViewItem'
import {useQuery} from 'react-query'
import axios from 'axios'
import {IResponseGroup} from './Group'
import {ToastContainer, toast} from 'react-toastify'
import { UpdateModal } from './UpdateAppModal'
const URL = process.env.REACT_APP_API_URL
type Props = {
  className: string
}
const exampleData = {
  id: 0,
  uid: '',
  name: '',
  phone_number: '',
  status: 0,
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
  id_hoinhomunit: 0
}
const Table: React.FC<Props> = ({className}) => {
  const [showCreateAppModal, setShowCreateAppModal] = useState<boolean>(false)
  const [showModelItem, setModelItem] = useState<boolean>(false)
  const [showModalupdate, setShowModalUpdate] = useState<boolean>(false)
  const [loading, setloading] = useState<boolean>(false)
  const [ifacebookupdate, setIfacebookupdate] = useState<IResponseGroup>(exampleData)
  const [dataItem, setDataItem] = useState<IResponseGroup>()
  const {isLoading, data, error} = useQuery({
    queryKey: ['facebook', loading],
    queryFn: async () => {
      setloading(false)
      const respone = await axios.get(`${URL}/uid/get-groups`)
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
          <span className='card-label fw-bold fs-3 mb-1'>DANH SÁCH GROUP FACEBOOK</span>
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
            Thêm mới group
          </a>
        </div>
      </div>
      {/* end::Header */}
      {/* begin::Body */}
      <div className='card-body py-3'>
        {/* begin::Table container */}
        <div className='table-responsive'>
          {/* begin::Table */}

          <table className='table align-middle table-striped gs-0 gy-4'>
            {/* begin::Table head */}
            <thead>
              <tr className='fw-bold text-muted'>
                <th className='min-w-50px text-center'>STT</th>
                <th className='ps-4 min-w-250px rounded-start'>TÊN</th>
                <th className='min-w-150px'>CẬP NHẬT</th>
                <th className='min-w-150px'>PHÂN LOẠI</th>
                <th className='min-w-100px'>SĐT</th>
                <th className='min-w-100px'>BẠN BÈ</th>
                <th className='min-w-100px'>ĐƠN VỊ</th>
                <th className='min-w-100px'>CTNV</th>
                <th className='min-w-200px text-center'>HOẠT ĐỘNG</th>
              </tr>
            </thead>
            {/* end::Table head */}
            {/* begin::Table body */}
            <tbody>
              {data &&
                data.map((el: IResponseGroup, index: number) => (
                  <tr key={index}>
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
                          <a href='#' className='text-dark fw-bold text-hover-primary mb-1 fs-6'>
                            {el.name.toUpperCase()}
                          </a>
                          <span className='text-muted fw-semibold text-muted d-block fs-7'>
                            {`UID: ${el.uid}`}
                          </span>
                        </div>
                      </div>
                    </td>
                    <td>
                      <span className='text-muted fw-semibold text-muted d-block fs-7'>
                        {el.updated_at.split('.')[0]}
                      </span>
                    </td>
                    <td>
                      <span className='badge badge-primary fs-7 fw-semibold'>
                        {el.status_name.toUpperCase()}
                      </span>
                    </td>
                    <td>
                      <span className='badge badge-light-primary fs-7 fw-semibold'>{el.phone_number}</span>
                    </td>
                    <td>
                      <span className='badge badge-light-success fs-7 fw-semibold'>
                        {el.reaction}
                      </span>
                    </td>
                    <td>
                      <span className='badge badge-success fs-7 fw-semibold'>
                        {el.unit_name}
                      </span>
                    </td>
                    <td>
                      <span className='badge badge-primary fs-7 fw-semibold'>
                        {el.task_name.toUpperCase()}
                      </span>
                    </td>
                    <td className='text-center'>
                      <span
                        className='btn btn-bg-light btn-secondary btn-active-color-primary btn-sm px-4 me-1'
                        onClick={() => {
                          setDataItem(el)
                          setModelItem(true)
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
                                let data = res.data.DATA
                                console.log(data.errors)
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
        title='THÊM GROUP MỚI'
      />
      <ModalViewItem
        show={showModelItem}
        handleClose={() => setModelItem(false)}
        // handleLoading={() => setloading(true)}
        igroup={dataItem}
        title='THÔNG TIN CHI TIẾT GROUP'
      />
        <UpdateModal
        show={showModalupdate}
        handleClose={() => setShowModalUpdate(false)}
        handleLoading={() => setloading(true)}
        title='CẬP NHẬT THÔNG TIN'
        dataModal={ifacebookupdate}
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

export {Table}
