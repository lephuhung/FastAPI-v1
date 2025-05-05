import {FC} from 'react'
import {Link} from 'react-router-dom'
import {KTSVG, toAbsoluteUrl} from '../../../_metronic/helpers'
import Avatar from 'react-avatar'
type ctnv = {
  ctnv_name: string
  count: number
}
type Props = {
  KOL: number
  THEODOI: number
  VaiAo: number
  badgeColor: string
  NVCB: string
  ctnv_hoinhom?: Array<ctnv>
  title: string
  ctnv_doituong?: Array<ctnv>
  //   date: string
  budget: string
  item: any
}

const CardItem: FC<Props> = ({
  badgeColor,
  title,
  budget,
  NVCB,
  KOL,
  ctnv_doituong,
  ctnv_hoinhom,
  VaiAo,
  THEODOI,
  item,
}) => {
  return (
    <Link
      to={`/thongke-donvi/details/${item.id}`}
      className='card border border-2 border-gray-300 '
    >
      <div className='card-header border-0 pt-9'>
        <div className='card-title m-0'>
          <Avatar name={title} round={true} size='50px' />
          {/* <Avatar facebookId="100008343750912" size="50" /> */}
        </div>
        <div className='card-toolbar'>
          <span className={`badge badge-light-${badgeColor} fw-bolder me-auto px-4 py-3 fs-3`}>
            {title}
          </span>
        </div>
      </div>

      <div className='card-body p-5'>
        {/* <p className='text-gray-400 fw-bold fs-5 mt-1 mb-7'>{description}</p> */}

        <div className='d-flex flex-wrap mb-1'>
          <div className='border border-gray-300 border-dashed rounded min-w-100px py-3 px-4 me-6 mb-3'>
            <div className='d-flex align-items-center'>
              <KTSVG
                path='/media/icons/duotune/arrows/arr066.svg'
                className='svg-icon-3 svg-icon-success me-2'
              />
              <div className='fs-2 fw-bolder'>{NVCB}</div>
            </div>

            <div className='fw-bold fs-6 text-gray-400'>Hội nhóm</div>
          </div>
          <div className='border border-gray-300 border-dashed rounded min-w-100px py-3 px-4 me-6 mb-3'>
            <div className='d-flex align-items-center'>
              <KTSVG
                path='/media/icons/duotune/arrows/arr066.svg'
                className='svg-icon-3 svg-icon-success me-2'
              />
              <div className='fs-2 fw-bolder'>{VaiAo}</div>
            </div>

            <div className='fw-bold fs-6 text-gray-400'>Vai ảo</div>
          </div>
          <div className='border border-gray-300 border-dashed rounded min-w-100px py-3 px-4 me-6 mb-3'>
            <div className='d-flex align-items-center'>
              <KTSVG
                path='/media/icons/duotune/arrows/arr066.svg'
                className='svg-icon-3 svg-icon-success me-2'
              />
              <div className='fs-2 fw-bolder'>{KOL}</div>
            </div>

            <div className='fw-bold fs-6 text-gray-400'>KOL</div>
          </div>
          <div className='border border-gray-300 border-dashed rounded min-w-100px py-3 px-4 me-6 mb-3'>
            <div className='d-flex align-items-center'>
              <KTSVG
                path='/media/icons/duotune/arrows/arr066.svg'
                className='svg-icon-3 svg-icon-success me-2'
              />
              <div className='fs-2 fw-bolder'>{THEODOI}</div>
            </div>

            <div className='fw-bold fs-6 text-gray-400'>Đối tượng</div>
          </div>
        </div>
        <div className='separator border-3 my-10'></div>
        <span>ĐỐI TƯỢNG</span>
        <div className='d-flex flex-wrap mb-1'>
          {item.doituong.ctnv &&
            item.doituong.ctnv.map((item: ctnv, index: number) => {
              return (
                <div
                  className='border border-gray-300 border-dashed rounded min-w-100px py-3 px-4 me-6 mb-3'
                  key={index}
                >
                  <div className='d-flex align-items-center'>
                    <KTSVG
                      path='/media/icons/duotune/arrows/arr066.svg'
                      className='svg-icon-3 svg-icon-success me-2'
                    />
                    <div className='fs-2 fw-bolder'>{item.count}</div>
                  </div>

                  <div className='fw-bold fs-6 text-gray-400'>{item.ctnv_name}</div>
                </div>
              )
            })}
        </div>
        <div className='separator border-3 my-10'></div>
        <span>HỘI NHÓM</span>
        <div className='d-flex flex-wrap mb-1'>
          {item.hoinhom.ctnv &&
            item.hoinhom.ctnv.map((item: ctnv, index: number) => {
              return (
                <div className='d-flex flex-wrap mb-1' key={index}>
                  <div
                    className='border border-gray-300 border-dashed rounded min-w-100px py-3 px-4 me-6 mb-3'
                    key={index}
                  >
                    <div className='d-flex align-items-center'>
                      <KTSVG
                        path='/media/icons/duotune/arrows/arr066.svg'
                        className='svg-icon-3 svg-icon-success me-2'
                      />
                      <div className='fs-2 fw-bolder'>{item.count}</div>
                    </div>

                    <div className='fw-bold fs-6 text-gray-400'>{item.ctnv_name}</div>
                  </div>
                </div>
              )
            })}
        </div>
      </div>
    </Link>
  )
}

export {CardItem}
