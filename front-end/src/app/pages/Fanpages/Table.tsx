/* eslint-disable jsx-a11y/anchor-is-valid */
import React, {useState} from 'react'
import {KTSVG, toAbsoluteUrl} from '../../../_metronic/helpers'
import {CreateAppModal} from './CreateAppModal'
import {useQuery} from 'react-query'
import axios from 'axios'
import {ModalViewItem} from './ModalViewItem'
import {IResponseFanpage, IFanpage, tinhchat} from './Fanpage'
import {ToastContainer, toast} from 'react-toastify'
import 'react-toastify/dist/ReactToastify.css'
import {UpdateModal} from './UpdateAppModal'
import clsx from 'clsx';
const URL = process.env.REACT_APP_API_URL
type Props = {
  className: string
}
const exampleData = {
  id: 0,
  uid: '',
  name: '',
  SDT: '',
  trangthai_id: 0,
  type_id: 0,
  ghichu: '',
  reaction: 0,
  Vaiao: false,
  created_at: '',
  updated_at: '',
  trangthai_name: '',
  trangthai_color: '',
  ctnv_name: '',
  donvi_name: '',
  tinhchat_id:0,
  id_hoinhomdonvi: 0,
}
const Table: React.FC<Props> = ({className}) => {
  const [showCreateAppModal, setShowCreateAppModal] = useState<boolean>(false)
  const [loading, setloading] = useState<boolean>(false)
  const [showModalupdate, setShowModalUpdate] = useState<boolean>(false)
  const [showModelItem, setModelItem] = useState<boolean>(false)
  const [ifacebookupdate, setIfacebookupdate] = useState<IResponseFanpage>(exampleData)
  const [ifanpage, setIfanpage] = useState<IResponseFanpage>()
  const tinhchatString = localStorage.getItem('tinhchat')
  const tinhchat: tinhchat[] = typeof tinhchatString === 'string' ? JSON.parse(tinhchatString) : []
  const {isLoading, data, error} = useQuery({
    queryKey: ['fanpage', loading],
    queryFn: async () => {
      setloading(false)
      const respone = await axios.get(`${URL}/uid/get-pages`)
      const {data} = respone
      return data
    },
  })
  if (isLoading) {
    ;<div>Loading</div>
  }
  if (error) {
    console.log(error)
  }
  return (
    <div className={`card ${className}`}>
      {/* begin::Header */}
      <div className='card-header border-0 pt-5' >
        <h3 className='card-title align-items-start flex-column'>
          <span className='card-label fw-bold fs-3 mb-1'>DANH SÁCH FANPAGES</span>
          {/* <span className='text-muted mt-1 fw-semibold fs-7'>Over 500 new products</span> */}
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
            Thêm mới Fanpage
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
              <tr className='fw-bold text-muted bg-light'>
                
                <th className='ps-4 min-w-350px rounded-start text-center'>TÊN</th>
                <th className='min-w-100px text-center'>TÍNH CHẤT</th>
                <th className='min-w-100px text-center'>PHÂN LOẠI</th>
                <th className='min-w-100px text-center'>SĐT</th>
                <th className='min-w-100px text-center'>BẠN BÈ</th>
                <th className='min-w-100px text-center'>ĐƠN VỊ</th>
                <th className='min-w-100px text-center'>CTNV</th>
                <th className='min-w-200px text-center'>HOẠT ĐỘNG</th>
              </tr>
            </thead>
            {/* end::Table head */}
            {/* begin::Table body */}
            <tbody>
              {data &&
                data.map((el: IResponseFanpage, index: number) => (
                  <tr key={index}>
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
                      {/* <a
                        href='#'
                        className='text-dark fw-bold text-hover-primary d-block mb-1 fs-6'
                      ></a> */}
                      <span className='badge badge-warning fs-7 fw-semibold'>
                        {tinhchat[el.tinhchat_id-1].name.toUpperCase()}
                      </span>
                    </td>
                    <td>
                      <span className='badge badge-light-primary fs-7 fw-semibold'>
                        {el.trangthai_name.toUpperCase()}
                      </span>
                    </td>
                    <td className='text-center'>
                      <span className='badge badge-primary fs-7 fw-semibold'>{el.SDT==='0' ? 'Chưa có': el.SDT}</span>
                    </td>
                    <td className='text-center'>
                      <span className='badge badge-success fs-7 fw-semibold'>{el.reaction}</span>
                    </td>
                    <td>
                      <span className='badge badge-success fs-7 fw-semibold'>{el.donvi_name}</span>
                    </td>
                    <td className='text-center'> 
                      <span className='badge badge-success fs-7 fw-semibold'>
                        {el.ctnv_name.toUpperCase()}
                      </span>
                    </td>
                    <td className='text-center'>
                      <span
                        className='btn btn-bg-light btn-secondary btn-active-color-primary btn-sm px-4 me-1'
                        onClick={() => {
                          setIfanpage(el)
                          setModelItem(true)
                        }}
                        // style={{border: '1px black dotted'}}
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
                        className='btn btn-icon btn-secondary btn-active-color-primary btn-sm'
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
        title='THÊM FANPAGE MỚI'
      />
      <ModalViewItem
        show={showModelItem}
        handleClose={() => setModelItem(false)}
        // handleLoading={() => setloading(true)}
        ifanpage={ifanpage}
        title='THÔNG TIN CHI TIẾT FANPAGE'
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
