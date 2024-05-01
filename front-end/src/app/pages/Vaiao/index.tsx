import React, {FC} from 'react'
import {useIntl} from 'react-intl'
import {PageTitle} from '../../../_metronic/layout/core'
import {Table} from './Table'
const GroupWrap: FC = () => {
  return <Table className='mb-5 mb-xl-8' />
}
const Vaiao: FC = () => {
  const intl = useIntl()
  return (
    <>
      <PageTitle breadcrumbs={[]}>{'DANH SÁCH VAI ẢO'}</PageTitle>
      <GroupWrap />
    </>
  )
}
export {Vaiao} 
