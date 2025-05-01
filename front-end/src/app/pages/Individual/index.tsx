import {FC} from 'react'
import {PageTitle} from '../../../_metronic/layout/core'
import {IndividualTable} from './Table'

const IndividualPage: FC = () => {
  return (
    <>
      <PageTitle breadcrumbs={[]}>Quản lý đối tượng</PageTitle>
      <IndividualTable className='mb-5 mb-xl-10'/>
    </>
  )
}

export {IndividualPage}