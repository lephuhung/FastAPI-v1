// import React from 'react'
import {Navigate, Routes, Route, Outlet} from 'react-router-dom'
import {PageTitle} from '../../../_metronic/layout/core'
import { RolePhong } from './RolePhong'
import { RoleXa}  from './RoleXa'
import { RoleAdmin } from './RoleAdmin'
import { ProfileHeader } from './ProfileHeader'
import { RoleDoi } from './RoleDoi'
const RoleBasePermissionPage = () => (
  <Routes>
    <Route
      element={
        <>
          <ProfileHeader />
          < Outlet/>
        </>
      }
    >
      <Route
        path='role-phong'
        element={
          <>
            <PageTitle breadcrumbs={[]}>PHÂN QUYỀN PHÒNG</PageTitle>
            <RolePhong className=""/>
          </>
        }
      />
      <Route
        path='role-xa'
        element={
          <>
            <PageTitle breadcrumbs={[]}>PHÂN QUYỀN XÃ</PageTitle>
            <RoleXa className="mb-5 mb-xl-8"/>
          </>
        }
      />
      <Route
        path='role-admin'
        element={
          <>
            <PageTitle breadcrumbs={[]}>PHÂN QUYỀN ADMIN</PageTitle>
            <RoleAdmin className="mb-5 mb-xl-8"/>
          </>
        }
      />
      <Route
        path='role-doi'
        element={
          <>
            <PageTitle breadcrumbs={[]}>PHÂN QUYỀN ĐỘI</PageTitle>
            <RoleDoi className="mb-5 mb-xl-8"/>
          </>
        }
      />
      <Route index element={<Navigate to='/permission/role-admin' />} />
    </Route>
  </Routes>
)

export default RoleBasePermissionPage