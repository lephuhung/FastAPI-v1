/* eslint-disable react-hooks/exhaustive-deps */
/* eslint-disable jsx-a11y/anchor-is-valid */

import { createPortal } from 'react-dom'
import { Modal } from 'react-bootstrap'
import { KTSVG } from '../../../_metronic/helpers'
import axios from 'axios';
import { useQuery } from 'react-query';
import {ITrangthaiResponse} from './trangthai'
type Props = {
  show: boolean
  handleClose: () => void
  title: string,
  className: string,
  UID: string,
  content: string,
  Post:ITrangthaiResponse
}
type Comments = {
  message: string,
  shares: number,
  reaction: number,
  created_time: string,
  from_uid:string
}
const URL = process.env.REACT_APP_API_URL;
const modalsRoot = document.getElementById('root-modals') || document.body

const ModalUIDPost = ({ show, handleClose, title, className, UID, content, Post }: Props) => {
  const { data, isLoading, error } = useQuery({
    queryKey: ['comment_of_post', UID],
    queryFn: async () => {
      const res = await axios.get(`${URL}/post/${UID}`)
      return res.data.DATA
    },
    placeholderData:[]
  })
  if (isLoading) { <div>Loading</div> }
  if (error) {
    console.log(error)
  }
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
        {/* ListView Begin::*/}
        <div className={`card ${className}`}>
          {/* begin::Header */}
          <div className='card-header align-items-center border-0 mt-4'>
            <h3 className='card-title align-items-start flex-column'>
              <span className='fw-bold mb-2 text-dark'>{content}</span>
              {/* <span className='text-muted fw-semibold fs-7'>{`shares: ${Post.shares} - reaction: ${Post.reaction}`}</span> */}
            </h3>
            <div className='card-toolbar'>
            </div>
          </div>
          {/* end::Header */}
          {/* begin::Body */}
          <div className='card-body pt-5'>
            {/* begin::Timeline */}
            <div className='timeline-label'>
              {/* begin::Item */}
              {Array.isArray(data)&& data?.map((el: Comments, index: number) =>
                <div className='timeline-item' key={index}>
                  <div className='timeline-label  text-gray-800 fs-18'>{el.created_time}</div>
                  <div className='timeline-badge'>
                    <i className='fa fa-genderless text-success fs-1'></i>
                  </div>
                  <div className='fw-light text-gray-800 ps-3'>
                    {`${el.message}  `}   
                    <a href='#' className='text-primary'>
                     - shares: {el.shares}
                    </a>
                    <a href='#' className='text-primary'>
                      - reaction: {el.reaction}
                    </a>
                    <a href='#' className='text-primary'>
                      - from: {el.from_uid}
                    </a>
                  </div>
                </div>
              )}
            </div>
            {/* end::Timeline */}
          </div>
          {/* end: Card Body */}
        </div>
        {/**ListView End */}
      </div>
    </Modal>,
    modalsRoot
  )
}

export { ModalUIDPost }
