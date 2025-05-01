/* eslint-disable jsx-a11y/anchor-is-valid */
import React, {useState} from 'react'
import {useQuery} from 'react-query'
import {KTSVG, toAbsoluteUrl} from '../../../_metronic/helpers'
import axios from 'axios'
import {individual  , individualResponse} from './individual'
import Avatar from 'react-avatar'
import {ModalViewDoituong} from './ModalViewDoituong'
import clsx from 'clsx'
import {CreateAppModal} from './CreateAppModal'
import {UpdateModal} from './UpdateAppModal'
import {ToastContainer, toast} from 'react-toastify'
import {CreateModelMLH} from './CreateAppModalMLH'

const URL = process.env.REACT_APP_API_URL

type Props = {
  className: string
}

const doituongexample = {
  id: '',
  full_name: '',
  national_id: '',
  citizen_id: '',
  image_url: '',
  date_of_birth: '',
  is_male: false,
  hometown: '',
  additional_info: '',
  phone_number: '',
  is_kol: false,
  created_at: '',
  updated_at: '',
  individual_units: [],
  unit: {id: 0, name: ''},
  task: {id: 0, name: ''},
}

const toolbarButtonMarginClass = 'ms-1 ms-lg-3'

interface IndividualResponse {
  id: string
  full_name: string
  national_id: string | null
  citizen_id: string | null
  image_url: string | null
  date_of_birth: string | null
  is_male: boolean | null
  hometown: string | null
  additional_info: string | null
  phone_number: string | null
  is_kol: boolean
  created_at: string
  updated_at: string
  unit?: {id: string, name: string}
  task?: {id: number, name: string}
}

export type {IndividualResponse}

