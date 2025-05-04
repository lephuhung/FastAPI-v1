/* eslint-disable jsx-a11y/anchor-is-valid */
import React, {useState} from 'react'
import {useQueries} from 'react-query'
import {KTSVG} from '../../../_metronic/helpers'
import {CardItemCtnv} from './CardItem-ctnv'
import {CardItemdoituongCtnv} from './CardItem-doituongctnv'
import axios from 'axios'
const URL = process.env.REACT_APP_API_URL

const Thongkectnv: React.FC = () => {
  const [loading, setloading] = useState<boolean>(false)
  const result = useQueries([
    {
      queryKey: ['posts'],
      queryFn: () =>
        axios.get(`${URL}/summary/social-accounts-units`).then((res) => {
          return res.data
        })
    }
  ])

  return (
    <div className='accordion accordion-icon-toggle' id='kt_accordion_2'>
      <div className='mb-5'>
        <div
          className='accordion-header py-3 d-flex'
          data-bs-toggle='collapse'
          data-bs-target='#kt_accordion_2_item_1'
        >
          <span className='accordion-icon'>
            <KTSVG className='svg-icon svg-icon-4' path='media/icons/duotune/arrows/arr064.svg' />
          </span>
          <h3 className='fs-4 text-gray-800 fw-bold mb-0 ms-4'>Phân loại CTNV theo hội nhóm</h3>
        </div>
        <div
          id='kt_accordion_2_item_1'
          className='fs-6 collapse show ps-10'
          data-bs-parent='#kt_accordion_2'
        >
          <div className='row g-5'>
            {result[0].data &&
              result[0].data.map((el: any, index: number) => {
                return (
                  <div className='col-md-6 col-xl-4' key={index}>
                    <CardItemCtnv title={el.unit.name} count={0} item={el} />
                  </div>
                )
              })}
          </div>
        </div>
      </div>
    </div>
  )
}

export {Thongkectnv}
