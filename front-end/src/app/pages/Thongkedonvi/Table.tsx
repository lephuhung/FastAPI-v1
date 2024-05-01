/* eslint-disable jsx-a11y/anchor-is-valid */
import React, {useState} from 'react'
import {KTSVG, toAbsoluteUrl} from '../../../_metronic/helpers'
import {useQuery} from 'react-query'
import instance from '../../modules/axiosInstance'

import {CardItem} from './CardItem-donvi'
import axios from 'axios'
import {doituong} from '../Doituong/doituong'
const URL = process.env.REACT_APP_API_URL
type Props = {
  className: string
}

const Table: React.FC<Props> = ({className}) => {
  const [loading, setloading] = useState<boolean>(false)
  const {isLoading, data, error} = useQuery({
    queryKey: ['thongke', loading],
    queryFn: async () => {
      setloading(false)
      const respone = await axios.get(`${URL}/thongke/thongkedonvi`)
      console.log(respone)
      const {data} = respone
      return data
    },
  })
  if (isLoading) {
    <div>Loading</div>
  }
  if(error){
    console.log(error)
  }

  return (
    <div>
      <div className='row g-5'>
        {data &&
          data.map((el: any, index: number) => {
            return (
              <div className='col-md-6 col-xl-4' key={index}>
                <CardItem
                  title={el.donvi}
                  badgeColor='primary'
                  budget='600'
                  VaiAo={el.hoinhom.VaiAo}
                  KOL={el.doituong.KOL}
                  NVCB={el.hoinhom.NVCB}
                  ctnv_doituong={el.doituong.cntv}
                  ctnv_hoinhom={el.hoinhom.cntv}
                  THEODOI={el.doituong.THEODOI}
                  item={el}
                />
              </div>
            )
          })}
      </div>
    </div>
  )
}

export {Table}
