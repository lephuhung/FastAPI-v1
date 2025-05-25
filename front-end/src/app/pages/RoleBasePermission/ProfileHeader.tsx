/* eslint-disable jsx-a11y/anchor-is-valid */
import React from 'react'
import {KTSVG, toAbsoluteUrl} from '../../../_metronic/helpers'
import {Link} from 'react-router-dom'
import {Dropdown1} from '../../../_metronic/partials'
import {useLocation} from 'react-router-dom'

const ProfileHeader: React.FC = () => {
  const location = useLocation()

  return (
    <div className='card mb-5 mb-xl-10'>
      <div className='card-body pt-9 pb-0'>
        <div className='d-flex flex-wrap flex-sm-nowrap mb-3'>

          <div className='flex-grow-1'>
            <span className='fs-2 fw-bolder pb-5 d-block'>Tổng hợp thông tin cấu hình</span>
            <div className='d-flex flex-wrap flex-stack border-bottom pb-5'>
              <div className='d-flex flex-column flex-grow-1'>
                <div className='d-flex flex-wrap'>
                  <div className='border border-gray-300 border-dashed rounded min-w-125px py-3 px-4 me-6 mb-3'>
                    <div className='d-flex align-items-center'>
                      <KTSVG
                        path='/media/icons/duotune/arrows/arr066.svg'
                        className='svg-icon-3 svg-icon-success me-2'
                      />
                      <div className='fs-2 fw-bolder'>4500</div>
                    </div>

                    <div className='fw-bold fs-6 text-gray-400'>Công tác nghiệp vụ</div>
                  </div>

                  <div className='border border-gray-300 border-dashed rounded min-w-125px py-3 px-4 me-6 mb-3'>
                    <div className='d-flex align-items-center'>
                      <KTSVG
                        path='/media/icons/duotune/arrows/arr065.svg'
                        className='svg-icon-3 svg-icon-danger me-2'
                      />
                      <div className='fs-2 fw-bolder'>75</div>
                    </div>

                    <div className='fw-bold fs-6 text-gray-400'>Phân quyền "Super Admin"</div>
                  </div>

                  <div className='border border-gray-300 border-dashed rounded min-w-125px py-3 px-4 me-6 mb-3'>
                    <div className='d-flex align-items-center'>
                      <KTSVG
                        path='/media/icons/duotune/arrows/arr066.svg'
                        className='svg-icon-3 svg-icon-success me-2'
                      />
                      <div className='fs-2 fw-bolder'>60</div>
                    </div>

                    <div className='fw-bold fs-6 text-gray-400'>Phân quyền "Phòng"</div>
                  </div>
                  <div className='border border-gray-300 border-dashed rounded min-w-125px py-3 px-4 me-6 mb-3'>
                    <div className='d-flex align-items-center'>
                      <KTSVG
                        path='/media/icons/duotune/arrows/arr066.svg'
                        className='svg-icon-3 svg-icon-success me-2'
                      />
                      <div className='fs-2 fw-bolder'>60</div>
                    </div>

                    <div className='fw-bold fs-6 text-gray-400'>Phân quyền "Xã"</div>
                  </div>
                </div>
                
              </div>
              </div>
            </div>
        </div>

        <div className='d-flex overflow-auto h-55px'>
          <ul className='nav nav-stretch nav-line-tabs nav-line-tabs-2x border-transparent fs-5 fw-bolder flex-nowrap'>
            <li className='nav-item'>
              <Link
                className={
                  `nav-link text-active-primary me-6 ` +
                  (location.pathname === '/permission/role-admin' && 'active')
                }
                to='/permission/role-admin'
              >
                Phân quyền Admin
              </Link>
            </li>
            <li className='nav-item'>
              <Link
                className={
                  `nav-link text-active-primary me-6 ` +
                  (location.pathname === '/permission/role-phong' && 'active')
                }
                to='/permission/role-phong'
              >
                Phân quyền Phòng
              </Link>
            </li>
            <li className='nav-item'>
              <Link
                className={
                  `nav-link text-active-primary me-6 ` +
                  (location.pathname === '/permission/role-xa' && 'active')
                }
                to='/permission/role-xa'
              >
                Phân quyền xã
              </Link>
            </li>
            <li className='nav-item'>
              <Link
                className={
                  `nav-link text-active-primary me-6 ` +
                  (location.pathname === '/permission/role-doi' && 'active')
                }
                to='/permission/role-doi'
              >
                Phân quyền đội
              </Link>
            </li>
          </ul>
        </div>
      </div>
    </div>
  )
}

export {ProfileHeader}
