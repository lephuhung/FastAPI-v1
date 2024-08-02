import React, {FC} from 'react'
import {useIntl} from 'react-intl'
import {PageTitle} from '../../../_metronic/layout/core'
import {Table} from './Table'
const GroupWrap: FC = () => {
  return <Table className='mb-5 mb-xl-8' />
}
const Group: FC = () => {
  const intl = useIntl()
  return (
    <>
      <PageTitle breadcrumbs={[]}>{intl.formatMessage({id: 'MENU.GROUP'})}</PageTitle>
      <GroupWrap />
    </>
  )
}
export {Group}
