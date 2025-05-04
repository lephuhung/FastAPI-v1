/* eslint-disable react-hooks/exhaustive-deps */
/* eslint-disable jsx-a11y/anchor-is-valid */

import {createPortal} from 'react-dom'
import {Modal} from 'react-bootstrap'
// import {defaultCreateAppData, ICreateAppData} from './IAppModels'
// import {StepperComponent} from '../../../assets/ts/components'
import {KTSVG} from '../../../_metronic/helpers'
import {Formik, Form, Field, useField, FieldAttributes} from 'formik'
import {account_type, status, unit, task, characteristics, relationship, SocialAccountResponse, SocialAccountTypeResponse, SocialAccountTypeGroup, SocialAccountSimple} from './SocialAccount'
import {toast} from 'react-toastify'
import instance from '../../modules/axiosInstance'
import '../SocialAccount/style.css'
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

const getTypeColor = (typeId: number) => {
  switch (typeId) {
    case 1: // Facebook cá nhân
      return '#1a73e8' // Blue
    case 2: // Nhóm Facebook
      return '#34a853' // Green
    case 3: // Fanpage Facebook/KOL
      return '#ea4335' // Red
    default:
      return '#5f6368' // Gray
  }
}

const CreateModelMLH = ({show, handleClose, handleLoading, title}: Props) => {
  const [dataadmin, setDataAdmin] = useState<Array<SocialAccountSimple & { type_id: number, type_name: string }>>([])
  const [data_relationship, setDataRelationship] = useState<characteristics[]>([])
  const [datarelation, setDataRelation] = useState<Array<SocialAccountSimple & { type_id: number, type_name: string }>>([])

  // Group data by type
  const groupDataByType = (data: Array<SocialAccountSimple & { type_id: number, type_name: string }>) => {
    return data.reduce((acc, item) => {
      const type = item.type_name.toUpperCase();
      if (!acc[type]) {
        acc[type] = [];
      }
      acc[type].push(item);
      return acc;
    }, {} as Record<string, typeof data>);
  };

  useEffect(() => {
    axios.get(`${URL}/relationships`).then((response) => {
      setDataRelationship(response.data)
    })
    axios.get(`${URL}/social-accounts/admin-accounts`).then((response) => {
      const transformedData = response.data.data.flatMap((typeGroup: any) => 
        typeGroup.data.map((account: any) => ({
          uid: account.uid,
          name: account.name,
          type_id: typeGroup.type_id,
          type_name: typeGroup.type_name
        }))
      )
      setDataAdmin(transformedData)
    })
    axios.get(`${URL}/social-accounts/relation-accounts`).then((response) => {
      const transformedData = response.data.data.flatMap((typeGroup: any) => 
        typeGroup.data.map((account: any) => ({
          uid: account.uid,
          name: account.name,
          type_id: typeGroup.type_id,
          type_name: typeGroup.type_name
        }))
      )
      setDataRelation(transformedData)
    })
  }, [])

  // Group admin and relation data
  const groupedAdminData = groupDataByType(dataadmin);
  const groupedRelationData = groupDataByType(datarelation);

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
        <div className='btn btn-sm btn-icon btn-active-color-primary' onClick={handleClose}>
          <KTSVG className='svg-icon-1' path='/media/icons/duotune/arrows/arr061.svg' />
        </div>
      </div>
      <div className='modal-body py-lg-10 px-lg-10'>
        <Formik
          initialValues={{
            uid_administrator: '',
            relationship_id: 0,
            social_account_uid: ''
          }}
          onSubmit={(values: any) => {
            console.log(values)
            axios
              .post(`${URL}/administrators`, values)
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
                  console.log('An error occurred:', error.message)
                }
              })
          }}
        >
        {({errors, touched}) => (
          <Form>
            <span>Bảng dữ liệu này nhằm đưa ra mối liên hệ giữa tài khoản Facebook với Nhóm Facebook hoặc Trang Facebook</span>
            <div className='mb-5' style={{display: 'flex', flexDirection: 'row', flexWrap: 'wrap', gap: '20px'}}>
              <div>
                <label className='form-label'>TÀI KHOẢN ADMIN</label>
                <MySelect label='Job Type' name='uid_administrator' width={250}>
                  <option value=''>Lựa chọn tài khoản admin</option>
                  {Object.entries(groupedAdminData).map(([typeName, accounts]) => (
                    <optgroup key={typeName} label={typeName}>
                      {accounts.map((data, index) => (
                        <option value={data.uid} key={index}>
                          {`${data.uid}: ${data.name.toUpperCase()}`}
                        </option>
                      ))}
                    </optgroup>
                  ))}
                </MySelect>
              </div>
              <div>
                <label className='form-label'>MỐI QUAN HỆ</label>
                <MySelect label='Job Type' name='relationship_id' width={150}>
                  <option value=''>Lựa chọn MQH</option>
                  {data_relationship.map((data: relationship, index: number) => (
                    <option value={data.id} key={index}>
                      {data.name.toUpperCase()}
                    </option>
                  ))}
                </MySelect>
              </div>
              <div>
                <label className='form-label'>TÀI KHOẢN QUAN HỆ</label>
                <MySelect label='Job Type' name='social_account_uid' width={250}>
                  <option value=''>Lựa chọn tài khoản quan hệ</option>
                  {Object.entries(groupedRelationData).map(([typeName, accounts]) => (
                    <optgroup key={typeName} label={typeName}>
                      {accounts.map((data, index) => (
                        <option value={data.uid} key={index}>
                          {`${data.uid}: ${data.name.toUpperCase()}`}
                        </option>
                      ))}
                    </optgroup>
                  ))}
                </MySelect>
              </div>
            </div>
            <div style={{display: 'flex', flexDirection: 'row-reverse', gap: '10px'}}>
              <button className='btn btn-info'>
                Xóa dữ liệu
              </button>
              <button className='btn btn-primary' type='submit'>
                Lưu
              </button>
            </div>
          </Form>)}
        </Formik>
      </div>
    </Modal>,
    modalsRoot
  )
}
interface MySelectProps extends FieldAttributes<any> {
  label: string
  width?: number
  name: string
  children?: React.ReactNode
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
export {CreateModelMLH}
