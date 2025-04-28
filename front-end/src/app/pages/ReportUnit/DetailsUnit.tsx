import React, {useEffect, useState} from 'react'
import {KTSVG, toAbsoluteUrl} from '../../../_metronic/helpers'
import {useQuery, useQueries} from 'react-query'
import { IResponseGroup } from '../Group/Group'
import Avatar from 'react-avatar'
import {useParams, useLocation} from 'react-router-dom'
import axios from 'axios'
import {PageTitle} from '../../../_metronic/layout/core'
import {individual, type,individualResponse} from '../Individual/individual'
import {ModalViewIndividual} from '../Individual/ModalViewIndividual'
import {ModalViewItem} from '../Group/ModalViewItem'
import {IResponseFacebook} from '../Facebook/IFacebook'
const URL = process.env.REACT_APP_API_URL
type Props = {
  id: any
}

const Details: React.FC<Props> = ({id}) => {
  const typeString = localStorage.getItem('type')
  const type: type[] = typeof typeString === 'string' ? JSON.parse(typeString) : []
  console.log(type)
  const [showModalIndividual, setshowModalIndividual] = useState<boolean>(false)
  const [individualitem, setindividualItem] = useState<individualResponse>()
  const [dataItem, setDataItem] = useState<IResponseGroup>()
  const [showModelItem, setModelItem] = useState<boolean>(false)
  const result = useQueries([
    {
      queryKey: ['unit'],
      queryFn: () =>
        axios.get(`${URL}/thongke/details/unit/${id}`).then((response) => {
          return response.data
        }),
    },
    {
      queryKey: ['individual'],
      queryFn: () =>
        axios.get(`${URL}/thongke/details/individual/${id}`).then((res) => {
          return res.data
        }),
    },
  ])

  return (
    <>
      {result[0].isLoading ? (
        <div>Loading</div>
      ) : (
        <div className='row g-5'>
          <div className='card mb-5 mb-xl-10'>
            <div className='card-header border-0 pt-5'>
              <h3 className='card-title align-items-start flex-column'>
                <span className='card-label fw-bold fs-3 mb-1'>
                  DANH SÁCH HỘI NHÓM HỘI NHÓM ĐƠN VỊ QUẢN LÝ
                </span>
              </h3>
              <div className=''></div>
              <div className='card-toolbar'></div>
            </div>

            <div className='card-body py-3'>
              {/* begin::Table container */}
              <div className='table-responsive'>
                {/* begin::Table */}
                <table className='table align-middle table-striped gs-0 gy-4'>
                  {/* begin::Table head  */}
                  <thead>
                    <th className='min-w-50px text-center'>STT</th>
                    <th className='ps-4 min-w-250px rounded-start'>TÊN</th>
                    {/* <th className='min-w-150px'>CẬP NHẬT</th> */}
                    <th className='min-w-150pxc text-center'>PHÂN LOẠI</th>
                    <th className='min-w-100px'>VAI ẢO</th>
                    <th className='min-w-100px'>BẠN BÈ</th>
                    <th className='min-w-100px text-center'>LOẠI</th>
                    <th className='min-w-100px text-center'>CTNV</th>
                    <th className='min-w-200px text-center'>HOẠT ĐỘNG</th>
                  </thead>
                  <tbody>
                    {result[0].data &&
                      result[0].data.map((el: IResponseFacebook, index: number) => (
                        <tr key={index}>
                          <td className='text-center'>
                            <span className='text-muted fw-semibold text-muted d-block fs-7'>
                              {index + 1}
                            </span>
                          </td>
                          <td>
                            <div className='d-flex align-items-center'>
                              <div className='symbol symbol-50px me-5'>
                                <img
                                  src={toAbsoluteUrl('/media/facebook.png')}
                                  className=''
                                  alt=''
                                />
                              </div>
                              <div className='d-flex justify-content-start flex-column'>
                                <a
                                  href='#'
                                  className='text-dark fw-bold text-hover-primary mb-1 fs-6'
                                >
                                  {el.name.toUpperCase()}
                                </a>
                                <span className='text-muted fw-semibold text-muted d-block fs-7'>
                                  {`UID: ${el.uid}`}
                                </span>
                              </div>
                            </div>
                          </td>

                          <td>
                            <span className='badge badge-primary fs-7 fw-semibold'>
                              {el.status_name.toUpperCase()}
                            </span>
                          </td>
                          <td>
                            <span className='badge badge-warning fs-7 fw-semibold'>
                              {el.Vaiao ? 'Vai ảo' : 'Không'}
                            </span>
                          </td>
                          <td>
                            <span className='badge badge-primary fs-7 fw-semibold'>
                              {el.reaction}
                            </span>
                          </td>
                          <td>
                            <span className='badge badge-danger fs-7 fw-semibold text-center'>
                              {type[el.account_type_id].name}
                            </span>
                          </td>
                          <td className='text-center'>
                            <span className='badge badge-success fs-7 fw-semibold'>
                              {el.task_name.toUpperCase()}
                            </span>
                          </td>
                          <td className='text-center'>
                            <span
                              className='btn btn-bg-light btn-color-muted btn-active-color-primary btn-sm px-4 me-1'
                              onClick={() => {
                                setDataItem(el)
                                setModelItem(true)
                              }}
                            >
                              Hiện thị
                            </span>

                            <a
                              href='#'
                              className='btn btn-icon btn-bg-light btn-active-color-primary btn-sm me-1'
                            >
                              <KTSVG
                                path='/media/icons/duotune/art/art005.svg'
                                className='svg-icon-3'
                              />
                            </a>
                            <a
                              href='#'
                              className='btn btn-icon btn-bg-light btn-active-color-primary btn-sm'
                              onClick={() => {
                                axios
                                  .delete(`${URL}/uid/${el.uid}`)
                                  .then((res) => {
                                    console.log(res.data)
                                  })
                                  .catch((e) => {})
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
          </div>
          <div className='row g-5'>
            {/* begin::Body */}
            <div className='card mb-5 mb-xl-5'>
              <div className='card-header border-0 pt-5'>
                <h3 className='card-title align-items-start flex-column'>
                  <span className='card-label fw-bold fs-3 mb-1'>
                    DANH SÁCH ĐỐI TƯỢNG/is_kol ĐƠN VỊ QUẢN LÝ
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
                    {/* begin::Table head */}
                    <thead>
                      <tr className='fw-bold text-muted'>
                        <th className='ps-4 min-w-5px rounded-start text-center'>STT</th>
                        <th className='min-w-150px text-center'>THÔNG TIN</th>
                        <th className='min-w-100px text-center'>SĐT</th>
                        <th className='min-w-200px text-center'>QUÊ QUÁN</th>
                        <th className='min-w-100px'>NGÀY SINH</th>
                        <th className='min-w-100px text-center'>is_kol</th>
                        <th className='min-w-150px text-center'>HÀNH ĐỘNG</th>
                      </tr>
                    </thead>
                    <tbody>
                      {result[1].data &&
                        result[1].data.map((el: individualResponse, index: number) => (
                          <tr key={index}>
                            <td className='text-center'>
                              <span className='text-muted fw-semibold text-muted d-block fs-7'>
                                {index + 1}
                              </span>
                            </td>
                            <td>
                              <div className='d-flex align-items-center'>
                                <div className='symbol symbol-50px me-5'>
                                  {el.image_url ? (
                                    <img src={el.image_url} className='' alt='' />
                                  ) : (
                                    <Avatar name={el.full_name} round={true} size='50' />
                                  )}
                                </div>
                                <div className='d-flex justify-content-start flex-column'>
                                  <a
                                    href='#'
                                    className='text-dark fw-bold text-hover-primary mb-1 fs-6'
                                  >
                                    {el.full_name.toUpperCase()}
                                  </a>
                                  <span className='text-muted fw-semibold text-muted d-block fs-7'>
                                    {`CCCD/CMND: ${el.id_number}`}
                                  </span>
                                </div>
                              </div>
                            </td>
                            <td>
                              <span className='badge badge-light-primary fs-7 fw-semibold'>
                                {el.phone_number}
                              </span>
                            </td>
                            <td>
                              <span className='badge badge-light-success fs-7 fw-semibold'>
                                {el.hometown}
                              </span>
                            </td>
                            <td>
                              <span className='text-muted fw-semibold text-muted d-block fs-7'>
                                {el.date_of_birth.toString()}
                              </span>
                            </td>
                            <td className='text-center'>
                              {el.is_kol === true ? (
                                <span className='badge badge-primary fs-7 fw-semibold fw-semibold'>
                                  KOLS
                                </span>
                              ) : (
                                <span className='badge badge-danger fs-7 fw-semibold fw-semibold'>
                                  Không
                                </span>
                              )}
                            </td>
                            <td>
                              <span
                                className='btn btn-bg-light btn-color-muted btn-active-color-primary btn-sm px-4 me-1'
                                onClick={() => {
                                  setindividualItem(el)
                                  setshowModalIndividual(true)
                                }}
                              >
                                Chi tiết
                              </span>

                              <a
                                href='#'
                                className='btn btn-icon btn-bg-light btn-active-color-primary btn-sm me-1'
                                onClick={() => {
                                  // setShowModalViewItem(true)
                                  // setIResponseHost(el)
                                }}
                              >
                                <KTSVG
                                  path='/media/icons/duotune/art/art005.svg'
                                  className='svg-icon-3'
                                />
                              </a>
                              <a
                                href='#'
                                className='btn btn-icon btn-bg-light btn-active-color-primary btn-sm'
                                onClick={() => {
                                  axios
                                    .delete(`${URL}/host/${el.id}`)
                                    .then((res) => {
                                      // if(res.data.STATUS==='200')setrefesh(true);
                                    })
                                    .catch((e) => {})
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
            </div>
          </div>
        </div>
      )}
      <ModalViewIndividual
        show={showModalIndividual}
        handleClose={() => setshowModalIndividual(false)}
        title='THÔNG TIN CHI TIẾT ĐỐI TƯỢNG'
        individual={individualitem}
      />
      <ModalViewItem
        show={showModelItem}
        handleClose={() => setModelItem(false)}
        // handleLoading={() => setloading(true)}
        igroup={dataItem}
        title='THÔNG TIN CHI TIẾT GROUP'
      />
    </>
  )
}
const DetailsUnit: React.FC = () => {
  const {id} = useParams()
  const {isLoading, data, error} = useQuery({
    queryKey: 'name',
    queryFn: () =>
      axios.get(`${URL}/unit/get/${id}`).then((res) => {
        return res.data
      }),
  })
  return (
    <>
      {data ? (
        <>
          <PageTitle breadcrumbs={[]}>{`THÔNG TIN ĐƠN VỊ ${data?.name}`}</PageTitle>
          <Details id={id} />
        </>
      ) : (
        <></>
      )}
    </>
  )
}
export {DetailsUnit}
