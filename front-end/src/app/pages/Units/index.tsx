import React from 'react';
import UnitTable from './Table';
import { useIntl } from 'react-intl';
import { PageTitle } from '../../../_metronic/layout/core';
// import './Table.css';

const Units: React.FC = () => {
  // You would typically get this from your routing or state management
  const unitId = 'd3a98a7e-8535-4ab0-aaa1-69aed21c16de'; // Replace with actual unit ID

  return (
    <>
      {/* <PageTitle breadcrumbs={[]}>{intl.formatMessage({ id: 'MENU.USERS' })}</PageTitle>  */}
      <div className="card">
        <div className="card-header">
          <h3 className="card-title">Unit Users Management</h3>
        </div>
        <div className="card-body">
          <UnitTable />
        </div>
      </div>
    </>
  );
};

export { Units };