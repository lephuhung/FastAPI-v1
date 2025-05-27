/* eslint-disable jsx-a11y/anchor-is-valid */
import React, {useState} from 'react'
import {useQuery} from 'react-query'
import {CardItemIndividual} from './CardItem-individuals'
import axios from 'axios'
const URL = process.env.REACT_APP_API_URL


const Thongkephanloai: React.FC = () => {
  const [loading, setloading] = useState<boolean>(false)
  const {isLoading, data, error} = useQuery({
    queryKey: ['thongketinhchat', loading],
    queryFn: async () => {
      setloading(false)
      const respone = await axios.get(`${URL}/summary/individuals-units`)
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
                <CardItemIndividual
                  title={el.unit.name}
                  count = {index}
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
