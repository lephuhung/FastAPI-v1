/* eslint-disable react-hooks/exhaustive-deps */
/* eslint-disable jsx-a11y/anchor-is-valid */

import {createPortal} from 'react-dom'
import {Modal} from 'react-bootstrap'
import * as Yup from 'yup'
import {KTSVG} from '../../../_metronic/helpers'
import {Formik, Form, Field, useField, FieldAttributes} from 'formik'
import {type, trangthai, donvi, ctnv, tinhchat} from '../Facebook/IFacebook'
import {IGroupModal} from './Group'
import {toast} from 'react-toastify'
import instance from '../../modules/axiosInstance'
import '../Facebook/style.css'
import {useEffect, useState} from 'react'
import styled from '@emotion/styled'
import axios from 'axios'
// import styled from 'styled-components';
type Props = {
  show: boolean
  handleClose: () => void
  handleLoading: () => void
  title: string
}
const URL = process.env.REACT_APP_API_URL
const modalsRoot = document.getElementById('root-modals') || document.body

const ValidateUid = Yup.object().shape({
  uid: Yup.string()
    .min(12, 'Quá ngắn!')
    .max(17, 'Quá dài!')
    .required('uid is required')
    .matches(/^\d+$/, 'uid chỉ nhận ký tự số'),
  reaction: Yup.string()
    .required('Số bạn bè cần nhập')
    .matches(/^\d+$/, 'Số lượng bạn bè chỉ nhận ký tự số'),
  SDT: Yup.string()
    .min(0, 'Quá ngắn')
    .max(11, 'Quá dài')
    .matches(/^\d+$/, 'Số điện thoại là ký tự số, nếu không có điền 0'),
  name: Yup.string().required(),
})
const CreateAppModal = ({show, handleClose, handleLoading, title}: Props) => {
  const [data, setData] = useState<trangthai[]>([])
  const tinhchatString = localStorage.getItem('tinhchat')
  const tinhchat: tinhchat[] = typeof tinhchatString === 'string' ? JSON.parse(tinhchatString) : []
  const donviString = localStorage.getItem('donvi')
  const donvi: donvi[] = typeof donviString === 'string' ? JSON.parse(donviString) : []
  const typeString = localStorage.getItem('type')
  const type: type[] = typeof typeString === 'string' ? JSON.parse(typeString) : []
  const ctnvString = localStorage.getItem('ctnv')
  const ctnv: ctnv[] = typeof ctnvString === 'string' ? JSON.parse(ctnvString) : []
  useEffect(() => {
    axios.get(`${URL}/trangthai`).then((response) => {
      setData(response.data)
    })
  }, [])
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
            uid: '',
            name: '',
            SDT: '0',
            reaction: 0,
            trangthai_id: 0,
            Vaiao: false,
            ghichu: '',
            type_id: 1,
            ctnv_id: 0,
            donvi_id: '',
            trangthai_name: '',
          }}
          validationSchema={ValidateUid}
          onSubmit={(values: IGroupModal) => {
            console.log(values)
            instance
              .post(`${URL}/uid/create`, values)
              .then((res) => {
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
                if (error.response && error.response.status === 403) {
                  toast.error('Thêm không thành công', {
                    position: 'bottom-right',
                    autoClose: 5000,
                    hideProgressBar: false,
                    closeOnClick: true,
                    pauseOnHover: true,
                    draggable: true,
                    progress: undefined,
                    theme: 'light',
                  })
                } else {
                  // Handle other errors
                  console.log('An error occurred:', error.message)
                }
              })
          }}
        >
          {({errors, touched}) => (
            <Form>
              <div className='mb-5' style={{display: 'flex', flexDirection: 'row'}}>
                <div style={{marginRight: '30px'}}>
                  <label className='form-label'>UID FACEBOOK</label>
                  <Field
                    type='text'
                    name='uid'
                    className='form-control'
                    placeholder=''
                    style={{width: '200px'}}
                  />
                  {errors.uid && touched.uid ? (
                    <StyledErrorMessage>{errors.uid}</StyledErrorMessage>
                  ) : null}
                </div>
                <div>
                  <label className='form-label'> PHÂN LOẠI HỘI NHÓM </label>
                  <MySelect width='200px' label='Job Type' name='trangthai_id'>
                    <option value=''>Lựa chọn phân loại</option>
                    {data.map((data: trangthai, index: number) => {
                      return (
                        <option value={data.id} key={index}>
                          {data.name}
                        </option>
                      )
                    })}
                  </MySelect>
                </div>
                <div style={{marginLeft: '30px'}}>
                  <label className='form-label'> TÍNH CHẤT HỘI NHÓM </label>
                  <MySelect width='200px' label='Job Type' name='tinhchat_id'>
                    <option value=''>Lựa chọn tính chất</option>
                    {tinhchat.map((data: tinhchat, index: number) => {
                      return (
                        <option value={data.id} key={index}>
                          {data.name.toUpperCase()}
                        </option>
                      )
                    })}
                  </MySelect>
                </div>
              </div>
              <div className='mb-5'>
                <label className='form-label'>TÊN FACEBOOK</label>
                <Field type='text' className='form-control' name='name' placeholder='LÊ PHÚ HƯNG' />
                {errors.name && touched.name ? (
                  <StyledErrorMessage>{errors.name}</StyledErrorMessage>
                ) : null}
              </div>
              <div className='mb-5' style={{display: 'flex', flexDirection: 'row'}}>
                <div className='mr-5' style={{marginRight: '10px'}}>
                  <label className='form-label'>SỐ LƯỢNG BẠN BÈ</label>
                  <Field
                    type='text'
                    name='reaction'
                    className='form-control form-control-white'
                    placeholder='123456'
                  />
                  {errors.reaction && touched.reaction ? (
                    <StyledErrorMessage>{errors.reaction}</StyledErrorMessage>
                  ) : null}
                </div>
                <div>
                  <label className='form-label'>SỐ ĐIỆN THOẠI</label>
                  <Field
                    type='text'
                    name='SDT'
                    className='form-control form-control-white'
                    placeholder='0912345678'
                  />
                  {errors.SDT && touched.SDT ? (
                    <StyledErrorMessage>{errors.SDT}</StyledErrorMessage>
                  ) : null}
                </div>
              </div>
              <div className='mb-5'>
                <label className='form-label'>GHI CHÚ</label>
                <MyTextArea
                  label='Ghi chú'
                  name='ghichu'
                  rows='6'
                  placeholder='Once upon a time there was a princess who lived at the top of a glass hill.'
                />
              </div>
              <div className='mb-5' style={{display: 'flex', flexDirection: 'row'}}>
                <div style={{marginRight: '30px'}}>
                  <label className='form-label'> ĐƠN VỊ THỰC HIỆN CÔNG TÁC NGHIỆP VỤ </label>
                  <MySelect label='Job Type' name='donvi_id'>
                    <option value=''>Lựa chọn đơn vị</option>
                    {donvi &&
                      donvi?.map((data: donvi, index: number) => {
                        return (
                          <option value={data.id} key={index}>
                            {data.name}
                          </option>
                        )
                      })}
                  </MySelect>
                </div>
                <div>
                  <label className='form-label'> CÔNG TÁC NGHIỆP VỤ </label>
                  <MySelect width='200px' label='Job Type' name='ctnv_id'>
                    <option value=''>Lựa chọn CTNV</option>
                    {ctnv.map((data: ctnv, index: number) => {
                      return (
                        <option value={data.id} key={index}>
                          {data.name}
                        </option>
                      )
                    })}
                  </MySelect>
                </div>
              </div>
              <div style={{display: 'flex', flexDirection: 'row-reverse'}}>
                <button className='btn btn-info' style={{marginLeft: '5px'}}>
                  Xóa dữ liệu
                </button>
                <button className='btn btn-primary' type='submit'>
                  Lưu
                </button>
              </div>
            </Form>
          )}
        </Formik>
      </div>
    </Modal>,
    modalsRoot
  )
}
interface MyTextAreaProps extends FieldAttributes<any> {
  label: string
}
interface MyCheckboxProps extends FieldAttributes<any> {
  children: React.ReactNode
}
interface MySelectProps extends FieldAttributes<any> {
  label: string
}

