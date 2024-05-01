
import React, { FC } from "react";
import Iframe from "react-iframe";
import { useIntl } from 'react-intl'
import { PageTitle } from '../../../_metronic/layout/core'
const SSH_PAGE: FC = () => {
    return (
        <>
            <Iframe url="http://localhost:2222"
                height="100%"
                width="100%"
                display="block"
                position="relative" />
        </>);
}
const SSH: FC = () => {
    const intl = useIntl()
    return (
        <>
            <PageTitle breadcrumbs={[]}>{intl.formatMessage({ id: 'MENU.SSH' })}</PageTitle>
            <SSH_PAGE/>
        </>
    )
}
export {SSH }