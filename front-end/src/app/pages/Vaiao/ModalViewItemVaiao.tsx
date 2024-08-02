/* eslint-disable react-hooks/exhaustive-deps */
/* eslint-disable jsx-a11y/anchor-is-valid */
import {useState, useEffect} from 'react'
import {createPortal} from 'react-dom'
import {Modal} from 'react-bootstrap'
import {KTSVG} from '../../../_metronic/helpers'
import {useNavigate} from 'react-router-dom'
import axios from 'axios'
import {type} from '../Facebook/IFacebook'

type Props = {
  show: boolean
  handleClose: () => void
  title: string
  id?: string
}
const PUBLIC_URL = process.env.PUBLIC_URL
const URL = process.env.REACT_APP_API_URL
const modalsRoot = document.getElementById('root-modals') || document.body

const ModalViewItemVaiao: React.FC<Props> = ({show, handleClose, title, id}) => {
  const [data, setData] = useState<any>()
  const navigate = useNavigate()
  const [error, setError] = useState('')
  const typeString = localStorage.getItem('type')
  const type: type[] = typeof typeString === 'string' ? JSON.parse(typeString) : []
  useEffect(() => {
    id &&
      axios
        .get(`${URL}/trichtin/get-all-by-vaiao/${id}`)
        .then((res) => {
          console.log(res.data)
          setData(res.data)
        })
        .catch(() => {})
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
      <div className='modal-body py-lg-10 px-lg-10'>
        {data ? <div>Chưa có trích tin</div> : <div></div>}
      </div>
    </Modal>,
    modalsRoot
  )
}

export {ModalViewItemVaiao}
