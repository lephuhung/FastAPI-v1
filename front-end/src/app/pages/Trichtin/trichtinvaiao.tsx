import React, {FC, useState} from 'react'
import Avatar from 'react-avatar'
import {KTSVG} from '../../../_metronic/helpers'
import {useIntl} from 'react-intl'
import {useQuery} from 'react-query'
import axios from 'axios'
import { CreateAppModal } from './CreateAppModal'
import {useParams} from 'react-router-dom'
import {trichtin} from './trichtin'
// import {ModalViewItemVaiao} from './ModalViewItemVaiao'
import { ModalViewItemTrichtin } from './ModalViewItemTrichtin'
type Props = {
  id: any
}
const URL = process.env.REACT_APP_API_URL


const Trichtin: FC<Props> = ({id}) => {
  const [showModal, setShowModal] = useState<boolean>(false)
  const [showModalIndividual, setshowModalIndividual] = useState<boolean>(false)
  const [trichtin, settrichtin] = useState<trichtin>()
  const {isLoading, data, error} = useQuery({
    queryKey: ['trichtinAll'],
    queryFn: () =>
      id && axios.get(`${URL}/trichtin/get-all-by-vaiao/${id}`).then((res) => {
        return res.data
      }),
  })
  if (isLoading) {
    <div>Loading</div>
  }
  return (
    <div className={'card mb-5 mb-xl-8'}>
      {/* begin::Header */}
      <div className='card-header border-0 pt-5'>
        <h3 className='card-title align-items-start flex-column'>
          <span className='card-label fw-bold fs-3 mb-1'>
            {`DANH SÁCH TRÍCH TIN ID: ${id}`}
          </span>
          {/* <span className='text-muted mt-1 fw-semibold fs-7'>Over 500 new products</span> */}
        </h3>
        <div className='card-toolbar'>
        </div>
      </div>
      {/* end::Header */}
      {/* begin::Body */}
      <div className='card-body py-3'>
        {/* begin::Table container */}
        <div className='table-responsive'>
          <table className='table align-middle '>
            {/* begin::Table head */}
            <thead>
              <tr className='fw-bold text-muted bg-light'>
                <th className='min-w-40px text-center'>STT</th>
                <th className='ps-4 min-w-200px rounded-start'>THỜI GIAN</th>
                <th className='min-w-100px'>CÁN BỘ TRÍCH TIN</th>
                <th className='min-w-250px'>NỘI DUNG</th>
                <th className='min-w-200px'>ĐỐI TƯỢNG</th>
                <th className='min-w-100px'>HÀNH ĐỘNG </th>
              </tr>
            </thead>
            {/* end::Table head */}
            {/* begin::Table body */}
            <tbody>
              {data &&
                data.map((el: trichtin, index: number) => (
                  <tr key={index}>
                    <td>
                      <span className='text-muted fw-semibold text-muted d-block fs-7 text-center'>
                        {index + 1}
                      </span>
                    </td>
                    <td>
                      <div className='d-flex align-items-center'>
                        <div className='d-flex justify-content-start flex-column'>
                          <span className='text-muted fw-semibold text-muted d-block fs-7'>
                            {`${el.updated_at.split('.')[0]}`}
                          </span>
                        </div>
                      </div>
                    </td>
                    <td>
                      <span className='badge badge-light-primary fs-7 fw-semibold'>
                        {el.user}
                      </span>
                    </td>
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
                      {el.hoinhom_name}
                      </span>
                    </td>
                    <td className='text-canter'>
                      <span className='btn btn-bg-light btn-color-muted btn-active-color-primary btn-sm px-4' onClick={() => {
                          settrichtin(el)
                          setshowModalIndividual(true)
                      }}>
                        Hiện thị
                      </span>
                    </td>
                  </tr>
                ))}
            </tbody>
            {/* end::Table body */}
          </table>
          <ModalViewItemTrichtin
            show={showModalIndividual}
            handleClose={() => setshowModalIndividual(false)}
            title='THÔNG TIN CHI TIẾT TRÍCH TIN'
            trichtin={trichtin}
          />
        </div>
      </div>
    </div>
  )
}
const TrichtinVaiaoWrap: FC = () => {
  const intl = useIntl()
  const {id} = useParams()
  return (
    <>
      {/* <PageTitle breadcrumbs={[]}>{intl.formatMessage({id: 'MENU.TELE'})}</PageTitle> */}
      <Trichtin id={id} />
    </>
  )
}
export {TrichtinVaiaoWrap}
