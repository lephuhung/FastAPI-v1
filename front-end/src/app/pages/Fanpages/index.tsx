import React, { FC } from "react";
import { useIntl } from 'react-intl'
import { PageTitle } from '../../../_metronic/layout/core'
import {Table} from './Table'
const FanpageWrap: FC = () => {
    return (
        <>
            <Table className="mb-5 mb-xl-8"/>
        </>
    )
}

const Fanpage: FC = () => {
    const intl = useIntl()
    return (
      <>
        <PageTitle breadcrumbs={[]}>{intl.formatMessage({ id: 'MENU.FANPAGE' })}</PageTitle>
        <FanpageWrap />
      </>
    )
  }
export { Fanpage }