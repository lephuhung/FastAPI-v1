/* eslint-disable react-hooks/exhaustive-deps */
/* eslint-disable jsx-a11y/anchor-is-valid */
import { useState, useEffect } from 'react'
import { createPortal } from 'react-dom'
import { Modal } from 'react-bootstrap'
import { KTSVG } from '../../../_metronic/helpers'
import axios from 'axios'
import { useQuery } from 'react-query'
import Avatar from 'react-avatar'
import {useNavigate} from 'react-router-dom'
import { SocialAccountResponse } from './SocialAccount';
import { account_type, SocialAccountModal, status, unit, task, characteristics } from './SocialAccount'
type Report = {
  id: number;
  social_account_uid: string;
  content_note: string;
  comment: string;
  action: string;
  linked_social_account_uid: string;
  created_at: string;
  updated_at: string;
  user: {
    id: string;
    name: string;
  } | null;
}

type Props = {
  show: boolean
  handleClose: () => void
  title: string,
  item?: SocialAccountResponse
}

const PUBLIC_URL = process.env.PUBLIC_URL
const URL = process.env.REACT_APP_API_URL
const modalsRoot = document.getElementById('root-modals') || document.body

const ModalViewItem = ({ show, handleClose, title, item }: Props) => {
  const navigate = useNavigate()
  const [data, setData] = useState<Report[]>([]);
  const [error, setError]=useState('');
  const unitsString = localStorage.getItem('units')
  const units: unit[] = typeof unitsString === 'string' ? JSON.parse(unitsString) : []
  const account_typeString = localStorage.getItem('account_types')
  const account_type: account_type[] = typeof account_typeString === 'string' ? JSON.parse(account_typeString) : []
  const characteristicsString = localStorage.getItem('characteristics')
  const characteristics: characteristics[] = typeof characteristicsString === 'string' ? JSON.parse(characteristicsString) : []
  const tasksString = localStorage.getItem('tasks')
  const tasks: task[] = typeof tasksString === 'string' ? JSON.parse(tasksString) : []
  const statusString = localStorage.getItem('statuses')
  const status: status[] = typeof statusString === 'string' ? JSON.parse(statusString) : []
  useEffect(() => {
    if (item?.uid) {
      console.log('Fetching reports for UID:', item.uid);
      axios.get(`${URL}/reports/social-account/${item.uid}`)
        .then((res) => {
          console.log('Reports response:', res.data);
          setData(res.data)
        })
        .catch((err) => {
          console.error('Error details:', {
            message: err.message,
            response: err.response?.data,
            status: err.response?.status
          });
          // setError('Không thể tải dữ liệu báo cáo');
        });
    }
  }, [item])

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
        {error ? <span className='text-danger'>{error}</span> : null}
        {/* begin::Close */}
        <div className='btn btn-sm btn-icon btn-active-color-primary' onClick={handleClose}>
          <KTSVG className='svg-icon-1' path='/media/icons/duotune/arrows/arr061.svg' />
        </div>
        {/* end::Close */}
      </div>
      {/* Start profile */}
      { item && <div className='card'>
        <div className='card-body pt-9 pb-0'>
          <div className='d-flex flex-wrap flex-sm-nowrap mb-3'>
            <div className='me-7 mb-4'>
              <div className='symbol symbol-100px symbol-lg-160px symbol-fixed position-relative'>
                  <Avatar name={item?.name} size='100' />
                <div className='position-absolute translate-middle bottom-0 start-100 mb-6 bg-success rounded-circle border border-4 border-white h-20px w-20px'></div>
              </div>
            </div>

            <div className='flex-grow-1'>
              <div className='d-flex justify-content-between align-items-start flex-wrap mb-2'>
                <div className='d-flex flex-column'>
                  <div className='d-flex align-items-center mb-2'>
                    <a href='#' className='text-gray-800 text-hover-primary fs-2 fw-bolder me-1'>
                      {item?.name}
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
                      {item?.is_active ? 'KÍCH HOẠT' : 'KHÔNG KÍCH HOẠT'}
                    </a>
                    <a
                      href='#'
                      className='d-flex align-items-center text-gray-400 text-hover-primary me-5 mb-2'
                    >
                      <KTSVG
                        path='/media/icons/duotune/general/gen018.svg'
                        className='svg-icon-4 me-1'
                      />
                      {item?.status_id}
                    </a>
                    <a
                      href='#'
                      className='d-flex align-items-center text-gray-400 text-hover-primary mb-2'
                    >
                      <KTSVG
                        path='/media/icons/duotune/communication/com011.svg'
                        className='svg-icon-4 me-1'
                      />
                      {`SĐT: ${item?.phone_number}`}
                    </a>
                  </div>
                </div>
                  <div className='card-toolbar' style={{marginLeft: 'auto'}}>
                    <button
                        type='button'
                        className='btn btn-sm btn-secondary'
                        onClick={(e) => {
                          navigate(`${PUBLIC_URL}/reports/social-account/${item?.uid}`)
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
                          {item?.task?.name}
                        </div>
                      </div>

                      <div className='fw-bold fs-6 text-gray-400'>{`Đơn vị: ${item?.unit?.name}`}</div>
                    </div>
                    <div className='border border-gray-300 border-dashed rounded min-w-125px py-3 px-4 me-6 mb-3'>
                      <div className='d-flex align-items-center'>
                        <KTSVG
                          path='/media/icons/duotune/arrows/arr066.svg'
                          className='svg-icon-3 svg-icon-success me-2'
                        />
                        <div className='fs-4 fw-bolder'>{item? item?.updated_at.split('T')[0]: 'Chưa rõ'}</div>
                      </div>

                      <div className='fw-bold fs-6 text-gray-400'>Cập nhật cuối</div>
                    </div>
                  </div>
                </div>

                {/* <div className='card card-flush card-px-0 card-border'> */}
                  <div className='py-5 fs-4' style={{
                    fontSize: '0.8rem',
                    border: '1px solid #e4e6ef',
                    borderRadius: '0.475rem',
                    backgroundColor: '#f8f9fa',
                    padding: '1rem',
                    marginTop: '1rem',
                    lineHeight: '1.5',
                    color: '#5E6278'
                  }}>
                    {item?.note ===''? 'Không có dữ liệu': item?.note}
                  </div>
                {/* </div> */}
              </div>
            </div>
          </div>
        <h3>DANH SÁCH TRÍCH TIN</h3>
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
    </Modal>,
    modalsRoot
  )
}

export { ModalViewItem }
