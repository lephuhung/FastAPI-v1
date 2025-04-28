import clsx from 'clsx'
import {KTSVG} from '../../../_metronic/helpers'
import { useState } from 'react'
/* eslint-disable jsx-a11y/anchor-is-valid */
type Props = {
  toggleBtnClass?: string
  toggleBtnIconClass?: string
  menuPlacement?: string
  menuTrigger?: string
}

const PopupMenu = ({
  toggleBtnClass = '',
  toggleBtnIconClass = 'svg-icon-2',
  menuPlacement = 'bottom-end',
  menuTrigger = "{default: 'click', lg: 'hover'}",
}: Props) => {
  const [mode, switchMode] = useState<string>('');
  return (
    <>
      {/* begin::Menu toggle */}
      <a
        href='#'
        className={clsx('btn btn-icon ', toggleBtnClass)}
        data-kt-menu-trigger={menuTrigger}
        data-kt-menu-attach='parent'
        data-kt-menu-placement={menuPlacement}
      >
        {mode === 'dark' && (
          <KTSVG
            path='/media/icons/duotune/general/gen061.svg'
            className={clsx('theme-light-hide', toggleBtnIconClass)}
          />
        )}

        {mode === 'light' && (
          <KTSVG
            path='/media/icons/duotune/general/gen060.svg'
            className={clsx('theme-dark-hide', toggleBtnIconClass)}
          />
        )}
      </a>
      {/* begin::Menu toggle */}

      {/* begin::Menu */}
      <div
        className='menu menu-sub menu-sub-dropdown menu-column menu-rounded menu-title-gray-700 menu-icon-muted menu-active-bg menu-state-primary fw-semibold py-4 fs-base w-175px'
        data-kt-menu='true'
      >
        {/* begin::Menu item */}
        <div className='menu-item px-3 my-0'>
          <a
            href='#'
            className={clsx('menu-link px-3 py-2')}
            onClick={() => switchMode('light')}
          >
            <span className='menu-icon' data-kt-element='icon'>
              <KTSVG path='/media/icons/duotune/general/gen060.svg' className='svg-icon-3' />
            </span>
            <span className='menu-title'>Sáng</span>
          </a>
        </div>
        {/* end::Menu item */}

        {/* begin::Menu item */}
        <div className='menu-item px-3 my-0'>
          <a
            href='#'
            className={clsx('menu-link px-3 py-2')}
            onClick={() => switchMode('dark')}
          >
            <span className='menu-icon' data-kt-element='icon'>
              <KTSVG path='/media/icons/duotune/general/gen061.svg' className='svg-icon-3' />
            </span>
            <span className='menu-title'>Tối</span>
          </a>
        </div>
        {/* end::Menu item */}

        {/* begin::Menu item */}
        <div className='menu-item px-3 my-0'>
          <a
            href='#'
            className={clsx('menu-link px-3 py-2')}
            onClick={() => switchMode('system')}
          >
            <span className='menu-icon' data-kt-element='icon'>
              <KTSVG path='/media/icons/duotune/general/gen062.svg' className='svg-icon-3' />
            </span>
            <span className='menu-title'>Theo hệ thống</span>
          </a>
        </div>
        {/* end::Menu item */}
      </div>
      {/* end::Menu */}
    </>
  )
}

export {PopupMenu}
