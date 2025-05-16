import React, { FC, useEffect } from 'react';
import { useIntl } from 'react-intl';
import { PageTitle } from '../../../_metronic/layout/core';
import {
  InstantSearch,
  Hits,
  SortBy,
  SearchBox,
  Pagination,
  Highlight,
  ClearRefinements,
  RefinementList,
  Configure,
  Snippet,
} from 'react-instantsearch';
import { instantMeiliSearch } from '@meilisearch/instant-meilisearch';
import { SearchClient } from 'instantsearch.js';
import { KTSVG, toAbsoluteUrl } from '../../../_metronic/helpers';
import Avatar from 'react-avatar'; // Giữ lại Avatar
import { toast } from 'react-toastify';

import 'instantsearch.css/themes/algolia-min.css';

const MEILISEARCH_HOST = process.env.REACT_APP_MEILI_HOST || 'http://localhost:7700'; 
const MEILISEARCH_API_KEY = process.env.REACT_APP_MEILI_KEY || 'TODO_SECURE_MASTER_KEY'; 

let searchClientInstance: SearchClient | null = null;
let searchClientInitializationError: string | null = null;

try {
  if (!MEILISEARCH_HOST ) {
 
    throw new Error('Meilisearch host (REACT_APP_MEILI_HOST) không được cấu hình đúng. Vui lòng kiểm tra file .env của bạn.');
  }
  if (!MEILISEARCH_API_KEY ) {
    throw new Error('Meilisearch API key (REACT_APP_MEILI_API_KEY) không được cấu hình đúng. Vui lòng kiểm tra file .env của bạn.');
  }

const { searchClient } = instantMeiliSearch(
  MEILISEARCH_HOST,
  MEILISEARCH_API_KEY,
  {
    finitePagination: true,
    primaryKey: 'id', // Assuming 'id' is the primary key for the 'reports' index in Meilisearch
    // Keep placeholder search if no search query is entered
    // keepZeroFacets: true, // Uncomment if you want to show all facet values even if count is 0
  }
);

  searchClientInstance = searchClient as unknown as SearchClient;

} catch (error: any) {
  console.error("Lỗi nghiêm trọng khi khởi tạo Meilisearch client:", error);
  searchClientInitializationError = error.message || "Lỗi không xác định khi khởi tạo Meilisearch client.";
}



interface SocialAccountHit {
  objectID: string; 
  id: string;    
  uid: string;    
  name?: string | null;
  reaction_count?: number | null;
  phone_number?: string | null;
  status_id?: number | null;
  type_id?: number | null;
  note?: string | null;
  is_active?: boolean | null;
  created_at: number; // Unix timestamp
  updated_at?: number | null; // Unix timestamp
  status_name?: string; 
  account_type_name?: string;
  _highlightResult?: any;
  _snippetResult?: any;
  __position: number;
  __queryID?: string;
}

