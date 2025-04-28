/* eslint-disable jsx-a11y/anchor-is-valid */
import React, {useState} from 'react'
import {KTSVG, toAbsoluteUrl} from '../../../_metronic/helpers'
import {useQuery} from 'react-query'
import instance from '../../modules/axiosInstance'

import {CardItem} from './CardItem-Unit'
import axios from 'axios'
import {individual} from '../Individual/individual'
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
      const respone = await axios.get(`${URL}/thongke/thongkeunit`)
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
                  title={el.unit}
                  badgeColor='primary'
                  budget='600'
                  VaiAo={el.hoinhom.VaiAo}
                  is_kol={el.individual.is_kol}
                  NVCB={el.hoinhom.NVCB}
                  task_individual={el.individual.cntv}
                  task_hoinhom={el.hoinhom.cntv}
                  THEODOI={el.individual.THEODOI}
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
