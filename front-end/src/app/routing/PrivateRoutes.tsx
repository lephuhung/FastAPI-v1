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
import { Facebook } from '../pages/Facebook'
import { Group } from '../pages/Group'
import { Fanpage } from '../pages/Fanpages'
import { Characteristic } from '../pages/Characteristic'
import { Vaiao } from '../pages/Vaiao'
import Search from '../pages/Search-datadoc'
import SearchPost from '../pages/Search-post'
import {CTNV} from '../pages/Task'
import {Moiquanhe} from '../pages/Moiquanhe'
import {Tags} from '../pages/Tags'
import {Status} from '../pages/Status'
import { Individual } from '../pages/Individual/index'
import { Details } from '../pages/Individual/details'
import {SSH} from '../pages/Utils/Ssh'
import { Phanloai } from '../pages/Utils/Phanloai'
import { ReportUnit } from '../pages/ReportUnit'
import { Thongkephanloai } from '../pages/ReportUnit/Thongkephanloai'
import {ReportCharacteristic} from '../pages/ReportUnit/ReportCharacteristic'
import { ReportTask } from '../pages/ReportUnit/ReportTask'
import { DetailsUnit} from '../pages/ReportUnit/DetailsUnit'
import { TrichtinWrap } from '../pages/Trichtin'
import { TrichtinVaiaoWrap } from '../pages/Trichtin/trichtinvaiao'
import { UIDSearch } from '../pages/Search/uid-search'
import {IndividualSearch } from '../pages/Search/IndividualSearch'
import { TrichinSearch } from '../pages/Search/trichtin-search'
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
        <Route path='facebook' element={<Facebook/>} />
        <Route path='group' element={<Group/>} />
        <Route path='Fanpage' element={<Fanpage/>} />
        <Route path='relationship' element={<Moiquanhe/>} />
        <Route path='characteristic' element={<Characteristic/>} />
        <Route path='vaiao' element={<Vaiao/>}/>
        <Route path='search-datadoc' element={<Search/>} />
        <Route path='search-post' element={<SearchPost/>} />
        <Route path='task' element={<CTNV/>} />
        <Route path='tags' element={<Tags/>} />
        <Route path='status' element={<Status/>} />
        <Route path='user' element={<User/>} />
        <Route path='individual/details/:id' element={<Details/>} />
        <Route path='individual' element={<Individual/>} />
        <Route path='report-unit/details/:id' element={<DetailsUnit/>} />
        <Route path='report-unit' element={<ReportUnit/>} />
        <Route path='report-phanloai' element={<Thongkephanloai/>} />
        <Route path='report-task' element={<ReportTask/>} /> 
        <Route path='report-characteristic' element={<ReportCharacteristic/>} />
        <Route path='trichtin/:id' element={<TrichtinWrap/>}/>
        <Route path='trichtinvaiao/:id' element={<TrichtinVaiaoWrap/>}/>
        <Route path='search-uid' element={<UIDSearch/>} />
        <Route path='search-individual' element={<IndividualSearch/>} />
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
