/* eslint-disable react-hooks/exhaustive-deps */
/* eslint-disable jsx-a11y/anchor-is-valid */

import { createPortal } from 'react-dom'
import { Modal } from 'react-bootstrap'
// import {defaultCreateAppData, ICreateAppData} from './IAppModels'
// import {StepperComponent} from '../../../assets/ts/components'
import { KTSVG } from '../../../_metronic/helpers'
import { Formik, Form, Field, useField, FieldAttributes } from 'formik'
import { account_type, SocialAccountModal, status, unit, task, characteristics } from './SocialAccount'
import { toast } from 'react-toastify'
import instance from '../../modules/axiosInstance'
import './style.css'
import { useEffect, useState } from 'react'
import styled from '@emotion/styled'
import axios from 'axios'
import { SocialAccountResponse } from './SocialAccount'
import * as Yup from 'yup'
type Props = {
  show: boolean
  handleClose: () => void
  handleLoading: () => void
  title: string
  dataModal: SocialAccountResponse
}
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
const URL = process.env.REACT_APP_API_URL
const modalsRoot = document.getElementById('root-modals') || document.body

const UpdateModal = ({ show, handleClose, handleLoading, title, dataModal }: Props) => {
  const [data, setData] = useState<status[]>([])
  const unitsString = localStorage.getItem('units')
  const units: unit[] = typeof unitsString === 'string' ? JSON.parse(unitsString) : []
  const account_typeString = localStorage.getItem('account_types')
  const account_type: account_type[] = typeof account_typeString === 'string' ? JSON.parse(account_typeString) : []
  const characteristicsString = localStorage.getItem('characteristics')
  const characteristics: characteristics[] = typeof characteristicsString === 'string' ? JSON.parse(characteristicsString) : []
  const tasksString = localStorage.getItem('tasks')
  const tasks: task[] = typeof tasksString === 'string' ? JSON.parse(tasksString) : []
  const statusString = localStorage.getItem('statuses')
  const status: status[] = typeof statusString === 'string' ? JSON.parse(statusString) : []
  useEffect(() => {
    // axios.get(`${URL}/trangthai`).then((response) => {
    //   setData(response.data)
    // })
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
        {/* begin::Close */}
        <div className='btn btn-sm btn-icon btn-active-color-primary' onClick={handleClose}>
          <KTSVG className='svg-icon-1' path='/media/icons/duotune/arrows/arr061.svg' />
        </div>
        {/* end::Close */}
      </div>

      <div className='modal-body py-lg-10 px-lg-10'>
        <Formik
          initialValues={{
            id: dataModal.id,
            uid: dataModal.uid,
            name: dataModal.name,
            reaction_count: dataModal.reaction_count,
            phone_number: dataModal.phone_number,
            status_id: dataModal.status_id,
            status_name: dataModal.status_name,
            type_id: dataModal.type_id,
            note: dataModal.note,
            is_active: dataModal.is_active,
            created_at: dataModal.created_at,
            updated_at: dataModal.updated_at,
            unit: {
              id: dataModal.unit?.id || '',
              name: dataModal.unit?.name || '',
            },
            task: {
              id: dataModal.task?.id || 0,
              name: dataModal.task?.name || '',
            }
          }}
          onSubmit={(values: SocialAccountResponse) => {
            console.log(values)
            axios
              .put(`${URL}/social-accounts/${dataModal.uid}`, values)
              .then((res: any) => {
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
          {({ errors, touched }) => (
            <Form>
              <div className='mb-5' style={{ display: 'flex', flexDirection: 'row' }}>
                <div style={{ marginRight: '30px' }}>
                  <label className='form-label'>UID FACEBOOK</label>
                  <Field type='text' name='uid' className='form-control' placeholder='' />
                  {errors.name && touched.name ? (
                    <StyledErrorMessage>{errors.name}</StyledErrorMessage>
                  ) : null}
                </div>
                <div>
                  <label className='form-label'> PHÂN LOẠI HỘI NHÓM </label>
                  <MySelect label='Job Type' name='status_id'>
                    <option value={dataModal.status_id}>{dataModal.status_name}</option>
                    {status &&
                      status?.map((data: status, index: number) => {
                        return (
                          <option value={data.id} key={index}>
                            {data.name}
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
              <div className='mb-5' style={{ display: 'flex', flexDirection: 'row' }}>
                <div className='mr-5' style={{ marginRight: '10px' }}>
                  <label className='form-label'>SỐ LƯỢNG BẠN BÈ</label>
                  <Field
                    type='text'
                    name='reaction'
                    className='form-control form-control-white'
                    placeholder='123456'
                  />
                  {errors.reaction_count && touched.reaction_count ? (
                    <StyledErrorMessage>{errors.reaction_count}</StyledErrorMessage>
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
                </div>
                <div style={{ marginLeft: '30px', paddingTop: '40px' }}>
                  <MyCheckbox name='Vaiao'> VAI ẢO</MyCheckbox>
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
                      <MySelect label='Job Type' name='unit_id'>
                        <option value=''>Lựa chọn đơn vị</option>
                        {units &&
                          units?.map((data: unit, index: number) => {
                            console.log(data.id, dataModal.unit?.id)
                            return (
                              <option value={data.id} key={index} selected={String(data.id) === String(dataModal.unit?.id)}>
                                {data.name}
                              </option>
                            )
                          })}
                      </MySelect>
                    </div>
                    <div>
                      <label className='form-label'> CÔNG TÁC NGHIỆP VỤ </label>
                      <MySelect label='Job Type' name='task_id'>
                        <option value=''>Lựa chọn CTNV</option>
                        {tasks.map((data: task, index: number) => {
                          console.log(data.id, dataModal.task?.id)
                          return (
                            <option value={data.id} key={index} selected={String(data.id) === String(dataModal.task?.id)}>
                              {data.name}
                            </option>
                          )
                        })}
                      </MySelect>
                    </div>
                  </div>
              <div style={{ display: 'flex', flexDirection: 'row-reverse' }}>
                <button className='btn btn-info' style={{ marginLeft: '5px' }}>
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
    </Modal >,
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

const MySelect: React.FC<MySelectProps> = ({ label, width, ...props }) => {
  const [field, meta] = useField(props as any)
  console.log("field:", field.value)
  return (
    <>
      <StyledSelect {...field} {...props} style={{ width: width }} />
      {meta.touched && meta.error ? (
        <StyledErrorMessage>{meta.error}</StyledErrorMessage>
      ) : field.value === undefined || field.value === '' || field.value === 0 ? (
        <StyledErrorMessage>Vui lòng lựa chọn</StyledErrorMessage>
      ) : null}
    </>
  )
}

const MyCheckbox: React.FC<MyCheckboxProps> = ({ children, ...props }) => {
  const [field, meta] = useField(props as any)

  return (
    <div>
      <div className='form-check form-check-custom form-check-solid'>
        <input
          className='form-check-input'
          {...field}
          {...props}
          type='checkbox'
          id='flexCheckDefault'
          checked={field.value}
        />
        {children}
      </div>
      {meta.touched && meta.error ? <div className='error'>{meta.error}</div> : null}
    </div>
  )
}
const MyTextArea: React.FC<MyTextAreaProps> = ({ label, ...props }) => {
  const [field, meta] = useField(props as any)

  return (
    <>
      {/* <label htmlFor={props.id || props.name}>{label}</label> */}
      <textarea className='text-area' {...field} {...props} />
      {meta.touched && meta.error ? <div className='error'>{meta.error}</div> : null}
    </>
  )
}
export { UpdateModal }
