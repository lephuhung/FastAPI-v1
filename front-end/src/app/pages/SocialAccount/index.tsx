import React, { FC } from "react";
import { PageTitle } from '../../../_metronic/layout/core'
import {Table} from './Table'
import { useParams } from 'react-router-dom'
import { useQuery } from 'react-query'
import axios from 'axios'

const URL = process.env.REACT_APP_API_URL

const SocialAccountWrap: FC<{uid: string, socialAccount: any, isLoading: boolean}> = ({uid, socialAccount, isLoading}) => {
    if (isLoading) {
        return <div>Loading...</div>
    }

    return (
        <>
            <Table className="mb-5 mb-xl-8" socialAccount={socialAccount} typeId={uid}/>
        </>
    )
}

const SocialAccount: FC = () => {
    const {uid} = useParams<{uid: string}>()
    const {data: socialAccount, isLoading} = useQuery(
        ['social-account', uid],
        () => axios.get(`${URL}/social-accounts/type/${uid}`).then(res => res.data)
    )
    return (
      <>
        <PageTitle breadcrumbs={[]}>{socialAccount?.account_type_name.toUpperCase()}</PageTitle>
        <SocialAccountWrap uid={uid || ''} socialAccount={socialAccount} isLoading={isLoading} />
      </>
    )
}

export { SocialAccount }