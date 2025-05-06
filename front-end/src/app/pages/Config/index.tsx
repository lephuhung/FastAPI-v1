import {Navigate, Routes, Route, Outlet} from 'react-router-dom'
import {PageLink, PageTitle} from '../../../_metronic/layout/core'
import {TableTasks} from './Table-tasks'
import {TableCharacteristics} from './Table-characteristics'
import {TableStatus} from './Table-status'
import {ProfileHeader} from './ProfileHeader'
import {TableTags} from './Table-tags'
import {Overview} from '../../modules/profile/components/Overview'


const ConfigPage = () => (
  <Routes>
    <Route
      element={
        <>
          <ProfileHeader />
          <Outlet />
        </>
      }
    >
      <Route
        path='tasks'
        element={
          <>
            <PageTitle breadcrumbs={[]}>CÔNG TÁC NGHIỆP VỤ</PageTitle>
            <TableTasks className="mb-5 mb-xl-8"/>
          </>
        }
      />
      <Route
        path='characteristic'
        element={
          <>
            <PageTitle breadcrumbs={[]}>Tính chất hội nhóm/ đối tượng</PageTitle>
            <TableCharacteristics className="mb-5 mb-xl-8"/>
          </>
        }
      />
      <Route
        path='status'
        element={
          <>
            <PageTitle breadcrumbs={[]}>Trạng thái</PageTitle>
            <TableStatus className="mb-5 mb-xl-8"/>
          </>
        }
      />
      <Route
        path='tags'
        element={
          <>
            <PageTitle breadcrumbs={[]}>Tags</PageTitle>
            <TableTags className="mb-5 mb-xl-8"/>
          </>
        }
      />
      <Route index element={<Navigate to='/config/tasks' />} />
    </Route>
  </Routes>
)

export default ConfigPage