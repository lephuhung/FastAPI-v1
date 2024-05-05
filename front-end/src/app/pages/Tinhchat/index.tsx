import React, { FC } from "react";
import { Table } from "./Table";
import { useIntl } from 'react-intl'
import { PageTitle } from '../../../_metronic/layout/core'
const DatadoWrap: FC = () => {
  return (
    <>
      <Table className="mb-5 mb-xl-8" />
    </>);
}
const Tinhchat: FC = () => {
  const intl = useIntl()
  return (
    <>
      <PageTitle breadcrumbs={[]}>{intl.formatMessage({ id: 'MENU.DATADOC' })}</PageTitle>
      <DatadoWrap />
    </>
  )
}
export { Tinhchat }