import { FC } from 'react'
import { Link } from 'react-router-dom'
import Avatar from 'react-avatar'
import { KTSVG } from '../../../_metronic/helpers'


type Props = {
  count: number,
  title: string,
  item: any
}

const CardItemCtnv: FC<Props> = ({
  title,
  count,
  item,
}) => {
  return (
    <Link
      to='/crafted/pages/profile/overview'
      className='card border border-2 border-gray-300 '
    >
      <div className='card-header border-0 pt-9'>
        <div className='card-title m-0'>
          <Avatar name={count.toString()} round={true} size='50px' />
          {/* <Avatar facebookId="100008343750912" size="50" /> */}
        </div>
        <div className='card-toolbar'>
          <span className={`badge badge-light-primary fw-bolder me-auto px-4 py-3 fs-3`}>
            {title && title.toUpperCase()}
          </span>
        </div>
      </div>

      <div className='card-body p-5' style={{ display: 'flex', flexDirection: 'column' }}>
        <div className='d-flex flex-wrap mb-1'>
          <div className='w-100 mb-5'>
            <div
              className='accordion-header py-3 d-flex'
              data-bs-toggle='collapse'
              data-bs-target='#kt_accordion_2_item_2'
            >
              <span className='accordion-icon'>
                <KTSVG className='svg-icon svg-icon-4' path='media/icons/duotune/arrows/arr064.svg' />
              </span>
              <h3 className='fs-4 text-gray-600 fw-bold mb-0 ms-4'>Công tác nghiệp vụ</h3>
            </div>
            {item.statistics &&
              Object.entries(item.statistics.tasks).map(([key, value]: [string, any]) => {
                return (
                  <div
                    className='border border-gray-300 border-dashed rounded min-w-100px py-3 px-4 me-6 mb-3 d-inline-block bg-light-primary'
                    key={key}
                  >
                    <div className='fw-bold fs-6 text-gray-600'>{value.name}</div>
                    <div className='fw-bold fs-6 text-gray-800'>{value.count}</div>
                  </div>
                )
              })}
          </div>

          <div className='w-100 mb-5'>
            <div
              className='accordion-header py-3 d-flex'
              data-bs-toggle='collapse'
              data-bs-target='#kt_accordion_2_item_2'
            >
              <span className='accordion-icon'>
                <KTSVG className='svg-icon svg-icon-4' path='media/icons/duotune/arrows/arr064.svg' />
              </span>
              <h3 className='fs-4 text-gray-600 fw-bold mb-0 ms-4'>Tính chất hội nhóm</h3>
            </div>
            {item.statistics &&
              Object.entries(item.statistics.characteristics).map(([key, value]: [string, any]) => {
                return (
                  <div
                    className='border border-gray-300 border-dashed rounded min-w-100px py-3 px-4 me-6 mb-3 d-inline-block bg-light-success'
                    key={key}
                  >
                    <div className='fw-bold fs-6 text-gray-600'>{value.name}</div>
                    <div className='fw-bold fs-6 text-gray-800'>{value.count}</div>
                  </div>
                )
              })}
          </div>

          <div className='w-100'>
            <div
              className='accordion-header py-3 d-flex'
              data-bs-toggle='collapse'
              data-bs-target='#kt_accordion_2_item_2'
            >
              <span className='accordion-icon'>
                <KTSVG className='svg-icon svg-icon-4' path='media/icons/duotune/arrows/arr064.svg' />
              </span>
              <h3 className='fs-4 text-gray-600 fw-bold mb-0 ms-4'>Tài khoản mạng xã hội</h3>
            </div>
            {item.statistics &&
              Object.entries(item.statistics.social_accounts).map(([key, value]: [string, any]) => {
                return (
                  <div
                    className='border border-gray-300 border-dashed rounded min-w-100px py-3 px-4 me-6 mb-3 d-inline-block bg-light-info'
                    key={key}
                  >
                    <div className='fw-bold fs-6 text-gray-600'>{value.name}</div>
                    <div className='fw-bold fs-6 text-gray-800'>{value.count}</div>
                  </div>
                )
              })}
          </div>
        </div>
      </div>
    </Link>
  )
}

export { CardItemCtnv }
