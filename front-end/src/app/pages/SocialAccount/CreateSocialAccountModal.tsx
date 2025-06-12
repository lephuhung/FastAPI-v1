/* eslint-disable react-hooks/exhaustive-deps */
/* eslint-disable jsx-a11y/anchor-is-valid */

import {createPortal} from 'react-dom'
import {Modal} from 'react-bootstrap'
// import {defaultCreateAppData, ICreateAppData} from './IAppModels'
// import {StepperComponent} from '../../../assets/ts/components'
import {KTSVG} from '../../../_metronic/helpers'
import {Formik, Form, Field, useField, FieldAttributes} from 'formik'
import {
  account_type,
  SocialAccountModal,
  status,
  unit,
  task,
  characteristics,
  tag,
} from './SocialAccount'
import {toast} from 'react-toastify'
import {useNavigate} from 'react-router-dom'
import './style.css'
import {useEffect, useState} from 'react'
import styled from '@emotion/styled'
import axios from 'axios'
import * as Yup from 'yup'
import {WithContext as ReactTags, SEPARATORS} from 'react-tag-input'
// import 'react-tag-input/example/reactTags.css'
// import styled from 'styled-components';
import './tag.css'
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
  reaction_count: Yup.string()
    .required('Số bạn bè cần nhập')
    .matches(/^\d+$/, 'Số lượng bạn bè chỉ nhận ký tự số'),
  phone_number: Yup.string()
    .min(0, 'Quá ngắn')
    .max(11, 'Quá dài')
    .matches(/^\d+$/, 'Số điện thoại là ký tự số, nếu không có điền 0'),
  name: Yup.string().required(),
})
const CreateSocialAccountModal = ({show, handleClose, handleLoading, title}: Props) => {
  const PUBLIC_URL = process.env.PUBLIC_URL
  const unitsString = localStorage.getItem('units')
  const navigate = useNavigate()
  const units: unit[] = typeof unitsString === 'string' ? JSON.parse(unitsString) : []
  const account_typeString = localStorage.getItem('account_types')
  const account_type: account_type[] =
    typeof account_typeString === 'string' ? JSON.parse(account_typeString) : []
  const characteristicsString = localStorage.getItem('characteristics')
  const characteristics: characteristics[] =
    typeof characteristicsString === 'string' ? JSON.parse(characteristicsString) : []
  const tasksString = localStorage.getItem('tasks')
  const tasks: task[] = typeof tasksString === 'string' ? JSON.parse(tasksString) : []
  const statusString = localStorage.getItem('statuses')
  const status: status[] = typeof statusString === 'string' ? JSON.parse(statusString) : []
  const tagsString = localStorage.getItem('tags')
  const tagsdata: tag[] = typeof tagsString === 'string' ? JSON.parse(tagsString) : []
  const [tags, setTags] = useState<Array<tag>>(tagsdata);
  const handleDelete = (index: number) => {
    setTags(tags.filter((_, i) => i !== index));
  };

  const onTagUpdate = (index: number, newTag: tag) => {
    const updatedTags = [...tags];
    updatedTags.splice(index, 1, newTag);
    setTags(updatedTags);
  };

  const handleAddition = (tag: tag) => {
    setTags((prevTags) => {
      return [...prevTags, tag];
    });
  };

  const handleDrag = (tag: tag, currPos: number, newPos: number) => {
    const newTags = tags.slice();

    newTags.splice(currPos, 1);
    newTags.splice(newPos, 0, tag);

    // re-render
    setTags(newTags);
  };

  const handleTagClick = (index: number) => {
    console.log('The tag at index ' + index + ' was clicked');
  };

  const onClearAll = () => {
    setTags([]);
  };
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
            phone_number: '0',
            reaction_number: 0,
            type_id: 0,
            characteristics_id: 0,
            note: '',
            task_id: 0,
            unit_id: '',
            status_id: 0,
            is_active: true,
            tags: [],
          }}
          validationSchema={ValidateUid}
          onSubmit={(values: SocialAccountModal) => {
            axios
              .post(`${URL}/social-accounts`, values)
              .then((respone) => {
                console.log(respone.status)
                if (respone.status === 200) {
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
              })
              .catch((error) => {
                if (error.response && error.response.status === 403) {
                  navigate(`${PUBLIC_URL}/auth`)
                }
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
          {({errors, touched}) => (
            <Form>
              <div
                className='mb-5'
                style={{display: 'flex', flexDirection: 'row', alignItems: 'center'}}
              >
                <div style={{marginRight: '30px'}}>
                  <label className='form-label'>UID TÀI KHOẢN MẠNG XÃ HỘI</label>
                  <Field type='text' name='uid' className='form-control' placeholder='' />
                  {errors.uid && touched.uid ? (
                    <StyledErrorMessage>{errors.uid}</StyledErrorMessage>
                  ) : null}
                </div>
                <div>
                  <label className='form-label'> TRẠNG THÁI TÀI KHOẢN</label>
                  <MySelect label='Job Type' name='status_id' width={200}>
                    <option value=''>Lựa chọn trạng thái</option>
                    {status.map((data: status, index: number) => {
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
                  <MySelect label='Job Type' name='characteristics_id' width={200}>
                    <option value=''>Lựa chọn tính chất</option>
                    {characteristics.map((data: characteristics, index: number) => {
                      return (
                        <option value={data.id} key={index}>
                          {data.name.toUpperCase()}
                        </option>
                      )
                    })}
                  </MySelect>
                </div>
                <div style={{marginLeft: '30px', display: 'flex', alignItems: 'center'}}>
                  <MyCheckbox name='is_active' checked={true}>
                    <span className='form-label'>HOẠT ĐỘNG</span>
                  </MyCheckbox>
                </div>
              </div>
              <div className='mb-5'>
                <label className='form-label'>TÊN TÀI KHOẢN</label>
                <Field type='text' className='form-control' name='name' placeholder='LÊ PHÚ HƯNG' />
                {errors.name && touched.name ? (
                  <StyledErrorMessage>{errors.name}</StyledErrorMessage>
                ) : null}
              </div>
              <div className='mb-5' style={{display: 'flex', flexDirection: 'row'}}>
                <div className='mr-5' style={{marginRight: '10px'}}>
                  <label className='form-label'>SỐ LƯỢNG BẠN B/THEO DÕI</label>
                  <Field
                    type='text'
                    name='reaction_number'
                    className='form-control form-control-white'
                    placeholder='123456'
                  />
                  {errors.reaction_number && touched.reaction_number ? (
                    <StyledErrorMessage>{errors.reaction_number}</StyledErrorMessage>
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
                  {errors.phone_number && touched.phone_number ? (
                    <StyledErrorMessage>{errors.phone_number}</StyledErrorMessage>
                  ) : null}
                </div>
                <div style={{marginLeft: '30px', paddingTop: '40px'}}>
                  <MySelect label='Job Type' name='type_id'>
                    <option value=''>Lựa chọn loại mạng xã hội</option>
                    {account_type &&
                      account_type?.map((data: account_type, index: number) => {
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
                    {tasks.map((data: task, index: number) => {
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
                <label className='form-label'>Tags</label>
                <div>
                  <Field name="tags">
                    {({ field, form }) => (
                      <ReactTags
                        tags={field.value}
                        suggestions={tagsdata}
                        delimiters={[SEPARATORS.ENTER, SEPARATORS.COMMA]}
                        handleDelete={(i:any) => {
                          const newTags = field.value.filter((tag:any, idx:any) => idx !== i)
                          form.setFieldValue('tags', newTags)
                        }}
                        handleAddition={(tag:any) => {
                          form.setFieldValue('tags', [...field.value, tag])
                        }}
                        handleDrag={(tag:any, currPos:any, newPos:any) => {
                          const newTags = [...field.value]
                          newTags.splice(currPos, 1)
                          newTags.splice(newPos, 0, tag)
                          form.setFieldValue('tags', newTags)
                        }}
                        inputFieldPosition="bottom"
                        placeholder="Nhập tag và nhấn Enter"
                        autocomplete
                      />
                    )}
                  </Field>
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
    <div style={{display: 'flex', alignItems: 'center'}}>
      <div
        className='form-check form-check-custom form-check-solid'
        style={{display: 'flex', alignItems: 'center'}}
      >
        <input
          className='form-check-input'
          {...field}
          {...props}
          type='checkbox'
          id='flexCheckDefault'
          style={{marginRight: '10px'}}
          checked={field.value}
        />
        <label style={{marginBottom: 0}}>{children}</label>
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
      {meta.touched && meta.error ? <div className='error'>{meta.error}</div> : null}
    </>
  )
}
export {CreateSocialAccountModal}
