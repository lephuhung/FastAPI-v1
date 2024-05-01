/* eslint-disable react-hooks/exhaustive-deps */
/* eslint-disable jsx-a11y/anchor-is-valid */
import { createPortal } from 'react-dom'
import { Modal } from 'react-bootstrap'
import { KTSVG } from '../../../_metronic/helpers'
import { Formik, Form, Field } from 'formik'
import { ITags } from './ITags'
import { toast } from 'react-toastify'
import axios from 'axios';
type Props = {
  show: boolean
  handleClose: () => void,
  handleLoading: () => void,
  title: string
}
const URL = process.env.REACT_APP_API_URL;
const modalsRoot = document.getElementById('root-modals') || document.body
const CreateAppModal = ({ show, handleClose, handleLoading ,title }: Props) => {
  // const [data, setData] = useState<ICreateAppData>(defaultCreateAppData)
  return createPortal(
    <Modal
      id='kt_modal_create_app'
      tabIndex={-1}
      aria-hidden='true'
      dialogClassName='modal-dialog modal-dialog-centered mw-900px'
      show={show}
      onHide={handleClose}
    // onEntered={loadStepper}
    >
      <div className='modal-header'>
        <h2>{title}</h2>
        {/* begin::Close */}
        <div className='btn btn-sm btn-icon btn-active-color-primary' onClick={handleClose}>
          <KTSVG className='svg-icon-1' path='/media/icons/duotune/arrows/arr061.svg' />
        </div>
        {/* end::Close */}
      </div>

      <div className='modal-body py-lg-10 px-lg-10'>
        <Formik
          initialValues={{
            name: '',
            color: '#0000000',
          }}
          onSubmit={(values: ITags) => {
            console.log(values);
            axios.post(`${URL}/tags/create-tags`, values).then((res) => {
              if (res.status === 200) {
                handleLoading()
                handleClose()
                toast.success('Thêm thành công', {
                  position: 'bottom-right',
                  autoClose: 5000,
                  hideProgressBar: false,
                  closeOnClick: true,
                  pauseOnHover: true,
                  draggable: true,
                  progress: undefined,
                  theme: 'light',
                })
              }
              if (res.status === 400) {
                let data = res.data.DATA
                console.log(data.errors)
                toast.warning('Thêm không thành công', {
                  position: 'bottom-right',
                  autoClose: 5000,
                  hideProgressBar: false,
                  closeOnClick: true,
                  pauseOnHover: true,
                  draggable: true,
                  progress: undefined,
                  theme: 'light',
                })
              }
            })
            .catch((error) => {
              if (error.response.status === 422) {
                toast.warning('Dữ liệu nhập vào chưa đầy đủ', {
                  position: 'top-center',
                  autoClose: 5000,
                  hideProgressBar: false,
                  closeOnClick: true,
                  pauseOnHover: true,
                  draggable: true,
                  progress: undefined,
                  theme: 'light',
                })
              } else {
                toast.warning('Thêm không thành công', {
                  position: 'top-center',
                  autoClose: 5000,
                  type: 'error',
                  hideProgressBar: false,
                  closeOnClick: true,
                  pauseOnHover: true,
                  draggable: true,
                  progress: undefined,
                  theme: 'light',
                })
              }
            })

          }}

        >
          <Form>
            <div className="mb-5">
              <label className="form-label">Tên Phân loại</label>
              <Field
                type="text"
                name="name"
                className="form-control"
                placeholder=""
              />
            </div>
            <div style={{ display: 'flex',flexDirection: 'row-reverse' }}>
              <button className="btn btn-info" style={{marginLeft:'5px'}}>Xóa dữ liệu</button>
              <button className="btn btn-primary" type="submit">Lưu</button>
            </div>
          </Form>

        </Formik>
      </div>
    </Modal>,
    modalsRoot
  )
}

export { CreateAppModal }
