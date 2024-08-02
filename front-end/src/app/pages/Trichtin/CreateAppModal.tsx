/* eslint-disable react-hooks/exhaustive-deps */
/* eslint-disable jsx-a11y/anchor-is-valid */
import {createPortal} from 'react-dom'
import {Modal} from 'react-bootstrap'
import {KTSVG} from '../../../_metronic/helpers'
import {Formik, Form, Field, useField, FieldAttributes} from 'formik'
import axios from 'axios'
import {toast} from 'react-toastify'
import {useParams} from 'react-router-dom'
import styled from '@emotion/styled'
// import ImageUploader, {FileObjectType as FileUploaderProps} from 'react-image-upload'
import 'react-image-upload/dist/index.css'
import {useCallback} from 'react'
import 'react-datepicker/dist/react-datepicker.css'
import {useQuery} from 'react-query'
import * as Yup from 'yup'
type Props = {
  show: boolean
  handleClose: () => void
  title: string
}
const URL = process.env.REACT_APP_API_URL

const Validatetrichtin = Yup.object().shape({
  nhanxet: Yup.string().required('Nhập nội dung nhận xét'),
  ghichu_noidung: Yup.string().required('Nhập nội dung trích tin'),
  xuly: Yup.string().required(),
})
const CreateAppModal = ({show, handleClose, title}: Props) => {
  const {id} = useParams()
  const {isLoading, data, error} = useQuery({
    queryKey: ['facebook'],
    queryFn: async () => {
      const respone = await axios.get(`${URL}/uid/get-vaiao`)
      const {data} = respone
      return data
    },
  })
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
            uid: id,
            ghichu_noidung: '',
            nhanxet: '',
            xuly: '',
            uid_vaiao: '',
          }}
          validationSchema={Validatetrichtin}
          onSubmit={(data: any) => {
            axios
              .post(`${URL}/trichtin/create`, data)
              .then((res) => {
                handleClose()
                toast.success('Thêm trích tin thành công', {
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
              .catch((e) => {
                toast.warning('Thêm trích tin không thành công', {
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
          }}
        >
          {({errors, touched}) => (
            <Form>
              <div className='mb-5'>
                <div style={{marginLeft: '30px'}}>
                  <div style={{display: 'flex', flexDirection: 'row'}}>
                    <div>
                      <label className='form-label'>ID Đối tượng</label>
                      <Field
                        type='text'
                        name='uid'
                        className='form-control'
                        placeholder=''
                        disabled={true}
                        style={{width: '500px'}}
                      />
                    </div>
                    <div style={{paddingLeft: '20px'}}>
                      <label className='form-label'> VAI ẢO TRÍCH TIN </label>
                      <MySelect label='Job Type' name='uid_vaiao'>
                        <option value=''>Lựa chọn Vai ảo </option>
                        {data &&
                          data.map((data: any, index: number) => {
                            return (
                              <option value={data.uid} key={index}>
                                {data.name}
                              </option>
                            )
                          })}
                      </MySelect>
                    </div>
                  </div>
                  <div className='mb-5'>
                    <label className='form-label'>NỘI DUNG TRÍCH TIN</label>
                    <MyTextArea
                      label='Trích tin'
                      name='ghichu_noidung'
                      rows='6'
                      placeholder='Once upon a time there was a princess who lived at the top of a glass hill.'
                    />
                  </div>
                  <div className='mb-5'>
                    <label className='form-label'>NHẬN XÉT</label>
                    <MyTextArea
                      label='Nhận xét'
                      name='nhanxet'
                      rows='6'
                      placeholder='Once upon a time there was a princess who lived at the top of a glass hill.'
                    />
                  </div>
                  <div className='mb-5'>
                    <label className='form-label'>ĐỀ XUẤT XỬ LÝ</label>
                    <MyTextArea
                      label='Xử lý'
                      name='xuly'
                      rows='6'
                      placeholder='Once upon a time there was a princess who lived at the top of a glass hill.'
                    />
                  </div>
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
const modalsRoot = document.getElementById('root-modals') || document.body
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
export {CreateAppModal}
