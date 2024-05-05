/* eslint-disable react-hooks/exhaustive-deps */
/* eslint-disable jsx-a11y/anchor-is-valid */

import {createPortal} from 'react-dom'
import {Modal} from 'react-bootstrap'
// import {defaultCreateAppData, ICreateAppData} from './IAppModels'
// import {StepperComponent} from '../../../assets/ts/components'
import {KTSVG} from '../../../_metronic/helpers'
import {Formik, Form, Field, useField, FieldAttributes} from 'formik'
import {type, trangthai, donvi, ctnv} from '../Facebook/IFacebook'
import {IGroupModal, IResponseGroup} from '../Group/Group'
import {IResponseFacebook} from '../Facebook/IFacebook'
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
const CreateAppModal = ({show, handleClose, handleLoading, title}: Props) => {
  const [datagroup, setDataGroup] = useState<IResponseGroup[]>([])
  const [datafacebook, setDataFacebook] = useState<IResponseFacebook[]>([])
  const donviString = localStorage.getItem('donvi')
  const donvi: donvi[] = typeof donviString === 'string' ? JSON.parse(donviString) : []
  const typeString = localStorage.getItem('type')
  const type: type[] = typeof typeString === 'string' ? JSON.parse(typeString) : []
  const ctnvString = localStorage.getItem('ctnv')
  const ctnv: ctnv[] = typeof ctnvString === 'string' ? JSON.parse(ctnvString) : []
  useEffect(() => {
    axios.get(`${URL}/uid/get-groups`).then((response) => {
      setDataGroup(response.data)
    })
    axios.get(`${URL}/uid/get-vaiao`).then((response) => {
      setDataFacebook(response.data)
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
            uid_vaiao: '',
            uid_hoinhom: '',
            active: 1,
          }}
          onSubmit={(values: any) => {
            console.log(values)
            instance
              .post(`${URL}/vaiao/create`, values)
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
                  <label className='form-label'>VAI ẢO FACEBOOK</label>
                  <MySelect label='Job Type' name='uid_vaiao' width={300}>
                    <option value=''>Lựa chọn vai ảo</option>
                    {datafacebook.map((data: IResponseFacebook, index: number) => {
                      return (
                        <option value={data.uid} key={index}>
                          {`${data.uid}: ${data.name.toUpperCase()}`}
                        </option>
                      )
                    })}
                  </MySelect>
                </div>
                <div>
                  <label className='form-label'> NẮM THÔNG TIN HỘI NHÓM </label>
                  <MySelect label='Job Type' name='uid_hoinhom' width={300}>
                    <option value=''>Lựa chọn hội nhóm</option>
                    {datagroup.map((data: IResponseGroup, index: number) => {
                      return (
                        <option value={data.uid} key={index}>
                          {`${data.uid}: ${data.name.toUpperCase()}`}
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

export {CreateAppModal}