// Define styled components if not imported
const StyledSelect = styled.select`
  color: var(--blue-700);
`

const StyledErrorMessage = styled.div`
  font-size: 12px;
  color: var(--red-600);
  width: 200px;
  margin-top: 0.25rem;
  &:before {
    content: '❌ ';
    font-size: 10px;
  }
  @media (prefers-color-scheme: dark) {
    color: var(--red-300);
  }
`
const MySelect: React.FC<MySelectProps> = ({label, width, ...props}) => {
  const [field, meta] = useField(props as any)

  return (
    <>
      <StyledSelect {...field} {...props} style={{width: width}} />
      {meta.touched && meta.error ? (
        <StyledErrorMessage>{meta.error}</StyledErrorMessage>
      ) : field.value === undefined || field.value === '' || field.value === 0 ? (
        <StyledErrorMessage>Vui lòng lựa chọn</StyledErrorMessage>
      ) : null}
    </>
  )
}

const MyCheckbox: React.FC<MyCheckboxProps> = ({children, ...props}) => {
  const [field, meta] = useField(props as any)

  return (
    <>
      <label className='checkbox'>
        <input {...field} {...props} type='checkbox' />
        {children}
      </label>
      {meta.touched && meta.error ? <div className='error'>{meta.error}</div> : null}
    </>
  )
}
const MyTextArea: React.FC<MyTextAreaProps> = ({label, ...props}) => {
  const [field, meta] = useField(props as any)

  return (
    <>
      {/* <label htmlFor={props.id || props.name}>{label}</label> */}
      <textarea className='text-area' {...field} {...props} />
      {meta.touched && meta.error ? <div className='error'>{meta.error}</div> : null}
    </>
  )
}
export {CreateAppModal}
