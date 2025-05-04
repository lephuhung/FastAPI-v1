/* eslint-disable react-hooks/exhaustive-deps */
/* eslint-disable jsx-a11y/anchor-is-valid */
import { createPortal } from 'react-dom'
import { Modal } from 'react-bootstrap'
import { KTSVG } from '../../../_metronic/helpers'
import { Formik, Form, Field, useField, FieldAttributes } from 'formik'
import { individual, units, tasks } from './individual'
import axios from 'axios'
import styled from '@emotion/styled'
// import ImageUploader, {FileObjectType as FileUploaderProps} from 'react-image-upload'
import 'react-image-upload/dist/index.css'
import ImageUploader from 'react-images-upload'
import { useCallback, useState } from 'react'
import DatePicker from 'react-datepicker'
import { toast } from 'react-toastify'
import 'react-datepicker/dist/react-datepicker.css'
import * as Yup from 'yup'
type Props = {
  show: boolean
  handleClose: () => void
  title: string
}
const URL = process.env.REACT_APP_API_URL
const ValidateDoituong = Yup.object().shape({
  date_of_birth: Yup.date().required(),
  citizen_id: Yup.string()
    .length(12)
    .matches(/^\d+$/, 'Số CMND có độ dài 9 chữ số'),
  national_id: Yup.string()
    .length(9)
    .matches(/^\d+$/, 'Số CCCD có độ dài 12 chữ số'),
  full_name: Yup.string().required(),
  hometown: Yup.string().required(),
  additional_info: Yup.string().required(),
})
const labelStyle = {
  display: 'inline-block',
  marginRight: '20px',
  fontFamily: 'Arial, sans-serif',
  fontSize: '16px',
  color: '#333'
};

