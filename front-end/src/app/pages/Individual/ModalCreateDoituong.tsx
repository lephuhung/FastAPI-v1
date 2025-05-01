import React, {useState} from 'react'
import {Modal, Button, Form} from 'react-bootstrap'
import {useQueryClient, useMutation} from 'react-query'
import {toast} from 'react-toastify'
import {createIndividual} from './individual'
import {IndividualResponse} from './Table'
import axios from 'axios'
import {Formik, Form as FormikForm, Field} from 'formik'
import * as Yup from 'yup'

interface Props {
  show: boolean
  handleClose: () => void
  title: string
  doituong?: IndividualResponse
  onSuccess: () => void
}

const validationSchema = Yup.object().shape({
  full_name: Yup.string().required('Full name is required'),
  phone_number: Yup.string(),
  national_id: Yup.string(),
  citizen_id: Yup.string(),
  date_of_birth: Yup.string(),
  is_male: Yup.boolean().nullable(),
  hometown: Yup.string(),
  additional_info: Yup.string(),
  is_kol: Yup.boolean(),
  image_url: Yup.string()
})

export const ModalCreateDoituong: React.FC<Props> = ({show, handleClose, title, onSuccess}) => {
  const initialValues: Partial<IndividualResponse> = {
    full_name: '',
    phone_number: '',
    national_id: '',
    citizen_id: '',
    date_of_birth: '',
    is_male: null,
    hometown: '',
    additional_info: '',
    is_kol: false,
    image_url: ''
  }

  const handleSubmit = async (values: Partial<IndividualResponse>) => {
    try {
      const response = await axios.post(`${process.env.REACT_APP_API_URL}/individuals`, values)
      if (response.data.STATUS === '200') {
        onSuccess()
        handleClose()
      }
    } catch (error) {
      console.error('Error creating individual:', error)
    }
  }

  return (
    <Modal show={show} onHide={handleClose} size='lg'>
      <Modal.Header closeButton>
        <Modal.Title>{title}</Modal.Title>
      </Modal.Header>
      <Modal.Body>
        <Formik
          initialValues={initialValues}
          validationSchema={validationSchema}
          onSubmit={handleSubmit}
        >
          {({errors, touched}) => (
            <FormikForm>
              <div className='mb-3'>
                <label className='form-label'>Full Name</label>
                <Field
                  type='text'
                  className='form-control'
                  name='full_name'
                />
                {errors.full_name && touched.full_name && (
                  <div className='text-danger'>{errors.full_name}</div>
                )}
              </div>
              <div className='mb-3'>
                <label className='form-label'>Phone Number</label>
                <Field
                  type='text'
                  className='form-control'
                  name='phone_number'
                />
              </div>
              <div className='mb-3'>
                <label className='form-label'>National ID</label>
                <Field
                  type='text'
                  className='form-control'
                  name='national_id'
                />
              </div>
              <div className='mb-3'>
                <label className='form-label'>Citizen ID</label>
                <Field
                  type='text'
                  className='form-control'
                  name='citizen_id'
                />
              </div>
              <div className='mb-3'>
                <label className='form-label'>Date of Birth</label>
                <Field
                  type='date'
                  className='form-control'
                  name='date_of_birth'
                />
              </div>
              <div className='mb-3'>
                <label className='form-label'>Gender</label>
                <Field
                  as='select'
                  className='form-select'
                  name='is_male'
                >
                  <option value=''>Select gender</option>
                  <option value='true'>Male</option>
                  <option value='false'>Female</option>
                </Field>
              </div>
              <div className='mb-3'>
                <label className='form-label'>Hometown</label>
                <Field
                  type='text'
                  className='form-control'
                  name='hometown'
                />
              </div>
              <div className='mb-3'>
                <label className='form-label'>Additional Info</label>
                <Field
                  as='textarea'
                  className='form-control'
                  name='additional_info'
                  rows={3}
                />
              </div>
              <div className='mb-3'>
                <div className='form-check'>
                  <Field
                    type='checkbox'
                    className='form-check-input'
                    name='is_kol'
                  />
                  <label className='form-check-label'>Is KOL</label>
                </div>
              </div>
              <div className='mb-3'>
                <label className='form-label'>Image URL</label>
                <Field
                  type='text'
                  className='form-control'
                  name='image_url'
                />
              </div>
              <div className='text-end'>
                <button type='button' className='btn btn-light me-2' onClick={handleClose}>
                  Cancel
                </button>
                <button type='submit' className='btn btn-primary'>
                  Create
                </button>
              </div>
            </FormikForm>
          )}
        </Formik>
      </Modal.Body>
    </Modal>
  )
} 