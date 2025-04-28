/* eslint-disable react-hooks/exhaustive-deps */
/* eslint-disable jsx-a11y/anchor-is-valid */
import {useState, useEffect} from 'react'
import {createPortal} from 'react-dom'
import {Modal} from 'react-bootstrap'
import {KTSVG} from '../../../_metronic/helpers'
import Avatar from 'react-avatar'
import {useNavigate} from 'react-router-dom'
import axios from 'axios'
import { type } from '../Facebook/IFacebook'
import {individualResponse} from './individual'
type Props = {
  show: boolean
  handleClose: () => void
  title: string
  individual?: individualResponse
}
const PUBLIC_URL = process.env.PUBLIC_URL
const URL = process.env.REACT_APP_API_URL
const modalsRoot = document.getElementById('root-modals') || document.body

const ModalViewIndividual: React.FC<Props> = ({show, handleClose, title, individual}) => {
  const [data, setData] = useState<any>()
  const navigate = useNavigate()
  const [error, setError] = useState('')
  const typeString = localStorage.getItem('account_type')
  const type: type[] = typeof typeString === 'string' ? JSON.parse(typeString) : []
  useEffect(() => {
    individual && axios
      .get(`${URL}/individuals/${individual?.id}`)
      .then((res) => {
        if (res.data.STATUS === '200') console.log('details' + res.data)
        setData(res.data)
        if (res.data.STATUS === '400') setError('TAI KHOAN DA BI KHOA')
      })
      .catch(() => {})
  }, [individual])
  function findItemById(id: string) {
    return type.find((item:type) => item.id === id);
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
                  <img src={individual.image_url} className='' alt='' />
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
                      {individual?.is_kol ? 'is_kol' : 'KHÔNG PHẢI is_kol'}
                    </a>
                    <a
                      href='#'
                      className='d-flex align-items-center text-gray-400 text-hover-primary me-5 mb-2'
                    >
                      <KTSVG
                        path='/media/icons/duotune/general/gen018.svg'
                        className='svg-icon-4 me-1'
                      />
                      {individual?.hometown}
                    </a>
                    <a
                      href='#'
                      className='d-flex align-items-center text-gray-400 text-hover-primary mb-2'
                    >
                      <KTSVG
                        path='/media/icons/duotune/communication/com011.svg'
                        className='svg-icon-4 me-1'
                      />
                      {`LOẠI KOLS: ${individual?.phone_number? individual.phone_number:'KHÔNG PHÂN LOẠI'}`}
                    </a>
                  </div>
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
                          {data ? data.hoinhom_details.length : '0'}
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
                          {data ? data.trichtin_count[0].count : '0'}
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
                        <div className='fs-4 fw-bolder'>{individual?.updated_at.split('.')[0]}</div>
                      </div>

                      <div className='fw-bold fs-6 text-gray-400'>Cập nhật cuối</div>
                    </div>
                  </div>
                </div>

                <div className='card card-flush card-px-0 card-border'>
                  <div className='card-header'>
                    <h3 className='fs-4 fw-bolder card-title'>THÔNG TIN ĐỐI TƯỢNG</h3>
                    <div className='card-toolbar'>
                      <button
                        type='button'
                        className='btn btn-sm btn-light'
                        onClick={(e) => {
                          navigate(`${PUBLIC_URL}/trichtin/${individual?.id}`)
                        }}
                        style={{marginRight: '10px'}}
                      >
                        Mở Trích tin
                      </button>
                      <button
                        type='button'
                        className='btn btn-sm btn-light'
                        onClick={(e) => {
                          navigate(`${PUBLIC_URL}/individual/details/${individual?.id}`)
                        }}
                      >
                        Mở hồ sơ chi tiết
                      </button>
                    </div>
                  </div>
                  <div className='card-body py-1 fs-5'>{individual?.additional_info}</div>
                </div>
              </div>
            </div>
          </div>
        </div>
        {/* <span className='badge badge-light mb-8'> HỘI NHÓM ĐỐI TƯỢNG LIÊN QUAN</span> */}
        <div className='separator my-10'></div>
        <div className='modal-body py-lg-10 px-lg-10'>
          <table className='table align-middle table-striped gs-0 gy-4'>
            {/* begin::Table head  */}
            <thead>
              <tr className='fw-bold text-muted'>
                <th className='min-w-40px text-center'>STT</th>
                <th className='ps-4 min-w-100px rounded-start'>HỘI NHÓM</th>
                <th className='min-w-100px'>MỐI LIÊN QUAN ĐỐI TƯỢNG</th>
                <th className='min-w-100px'>LOẠI TÀI KHOẢN</th>
              </tr>
            </thead>
            <tbody>
              {data &&
                data.hoinhom_details.map((el: any, index: number) => (
                  <tr key={index}>
                    <td>
                      <span className='text-muted fw-semibold text-muted d-block fs-7 text-center'>
                        {index}
                      </span>
                    </td>
                    <td>
                      <div className='d-flex align-items-center'>
                        <div className='d-flex justify-content-start flex-column'>
                          <a href='#' className='text-dark fw-bold text-hover-primary mb-1 fs-6'>
                            {el.uid_name}
                          </a>
                          <span className='text-muted fw-semibold text-muted d-block fs-7'>
                            {`UID: ${el.uid}`}
                          </span>
                        </div>
                      </div>
                    </td>
                    <td>
                      <span className='badge badge-primary fs-7 fw-semibold'>
                        {el.relationship_name.toUpperCase()}
                      </span>
                    </td>
                    <td>
                      <span className='badge badge-success fs-7 fw-semibold'>
                        {findItemById(el.account_type_id)?.name.toUpperCase()}
                      </span>
                    </td>
                  </tr>
                ))}
            </tbody>
            {/* end::Table body */}
          </table>
          <div className='separator my-10'></div>
          <span className='text-muted fw-semibold text-muted d-block fs-7 mb-8'>
            {' '}
            TRÍCH TIN GẦN ĐÂY
          </span>
          <div className='row g-5'>
            {data &&
              data.trichtin_details.map((el: any, index: number) => (
                <div className='col-lg-6' key={index}>
                  <div className='card card-custom card-stretch shadow mb-5'>
                    <div className='card-header'>
                      <h5 className='card-title'>{`Trích tin ngày: ${
                        el.updated_at.split('T')[0]
                      }`}</h5>
                    </div>
                    <div className='card-body'>{el.ghichu_noidung}</div>
                    <div className='card-footer'>{`UID VAI ẢO: ${el.uid_vaiao}`}</div>
                  </div>
                </div>
              ))}
          </div>
        </div>
      </div>
    </Modal>,
    modalsRoot
  )
}

export {ModalViewIndividual}