const radioStyle = {
  marginRight: '5px',
  verticalAlign: 'middle'
};
const CreateAppModal = ({ show, handleClose, title }: Props) => {
  const unitsString = localStorage.getItem('units')
  const [KOLL, setKOLL] = useState<boolean>(false)
  const units: units[] = typeof unitsString === 'string' ? JSON.parse(unitsString) : []
  const tasksString = localStorage.getItem('tasks')
  const tasks: tasks[] = typeof tasksString === 'string' ? JSON.parse(tasksString) : []
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
            full_name: '',
            national_id: '',
            citizen_id: '',
            image_url: '',
            date_of_birth: '',
            is_male: '1',
            hometown: '',
            additional_info: 'Chưa có thông tin',
            phone_number: '',
            is_kol: false,
            task_id: 0,
            unit_id: '',
          }}
          validationSchema={ValidateDoituong}
          onSubmit={(data: any) => {
            data.date_of_birth = new Date(data.date_of_birth).toISOString().split('T')[0]
            data.is_male === '1' ? (data.is_male = true) : (data.is_male = false)
            // Tách unit_id và task_id ra khỏi data
            const { unit_id, task_id, ...individualData } = data

            // Tạo đối tượng gửi lên server
            const requestData = {
              ...individualData,
              individual_units: unit_id && task_id ? [{
                unit_id: unit_id,
                task_id: task_id
              }] : []
            }
            axios
              .post(`${URL}/individuals`, requestData)
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
                <ImagUploder name='image_url' />
                <div style={{ marginLeft: '30px' }}>
                  <div style={{ display: 'flex', flexDirection: 'row' }}>
                    <div>
                      <label className='form-label'>TÊN ĐỐI TƯỢNG</label>
                      <Field
                        type='text'
                        name='full_name'
                        className='form-control'
                        placeholder=''
                        style={{ width: '500px' }}
                      />
                      {errors.full_name && touched.full_name ? (
                        <StyledErrorMessage>{String(errors.full_name)}</StyledErrorMessage>
                      ) : null}
                    </div>
                    <div style={{ marginLeft: '30px', paddingTop: '40px' }}>
                      <MyCheckbox name='is_kol' setKOL={setKOLL} KOL={KOLL}>  {`  KOL`}</MyCheckbox>
                    </div>
                  </div>
                  <div style={{ display: 'flex', flexDirection: 'row' }}>
                    <div className='mb-5'>
                      <label className='form-label'>CCCD</label>
                      <Field
                        type='text'
                        className='form-control'
                        name='citizen_id'
                        placeholder='042......'
                      />
                      {errors.citizen_id && touched.citizen_id ? (
                        <StyledErrorMessage>{String(errors.citizen_id)}</StyledErrorMessage>
                      ) : null}
                    </div>
                    <div className='mb-5' style={{ marginLeft: '30px' }}>
                      <label className='form-label'>CMND</label>
                      <Field
                        type='text'
                        className='form-control'
                        name='national_id'
                        placeholder='18......'
                      />
                      {errors.national_id && touched.national_id ? (
                        <StyledErrorMessage>{String(errors.national_id)}</StyledErrorMessage>
                      ) : null}
                    </div>
                    <div style={{ display: 'flex', flexDirection: 'row', marginLeft: '30px' }}>
                      <div
                        role='group'
                        aria-labelledby='my-radio-group'
                        style={{ display: 'flex', flexDirection: 'row', alignItems: 'center' }}
                      >
                        <div
                          className='form-check form-check-custom form-check-solid'
                          style={{ marginRight: '30px' }}
                        >
                          <label style={labelStyle}>
                            <Field type='radio' name='is_male' value='1' style={radioStyle} />
                            Nam
                          </label>
                        </div>
                        <div className='form-check form-check-custom form-check-solid'>
                          <label style={labelStyle}>
                            <Field type='radio' name='is_male' value='2' style={radioStyle} />
                            Nữ
                          </label>
                        </div>
                      </div>
                    </div>
                  </div>
                  <div style={{ display: 'flex', flexDirection: 'row' }}>
                    <div className='mb-5' style={{ paddingRight: '30px' }}>
                      <label className='form-label'> Số điện thoại  </label>
                      <Field
                        type='text'
                        className='form-control'
                        name='phone_number'
                        placeholder='09.....'
                      />
                      {errors.phone_number && touched.phone_number ? (
                        <StyledErrorMessage>{String(errors.phone_number)}</StyledErrorMessage>
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
                      <StyledErrorMessage>{String(errors.hometown)}</StyledErrorMessage>
                    ) : null}
                  </div>
                  <div className='mb-5'>
                    <label className='form-label'>Thông tin bổ sung</label>
                    <MyTextArea
                      label='Ghi chú'
                      name='additional_info'
                      rows='6'
                      placeholder='Once upon a time there was a princess who lived at the top of a glass hill.'
                    />
                  </div>
                  <div className='mb-5' style={{ display: 'flex', flexDirection: 'row' }}>
                    <div style={{ marginRight: '30px' }}>
                      <label className='form-label'> ĐƠN VỊ THỰC HIỆN CÔNG TÁC NGHIỆP VỤ </label>
                      <MySelect label='Job Type' name='unit_id' width={200}>
                        <option value=''>Lựa chọn đơn vị</option>
                        {units &&
                          units?.map((data: units, index: number) => {
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
                      <MySelect label='Job Type' name='task_id' width={200}>
                        <option value=''>Lựa chọn CTNV</option>
                        {tasks.map((data: tasks, index: number) => {
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
    </Modal>,
    modalsRoot
  )
}
interface MyTextAreaProps extends FieldAttributes<any> {
  label: string
}
interface MyCheckboxProps extends FieldAttributes<any> {
  children: React.ReactNode
  setKOL?: (value: boolean) => void
  KOL?: boolean
  name: string
}
interface MySelectProps extends FieldAttributes<any> {
  label: string
  width: number | undefined
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
export const ToggleField = (props: ToggleFieldProps) => {
  const [field] = useField<boolean>(props)
  const handleChange = useCallback(
    (event: any) => field.onChange(event.target.value === 'Yes'),
    [field.onChange]
  )

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
const ImagUploder: React.FC<ImageuploadProps> = ({ name, ...props }) => {
  const [field, meta, helpers] = useField(name)
  const { value } = meta
  const { setValue } = helpers
  return (
    <>
      <ImageUploader
        withIcon={false}
        withPreview={true}
        label={''}
        buttonText='Thêm ảnh đại diện'
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
const MyDatePicker = ({ name = '', ...rest }) => {
  const [field, meta, helpers] = useField(name)

  const { value } = meta
  const { setValue } = helpers

  return (
    <div style={{ display: 'flex', flexDirection: 'column' }}>
      <DatePicker {...field} {...rest} selected={value} onChange={(date) => setValue(date)} />
      {meta.error && meta.touched && <StyledErrorMessage>{meta.error}</StyledErrorMessage>}
    </div>
  )
}

const MySelect: React.FC<MySelectProps> = ({ label, width, ...props }) => {
  const [field, meta] = useField(props as any)
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
const MyCheckbox: React.FC<MyCheckboxProps> = ({ children, setKOL, KOL, name, ...props }) => {
  const [field, meta, helpers] = useField(props as any)
  const handleCheckboxChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const newValue = e.target.checked; // Get the new value of the checkbox
    helpers.setValue(newValue); // Update the formik field value
    setKOL && setKOL(newValue); // Update KOL state if setKOL exists
  };
  return (
    <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
      <div className='form-check form-check-custom form-check-solid' style={{ display: 'flex', alignItems: 'center' }}>
        <input
          className='form-check-input'
          {...field}
          {...props}
          type='checkbox'
          id='flexCheckDefault'
          style={{ paddingRight: '10px' }}
          checked={field.value}
          onChange={handleCheckboxChange}
        />
        {children}
      </div>
      {meta.touched && meta.error ? <div className='error'>{meta.error}</div> : null}
    </div>
  )
}

const modalsRoot = document.getElementById('root-modals') || document.body
const MyTextArea: React.FC<MyTextAreaProps> = ({ label, ...props }) => {
  const [field, meta] = useField(props as any)

  return (
    <>
      {/* <label htmlFor={props.id || props.name}>{label}</label> */}
      <textarea className='text-area' {...field} {...props} />
      {meta.touched && meta.error ? (
        <StyledErrorMessage>{meta.error}</StyledErrorMessage>
      ) : field.value === undefined || field.value === '' || field.value === 0 ? (
        <StyledErrorMessage>Nhập thông tin bổ sung</StyledErrorMessage>
      ) : null}
    </>

  )
}
export { CreateAppModal }
