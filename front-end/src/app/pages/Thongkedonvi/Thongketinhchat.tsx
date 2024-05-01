/* eslint-disable jsx-a11y/anchor-is-valid */
import React, {useState} from 'react'
import {KTSVG, toAbsoluteUrl} from '../../../_metronic/helpers'
import {useQuery} from 'react-query'
import instance from '../../modules/axiosInstance'

import {CardItemTinhchat} from './CardItem-tinhchat'
import axios from 'axios'
import {doituong} from '../Doituong/doituong'
const URL = process.env.REACT_APP_API_URL


const Thongketinhchat: React.FC = () => {
  const [loading, setloading] = useState<boolean>(false)
  const {isLoading, data, error} = useQuery({
    queryKey: ['thongketinhchat', loading],
    queryFn: async () => {
      setloading(false)
      const respone = await axios.get(`${URL}/thongke/thongketinhchat`)
      const {data} = respone
      console.log(data)
      return data
    },
  })
  if (isLoading) {
    <div>Loading</div>
  }
  if (error) {
    console.log(error)
  }
  return (
    <div>
      <div className='row g-5'>
        {data &&
          data.map((el: any, index: number) => {
            return (
              <div className='col-md-6 col-xl-4' key={index}>
                <CardItemTinhchat
                  title={el.name}
                  count = {el.count}
                  item={el}
                />
              </div>
            )
          })}
      </div>
    </div>
  )
}

export {Thongketinhchat}
