/* eslint-disable react-hooks/exhaustive-deps */
/* eslint-disable jsx-a11y/anchor-is-valid */
import {useState} from 'react'
import {createPortal} from 'react-dom'
import {Modal} from 'react-bootstrap'
import {KTSVG} from '../../../_metronic/helpers'
import {Formik, Form, Field} from 'formik'
import {Irelationship} from './IMoiquanhe'
import instance from '../../modules/axiosInstance'
import Select from 'react-select'
import {useQuery} from 'react-query'
import {FormikReactSelect, MyOption} from './CustomSelect'
type Props = {
  show: boolean
  handleClose: () => void
  title: string
}
type option = {
  value: string | number
  label: string
}
const URL = process.env.REACT_APP_API_URL
const modalsRoot = document.getElementById('root-modals') || document.body

const CreateAppModal = ({show, handleClose, title}: Props) => {
  const [value, setvalue] = useState<number>(1)
  const [token, setToken] = useState<string>('')
  const {data} = useQuery({
    queryKey: ['client'],
    queryFn: async () => {
      const res = await instance.get(`${URL}/client`)
      var data1 = res.data.DATA.data.map((el: any) => {
        return {
          value: el.id,
          label: `${el.UID} - ${el.facebook_name}`,
        }
      })
      return data1
    },
  })
  const {data: UIData} = useQuery({
    queryKey: ['UIData', value],
    queryFn: async () => {
      const res = await instance.get(`${URL}/uid?type=9`)
      var data1 = res.data.DATA.map((el: any) => {
        return {
          value: el.uid,
          label: `${el.uid} - ${el.name}`,
          account_type_id: el.account_type_id,
          name: el.name,
        }
      })
      return data1
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
            host_name: '',
            access_token: token,
            id_client: '',
            uid: '',
            name: '',
            account_type_id: 1,
            time_to_crawler: 0,
            time_get_host: 0,
          }}
          onSubmit={(values: Irelationship) => {
            instance
              .post(`${URL}/host`, values)
              .then((res) => {
                if (res.data.STATUS === '200') handleClose()
              })
              .catch((error) => {
                if (error.status === 403) {
                  handleClose()
                }
              })
          }}
        >
          {({
            values,
            errors,
            touched,
            handleChange,
            handleBlur,
            handleSubmit,
            isSubmitting,
            setFieldValue,
            resetForm,
            /* and other goodies */
          }) => (
            <Form>
              <div className='mb-5'>
                <label className='form-label'>TÊN HOST</label>
                <Field type='text' name='host_name' className='form-control' placeholder='' />
              </div>
              <div className='mb-5'>
                <label className='form-label'>API TOKEN</label>
                <div style={{display: 'flex', height: '50px'}}>
                  <Field
                    type='text'
                    className='form-control'
                    name='access_token'
                    placeholder='Bấm API Token để tạo ra token cho host'
                  />
                  <button
                    className='btn btn-danger'
                    style={{marginLeft: '10px', width: '140px'}}
                    onClick={() => {
                      instance.get(`${URL}/token`).then((res) => {
                        setToken(res.data.DATA)
                        setFieldValue('access_token', res.data.DATA)
                      })
                    }}
                  >
                    Tạo Token
                  </button>
                </div>
              </div>
              <div className='mb-5'>
                <label className='form-label'>UID HỘI NHÓM</label>
                <Select
                  name='uid'
                  defaultValue={{
                    // value: 1,
                    label: 'Lựa chọn tài khoản cần theo dõi',
                  }}
                  // options={UIData}
                  onChange={(val) => {
                    const _val = val as MyOption[] | MyOption
                    const isArray = Array.isArray(_val)
                    if (isArray) {
                      const values = _val.map((o) => o.value)
                      setFieldValue('uid', values)
                    } else {
                      setFieldValue('uid', _val.value)
                      setFieldValue('account_type_id', _val.account_type_id)
                      setFieldValue('name', _val.name)
                      setvalue(_val.value)
                    }
                  }}
                />
              </div>
              <div className='mb-5'>
                <label className='form-label'>LỰA CHỌN CLIENT</label>
                <FormikReactSelect name='id_client' options={data} />
              </div>
              <div className='mb-10' style={{display: 'flex', flexDirection: 'row'}}>
                <div>
                  <label className='form-label'>THỜI GIAN CÀO BÀI</label>
                  <Field
                    type='number'
                    name='time_to_crawler'
                    className='form-control form-control-white'
                    placeholder='0'
                  />
                </div>
                <div style={{marginLeft: '10px'}}>
                  <label className='form-label'>THỜI GIAN LẤY DỮ LIỆU MẪU</label>
                  <Field
                    type='number'
                    name='time_get_host'
                    className='form-control form-control-white'
                    placeholder='0'
                  />
                </div>
              </div>
              <div style={{display: 'flex', flexDirection: 'row-reverse'}}>
                <button
                  className='btn btn-info'
                  style={{marginLeft: '5px'}}
                  onClick={() => resetForm()}
                >
                  Xóa dữ liệu
                </button>
                <button
                  className='btn btn-primary'
                  type='submit'
                  style={{marginLeft: '5px'}}
                  data-kt-indicator='on'
                >
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
