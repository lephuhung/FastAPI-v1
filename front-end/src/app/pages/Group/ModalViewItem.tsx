/* eslint-disable react-hooks/exhaustive-deps */
/* eslint-disable jsx-a11y/anchor-is-valid */
import { useState, useEffect } from 'react'
import { createPortal } from 'react-dom'
import { Modal } from 'react-bootstrap'
import { KTSVG } from '../../../_metronic/helpers'
import axios from 'axios'
import { useQuery } from 'react-query'
import {useNavigate} from 'react-router-dom'
import Avatar from 'react-avatar'
import { IGroup,IResponseGroup } from './Group';
type Props = {
  show: boolean
  handleClose: () => void
  title: string,
  igroup?: IResponseGroup
}

const PUBLIC_URL = process.env.PUBLIC_URL
const URL = process.env.REACT_APP_API_URL
const modalsRoot = document.getElementById('root-modals') || document.body

const ModalViewItem = ({ show, handleClose, title, igroup }: Props) => {
  const [data, setData] = useState<any>();
  const [error, setError]=useState('');
  const navigate = useNavigate()
  useEffect(() => {
    axios.get(`${URL}/uid/get-history/${igroup?.uid}`, )
      .then((res) => {
        if (res.data.STATUS === '200')
        console.log(res.data)
          setData(res.data)
        if (res.data.STATUS === '400')
          setError('TAI KHOAN DA BI KHOA');
      })
      .catch(() => { });
  }, [igroup])

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
        {error===''? <span>{error}</span>:<></>}
        {/* begin::Close */}
        <div className='btn btn-sm btn-icon btn-active-color-primary' onClick={handleClose}>
          <KTSVG className='svg-icon-1' path='/media/icons/duotune/arrows/arr061.svg' />
        </div>
        {/* end::Close */}
      </div>
      {/* Start profile */}
      { igroup && <div className='card'>
        <div className='card-body pt-9 pb-0'>
          <div className='d-flex flex-wrap flex-sm-nowrap mb-3'>
            <div className='me-7 mb-4'>
              <div className='symbol symbol-100px symbol-lg-160px symbol-fixed position-relative'>
                  <Avatar name={igroup?.name} size='100' />
                <div className='position-absolute translate-middle bottom-0 start-100 mb-6 bg-success rounded-circle border border-4 border-white h-20px w-20px'></div>
              </div>
            </div>

            <div className='flex-grow-1'>
              <div className='d-flex justify-content-between align-items-start flex-wrap mb-2'>
                <div className='d-flex flex-column'>
                  <div className='d-flex align-items-center mb-2'>
                    <a href='#' className='text-gray-800 text-hover-primary fs-2 fw-bolder me-1'>
                      {igroup?.name}
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
                      {igroup?.Vaiao ? 'VAI AO' : 'KHÔNG VAI ẢO'}
                    </a>
                    <a
                      href='#'
                      className='d-flex align-items-center text-gray-400 text-hover-primary me-5 mb-2'
                    >
                      <KTSVG
                        path='/media/icons/duotune/general/gen018.svg'
                        className='svg-icon-4 me-1'
                      />
                      {igroup?.status_name}
                    </a>
                    <a
                      href='#'
                      className='d-flex align-items-center text-gray-400 text-hover-primary mb-2'
                    >
                      <KTSVG
                        path='/media/icons/duotune/communication/com011.svg'
                        className='svg-icon-4 me-1'
                      />
                      {`SĐT: ${igroup?.phone_number}`}
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
                         {data.length}
                        </div>
                      </div>

                      <div className='fw-bold fs-6 text-gray-400'>Lần cập nhật</div>
                    </div>

                    <div className='border border-gray-300 border-dashed rounded min-w-125px py-3 px-4 me-6 mb-3'>
                      <div className='d-flex align-items-center'>
                        <KTSVG
                          path='/media/icons/duotune/arrows/arr066.svg'
                          className='svg-icon-3 svg-icon-primary me-2'
                        />
                        <div className='fs-2 fw-bolder'>
                          0
                        </div>
                      </div>

                      <div className='fw-bold fs-6 text-gray-400'>Trích tin</div>
                    </div>
                    <div className='border border-gray-300 border-dashed rounded min-w-125px py-3 px-4 me-6 mb-3'>
                      <div className='d-flex align-items-center'>
                        <KTSVG
                          path='/media/icons/duotune/arrows/arr066.svg'
                          className='svg-icon-3 svg-icon-primary me-2'
                        />
                        <div className='fs-2 fw-bolder'>
                          {igroup.task_name}
                        </div>
                      </div>

                      <div className='fw-bold fs-6 text-gray-400'>{`Đơn vị: ${igroup.unit_name}`}</div>
                    </div>
                    <div className='border border-gray-300 border-dashed rounded min-w-125px py-3 px-4 me-6 mb-3'>
                      <div className='d-flex align-items-center'>
                        <KTSVG
                          path='/media/icons/duotune/arrows/arr066.svg'
                          className='svg-icon-3 svg-icon-success me-2'
                        />
                        <div className='fs-4 fw-bolder'>{igroup? igroup?.updated_at.split(' ')[0]: 'Chưa rõ'}</div>
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
                          navigate(`${PUBLIC_URL}/trichtin/${igroup.uid}`)
                        }}
                        style={{marginRight: '10px'}}
                      >
                        Mở Trích tin
                      </button>
                      <button type='button' className='btn btn-sm btn-light'>
                        Mở hồ sơ chi tiết
                      </button>
                    </div>
                  </div>
                  <div className='card-body py-5 fs-4'>{igroup?.note ===''? 'Không có dữ liệu': igroup?.note}</div>
                </div>
              </div>
            </div>
          </div>
          <div className="separator my-10"></div>
        <h3>LỊCH SỬ THAY ĐỔI</h3>
        </div>
        </div>
        }
        {/* End profile */}
      <div className='modal-body'>
        <table className='table align-middle '>
          {/* begin::Table head */}
          <thead>
            <tr className='fw-bold text-muted bg-light'>
              <th className='min-w-40px text-center'>STT</th>
              <th className='ps-4 min-w-200px rounded-start'>UID</th>
              <th className='min-w-100px'>BẠN BÈ</th>
              <th className='min-w-300px'>GHI CHÚ</th>
            </tr>
          </thead>
          {/* end::Table head */}
          {/* begin::Table body */}
          <tbody>
            {data && data.map((el: IResponseGroup, index: number) =>
              <tr key={index}>
                <td>
                  <span className='text-muted fw-semibold text-muted d-block fs-7 text-center'>{index+1}</span>
                </td>
                <td>
                  <div className='d-flex align-items-center'>
                    <div className='d-flex justify-content-start flex-column'>
                      <a href='#' className='text-dark fw-bold text-hover-primary mb-1 fs-6'>
                        {el.name}
                      </a>
                      <span className='text-muted fw-semibold text-muted d-block fs-7'>
                        {el.updated_at.split('.')[0]}
                      </span>
                    </div>
                  </div>
                </td>
                <td>
                  <span className='badge badge-light-primary fs-7 fw-semibold'>{el.reaction}</span>
                </td>
                <td>
                  <span className='text-muted fw-semibold text-muted d-block fs-7' style={{whiteSpace:'pre-wrap'}}>{el.note}</span>
                </td>
              </tr>
            )}
          </tbody>
          {/* end::Table body */}
        </table>
      </div>
    </Modal>,
    modalsRoot
  )
}

export { ModalViewItem }
