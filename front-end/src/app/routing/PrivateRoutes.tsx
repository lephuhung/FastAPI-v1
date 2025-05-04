import {lazy, FC, Suspense} from 'react'
import {Route, Routes, Navigate} from 'react-router-dom'
import {MasterLayout} from '../../_metronic/layout/MasterLayout'
import TopBarProgress from 'react-topbar-progress-indicator'
import {DashboardWrapper} from '../pages/dashboard/DashboardWrapper'
// import {MenuTestPage} from '../pages/MenuTestPage'
import {getCSSVariableValue} from '../../_metronic/assets/ts/_utils'
import {WithChildren} from '../../_metronic/helpers'
// import BuilderPageWrapper from '../pages/layout-builder/BuilderPageWrapper'
import { User } from '../pages/Users'
import { Tinhchat } from '../pages/Tinhchat'
import Search from '../pages/Search-datadoc'
import SearchPost from '../pages/Search-post'
import {CTNV} from '../pages/CTNV'
import {Moiquanhe} from '../pages/Moiquanhe'
import {Tags} from '../pages/Tags'
import {Trangthai} from '../pages/Trangthai'
import { IndividualPage } from '../pages/Individual'
import { IndividualDetailsPage } from '../pages/Individual/details'
import {SSH} from '../pages/Utils/Ssh'
import { Phanloai } from '../pages/Utils/Phanloai'
import { Thongkedonvi } from '../pages/Summary'
import { Thongkephanloai } from '../pages/Summary/Summary_individual_unit'
import {Thongketinhchat} from '../pages/Summary/Thongketinhchat'
import { Thongkectnv } from '../pages/Summary/Summary_social_account_unit'
import { Details_donvi} from '../pages/Summary/details-donvi'
import { ReportWrap } from '../pages/Report'
import { UIDSearch } from '../pages/Search/uid-search'
// import {individualsearch } from '../pages/Search/doituong-search'
import { TrichinSearch } from '../pages/Search/trichtin-search'
import { SocialAccount } from '../pages/SocialAccount'
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
        {/* Redirect to Dashboard after success login/registartion */}
        <Route path='auth/*' element={<Navigate to='/dashboard' />} />
        {/* Pages */}
        <Route path='ssh' element={<SSH/>}/>
        <Route path='phanloai' element={<Phanloai/>}/>
        <Route path='dashboard' element={<DashboardWrapper />} />
        <Route path='users' element={<User/>} />
        <Route path='social-account/:uid' element={<SocialAccount/>} />
        <Route path='moiquanhe' element={<Moiquanhe/>} />
        <Route path='tinhchat' element={<Tinhchat/>} />
        <Route path='search-datadoc' element={<Search/>} />
        <Route path='search-post' element={<SearchPost/>} />
        <Route path='ctnv' element={<CTNV/>} />
        <Route path='tags' element={<Tags/>} />
        <Route path='trangthai' element={<Trangthai/>} />
        <Route path='user' element={<User/>} />
        <Route path='individual/details/:id' element={<IndividualDetailsPage/>} />
        <Route path='individual' element={<IndividualPage/>} />
        <Route path='thongke-donvi/details/:id' element={<Details_donvi/>} />
        {/* <Route path='thongke-donvi' element={<Thongkedonvi/>} />
        <Route path='thongke-phanloai' element={<Thongkephanloai/>} /> */}
        <Route path='summary-individual-unit' element={<Thongkephanloai/>} />
        <Route path='summary-social-account-unit' element={<Thongkectnv/>} />
        {/* <Route path='reports/:id' element={<ReportWrap/>}/> */}
        <Route path='reports/social-account/:id' element={<ReportWrap/>}/>
        <Route path='search-uid' element={<UIDSearch/>} />
        {/* <Route path='search-doituong' element={<individualsearch/>} /> */}
        <Route path='search-trichtin' element={<TrichinSearch/>} />
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
