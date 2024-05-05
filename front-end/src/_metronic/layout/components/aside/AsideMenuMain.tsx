/* eslint-disable react/jsx-no-target-blank */
import React from 'react'
import {useIntl} from 'react-intl'
// import { KTSVG } from '../../../helpers'
import {AsideMenuItemWithSub} from './AsideMenuItemWithSub'
import {AsideMenuItem} from './AsideMenuItem'

export function AsideMenuMain() {
  const intl = useIntl()

  return (
    <>
      <AsideMenuItem
        to='/dashboard'
        icon='/media/icons/duotune/art/art002.svg'
        title={intl.formatMessage({id: 'MENU.DASHBOARD'})}
        fontIcon='bi-app-indicator'
      />
      <div className='menu-item'>
        <div className='menu-content pt-8 pb-2'>
          <span className='menu-section text-muted text-uppercase fs-8 ls-1'>Danh mục </span>
        </div>
      </div>
      <AsideMenuItemWithSub
        to='#'
        title='DANH MỤC HỘI NHÓM'
        fontIcon='bi-archive'
        icon='/media/icons/duotune/general/gen022.svg'
      >
        <AsideMenuItem to='/facebook' title='Danh sách Facebook' hasBullet={true} />
        <AsideMenuItem to='/group' title='Danh sách Group' hasBullet={true} />
        <AsideMenuItem to='/fanpage' title='Danh sách Fanpage' hasBullet={true} />
        <AsideMenuItem to='/vaiao' title='Danh sách Vai Ảo' hasBullet={true} />
      </AsideMenuItemWithSub>
      <AsideMenuItem
        to='/doituong'
        icon='/media/icons/duotune/art/art002.svg'
        title='ĐỐI TƯỢNG/KOL'
        fontIcon='bi-app-indicator'
      />
      <AsideMenuItemWithSub
        to='/datadoc'
        title='KHAI THÁC THÔNG TIN'
        fontIcon='bi-archive'
        icon='/media/icons/duotune/general/gen025.svg '
      >
        <AsideMenuItem to='/thongke-donvi' title='Thống kê theo đơn vị' hasBullet={true} />
        <AsideMenuItem to='/thongke-tinhchat' title='Thống kê theo tính chất' hasBullet={true} />
        <AsideMenuItem to='/thongke-phanloai' title='Thống kê theo phân loại' hasBullet={true} />
        <AsideMenuItem to='/thongke-ctnv' title='Thống kê theo công tác NV' hasBullet={true} />
      </AsideMenuItemWithSub>
      <AsideMenuItemWithSub
        to='/post'
        title='CẤU HÌNH DỮ LIỆU'
        fontIcon='bi-archive'
        icon='/media/icons/duotune/general/gen022.svg'
      >
        <AsideMenuItem to='/tags' title='TAGS' hasBullet={true} />
        <AsideMenuItem to='/tinhchat' title='TÍNH CHẤT' hasBullet={true} />
        <AsideMenuItem to='/trangthai' title='PHÂN LOẠI' hasBullet={true} />
        <AsideMenuItem to='/moiquanhe' title='MỐI QUAN HÊ' hasBullet={true} />
        <AsideMenuItem to='/ctnv' title='CÔNG TÁC NGHIỆP VỤ' hasBullet={true} />
      </AsideMenuItemWithSub>

      <AsideMenuItemWithSub
        to='/crafted/widgets'
        title='TÌM KIẾM'
        icon='/media/icons/duotune/general/gen021.svg'
        fontIcon='bi-layers'
      >
        <AsideMenuItem to='/search-trichtin' title='Từ khóa trong trích tin' hasBullet={true} />
        <AsideMenuItem to='/search-uid' title='Từ khóa trong hội nhóm' hasBullet={true} />
        <AsideMenuItem to='/search-doituong' title='Từ khóa trong đối tượng' hasBullet={true} />
        <AsideMenuItem to='/search-tags' title='Theo Tags' hasBullet={true} />
      </AsideMenuItemWithSub>
      <div className='menu-item'>
        <div className='menu-content pt-8 pb-2'>
          <span className='menu-section text-muted text-uppercase fs-8 ls-1'>
            Cấu hình hệ thống
          </span>
        </div>
      </div>
      <AsideMenuItemWithSub
        to='#'
        title='QUẢN TRỊ NGƯỜI DÙNG'
        icon='/media/icons/duotune/communication/com006.svg'
        fontIcon='bi-person'
      >
        <AsideMenuItem to='/permission' title='Phân Quyền' hasBullet={true} />
        <AsideMenuItem to='/user' title='Tài khoản' hasBullet={true} />
        <AsideMenuItem to='/donvi' title='Đơn vị' hasBullet={true} />
      </AsideMenuItemWithSub>
      <AsideMenuItem
        to='/tele'
        title='THÔNG BÁO'
        fontIcon='bi-chat-left'
        icon='/media/icons/duotune/communication/com012.svg'
      ></AsideMenuItem>
    </>
  )
}