const UIDSearch: FC = () => {
  const intl = useIntl();

  const [accountTypes, setAccountTypes] = React.useState<any[]>([]);
  const [statuses, setStatuses] = React.useState<any[]>([]);

  useEffect(() => {
    const typeString = localStorage.getItem('account_types');
    if (typeString) setAccountTypes(JSON.parse(typeString));

    
    const statusesString = localStorage.getItem('statuses');
    if (statusesString) setStatuses(JSON.parse(statusesString));

  }, []);

  const getStatusName = (statusId?: number | null): string => {
    if (statusId === null || statusId === undefined) return 'N/A';
    const status = statuses.find(s => s.id === statusId);
    return status ? status.name : `ID: ${statusId}`;
  };

  const getColorForStatus = (statusId?: number | null): string => {
    if (statusId === null || statusId === undefined) return 'secondary'; 
    // Ánh xạ status_id sang tên màu Metronic
    // 1: Hoạt động (Green)
    // 2: Riêng tư (Red)
    // 3: Khóa trang cá nhân (Yellow)
    // 4: Dừng hoạt động (Cyan/Blue)
    // 5: Cần theo dõi (Magenta/Purple)
    switch (statusId) {
      case 1: return 'success';
      case 2: return 'info';
      case 3: return 'danger';
      case 4: return 'secondary';
      case 5: return 'primary'; 
      default: return 'warning'; 
    }
  };

  const getAccountTypeName = (typeId?: number | null): string => {
     if (typeId === null || typeId === undefined) return 'N/A';
    const type = accountTypes.find(t => t.id === typeId);
    return type ? type.name : `ID: ${typeId}`;
  };

  const HitComponent: FC<{ hit: SocialAccountHit }> = ({ hit }) => {
 
    const handleDetail = (accountId: string) => {
      console.log(`View Detail for Account ID (UID): ${accountId}`);
      toast.info(`Xem chi tiết tài khoản UID: ${accountId}`);
    };

    const handleEdit = (accountId: string) => {
      console.log(`Edit Account ID (UID): ${accountId}`);
      toast.info(`Chỉnh sửa tài khoản UID: ${accountId}`);
    };

    const handleDelete = async (accountId: string, accountName?: string | null) => {
      if (window.confirm(`Chắc chắn muốn xóa tài khoản "${accountName || accountId}"?`)) {
        console.log(`Delete Account ID (UID): ${accountId}`);
        // try {
        //   const response = await instance.delete(`${URL_API}/social-accounts/${accountId}`); // Giả sử endpoint là /social-accounts/:uid
        //   if (response.status === 200 || response.status === 204) {
        //     toast.success(`Xóa tài khoản "${accountName || accountId}" thành công!`);
        //   } else {
        //     toast.error(`Xóa tài khoản thất bại.`);
        //   }
        // } catch (error) {
        //   toast.error(`Lỗi khi xóa tài khoản.`);
        // }
        toast.warn(`Chức năng xóa cho UID: ${accountId} cần được triển khai.`);
      }
    };
    
    const displayName = hit.name || `UID: ${hit.uid}`;
    const statusColor = getColorForStatus(hit.status_id);

    return (
      <div className='mb-7'> 
        <div className='card card-custom gutter-b shadow-sm'>
          <div className='card-header align-items-center'>
            <div className='card-title d-flex align-items-center'>
              <div className='symbol symbol-50px symbol-circle me-4'>
                <img src={toAbsoluteUrl('/media/svg/brand-logos/facebook-4.svg')} alt={displayName} />
           
              </div>
              <div className='flex-grow-1'>
                <h3 className='card-label text-dark fw-bold text-hover-primary fs-6 mb-0'>
                  <Highlight attribute='name' hit={hit} />
                  {!hit.name && <Highlight attribute='uid' hit={hit} />}
                </h3>
                <span className='text-muted d-block fw-semibold fs-7'>
                  UID: <Highlight attribute='uid' hit={hit} />
                </span>
              </div>
            </div>
            <div className='card-toolbar'>
              <button title='Chi tiết' className='btn btn-icon btn-sm btn-light-primary me-2' onClick={() => handleDetail(hit.uid)}>
                <KTSVG path='/media/icons/duotune/general/gen005.svg' className='svg-icon-3' />
              </button>
              <button title='Chỉnh sửa' className='btn btn-icon btn-sm btn-light-warning me-2' onClick={() => handleEdit(hit.uid)}>
                <KTSVG path='/media/icons/duotune/art/art005.svg' className='svg-icon-3' />
              </button>
              <button title='Xóa' className='btn btn-icon btn-sm btn-light-danger' onClick={() => handleDelete(hit.uid, hit.name)}>
                <KTSVG path='/media/icons/duotune/general/gen027.svg' className='svg-icon-3' />
              </button>
            </div>
          </div>
          <div className='card-body p-5'>
            {hit.phone_number && (
              <div className='mb-3'>
                <span className='fw-bold text-gray-800 fs-7'>Số điện thoại: </span>
                <span className='text-gray-600 fs-7'>
                  <Highlight attribute='phone_number' hit={hit} />
                </span>
              </div>
            )}
             <div className='mb-3'>
                <span className='fw-bold text-gray-800 fs-7'>Loại tài khoản: </span>
                <span className='badge badge-light-info fs-7'>
                    {getAccountTypeName(hit.type_id)}
                </span>
              </div>
            <div className='mb-3'>
              <span className='fw-bold text-gray-800 fs-7'>Trạng thái: </span>
              <span className={`badge badge-light-${statusColor} fs-7`}>
                {getStatusName(hit.status_id)}
              </span>
            </div>
            {hit.reaction_count !== null && hit.reaction_count !== undefined && (
              <div className='mb-3'>
                <span className='fw-bold text-gray-800 fs-7'>Lượt tương tác: </span>
                <span className='text-gray-600 fs-7'>{hit.reaction_count}</span>
              </div>
            )}
            {hit.note && (
              <div className='mb-3'>
                <p className='text-gray-800 fw-bold fs-7 mb-1'>Ghi chú:</p>
                <div className='text-gray-600 fs-7 report-card-snippet'> 
                  <Snippet attribute='note' hit={hit} />
                </div>
              </div>
            )}
          </div>
          <div className='card-footer d-flex justify-content-end'>
            <span className='text-muted fs-7 fw-semibold'>
                Cập nhật: {hit.updated_at
                  ? new Date(hit.updated_at * 1000).toLocaleString('vi-VN')
                  : new Date(hit.created_at * 1000).toLocaleString('vi-VN')}
            </span>
          </div>
        </div>
      </div>
    );
  };

  if (searchClientInitializationError || !searchClientInstance) {
    return (
      <>
        <PageTitle breadcrumbs={[]}>Lỗi Cấu Hình Tìm Kiếm</PageTitle>
        <div className='card'>
          <div className='card-body'>
            <div className='alert alert-danger'>
              <h4 className='alert-heading'>Không thể khởi tạo Meilisearch client!</h4>
              <p>Đã xảy ra lỗi trong quá trình thiết lập kết nối đến server tìm kiếm. Chức năng tìm kiếm sẽ không hoạt động.</p>
              <hr />
              <p className='mb-0'>
                <strong>Chi tiết lỗi:</strong> {searchClientInitializationError || "Không có thông tin lỗi cụ thể."}
              </p>
              <div className='mt-2'>
                <strong>Gợi ý:</strong>
                <ul>
                  <li>Kiểm tra lại các biến <code>REACT_APP_MEILI_HOST</code> và <code>REACT_APP_MEILI_KEY</code> trong file <code>.env</code> của bạn.</li>
                  <li>Đảm bảo server Meilisearch đang chạy và có thể truy cập được từ địa chỉ: <code>{MEILISEARCH_HOST || 'Chưa cấu hình HOST'}</code>.</li>
                  <li>Kiểm tra console của trình duyệt (F12) để biết thêm thông tin chi tiết.</li>
                  <li>Sau khi sửa file <code>.env</code>, bạn cần khởi động lại server phát triển React.</li>
                </ul>
              </div>
            </div>
          </div>
        </div>
      </>
    );
  }

  return (
    <>
      <PageTitle breadcrumbs={[]}>
        {intl.formatMessage({ id: 'MENU.UID.SEARCH', defaultMessage: 'TÌM KIẾM TÀI KHOẢN MẠNG XÃ HỘI, HỘI NHÓM' })}
      </PageTitle>
      <div className='card'> 
        <InstantSearch searchClient={searchClientInstance} indexName='social_accounts'>
          <Configure
            hitsPerPage={5} 
            attributesToSnippet={['note:50']} 
            snippetEllipsisText={'...'}
          />
          <div className='card-header border-0 pt-5'>
             <div className='w-100'>
                 <SearchBox
                    placeholder='Nhập UID, tên tài khoản, SĐT, ghi chú...'
                    autoFocus
                    className='form-control form-control-lg form-control-solid' 
                  />
            </div>
          </div>
          <div className='card-body py-3'>
            <div className='row'>
              <div className='col-lg-3'>
                <div className='mb-5 p-4 border rounded bg-light'>
                  <h4>Bộ lọc & Sắp xếp</h4>
                  <ClearRefinements
                    translations={{
                      resetButtonText: 'Xóa bộ lọc',
                    }}
                    className='btn btn-sm btn-outline-secondary w-100 mb-3'
                  />
                  <h5 className='mt-3 mb-2'>Sắp xếp theo</h5>
                  <SortBy
                    items={[
                      { value: 'social_accounts', label: 'Liên quan nhất' },
                      { value: 'social_accounts:name:asc', label: 'Tên (A-Z)' },
                      { value: 'social_accounts:name:desc', label: 'Tên (Z-A)' },
                      { value: 'social_accounts:reaction_count:desc', label: 'Tương tác (Cao-Thấp)' },
                      { value: 'social_accounts:reaction_count:asc', label: 'Tương tác (Thấp-Cao)' },
                      { value: 'social_accounts:created_at:desc', label: 'Ngày tạo (mới nhất)' },
                      { value: 'social_accounts:updated_at:desc', label: 'Cập nhật (mới nhất)' },
                    ]}
                    className="mb-3"
                  />
                  <h5 className='mt-4 mb-2'>Loại tài khoản</h5>
                  <RefinementList
                    attribute='type_id' 
                    transformItems={(items) =>
                        items.map((item) => ({
                          ...item,
                          label: getAccountTypeName(parseInt(item.label, 10)), 
                        }))
                      }
                    translations={{
                        noResultsText: 'Không có loại tài khoản.',
                    }}
                  />
                 
                  <h5 className='mt-4 mb-2'>Trạng thái</h5>
                  <RefinementList
                    attribute='status_id' 
                    transformItems={(items) =>
                        items.map((item) => ({
                          ...item,
                          label: getStatusName(parseInt(item.label, 10)),
                        }))
                      }
                    translations={{
                        noResultsText: 'Không có trạng thái.',
                    }}
                  />
                </div>
              </div>
              <div className='col-lg-9'>
                <div className="report-hits-container"> 
                    <Hits 
                      hitComponent={HitComponent} 
                      classNames={{ 
                        list: 'list-unstyled p-0 m-0', 
                        item: 'd-block w-100', 
                      }}
                    />
                </div>
                <div className='d-flex justify-content-center mt-5'>
                  <Pagination showLast={true} />
                </div>
              </div>
            </div>
          </div>
        </InstantSearch>
      </div>
    </>
  );
};

export { UIDSearch  };
