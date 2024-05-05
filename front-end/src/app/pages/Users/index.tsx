import React, { FC } from "react";
import {Table} from "./Table";
import { useIntl } from 'react-intl'
import { PageTitle } from '../../../_metronic/layout/core'
const WrapTable : FC = ()=>{
    return (
        <Table className="mb-5 mb-xl-8"/>
    )
}
const User: FC = () => {
    const intl = useIntl()
    return (
        <>
        <PageTitle breadcrumbs={[]}>{intl.formatMessage({ id: 'MENU.USERS' })}</PageTitle>
       <WrapTable/>
        </>
    );
}
export { User }