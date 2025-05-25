/* eslint-disable react-hooks/exhaustive-deps */
/* eslint-disable jsx-a11y/anchor-is-valid */
import {useState, useEffect} from 'react'
import {createPortal} from 'react-dom'
import {Modal} from 'react-bootstrap'
import {KTSVG} from '../../../_metronic/helpers'
import Avatar from 'react-avatar'
import {useNavigate} from 'react-router-dom'
import axios from 'axios'
import {account_type} from '../SocialAccount/SocialAccount'
import {Report} from './individual'
import {IndividualResponse} from './Table'

type Props = {
  show: boolean
  handleClose: () => void
  title: string
  individual: IndividualResponse | undefined
}

const PUBLIC_URL = process.env.PUBLIC_URL
const URL = process.env.REACT_APP_API_URL
const modalsRoot = document.getElementById('root-modals') || document.body

export const ModalViewDoituong: React.FC<Props> = ({show, handleClose, title, individual}) => {
  const [data, setData] = useState<any>()
  const navigate = useNavigate()
  const [error, setError] = useState('')
  const typeString = localStorage.getItem('type')
  const type: account_type[] = typeof typeString === 'string' ? JSON.parse(typeString) : []
  useEffect(() => {
    individual && axios
      .get(`${URL}/reports/social-account/${individual?.id}`)
      .then((res) => {
        if (res.data.STATUS === '200') console.log('details' + res.data)
        setData(res.data)
        if (res.data.STATUS === '400') setError('TAI KHOAN DA BI KHOA')
      })
      .catch(() => {})
  }, [individual])
  function findItemById(id: string) {
    return type.find((item:account_type) => item.id === id);
  }
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
      <div className='card mb-5 mb-xl-10'>
        <div className='card-body pt-9 pb-0'>
          <div className='d-flex flex-wrap flex-sm-nowrap mb-3'>
            <div className='me-7 mb-4'>
              <div className='symbol symbol-100px symbol-lg-160px symbol-fixed position-relative'>
                {individual?.image_url ? (
                  <img src={individual.image_url} className='' alt={individual.full_name} />
                ) : (
                  <Avatar name={individual?.full_name} size='100' />
                )}

                <div className='position-absolute translate-middle bottom-0 start-100 mb-6 bg-success rounded-circle border border-4 border-white h-20px w-20px'></div>
              </div>
            </div>

            <div className='flex-grow-1'>
              <div className='d-flex justify-content-between align-items-start flex-wrap mb-2'>
                <div className='d-flex flex-column'>
                  <div className='d-flex align-items-center mb-2'>
                    <a href='#' className='text-gray-800 text-hover-primary fs-2 fw-bolder me-1'>
                      {individual?.full_name.toUpperCase()}
                    </a>
                    <a href='#'>
                      <KTSVG
                        path='/media/icons/duotune/general/gen026.svg'
                        className='svg-icon-1 svg-icon-primary'
                      />
                    </a>
                  </div>

                  <div className='d-flex flex-wrap fw-bold fs-6 mb-4 pe-2'>
                    <a
                      href='#'
                      className='d-flex align-items-center text-gray-400 text-hover-primary me-5 mb-2'
                    >
                      <KTSVG
                        path='/media/icons/duotune/communication/com006.svg'
                        className='svg-icon-4 me-1'
                      />
                      {individual?.is_kol ? 'KOL' : 'KHÔNG PHẢI KOL'}
                    </a>
                    <a
                      href='#'
                      className='d-flex align-items-center text-gray-400 text-hover-primary me-5 mb-2'
                    >
                      <KTSVG
                        path='/media/icons/duotune/general/gen018.svg'
                        className='svg-icon-4 me-1'
                      />
                      {individual?.hometown || 'N/A'}
                    </a>
                    <a
                      href='#'
                      className='d-flex align-items-center text-gray-400 text-hover-primary mb-2'
                    >
                      <KTSVG
                        path='/media/icons/duotune/communication/com011.svg'
                        className='svg-icon-4 me-1'
                      />
                     {individual?.phone_number}
                    </a>
                  </div>
                </div>
                  <div className='card-toolbar' style={{marginLeft: 'auto'}}>
                    <button
                        type='button'
                        className='btn btn-sm btn-secondary'
                        onClick={(e) => {
                          navigate(`${PUBLIC_URL}/reports/individuals/${individual?.id}`)
                        }}
                        style={{marginRight: '10px'}}
                      >
                        Mở Trích tin
                      </button>
                      <button type='button' className='btn btn-sm btn-secondary'>
                        Mở hồ sơ chi tiết
                      </button>
                    </div>
              </div>

              <div className='d-flex flex-wrap flex-stack'>
                <div className='d-flex flex-column flex-grow-1 pe-8'>
                  <div className='d-flex flex-wrap'>
                    <div className='border border-gray-300 border-dashed rounded min-w-125px py-3 px-4 me-6 mb-3'>
                      <div className='d-flex align-items-center'>
                        <KTSVG
                          path='/media/icons/duotune/arrows/arr066.svg'
                          className='svg-icon-3 svg-icon-success me-2'
                        />
                        <div className='fs-2 fw-bolder'>
                          {individual ? individual.national_id : ''}
                        </div>
                      </div>

                      <div className='fw-bold fs-6 text-gray-400'>Hội nhóm</div>
                    </div>

                    <div className='border border-gray-300 border-dashed rounded min-w-125px py-3 px-4 me-6 mb-3'>
                      <div className='d-flex align-items-center'>
                        <KTSVG
                          path='/media/icons/duotune/arrows/arr065.svg'
                          className='svg-icon-3 svg-icon-danger me-2'
                        />
                        <div className='fs-2 fw-bolder'>
                          {data?.length}
                        </div>
                      </div>

                      <div className='fw-bold fs-6 text-gray-400'>Trích tin</div>
                    </div>

                    <div className='border border-gray-300 border-dashed rounded min-w-125px py-3 px-4 me-6 mb-3'>
                      <div className='d-flex align-items-center'>
                        <KTSVG
                          path='/media/icons/duotune/arrows/arr066.svg'
                          className='svg-icon-3 svg-icon-success me-2'
                        />
                        <div className='fs-4 fw-bolder'>{individual?.updated_at.split('T')[0]}</div>
                      </div>

                      <div className='fw-bold fs-6 text-gray-400'>Cập nhật cuối</div>
                    </div>
                  </div>
                </div>

                <div className='card card-flush card-px-0 card-border'>
                  <div className='card-header'>
                    <h4 className='fs-4 fw-bolder card-title'>THÔNG TIN ĐỐI TƯỢNG</h4>
                  <span className='card-body py-1 fs-5'>{individual?.additional_info}</span>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        {/* <span className='badge badge-light mb-8'> HỘI NHÓM ĐỐI TƯỢNG LIÊN QUAN</span> */}
        <div className='separator my-10'></div>
        <div className='modal-body'>
        <table className='table align-middle '>
          {/* begin::Table head */}
          <thead>
            <tr className='fw-bold text-muted bg-light'>
              <th className='min-w-40px text-center'>STT</th>
              <th className='ps-4 min-w-200px rounded-start'>NGƯỜI CẬP NHẬT</th>
              <th className='min-w-100px'>THỜI GIAN</th>
              <th className='min-w-300px'>NỘI DUNG</th>
              <th className='min-w-100px'>ĐÁNH GIÁ</th>
            </tr>
          </thead>
          {/* end::Table head */}
          {/* begin::Table body */}
          <tbody>
            {data && data.map((report: Report, index: number) =>
              <tr key={index}>
                <td>
                  <span className='text-muted fw-semibold text-muted d-block fs-7 text-center'>{index+1}</span>
                </td>
                <td>
                  <div className='d-flex align-items-center'>
                    <div className='d-flex justify-content-start flex-column'>
                      <span className='text-dark text-hover-primary mb-1 fs-6'>
                        {report.user?.name || 'Không xác định'}
                      </span>
                    </div>
                  </div>
                </td>
                <td>
                  <span className='text-muted fw-semibold text-muted d-block fs-7'>
                    {new Date(report.updated_at).toLocaleString()}
                  </span>
                </td>
                <td>
                  <div className='d-flex flex-column'>
                    <div className='text-wrap text-break' style={{
                      maxWidth: '300px',
                      overflow: 'hidden',
                      textOverflow: 'ellipsis',
                      display: '-webkit-box',
                      WebkitLineClamp: 2,
                      WebkitBoxOrient: 'vertical',
                      fontSize: '0.9rem',
                      lineHeight: '1.4'
                    }}>
                      {report.content_note || report.comment || 'Không có nội dung'}
                    </div>
                  </div>
                </td>
                <td>
                  <div className='d-flex flex-column'>
                    <div className='text-wrap text-break' style={{
                      maxWidth: '300px',
                      overflow: 'hidden',
                      textOverflow: 'ellipsis',
                      display: '-webkit-box',
                      WebkitLineClamp: 2,
                      WebkitBoxOrient: 'vertical',
                      fontSize: '0.9rem',
                      lineHeight: '1.4'
                    }}>
                      {report.action || 'Chưa có nội dung'}
                    </div>
                  </div>
                </td>
                {/* <td>
                  <span className='badge badge-light-primary fs-7 fw-semibold'>
                    {report.action || 'Không có hành động'}
                  </span>
                </td> */}
              </tr>
            )}
          </tbody>
          {/* end::Table body */}
        </table>
      </div>
      </div>
    </Modal>,
    modalsRoot
  )
}
