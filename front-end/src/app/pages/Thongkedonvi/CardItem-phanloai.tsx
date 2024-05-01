import {FC} from 'react'
import {Link} from 'react-router-dom'
import Avatar from 'react-avatar'


type Props = {
  count:number,
  title: string,
  item: any
}

const CardItemPhanloai: FC<Props> = ({
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
            {title&&title.toUpperCase()}
          </span>
        </div>
      </div>

      <div className='card-body p-5' style={{display: 'flex', flexDirection:'column'}}>
        <div className='d-flex flex-wrap mb-1'>
        {item.uid_names &&
          item.uid_names.map((item: string, index: number) => {
            return (
                <div
                  className='border border-gray-300 border-dashed rounded min-w-100px py-3 px-4 me-6 mb-3'
                  key={index}
                >
                  <div className='fw-bold fs-6 text-gray-400'>{item}</div>
                </div>
            )
          })}
          </div>
      </div>
    </Link>
  )
}

export {CardItemPhanloai}
