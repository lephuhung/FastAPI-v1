/* eslint-disable jsx-a11y/anchor-is-valid */
import {FC, useEffect} from 'react'
import {useIntl} from 'react-intl'
import {PageTitle} from '../../../_metronic/layout/core'
import axios from 'axios'
import {useQueries} from 'react-query'
import {trichtin} from '../Trichtin/trichtin'
import {KTSVG} from '../../../_metronic/helpers'
import {
  StatisticsWidget4,
  StatisticsWidget5,
  StatisticsWidget6,
} from '../../../_metronic/partials/widgets'

const URL = process.env.REACT_APP_API_URL
const DashboardPage: FC = () => {
  const result = useQueries([
    {
      queryKey: ['dashboard_individual'],
      queryFn: () =>
        axios.get(`${URL}/dashboard/individual`).then((res) => {
          return res.data
        }),
    },
    {
      queryKey: ['dashboard_uid'],
      queryFn: () =>
        axios.get(`${URL}/dashboard/uid`).then((res) => {
          return res.data
        }),
    },
    {
      queryKey: ['dashboard_trichtin'],
      queryFn: () =>
        axios.get(`${URL}/dashboard/trichtin`).then((res) => {
          return res.data
        }),
    },
  ])
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
          <h3 className='fs-4 text-gray-800 fw-bold mb-0 ms-4'>TỔNG QUAN THÔNG TIN HỘI NHÓM, VAI ẢO, ĐỐI TƯỢNG, is_kol</h3>
        </div>
        <div
          id='kt_accordion_2_item_1'
          className='fs-6 collapse show ps-10'
          data-bs-parent='#kt_accordion_2'
        >
          <div className='row g-5'>
            <div className='row g-5 g-xl-8'>
              <div className='col-xl-3'>
                {result[0] && (
                  <StatisticsWidget6
                    className='card-xl-stretch mb-xl-8'
                    color='success'
                    title='is_kol'
                    description='SỐ LƯỢNG is_kol'
                    progress={result[0].data?.is_kol}
                  />
                )}
              </div>

              <div className='col-xl-3'>
                {result[0] && (
                  <StatisticsWidget6
                    className='card-xl-stretch mb-xl-8'
                    color='success'
                    title=' ĐỐI TƯỢNG'
                    description='SỐ LƯỢNG ĐỐI TƯỢNG'
                    progress={result[0].data?.individual}
                  />
                )}
              </div>
              <div className='col-xl-3'>
                {result[1] && (
                  <StatisticsWidget6
                    className='card-xl-stretch mb-xl-8'
                    color='success'
                    title='Số VAI ẢO'
                    description='SỐ VAI ẢO'
                    progress={result[1].data?.vaiao ? result[1].data?.vaiao : 0}
                  />
                )}
              </div>
              <div className='col-xl-3'>
                {result[1] && (
                  <StatisticsWidget6
                    className='card-xl-stretch mb-xl-8'
                    color='success'
                    title='Số HỘI NHÓM'
                    description='SỐ HỘI NHÓM'
                    progress={result[1].data?.uid_count ? result[1].data?.uid_count : 0}
                  />
                )}
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
                <KTSVG
                  className='svg-icon svg-icon-4'
                  path='media/icons/duotune/arrows/arr064.svg'
                />
              </span>
              <h3 className='fs-4 text-gray-800 fw-bold mb-0 ms-4'>
                PHÂN LOẠI CTNV ĐỐI TƯỢNG
              </h3>
            </div>
            <div
              id='kt_accordion_2_item_2'
              className='collapse fs-6 ps-10 show ps-10'
              data-bs-parent='#kt_accordion_2'
            >
              <div className='row g-5'>
                {result[0].data &&
                  result[0].data.task_individual.map((el: any, index: number) => {
                    return (
                      <div className='col-xl-3' key={index}>
                        {
                          <StatisticsWidget6
                            className='card-xl-stretch mb-xl-8'
                            color='primary'
                            title={`DIỆN ${el.task_name.toUpperCase()}`}
                            description='SỐ LƯỢNG ĐỐI TƯỢNG '
                            progress={el.count}
                          />
                        }
                      </div>
                    )
                  })}
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
                <KTSVG
                  className='svg-icon svg-icon-4'
                  path='media/icons/duotune/arrows/arr064.svg'
                />
              </span>
              <h3 className='fs-4 text-gray-800 fw-bold mb-0 ms-4'>
                PHÂN LOẠI CTNV HỘI NHÓM
              </h3>
            </div>
            <div
              id='kt_accordion_2_item_2'
              className='collapse fs-6 ps-10 show ps-10'
              data-bs-parent='#kt_accordion_2'
            >
              <div className='row g-5'>
                {result[1].data &&
                  result[1].data.task_uid.map((el: any, index: number) => {
                    return (
                      <div className='col-xl-3' key={index}>
                        {
                          <StatisticsWidget6
                            className='card-xl-stretch mb-xl-8'
                            color='info'
                            title={`DIỆN ${el.task_name.toUpperCase()}`}
                            description='SỐ LƯỢNG HỘI NHÓM'
                            progress={el.count}
                          />
                        }
                      </div>
                    )
                  })}
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
          <h3 className='fs-4 text-gray-800 fw-bold mb-0 ms-4'>PHÂN LOẠI HỘI NHÓM</h3>
        </div>
        <div
          id='kt_accordion_2_item_2'
          className='collapse fs-6 ps-10 show ps-10'
          data-bs-parent='#kt_accordion_2'
        >
          <div className='row g-5'>
            {result[1].data &&
              result[1].data.uid_type.map((el: any, index: number) => {
                return (
                  <div className='col-xl-3' key={index}>
                    {
                      <StatisticsWidget6
                        className='card-xl-stretch mb-xl-8'
                        color='danger'
                        title={`${el.type_name.toUpperCase()}`}
                        description='SỐ LƯỢNG HỘI NHÓM'
                        progress={el.count}
                      />
                    }
                  </div>
                )
              })}
          </div>
        </div>
      </div>
    </div>
  )
}
const DashboardWrapper: FC = () => {
  const intl = useIntl()
  useEffect(() => {
    axios.get(`${URL}/units`).then((res) => {
      localStorage.setItem('unit', JSON.stringify(res.data))
    })
    axios.get(`${URL}/account-types`).then((res) => {
      localStorage.setItem('account_type', JSON.stringify(res.data))
    })
    axios.get(`${URL}/tasks`).then((res) => {
      localStorage.setItem('tasks', JSON.stringify(res.data))
    })
    axios.get(`${URL}/characteristics`).then((res) => {
      localStorage.setItem('characteristic', JSON.stringify(res.data))
    })
    axios.get(`${URL}/statuses`).then((response) => {
      localStorage.setItem('statuses', JSON.stringify(response.data))
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
