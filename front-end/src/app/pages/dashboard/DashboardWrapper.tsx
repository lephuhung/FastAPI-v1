/* eslint-disable jsx-a11y/anchor-is-valid */
import {FC, useEffect} from 'react'
import {useIntl} from 'react-intl'
import {PageTitle} from '../../../_metronic/layout/core'
import axios from 'axios'
import {useQuery} from 'react-query'
import {KTSVG} from '../../../_metronic/helpers'
import {
  StatisticsWidget6,
} from '../../../_metronic/partials/widgets'

const URL = process.env.REACT_APP_API_URL

interface DashboardStats {
  account_type_stats: {
    total_individuals: number
    total_social_accounts: number
    account_type_stats: Array<{
      name: string
      count: number
    }>
  }
  task_stats: {
    combined_task_stats: Array<{
      id: number
      name: string
      individual_count: number
      social_account_count: number
    }>
  }
  type_4_social_accounts: number
}

const DashboardPage: FC = () => {
  const {data: dashboardStats, isLoading} = useQuery<DashboardStats>(
    'dashboard_stats',
    () => axios.get(`${URL}/dashboard/stats`).then((res:any) => res.data)
  )

  if (isLoading) {
    return <div>Loading...</div>
  }

  return (
    <div className='accordion accordion-icon-toggle' id='kt_accordion_2'>
      <div className='mb-5'>
        <div
          className='accordion-header py-3 d-flex'
          data-bs-toggle='collapse'
          data-bs-target='#kt_accordion_2_item_1'
        >
          <span className='accordion-icon'>
            <KTSVG className='svg-icon svg-icon-4' path='media/icons/duotune/arrows/arr064.svg' />
          </span>
          <h3 className='fs-4 text-gray-800 fw-bold mb-0 ms-4'>TỔNG QUAN THÔNG TIN</h3>
        </div>
        <div
          id='kt_accordion_2_item_1'
          className='fs-6 collapse show ps-10'
          data-bs-parent='#kt_accordion_2'
        >
          <div className='row g-5'>
            <div className='row g-5 g-xl-8'>
              <div className='col-xl-3'>
                <StatisticsWidget6
                  className='card-xl-stretch mb-xl-8'
                  color='success'
                  title='ĐỐI TƯỢNG'
                  description='TỔNG SỐ ĐỐI TƯỢNG'
                  progress={String(dashboardStats?.account_type_stats.total_individuals || 0)}
                />
              </div>

              <div className='col-xl-3'>
                <StatisticsWidget6
                  className='card-xl-stretch mb-xl-8'
                  color='success'
                  title='TÀI KHOẢN'
                  description='TỔNG SỐ TÀI KHOẢN'
                  progress={String(dashboardStats?.account_type_stats.total_social_accounts || 0)}
                />
              </div>
            </div>
          </div>
        </div>
      </div>

      <div className='mb-5'>
        <div
          className='accordion-header py-3 d-flex'
          data-bs-toggle='collapse'
          data-bs-target='#kt_accordion_2_item_2'
        >
          <span className='accordion-icon'>
            <KTSVG className='svg-icon svg-icon-4' path='media/icons/duotune/arrows/arr064.svg' />
          </span>
          <h3 className='fs-4 text-gray-800 fw-bold mb-0 ms-4'>PHÂN LOẠI TÀI KHOẢN</h3>
        </div>
        <div
          id='kt_accordion_2_item_2'
          className='collapse fs-6 ps-10 show ps-10'
          data-bs-parent='#kt_accordion_2'
        >
          <div className='row g-5'>
            {dashboardStats?.account_type_stats.account_type_stats.map((stat:any, index:number) => (
              <div className='col-xl-3' key={index}>
                <StatisticsWidget6
                  className='card-xl-stretch mb-xl-8'
                  color='primary'
                  title={stat.name.toUpperCase()}
                  description='SỐ LƯỢNG TÀI KHOẢN'
                  progress={String(stat.count)}
                />
              </div>
            ))}
          </div>
        </div>
      </div>

      <div className='mb-5'>
        <div
          className='accordion-header py-3 d-flex'
          data-bs-toggle='collapse'
          data-bs-target='#kt_accordion_2_item_3'
        >
          <span className='accordion-icon'>
            <KTSVG className='svg-icon svg-icon-4' path='media/icons/duotune/arrows/arr064.svg' />
          </span>
          <h3 className='fs-4 text-gray-800 fw-bold mb-0 ms-4'>THỐNG KÊ THEO NHIỆM VỤ</h3>
        </div>
        <div
          id='kt_accordion_2_item_3'
          className='collapse fs-6 ps-10 show ps-10'
          data-bs-parent='#kt_accordion_2'
        >
          <div className='row g-5'>
            {dashboardStats?.task_stats.combined_task_stats.map((stat:any, index:number) => (
              <div className='col-xl-4' key={index}>
                <div className='card bg-light-info card-xl-stretch mb-xl-8'>
                  <div className='card-header border-0'>
                    <h3 className='card-title fw-bold text-info fs-5'>{stat.name.toUpperCase()}</h3>
                  </div>
                  <div className='card-body my-3'>
                    <div className='d-flex flex-column'>
                      <div className='d-flex align-items-center mb-3'>
                        <div className='d-flex flex-column w-100'>
                          <div className='d-flex justify-content-between align-items-center mb-5'>
                            <div className='d-flex flex-column'>
                              <span className='text-dark fs-1 fw-bold me-2'>{stat.individual_count}</span>
                              <span className='fw-semibold text-muted fs-7'>ĐỐI TƯỢNG</span>
                            </div>
                            <div className='d-flex flex-column'>
                              <span className='text-dark fs-1 fw-bold me-2'>{stat.social_account_count}</span>
                              <span className='fw-semibold text-muted fs-7'>TÀI KHOẢN</span>
                            </div>
                          </div>
                          <div className='progress h-7px bg-info bg-opacity-50'>
                            <div
                              className='progress-bar bg-info'
                              role='progressbar'
                              style={{width: `${(stat.individual_count / (stat.individual_count + stat.social_account_count)) * 100}%`}}
                            />
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            ))}
          </div>
        </div>
      </div>
    </div>
  )
}

const DashboardWrapper: FC = () => {
  const intl = useIntl()
  useEffect(() => {
    axios.get(`${URL}/units/`).then((res:any) => {
      localStorage.setItem('units', JSON.stringify(res.data))
    })
    axios.get(`${URL}/account-types`).then((res:any) => {
      localStorage.setItem('account_types', JSON.stringify(res.data))
    })
    axios.get(`${URL}/tasks`).then((res:any) => {
      localStorage.setItem('tasks', JSON.stringify(res.data))
    })
    axios.get(`${URL}/characteristics`).then((res:any) => {
      localStorage.setItem('characteristics', JSON.stringify(res.data))
    })
    axios.get(`${URL}/statuses`).then((response:any) => {
      localStorage.setItem('statuses', JSON.stringify(response.data))
    })
    axios.get(`${URL}/tags`).then((response:any) => {
      localStorage.setItem('tags', JSON.stringify(response.data))
    })
  }, [])
  return (
    <>
      <PageTitle breadcrumbs={[]}>{intl.formatMessage({id: 'MENU.DASHBOARD'})}</PageTitle>
      <DashboardPage />
    </>
  )
}

export {DashboardWrapper}
