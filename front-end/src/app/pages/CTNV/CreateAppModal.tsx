/* eslint-disable react-hooks/exhaustive-deps */
/* eslint-disable jsx-a11y/anchor-is-valid */
import { createPortal } from 'react-dom'
import { Modal } from 'react-bootstrap'

import { KTSVG } from '../../../_metronic/helpers'
import { Formik, Form, Field } from 'formik'
import { Ictnv } from './CTNV'
import axios from 'axios';
type Props = {
  show: boolean
  handleClose: () => void
  title: string
}
const URL = process.env.REACT_APP_API_URL;
const modalsRoot = document.getElementById('root-modals') || document.body

const CreateAppModal = ({ show, handleClose, title }: Props) => {
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
        {/* begin::Close */}
        <div className='btn btn-sm btn-icon btn-active-color-primary' onClick={handleClose}>
          <KTSVG className='svg-icon-1' path='/media/icons/duotune/arrows/arr061.svg' />
        </div>
        {/* end::Close */}
      </div>

      <div className='modal-body py-lg-10 px-lg-10'>
        <Formik
          initialValues={{
            id:0,
            name: '',
            url: '',
            config_name:'',
          }}
          onSubmit={(values: Ictnv) => {
            console.log(values);
            axios.post(`${URL}/ctnv/create`, values).then((res) => {
              
            }).catch((error) => {
              if(error.status === 403) {
                handleClose()
              }
            });
          }}

        >
          <Form>

            <div className="mb-5">
              <label className="form-label"> TÊN BÁO </label>
              <Field
                type="text"
                name="name"
                className="form-control"
                placeholder="100064489458115"
              />
            </div>
            <div className="mb-5">
              <label className="form-label">URL BÁO</label>
              <Field
                type="text"
                className="form-control"
                name='url'
                placeholder="Tin nhanh 24h"
              />
            </div>
            <div className="mb-5">
              <label className="form-label">TÊN FILE CONFIG</label>
              <Field
                type="text"
                name='config_name'
                className="form-control form-control-white"
                
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
