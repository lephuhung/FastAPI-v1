/* eslint-disable jsx-a11y/anchor-is-valid */
import React, {useState} from 'react'
import {useQuery} from 'react-query'

import { CardItemPhanloai } from './CardItem-phanloai'
import axios from 'axios'
const URL = process.env.REACT_APP_API_URL


const Thongkephanloai: React.FC = () => {
  const [loading, setloading] = useState<boolean>(false)
  const {isLoading, data, error} = useQuery({
    queryKey: ['thongkecharacteristic', loading],
    queryFn: async () => {
      setloading(false)
      const respone = await axios.get(`${URL}/thongke/thongkephanloai`)
      const {data} = respone
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
                <CardItemPhanloai
                  title={el.status_name}
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

export {Thongkephanloai}
