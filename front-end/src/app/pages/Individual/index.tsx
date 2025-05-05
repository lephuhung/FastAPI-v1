import {FC} from 'react'
import {PageTitle} from '../../../_metronic/layout/core'
import {IndividualTable} from './Table'

const IndividualPage: FC = () => {
  return (
    <>
      <PageTitle breadcrumbs={[]}>DANH SÁCH ĐỐI TƯỢNG/KOL TRÊN ĐỊA BÀN</PageTitle>
      <IndividualTable className='mb-5 mb-xl-10'/>
    </>
  )
}

export {IndividualPage}