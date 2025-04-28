/* eslint-disable react-hooks/exhaustive-deps */
/* eslint-disable jsx-a11y/anchor-is-valid */
import {useState, useEffect} from 'react'
import {createPortal} from 'react-dom'
import {Modal} from 'react-bootstrap'
import {KTSVG, toAbsoluteUrl} from '../../../_metronic/helpers'
import Avatar from 'react-avatar'
import {useNavigate} from 'react-router-dom'
import axios from 'axios'
import {useQuery} from '@tanstack/react-query'
import {trichtin} from './trichtin'
type Props = {
  show: boolean
  handleClose: () => void
  title: string
  trichtin?: trichtin
}
const PUBLIC_URL = process.env.PUBLIC_URL
const URL = process.env.REACT_APP_API_URL
const modalsRoot = document.getElementById('root-modals') || document.body

const ModalViewItemTrichtin: React.FC<Props> = ({show, handleClose, title, trichtin}) => {
  const [data, setData] = useState<any>()
  const navigate = useNavigate()
  const [error, setError] = useState('')
  const type = ['Nhóm Facebook', 'Tài khoản Facebook cá nhân', 'Trang Facebook']
  useEffect(() => {
    // axios
    //   .get(`${URL}/individual/details/${individual?.id}`)
    //   .then((res) => {
    //     if (res.data.STATUS === '200') console.log('details' + res.data)
    //     setData(res.data)
    //     if (res.data.STATUS === '400') setError('TAI KHOAN DA BI KHOA')
    //   })
    // .catch(() => {})
  }, [])
  return createPortal(
    <Modal
      id='kt_modal_create_app'
      tabIndex={-1}
      aria-hidden='true'
      dialogClassName='modal-dialog modal-dialog-centered mw-900px'
      show={show}
      onHide={handleClose}
    >
      <div className='modal-header'>
        <h2>{title}</h2>
        {error === '' ? <span>{error}</span> : <></>}
        {/* begin::Close */}
        <div className='btn btn-sm btn-icon btn-active-color-primary' onClick={handleClose}>
          <KTSVG className='svg-icon-1' path='/media/icons/duotune/arrows/arr061.svg' />
        </div>
        {/* end::Close */}
      </div>
      <div className='card'>
        {/* begin::Body */}
        <div className='card-body pb-0'>
          {/* begin::Header */}
          <div className='d-flex align-items-center mb-3'>
            {/* begin::User */}
            <div className='d-flex align-items-center flex-grow-1'>
              {/* begin::Avatar */}
              <div className='symbol symbol-45px me-5'>
                <img src={toAbsoluteUrl('/media/avatars/300-21.jpg')} alt='' />
              </div>
              {/* end::Avatar */}

              {/* begin::Info */}
              <div className='d-flex flex-column'>
                <a href='#' className='text-gray-800 text-hover-primary fs-6 fw-bold'>
                  {trichtin?.user}
                </a>
                <span className='text-gray-400 fw-semibold'>{trichtin?.updated_at}</span>
              </div>
              {/* end::Info */}
            </div>
            {/* end::User */}

            {/* begin::Menu */}
            <div className='my-0'>
            </div>
            {/* end::Menu */}
          </div>
          {/* end::Header */}

          {/* begin::Post */}
          <div className='mb-7'>
            {/* begin::Text */}
            <div className='text-gray-800 mb-5'>
              {trichtin?.ghichu_noidung}
            </div>
            {/* end::Text */}

            {/* begin::Toolbar */}
            <div className='d-flex align-items-center mb-5'>
              <a
                href='#'
                className='btn btn-sm btn-light btn-color-muted btn-active-light-success px-4 py-2 me-4'
              >
                <KTSVG
                  path='/media/icons/duotune/communication/com012.svg'
                  className='svg-icon-2'
                />
                {`Vai ảo: ${trichtin?.uid_vaiao}`} 
              </a>

              <a
                href='#'
                className='btn btn-sm btn-light btn-color-muted btn-active-light-danger px-4 py-2'
              >
                <KTSVG path='/media/icons/duotune/general/gen030.svg' className='svg-icon-2' />
                {`UID được trích tin: ${trichtin?.uid}|${trichtin?.hoinhom_name}`}
              </a>
            </div>
            {/* end::Toolbar */}
          </div>
          {/* end::Post */}

          {/* begin::Replies */}
          <div className='mb-7 ps-10'>
            {/* begin::Reply */}
            <div className='d-flex mb-5'>
              {/* begin::Avatar */}
              <div className='symbol symbol-45px me-5'>
                <img src={toAbsoluteUrl('/media/avatars/300-14.jpg')} alt='' />
              </div>
              {/* end::Avatar */}

              {/* begin::Info */}
              <div className='d-flex flex-column flex-row-fluid'>
                {/* begin::Info */}
                <div className='d-flex align-items-center flex-wrap mb-1'>
                  <a href='#' className='text-gray-800 text-hover-primary fw-bold me-2'>
                    Nhận xét
                  </a>
                </div>
                {/* end::Info */}

                {/* begin::Post */}
                <span className='text-gray-800 fs-7 fw-normal pt-1'>
                  {trichtin?.nhanxet}
                </span>
                {/* end::Post */}
              </div>
              {/* end::Info */}
            </div>
            {/* end::Reply */}

            {/* begin::Reply */}
            <div className='d-flex'>
              {/* begin::Avatar */}
              <div className='symbol symbol-45px me-5'>
                <img src={toAbsoluteUrl('/media/avatars/300-9.jpg')} alt='' />
              </div>
              {/* end::Avatar */}

              {/* begin::Info */}
              <div className='d-flex flex-column flex-row-fluid'>
                {/* begin::Info */}
                <div className='d-flex align-items-center flex-wrap mb-1'>
                  <a href='#' className='text-gray-800 text-hover-primary fw-bold me-2'>
                    Đề xuất
                  </a>
                </div>
                {/* end::Info */}

                {/* begin::Post */}
                <span className='text-gray-800 fs-7 fw-normal pt-1'>
                  {trichtin?.xuly}
                </span>
                {/* end::Post */}
              </div>
              {/* end::Info */}
            </div>
            {/* end::Reply */}
          </div>
        </div>
      </div>
    </Modal>,
    modalsRoot
  )
}

export {ModalViewItemTrichtin}
