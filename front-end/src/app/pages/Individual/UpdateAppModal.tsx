/* eslint-disable react-hooks/exhaustive-deps */
/* eslint-disable jsx-a11y/anchor-is-valid */
import {createPortal} from 'react-dom'
import {Modal} from 'react-bootstrap'
import { useState } from 'react'
import {KTSVG} from '../../../_metronic/helpers'
import {Formik, Form, Field, useField, FieldAttributes} from 'formik'
import {individual, individualResponse, task, unit} from './individual'
import axios from 'axios'
import styled from '@emotion/styled'
// import ImageUploader, {FileObjectType as FileUploaderProps} from 'react-image-upload'
import 'react-image-upload/dist/index.css'
import ImageUploader from 'react-images-upload'
import {toast} from 'react-toastify'
import {useCallback} from 'react'
import DatePicker from 'react-datepicker'
import 'react-datepicker/dist/react-datepicker.css'
import * as Yup from 'yup'
import Avatar from 'react-avatar'
type Props = {
  show: boolean
  handleClose: () => void
  title: string
  individual: individualResponse
}
const URL = process.env.REACT_APP_API_URL
const ValidateIndividual = Yup.object().shape({
  date_of_birth: Yup.date().required(),
  id_number: Yup.string()
    .length(12)
    .matches(/^\d+$/, 'Số national_id có độ dài 9 chữ số'),
  phone_number: Yup.string()
    .length(10)
    .matches(/^\d+$/, 'Số điện thoại có độ dài 10 chữ số'),
  kols_type: Yup.string().required(),
  full_name: Yup.string().required(),
  hometown: Yup.string().required(),
})
const modalsRoot = document.getElementById('root-modals') || document.body
const UpdateModal = ({show, handleClose, title, individual}: Props) => {
  const unitString = localStorage.getItem('unit')
  const [is_kol, setKOL]= useState<boolean>(true)
  const unit: unit[] = typeof unitString === 'string' ? JSON.parse(unitString) : []
  const taskString = localStorage.getItem('task')
  const task: task[] = typeof taskString === 'string' ? JSON.parse(taskString) : []
  const individualclone = {
    ...individual,
    is_male: individual.is_male ? "1" : "2",
  }
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
          initialValues={individualclone}
          validationSchema={ValidateIndividual}
          onSubmit={(data: any) => {
            data.date_of_birth = new Date(data.date_of_birth).toISOString().split('T')[0]
            data.is_male === '1' ? (data.is_male = true) : (data.is_male = false)
            axios
              .post(`${URL}/individuals/${individual.id}`, data)
              .then((res) => {
                if (res.status === 200) {
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
                } else {
                  let data = res.data.message
                  toast.warning(data, {
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
                let data = error.response.data.message
                toast.warning(data, {
                  position: 'bottom-right',
                  autoClose: 5000,
                  hideProgressBar: false,
                  closeOnClick: true,
                  pauseOnHover: true,
                  draggable: true,
                  progress: undefined,
                  theme: 'light',
                })
              })
            console.log(data)
          }}
        >
          {({errors, touched}) => (
            <Form>
              <div className='mb-5' style={{display: 'flex', flexDirection: 'row'}}>
                <div style={{display: 'flex', flexDirection: 'column'}}>
                  {individual.image_url? 
                  <img src={individual.image_url} width={250} height={250} alt='Ảnh đại diện' />:<Avatar name={individual.full_name}  size='100' />
}
                  <ImagUploder name='image_url' />
                </div>
                <div style={{marginLeft: '30px'}}>
                  <div style={{display: 'flex', flexDirection: 'row'}}>
                    <div>
                      <label className='form-label'>TÊN ĐỐI TƯỢNG</label>
                      <Field
                        type='text'
                        name='full_name'
                        className='form-control'
                        placeholder=''
                        style={{width: '500px'}}
                      />
                      {errors.full_name && touched.full_name ? (
                        <StyledErrorMessage>{errors.full_name}</StyledErrorMessage>
                      ) : null}
                    </div>
                    <div style={{marginLeft: '30px', paddingTop: '40px'}}>
                      <MyCheckbox name='is_kol' setKOL={setKOL} is_kol ={is_kol}>KOLs</MyCheckbox>
                    </div>
                  </div>
                  <div style={{display: 'flex', flexDirection: 'row'}}>
                    <div className='mb-5'>
                      <label className='form-label'>CCCD/CMND</label>
                      <Field
                        type='text'
                        className='form-control'
                        name='id_number'
                        placeholder='042......'
                      />
                      {errors.id_number && touched.id_number ? (
                        <StyledErrorMessage>{errors.id_number}</StyledErrorMessage>
                      ) : null}
                    </div>
                    <div className='mb-5' style={{marginLeft: '30px'}}>
                      <label className='form-label'>Số điện thoại</label>
                      <Field
                        type='text'
                        className='form-control'
                        name='phone_number'
                        placeholder='18......'
                      />
                      {errors.phone_number && touched.phone_number ? (
                        <StyledErrorMessage>{errors.phone_number}</StyledErrorMessage>
                      ) : null}
                    </div>
                    <div style={{display: 'flex', flexDirection: 'row', marginLeft: '30px'}}>
                      <div
                        role='group'
                        aria-labelledby='my-radio-group'
                        style={{display: 'flex', flexDirection: 'row'}}
                      >
                        <div
                          className='form-check form-check-custom form-check-solid'
                          style={{marginRight: '30px'}}
                        >
                          <label>
                            <Field type='radio' name='is_male' value='1' />
                            Nam
                          </label>
                        </div>
                        <div className='form-check form-check-custom form-check-solid'>
                          <label>
                            <Field type='radio' name='is_male' value='2' />
                            Nữ
                          </label>
                        </div>
                      </div>
                    </div>
                  </div>
                  <div style={{display: 'flex', flexDirection: 'row'}}>
                    <div className='mb-5' style={{paddingRight: '30px'}}>
                      <label className='form-label'> LOẠI KOLS </label>
                      <MySelect label='Job Type' name='kols_type' disabled={!is_kol} width={200}>
                        <option value=''>Lựa chọn loại KOLS</option>
                        <option value='KOLS MẠNG'>KOLS MẠNG</option>
                        <option value='KOLS UY TÍN'>KOLS UY TÍN</option>
                        <option value='KOLS ẨN'>KOLS ẨN</option>
                      </MySelect>
                      {errors.kols_type && touched.kols_type ? (
                        <StyledErrorMessage>{errors.kols_type}</StyledErrorMessage>
                      ) : null}
                    </div>
                    <div>
                      <label className='form-label'>Ngày/tháng/năm sinh</label>
                      <MyDatePicker name='date_of_birth' />
                    </div>
                  </div>
                  <div className='mb-5'>
                    <label className='form-label'>Quê quán</label>
                    <Field
                      type='text'
                      className='form-control'
                      name='hometown'
                      placeholder='Xã .....'
                    />
                    {errors.hometown && touched.hometown ? (
                      <StyledErrorMessage>{errors.hometown}</StyledErrorMessage>
                    ) : null}
                  </div>
                  <div className='mb-5'>
                    <label className='form-label'>Thông tin bổ sung</label>
                    <MyTextArea
                      label='Ghi chú'
                      name='additional_info'
                      rows='6'
                      placeholder='Nhập các thông tin của đối tượng, bao gồm số điện thoại, tính cách, liên quan, ....Tất cả thông tin này được dùng để tìm kiếm chính xác'
                    />
                  </div>
                  <div className='mb-5' style={{display: 'flex', flexDirection: 'row'}}>
                    <div style={{marginRight: '30px'}}>
                      <label className='form-label'> ĐƠN VỊ THỰC HIỆN CÔNG TÁC NGHIỆP VỤ </label>
                      <MySelect label='Job Type' name='unit_id'>
                        <option value=''>Lựa chọn đơn vị</option>
                        {unit &&
                          unit?.map((data: unit, index: number) => {
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
                      <MySelect label='Job Type' name='task_id'>
                        <option value=''>Lựa chọn CTNV</option>
                        {task.map((data: task, index: number) => {
                          return (
                            <option value={data.id} key={index}>
                              {data.name}
                            </option>
                          )
                        })}
                      </MySelect>
                    </div>
                  </div>
                </div>
              </div>
              <div style={{display: 'flex', flexDirection: 'row-reverse'}}>
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
interface ImageuploadProps extends FieldAttributes<any> {
  name: string
}
const StyledSelect = styled.select`
  color: var(--blue-700);
`
export interface ToggleFieldProps {
  name: string
}

// toggle field converts yes or no to true or false
export const ToggleField = (props: ToggleFieldProps) => {
  const [field] = useField<boolean>(props)

  // Yes = true, otherwise false
  const handleChange = useCallback(
    (event: any) => field.onChange(event.target.value === 'Yes'),
    [field.onChange]
  )

  // use `field` but override onChange
  return (
    <>
      <label>
        <Field {...field} type='radio' value='Yes' onChange={handleChange} />
        Yes
      </label>
      <label>
        <Field {...field} type='radio' value='No' onChange={handleChange} />
        No
      </label>
    </>
  )
}
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
const ImagUploder: React.FC<ImageuploadProps> = ({name, ...props}) => {
  const [field, meta, helpers] = useField(name)
  const {value} = meta
  const {setValue} = helpers
  return (
    <>
      <ImageUploader
        withIcon={false}
        withPreview={true}
        label={''}
        buttonText='Thay ảnh đại diện'
        buttonClassName='upload-btn waves-effect waves-light red light-blue darken-4'
        imgExtension={['.jpg', '.gif', '.png', '.gif']}
        onChange={(e, f) => setValue(f[0])}
        maxFileSize={5242880}
        fileContainerStyle={{
          borderRedius: '30px',
          border: '2px solid #eae8e8',
        }}
      />
    </>
  )
}
const MyDatePicker = ({name = '', ...rest}) => {
  const [field, meta, helpers] = useField(name)

  const {value} = meta
  const {setValue} = helpers

  return (
    <div style={{display: 'flex', flexDirection: 'column'}}>
      <DatePicker {...field} {...rest} selected={value} onChange={(date) => setValue(date)} />
      {meta.error && meta.touched && <StyledErrorMessage>{meta.error}</StyledErrorMessage>}
    </div>
  )
}

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
const MyCheckbox: React.FC<MyCheckboxProps> = ({children,setKOL, is_kol ,...props}) => {
  const [field, meta, helpers] = useField(props as any)
  const handleCheckboxChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const newValue = e.target.checked; // Get the new value of the checkbox
    helpers.setValue(newValue); // Update the formik field value
    setKOL(newValue); // Update is_kol state
  };
  return (
    <div style={{display: 'flex', alignItems: 'center', justifyContent: 'space-between'}}>
      <div className='form-check form-check-custom form-check-solid'>
        <input
          className='form-check-input'
          {...field}
          {...props}
          type='checkbox'
          id='flexCheckDefault'
          style={{paddingRight: '10px'}}
          checked={field.value}
          onChange={handleCheckboxChange}
        />
        {children}
      </div>
      {meta.touched && meta.error ? <div className='error'>{meta.error}</div> : null}
    </div>
  )
}
const MyTextArea: React.FC<MyTextAreaProps> = ({label, ...props}) => {
  const [field, meta] = useField(props as any)

  return (
    <>
      {/* <label htmlFor={props.id || props.name}>{label}</label> */}
      <textarea className='text-area' {...field} {...props} />
      {meta.touched && meta.error ? (
        <StyledErrorMessage>{meta.error}</StyledErrorMessage>
      ) : field.value === undefined || field.value === '' || field.value === 0 ? (
        <StyledErrorMessage>Vui lòng lựa chọn</StyledErrorMessage>
      ) : null}
    </>
  )
}
export {UpdateModal}
