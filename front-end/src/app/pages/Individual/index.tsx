import React, { FC } from "react";
import { Table } from "./Table";
import { useIntl } from 'react-intl'
import { PageTitle } from '../../../_metronic/layout/core'
const PostWrap: FC = () => {
  return (
  <>
  <Table className="mb-5 mb-xl-8"/>
  </>);
}
const Individual: FC = () => {
  const intl = useIntl()
  return (
    <>
      <PageTitle breadcrumbs={[]}>{'DANH SÁCH ĐỐI TƯỢNG/KOLs'}</PageTitle>
      <PostWrap />
    </>
  )
}
export { Individual }