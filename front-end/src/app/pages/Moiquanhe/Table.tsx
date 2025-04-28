/* eslint-disable jsx-a11y/anchor-is-valid */
import React, {useState} from 'react'
import {KTSVG, toAbsoluteUrl} from '../../../_metronic/helpers'
import {CreateAppModal} from './CreateAppModal'
import {useQuery} from 'react-query'
import axios from 'axios'
import {IResponserelationship} from './IMoiquanhe'
import {useCopyToClipboard} from './useCopyToClipboard'
import { ToastContainer } from 'react-toastify'
const URL = `${process.env.REACT_APP_API_URL}`
type Props = {
  className: string
}
const Table: React.FC<Props> = ({className}) => {
  const [showCreateAppModal, setShowCreateAppModal] = useState<boolean>(false)
  const [showModalViewItem, setShowModalViewItem] = useState<boolean>(false)
  const [IResponsehost, setIResponseHost] = useState<IResponserelationship>({
    id:0,
    name:'',
    created_at: '',
    updated_at: '',
  })
  const [value, copy] = useCopyToClipboard()
  const [refresh, setrefesh]= useState<boolean>(false);
  const {isLoading, data, error} = useQuery({
    queryKey: ['host', refresh],
    queryFn: async () => {
      const respone = await axios.get(`${URL}/relationships`)
      const {data} = respone
      return data
    },
  })
  if (isLoading) {
    <div>Loading</div>
  }
  if (error) {
    console.log(error)
  }
  return (
    <div className={`card ${className}`}>
      {/* begin::Header */}
      <div className='card-header border-0 pt-5'>
        <h3 className='card-title align-items-start flex-column'>
          <span className='card-label fw-bold fs-3 mb-1'>DANH SÁCH HOST</span>
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
            Thêm mới Host
          </a>
        </div>
      </div>
      {/* end::Header */}
      {/* begin::Body */}
      <div className='card-body py-3'>
        {/* begin::Table container */}
        <div className='table-responsive'>
          {/* begin::Table */}
          <table className='table align-middle gs-0 gy-4'>
            {/* begin::Table head */}
            <thead>
              <tr className='fw-bold text-muted bg-light'>
                <th className='ps-4 min-w-325px rounded-start'>TÊN</th>
                {/* <th className='min-w-125px'>UID</th> */}
                <th className='min-w-150px'>THỜI GIAN TẠO</th>
                <th className='min-w-150px rounded-end'>HÀNH ĐỘNG</th>
              </tr>
            </thead>
            {/* end::Table head */}
            {/* begin::Table body */}
            <tbody>
              {data &&
                data.map((el: IResponserelationship, index: number) => (
                  <tr key={index}>
                    <td>
                      <div className='d-flex align-items-center'>
                        <div className='symbol symbol-50px me-5'>
                          <img
                            src={toAbsoluteUrl('/media/stock/600x400/img-26.jpg')}
                            className=''
                            alt=''
                          />
                        </div>
                        <div className='d-flex justify-content-start flex-column'>
                          <a href='#' className='text-dark fw-bold text-hover-primary mb-1 fs-6'>
                            {el.name.toUpperCase()}
                          </a>
                          <span className='text-muted fw-semibold text-muted d-block fs-7'>
                            {`ID: ${el.id}`}
                          </span>
                        </div>
                      </div>
                    </td>
                    <td>
                      <span className='text-muted fw-semibold text-muted d-block fs-7'>
                        {el.created_at}
                      </span>
                    </td>
                    <td>
                      <a
                        href='#'
                        className='btn btn-icon btn-bg-light btn-active-color-primary btn-sm me-1'
                        onClick={() => {
                          setShowModalViewItem(true)
                          setIResponseHost(el)
                        }}
                      >
                        <KTSVG path='/media/icons/duotune/art/art005.svg' className='svg-icon-3' />
                      </a>
                      <a
                        href='#'
                        className='btn btn-icon btn-bg-light btn-active-color-primary btn-sm'
                        onClick={() => {
                          axios
                            .delete(`${URL}/host/${el.id}`)
                            .then((res) => {
                              if(res.data.STATUS==='200')setrefesh(true);
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
            {/* enxxd::Table body */}
          </table>
          {/* end::Table */}
        </div>
        {/* end::Table container */}
      </div>
      {/* begin::Body */}
      {/* <CreateAppModal
        show={showCreateAppModal}
        handleClose={() => setShowCreateAppModal(false)}
        title='Thêm Host mới'
      /> */}
      
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