export const IndividualTable: React.FC<Props> = ({className}) => {
  const [showModal, setShowModal] = useState<boolean>(false)
  const [showModalDoituong, setshowModalDoituong] = useState<boolean>(false)
  const [loading, setLoading] = useState<boolean>(false)
  const [showModalMLH, setShowModalMLH] = useState<boolean>(false)
  const [showModalDoituongupdate, setshowModalDoituongupdate] = useState<boolean>(false)
  const [doituongitem, setdoituongItem] = useState<individualResponse>()
  const [doituongitemupdate, setdoituongItemUpdate] = useState<individualResponse>(doituongexample)
  const [showModalUpdate, setShowModalUpdate] = useState<boolean>(false)
  const [showModalView, setShowModalView] = useState<boolean>(false)
  const [selectedIndividual, setSelectedIndividual] = useState<IndividualResponse | undefined>(undefined)
  const [selectedIndividualUpdate, setSelectedIndividualUpdate] = useState<IndividualResponse | undefined>(undefined)
  const {isLoading, data, error} = useQuery({
    queryKey: 'individuals',
    queryFn: async () => {
      const respone = await axios.get(`${URL}/individuals`)
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
      <div className='card-header border-0 pt-5'>
        <h3 className='card-title align-items-start flex-column'>
          {/* <span className='card-label fw-bold fs-3 mb-1'>
            DANH SÁCH ĐỐI TƯỢNG/KOL TRÊN ĐỊA BÀN{' '}
          </span> */}
          {/* <span className='text-muted mt-1 fw-semibold fs-7'>Over 500 new products</span> */}
        </h3>
        <div className={clsx('d-flex align-items-stretch', toolbarButtonMarginClass)}></div>
        <div className='card-toolbar'>
          <a
            href='#'
            className='btn btn-sm btn-light-primary'
            onClick={() => {
              setShowModal(true)
            }}
          >
            <KTSVG path='/media/icons/duotune/arrows/arr075.svg' className='svg-icon-2' />
            Thêm mới Đối tượng/KOL
          </a>
          <a
            href='#'
            className='btn btn-sm btn-light-primary'
            onClick={() => {
              setShowModalMLH(true)
            }}
            style={{marginLeft: '30px'}}
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
          <table className='table align-middle table-striped gs-0 gy-4'>
            {/* begin::Table head */}
            <thead>
              <tr className='fw-bold fs-6 text-gray-800 border-bottom border-gray-200'>
                <th className='min-w-200px text-center'>THÔNG TIN</th>
                <th className='min-w-100px text-center'>SỐ ĐIỆN THOẠI</th>
                <th className='min-w-150px rounded-start text-center'>QUÊ QUÁN</th>
                <th className='min-w-100px text-center'>GIỚI TÍNH</th>
                <th className='min-w-50px text-center'>KOL</th>
                <th className='min-w-150px text-center'>HÀNH ĐỘNG</th>
              </tr>
            </thead>
            <tbody className='text-gray-600 fw-semibold'>
              {isLoading ? (
                <tr>
                  <td colSpan={7} className='text-center'>
                    Đang tải...
                  </td>
                </tr>
              ) : data && data.length === 0 ? (
                <tr>
                  <td colSpan={7} className='text-center'>
                    Không có dữ liệu
                  </td>
                </tr>
              ) : (
                data.map((el: IndividualResponse, index: number) => (
                  <tr key={el.id}>
                    <td>
                      <div className='d-flex align-items-center'>
                        <div className='symbol symbol-50px me-5'>
                          {el.image_url ? (
                            <img src={el.image_url} className='' alt='' />
                          ) : (
                            <Avatar name={el.full_name.slice(0,20)} round={true} size='50' />
                          )}
                        </div>
                        <div className='d-flex justify-content-start flex-column'>
                          <a href='#' className='text-dark fw-bold text-hover-primary mb-1 fs-6'>
                            {el.full_name.toUpperCase()}
                          </a>
                          <span className='text-muted fw-semibold text-muted d-block fs-7'>
                            {el.citizen_id && el.national_id 
                              ? `CCCD/CMND: ${el.citizen_id}/${el.national_id}`
                              : 'Không có thông tin CCCD/CMND'}
                          </span>
                        </div>
                      </div>
                    </td>
                    <td className='text-center'>
                      {el.phone_number ? (
                        <span className='badge badge-primary fs-7 fw-semibold'>{el.phone_number}</span>
                      ) : (
                        <span className='badge badge-info fs-7 fw-semibold'>Chưa có</span>
                      )}
                    </td>
                    <td className='text-center'>
                      <span className='badge badge-light-success fs-7 fw-semibold'>
                        {el.hometown ? el.hometown.slice(0, 30) : 'Chưa có'}
                      </span>
                    </td>
                    <td className='text-center'>
                      <span className='badge badge-primary fs-7 fw-semibold'>
                        {el.is_male ? 'Nam' : 'Nữ'}
                      </span>
                    </td>
                    <td className='text-center'>
                      {el.is_kol ? (
                        <span className='badge badge-primary fs-7 fw-semibold'>
                          KOL
                        </span>
                      ) : (
                        <span className='badge badge-danger fs-7 fw-semibold'>
                          KHÔNG
                        </span>
                      )}
                    </td>
                    <td>
                      <a
                        href='#'
                        className='btn btn-icon btn-bg-light btn-secondary btn-active-color-primary btn-sm me-1'
                        onClick={() => {
                          setSelectedIndividual(el)
                          setshowModalDoituong(true)
                        }}
                      >
                        <KTSVG path="media/icons/duotune/general/gen036.svg" className="svg-icon-3" />
                      </a>
                      <a
                        href='#'
                        className='btn btn-icon btn-bg-light btn-secondary btn-active-color-primary btn-sm me-1'
                        onClick={() => {
                          setSelectedIndividualUpdate(el)
                          setshowModalDoituongupdate(true)
                        }}
                      >
                        <KTSVG path='/media/icons/duotune/art/art005.svg' className='svg-icon-3' />
                      </a>
                      <a
                        href='#'
                        className='btn btn-icon btn-bg-light btn-secondary btn-active-color-primary btn-sm'
                        onClick={() => {
                          axios
                            .delete(`${URL}/individuals/${el.id}`)
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
                ))
              )}
            </tbody>
            {/* end::Table body */}
          </table>
          <ModalViewDoituong
            show={showModalDoituong}
            handleClose={() => setshowModalDoituong(false)}
            title='THÔNG TIN CHI TIẾT ĐỐI TƯỢNG'
            individual={selectedIndividual}
          />
          {selectedIndividualUpdate && (
            <UpdateModal
              show={showModalDoituongupdate}
              handleClose={() => setshowModalDoituongupdate(false)}
              title='THÔNG TIN CHI TIẾT ĐỐI TƯỢNG'
              individual={selectedIndividualUpdate}
            />
          )}
          <CreateAppModal
            show={showModal}
            handleClose={() => setShowModal(false)}
            title='THÊM MỚI ĐỐI TƯỢNG'
          />
          <CreateModelMLH
            show={showModalMLH}
            handleClose={() => setShowModalMLH(false)}
            handleLoading={() => setLoading(true)}
            title='CẬP NHẬT MỐI LIÊN HỆ GIỮA TÀI KHOẢN FACEBOOK'
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

          {/* end::Table */}
        </div>
        {/* end::Table container */}
      </div>
      {/* begin::Body */}
    </div>
  )
}
export function cutString(string: string, maxLength: number): string {
  if (string != null && string.length > maxLength) {
    string = string.substring(0, maxLength)
  }
  return string
}
