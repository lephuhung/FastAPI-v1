import React, {FC} from 'react'
import Avatar from 'react-avatar'
import {KTSVG} from '../../../_metronic/helpers'
import {useIntl} from 'react-intl'
import {useQueries} from 'react-query'
import axios from 'axios'
import {useParams} from 'react-router-dom'
import {PageTitle} from '../../../_metronic/layout/core'
import { type } from './doituong'
type Props = {
  id: any
}
const URL = process.env.REACT_APP_API_URL

const DeatailsDoituong: FC<Props> = ({id}) => {
  const typeString = localStorage.getItem('type')
  const type: type[] = typeof typeString === 'string' ? JSON.parse(typeString) : []
  const result = useQueries([
    {
      queryKey: ['posts'],
      queryFn: () =>
        axios.get(`${URL}/doituong/view/${id}`).then((res) => {
          return res.data
        }),
    },
    {
      queryKey: ['users'],
      queryFn: () =>
        axios.get(`${URL}/doituong/details/${id}`).then((res) => {
          return res.data
        }),
    },
  ])
  if (result[0].isLoading) {
    <div>Loading</div>
  }
  return (
    // <></>
    <>
      {result[0].isLoading ? (
        <div>Loading</div>
      ) : (
        <div>
          <div className='card mb-5 mb-xl-10'>
            <div className='card-body pt-9 pb-0'>
              <div className='d-flex flex-wrap flex-sm-nowrap mb-3'>
                <div className='me-7 mb-4'>
                  <div className='symbol symbol-100px symbol-lg-160px symbol-fixed position-relative'>
                    {result[0].data.Image ? (
                      <img src={result[0].data?.Image} className='' alt='' />
                    ) : (
                      <Avatar name={result[0].data.client_name} size='100' />
                    )}

                    <div className='position-absolute translate-middle bottom-0 start-100 mb-6 bg-success rounded-circle border border-4 border-white h-20px w-20px'></div>
                  </div>
                </div>

                <div className='flex-grow-1'>
                  <div className='d-flex justify-content-between align-items-start flex-wrap mb-2'>
                    <div className='d-flex flex-column'>
                      <div className='d-flex align-items-center mb-2'>
                        <a
                          href='#'
                          className='text-gray-800 text-hover-primary fs-2 fw-bolder me-1'
                        >
                          {result[0].data && result[0].data.client_name.toUpperCase()}
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
                          {result[0].data && result[0].data.KOL ? 'KOL' : 'KHÔNG'}
                        </a>
                        <a
                          href='#'
                          className='d-flex align-items-center text-gray-400 text-hover-primary me-5 mb-2'
                        >
                          <KTSVG
                            path='/media/icons/duotune/general/gen018.svg'
                            className='svg-icon-4 me-1'
                          />
                          {result[0].data && result[0].data.Quequan}
                        </a>
                        <a
                          href='#'
                          className='d-flex align-items-center text-gray-400 text-hover-primary mb-2'
                        >
                          <KTSVG
                            path='/media/icons/duotune/communication/com011.svg'
                            className='svg-icon-4 me-1'
                          />
                          {result[0].data && `LOẠI KOL: ${result[0].data.SDT}`}
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
                              {result[1].data ? result[1].data.hoinhom_details.length : '0'}
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
                              {result[1].data ? result[1].data.trichtin_count[0].count : '0'}
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
                            <div className='fs-4 fw-bolder'>
                              {result[0].data ? result[0].data.updated_at.split('.')[0] : ''}
                            </div>
                          </div>

                          <div className='fw-bold fs-6 text-gray-400'>Cập nhật cuối</div>
                        </div>
                      </div>
                    </div>
                  </div>
                  <h3>Thông tin bổ sung đối tượng: </h3>
                  <span>
                    {result[0].data ? result[0].data.Thongtinbosung : 'Chưa có thông tin'}
                  </span>
                </div>
              </div>
            </div>
          </div>
          <div className='card mb-5 mb-xl-10'>
            {/* begin::Header */}
            <div className='card-header border-0 pt-5'>
              <h3 className='card-title align-items-start flex-column'>
                <span className='card-label fw-bold fs-3 mb-1'>
                  DANH SÁCH HỘI NHÓM ĐỐI TƯỢNG CÓ LIÊN QUAN
                </span>
                {/* <span className='text-muted mt-1 fw-semibold fs-7'>Over 500 new products</span> */}
              </h3>
              <div className=''></div>
              <div className='card-toolbar'></div>
            </div>
            {/* end::Header */}
            {/* begin::Body */}
            <div className='card-body py-3'>
              {/* begin::Table container */}
              <div className='table-responsive'>
                {/* begin::Table */}
                <table className='table align-middle table-striped gs-0 gy-4'>
                  {/* begin::Table head  */}
                  <thead>
                    <tr className='fw-bold text-muted'>
                      <th className='min-w-40px text-center'>STT</th>
                      <th className='ps-4 min-w-100px rounded-start'>HỘI NHÓM</th>
                      <th className='min-w-100px'>MỐI LIÊN QUAN VỚI ĐỐI TƯỢNG</th>
                      <th className='min-w-100px'>LOẠI TÀI KHOẢN</th>
                      {/* <th className='min-w-100px text-end rounded-end'></th> */}
                    </tr>
                  </thead>
                  {/* end::Table head */}
                  {/* begin::Table body */}
                  <tbody>
                    {result[1].data &&
                      result[1].data.hoinhom_details.map((el: any, index: number) => (
                        <tr key={index}>
                          <td>
                            <span className='text-muted fw-semibold text-muted d-block fs-7 text-center'>
                              {index}
                            </span>
                          </td>
                          <td>
                            <div className='d-flex align-items-center'>
                              <div className='d-flex justify-content-start flex-column'>
                                <a
                                  href='#'
                                  className='text-dark fw-bold text-hover-primary mb-1 fs-6'
                                >
                                  {el.uid_name}
                                </a>
                                <span className='text-muted fw-semibold text-muted d-block fs-7'>
                                  {`UID: ${el.uid}`}
                                </span>
                              </div>
                            </div>
                          </td>
                          {/* <td>
                  <span className='badge badge-light-primary fs-7 fw-semibold'>{el.uid_name}</span>
                </td> */}
                          <td>
                            <span className='badge badge-light-success fs-7 fw-semibold'>
                              {el.moiquanhe_name.toUpperCase()}
                            </span>
                          </td>
                          <td>
                            <span className='badge badge-light-success fs-7 fw-semibold'>
                              {type[el.type_id].name.toUpperCase()}
                            </span>
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
          </div>
          <div className='card mb-5 mb-xl-10'>
            {/* begin::Header */}
            <div className='card-header border-0 pt-5'>
              <h3 className='card-title align-items-start flex-column'>
                <span className='card-label fw-bold fs-3 mb-1'>DANH SÁCH TRÍCH TIN GẦN ĐÂY</span>
                {/* <span className='text-muted mt-1 fw-semibold fs-7'>Over 500 new products</span> */}
              </h3>
              <div className=''></div>
              <div className='card-toolbar'></div>
            </div>
            {/* end::Header */}
            {/* begin::Body */}
            <div className='card-body py-3'>
              {/* begin::Table container */}
              <div className='table-responsive'>
                {/* begin::Table */}
                <table className='table align-middle table-striped .gx-7 '>
                  {/* begin::Table head  */}
                  <thead>
                    <tr className='fw-bold text-muted'>
                      <th className='min-w-40px text-center'>STT</th>
                      <th className='ps-4 min-w-100px rounded-start'>THỜI GIAN</th>
                      <th className='min-w-100px'>NỘI DUNG</th>
                      <th className='min-w-100px'>LOẠI TÀI KHOẢN</th>
                      {/* <th className='min-w-100px text-end rounded-end'></th> */}
                    </tr>
                  </thead>
                  {/* end::Table head */}
                  {/* begin::Table body */}
                  <tbody>
                    {result[1].data &&
                      result[1].data.trichtin_details.map((el: any, index: number) => (
                        <tr key={index}>
                          <td>
                            <span className='text-muted fw-semibold text-muted d-block fs-7 text-center'>
                              {index}
                            </span>
                          </td>
                          <td>
                            <div className='d-flex align-items-center'>
                              <div className='d-flex justify-content-start flex-column'>
                                <a href='#' className='text-dark text-hover-primary mb-1 fs-6'>
                                  {el.updated_at.split('T')[0]}
                                </a>
                                {/* <span className='text-muted fw-semibold text-muted d-block fs-7'>
                            {el.ghichu_noidung}
                          </span> */}
                              </div>
                            </div>
                          </td>
                          {/* <td>
                  <span className='badge badge-light-primary fs-7 fw-semibold'>{el.uid_name}</span>
                </td> */}
                          <td>
                            <span
                              className='text-muted fw-semibold text-muted d-block fs-7'
                              style={{whiteSpace: 'pre-wrap'}}
                            >
                              {el.ghichu_noidung}
                            </span>
                          </td>
                          <td>
                            <span className='badge badge-light-success fs-7 fw-semibold'>
                              {el.uid_vaiao}
                            </span>
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
          </div>
        </div>
      )}
    </>
  )
}
const Details: FC = () => {
  const intl = useIntl()
  const {id} = useParams()
  return (
    <>
      <PageTitle breadcrumbs={[]}>{intl.formatMessage({id: 'MENU.TELE'})}</PageTitle>
      <DeatailsDoituong id={id} />
    </>
  )
}
export {Details}
