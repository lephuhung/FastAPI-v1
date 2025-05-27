import {lazy, FC, Suspense} from 'react'
import {Route, Routes, Navigate} from 'react-router-dom'
import {MasterLayout} from '../../_metronic/layout/MasterLayout'
import TopBarProgress from 'react-topbar-progress-indicator'
import {DashboardWrapper} from '../pages/dashboard/DashboardWrapper'
import {getCSSVariableValue} from '../../_metronic/assets/ts/_utils'
import {WithChildren} from '../../_metronic/helpers'
import {Users} from '../pages/Users'
import Search from '../pages/Search-datadoc'
import SearchPost from '../pages/Search-post'
import ConfigPage from '../pages/Config'
import {IndividualPage} from '../pages/Individual'
import {IndividualDetailsPage} from '../pages/Individual/details'
import {SSH} from '../pages/Utils/Ssh'
import {Phanloai} from '../pages/Utils/Phanloai'
import {Units} from '../pages/Units'
import {Thongkephanloai} from '../pages/Summary/Summary_individual_unit'
import {Thongkectnv} from '../pages/Summary/Summary_social_account_unit'
// import {Details_donvi} from '../pages/Summary/details-donvi'
import {ReportWrap} from '../pages/Report'
import {UIDSearch} from '../pages/Search/uid-search'
import {TrichTinSearch} from '../pages/Search/trichtin-search'
import {DoituongSearch} from '../pages/Search/doituong-search'
import {SocialAccount} from '../pages/SocialAccount'
import RoleBasePermissionPage from '../pages/RoleBasePermission'
const PrivateRoutes = () => {
  const ProfilePage = lazy(() => import('../modules/profile/ProfilePage'))
  const WizardsPage = lazy(() => import('../modules/wizards/WizardsPage'))
  const AccountPage = lazy(() => import('../modules/accounts/AccountPage'))
  const WidgetsPage = lazy(() => import('../modules/widgets/WidgetsPage'))
  const ChatPage = lazy(() => import('../modules/apps/chat/ChatPage'))
  const UsersPage = lazy(() => import('../modules/apps/user-management/UsersPage'))

  return (
    <Routes>
      <Route element={<MasterLayout />}>
        <Route path='auth/*' element={<Navigate to='/dashboard' />} />
        {/* Pages */}
        <Route path='ssh' element={<SSH />} />
        <Route path='phanloai' element={<Phanloai />} />
        <Route path='dashboard' element={<DashboardWrapper />} />
        <Route path='users' element={<Users />} />
        <Route path='social-account/:uid' element={<SocialAccount />} />
        <Route path='search-datadoc' element={<Search />} />
        <Route path='search-post' element={<SearchPost />} />
        <Route path='individual/details/:id' element={<IndividualDetailsPage />} />
        <Route path='individual' element={<IndividualPage />} />
        <Route path='units' element={<Units />} />
        <Route path='summary-individual-unit' element={<Thongkephanloai />} />
        <Route path='summary-social-account-unit' element={<Thongkectnv />} /> 
        <Route path='reports/social-account/:id' element={<ReportWrap />} />
        <Route path='reports/individuals/:id' element={<ReportWrap />} />
        <Route path='search-uid' element={<UIDSearch />} />
        <Route path='search-trichtin' element={<TrichTinSearch />} />
        <Route path='search-doituong' element={<DoituongSearch />} />
        <Route
          path='config/*'
          element={
            <SuspensedView>
              <ConfigPage />
            </SuspensedView>
          }
        />
        <Route
          path='permission/*'
          element={
            <SuspensedView>
              <RoleBasePermissionPage />
            </SuspensedView>
          }
        />
        <Route
          path='crafted/pages/profile/*'
          element={
            <SuspensedView>
              <ProfilePage />
            </SuspensedView>
          }
        />
        <Route
          path='crafted/pages/wizards/*'
          element={
            <SuspensedView>
              <WizardsPage />
            </SuspensedView>
          }
        />
        <Route
          path='crafted/widgets/*'
          element={
            <SuspensedView>
              <WidgetsPage />
            </SuspensedView>
          }
        />
        <Route
          path='crafted/account/*'
          element={
            <SuspensedView>
              <AccountPage />
            </SuspensedView>
          }
        />
        <Route
          path='apps/chat/*'
          element={
            <SuspensedView>
              <ChatPage />
            </SuspensedView>
          }
        />
        <Route
          path='apps/user-management/*'
          element={
            <SuspensedView>
              <UsersPage />
            </SuspensedView>
          }
        />
        {/* Page Not Found */}
        <Route path='*' element={<Navigate to='/error/404' />} />
      </Route>
    </Routes>
  )
}

const SuspensedView: FC<WithChildren> = ({children}) => {
  const baseColor = getCSSVariableValue('--kt-primary')
  TopBarProgress.config({
    barColors: {
      '0': baseColor,
    },
    barThickness: 1,
    shadowBlur: 5,
  })
  return <Suspense fallback={<TopBarProgress />}>{children}</Suspense>
}

export {PrivateRoutes}
