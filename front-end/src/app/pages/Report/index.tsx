import React, {FC, useState} from 'react'
import Avatar from 'react-avatar'
import {KTSVG} from '../../../_metronic/helpers'
import {useIntl} from 'react-intl'
import {useQuery, useMutation, useQueryClient} from 'react-query'
import axios from 'axios'
import {CreateAppModal} from './CreateAppModal'
import {useParams} from 'react-router-dom'
import {report} from './reports'
import { PageTitle } from '../../../_metronic/layout/core'
import {ToastContainer, toast} from 'react-toastify'
// import {ModalViewItemVaiao} from './ModalViewItemVaiao'
import {ModalViewAddrReport} from './ModalViewAddrReport'

const URL = process.env.REACT_APP_API_URL

const Trichtin: FC<{id: string}> = ({id}) => {
  const [showModal, setShowModal] = useState<boolean>(false)
  const [showModalDoituong, setshowModalDoituong] = useState<boolean>(false)
  const [selectedReport, setSelectedReport] = useState<report | undefined>(undefined)
  const queryClient = useQueryClient()

  const {isLoading, data, error} = useQuery<report[]>({
    queryKey: ['reports', id],
    queryFn: () =>
      axios.get(`${URL}/reports/social-account/${id}`).then((res) => res.data),
    enabled: !!id
  })

  const deleteMutation = useMutation({
    mutationFn: (reportId: number) => 
      axios.delete(`${URL}/reports/${reportId}`),
    onSuccess: () => {
      queryClient.invalidateQueries({queryKey: ['reports', id]})
      toast.success('Xóa trích tin thành công')
    },
    onError: () => {
      toast.error('Có lỗi xảy ra khi xóa trích tin')
    }
  })

  const handleDelete = (reportId: number) => {
    if (window.confirm('Bạn có chắc chắn muốn xóa trích tin này?')) {
      deleteMutation.mutate(reportId)
    }
  }

  if (isLoading) {
    return <div>Loading...</div>
  }

  if (error) {
    return <div>Error loading reports</div>
  }

  return (
    <div className={'card mb-5 mb-xl-8'}>
      {/* begin::Header */}
      <div className='card-header border-0 pt-5'>
        <h3 className='card-title align-items-start flex-column'>
          <span className='card-label fw-bold fs-3 mb-1'>{`DANH SÁCH TRÍCH TIN ID: ${id}`}</span>
        </h3>
        <div className='card-toolbar'>
          <a
            href='#'
            className='btn btn-sm btn-light-primary'
            onClick={() => {
              setShowModal(true)
            }}
          >
            <KTSVG path='/media/icons/duotune/arrows/arr075.svg' className='svg-icon-2' />
            Thêm mới trích tin
          </a>
        </div>
      </div>
      {/* end::Header */}
      {/* begin::Body */}
      <div className='card-body py-3'>
        {/* begin::Table container */}
        <div className='table-responsive'>
          <table className='table align-middle table-row-dashed fs-6 gy-5'>
            <thead>
              <tr className='text-start text-muted fw-bold fs-7 text-uppercase gs-0'>
                <th className='min-w-50px'>STT</th>
                <th className='min-w-125px'>Người cập nhật</th>
                <th className='min-w-125px'>Thời gian</th>
                <th className='min-w-300px'>Nội dung</th>
                <th className='min-w-200px'>Hành động</th>
              </tr>
            </thead>
            <tbody className='text-gray-600 fw-semibold'>
              {data?.map((report, index) => (
                <tr key={report.id}>
                  <td>{index + 1}</td>
                  <td>{report.user?.name || 'Không xác định'}</td>
                  <td>{new Date(report.updated_at).toLocaleString()}</td>
                  <td>
                    <div className='d-flex flex-column'>
                      <div className='text-wrap text-break' style={{
                        maxWidth: '300px',
                        overflow: 'hidden',
                        textOverflow: 'ellipsis',
                        display: '-webkit-box',
                        WebkitLineClamp: 2,
                        WebkitBoxOrient: 'vertical'
                      }}>
                        {report.content_note || report.comment || 'Không có nội dung'}
                      </div>
                    </div>
                  </td>
                  <td>
                    <div className='d-flex flex-column'>
                      <div className='text-wrap text-break' style={{maxWidth: '200px'}}>
                        <div className='d-flex gap-2'>
                          <button
                            className='btn btn-sm btn-light-primary'
                            onClick={() => {
                              setSelectedReport(report)
                              setshowModalDoituong(true)
                            }}
                          >
                            <KTSVG path='/media/icons/duotune/general/gen055.svg' className='svg-icon-2' />
                            Hiển thị
                          </button>
                          <button
                            className='btn btn-sm btn-light-danger'
                            onClick={() => handleDelete(report.id)}
                          >
                            <KTSVG path='/media/icons/duotune/general/gen027.svg' className='svg-icon-2' />
                            Xóa
                          </button>
                        </div>
                      </div>
                    </div>
                  </td>
                </tr>
              ))}
              {(!data || data.length === 0) && (
                <tr>
                  <td colSpan={5} className='text-center'>
                    Không có dữ liệu trích tin
                  </td>
                </tr>
              )}
            </tbody>
          </table>
          <ModalViewAddrReport
            show={showModalDoituong}
            handleClose={() => setshowModalDoituong(false)}
            title='THÔNG TIN CHI TIẾT TRÍCH TIN'
            report={selectedReport}
          />
          <CreateAppModal
            show={showModal}
            handleClose={() => setShowModal(false)}
            title='THÊM MỚI TRÍCH TIN'
            id={id}
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
      </div>
    </div>
  )
}

const ReportWrap: FC = () => {
  const intl = useIntl()
  const {id} = useParams()
  return (
    <>
      {/* <PageTitle breadcrumbs={[]}>{'Danh sách trích tin'}</PageTitle> */}
      <Trichtin id={id || ''} />
    </>
  )
}

export {ReportWrap}
