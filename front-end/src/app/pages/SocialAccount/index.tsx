import React, { FC } from "react";
import { useIntl } from 'react-intl'
import { PageTitle } from '../../../_metronic/layout/core'
import {Table} from './Table'
import { useParams } from 'react-router-dom'
import { useQuery } from 'react-query'
import axios from 'axios'

const URL = process.env.REACT_APP_API_URL

const SocialAccountWrap: FC<{uid: string}> = ({uid}) => {
    const {data: socialAccount, isLoading} = useQuery(
        ['social-account', uid],
        () => axios.get(`${URL}/social-accounts/type/${uid}`).then(res => res.data)
    )

    if (isLoading) {
        return <div>Loading...</div>
    }

    return (
        <>
            <Table className="mb-5 mb-xl-8" socialAccount={socialAccount}/>
        </>
    )
}

const SocialAccount: FC = () => {
    const intl = useIntl()
    const {uid} = useParams<{uid: string}>()

    return (
      <>
        {/* <PageTitle breadcrumbs={[]}>{intl.formatMessage({ id: 'MENU.FACEBOOK' })}</PageTitle> */}
        <SocialAccountWrap uid={uid || ''} />
      </>
    )
}

export { SocialAccount }