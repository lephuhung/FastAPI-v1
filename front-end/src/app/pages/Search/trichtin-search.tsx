import React, { FC, useEffect } from 'react';
import { useIntl } from 'react-intl';
import { PageTitle } from '../../../_metronic/layout/core';
import { KTSVG } from '../../../_metronic/helpers';
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



interface ReportHit {
  objectID: string;
  id: number;
  social_account_uid?: string | null;
  content_note?: string | null;
  comment?: string | null;
  action?: string | null;
  related_social_account_uid?: string | null;
  user_id?: string | null;
  username?: string | null;
  created_at: number;
  updated_at?: number | null;
  _highlightResult?: any;
  _snippetResult?: any;
  __position: number;
  __queryID?: string;
}

const TrichTinSearch: FC = () => {
  const intl = useIntl();

  const HitComponent: FC<{ hit: ReportHit }> = ({ hit }) => {
    const initialChar = hit.username ? hit.username.charAt(0).toUpperCase() : 
                        (hit.social_account_uid ? hit.social_account_uid.charAt(0).toUpperCase() : 'R');
    const symbolColor = hit.username ? 'success' : 'primary';

 
    const handleEditTrichTin = (reportId: number) => {
      alert(`Chỉnh sửa trích tin với ID: ${reportId}`);
    };
    
    const handleDanhDau = (reportId: number) => {
      console.log(`Xử lý tuỳ chọn: ${reportId}`);
    };


    return (
      <div className='mb-7 w-100'> 

        <div className='card card-custom gutter-b shadow-sm'> 
          <div className='card-header'>
            <div className='card-title'>
              <div className='symbol symbol-50px symbol-circle me-4'>
                <span className={`symbol-label bg-light-${symbolColor} text-${symbolColor} fs-2 fw-bold`}>
                  {initialChar}  {/*TODO: Thay bằng image_url của individual*/}
                </span>
              </div>
              <div className='flex-grow-1'> 
              <h3 className='card-label'>

                <Highlight attribute='social_account_uid' hit={hit} />
                {!hit.social_account_uid && 'Trích tin không xác định'}

                {hit.username && (
                  <small className='d-block text-muted mt-1'>
                    Tài khoản quản lý: {hit.username}
                  </small>
                )}
                {!hit.username && hit.user_id && (
                   <small className='d-block text-muted mt-1'>
                    User ID: <Highlight attribute='user_id' hit={hit} />
                  </small>
                )}
              </h3>
              </div>
            </div>
            <div className='card-toolbar'>

                <button
                  type='button'
                  className='btn btn-sm btn-icon btn-light-primary me-2' 
                  title='Cập nhật'
                  onClick={() => handleEditTrichTin(hit.id)}
                >
                  <KTSVG path='/media/icons/duotune/general/gen055.svg' className='svg-icon-2' />
                </button>

                <button
                  type='button'
                  className='btn btn-sm btn-icon btn-light-warning' 
                  title='Đánh dấu'
                  onClick={() => handleDanhDau(hit.id)}
                >
                  <KTSVG path='/media/icons/duotune/general/gen003.svg' className='svg-icon-2' />
                </button>
                
            </div>
          </div>
          <div className='card-body p-5'> 
            {hit.content_note && (
              <div className='mb-4'> 
                <p className='text-gray-800 fw-bold fs-6 mb-1'>Nội dung trích:</p> 
                <div className='text-gray-700 fs-7 report-card-snippet'> 
                  <Snippet attribute='content_note' hit={hit} />
                </div>
              </div>
            )}
            {hit.comment && (
              <div className='mb-4'>
                <p className='text-gray-800 fw-bold fs-6 mb-1'>Nhận xét:</p>
                <div className='text-gray-700 fs-7 report-card-snippet'> 
                  <Snippet attribute='comment' hit={hit} />
                </div>
              </div>
            )}
            {hit.action && (
              <div className='mb-4'>
                <p className='text-gray-800 fw-bold fs-6 mb-1'>Hành động:</p>
                <div className='text-gray-700 fs-7'> 
                   <Highlight attribute='action' hit={hit} />
                </div>
              </div>
            )}

          </div>
          <div className='card-footer d-flex justify-content-end'>
            <span className='text-muted fs-7 fw-semibold'>
                Cập nhật: {hit.updated_at
                  ? new Date(hit.updated_at * 1000).toLocaleString('vi-VN') // Hiển thị cả giờ
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
        {intl.formatMessage({ id: 'MENU.TRICHTIN.SEARCH', defaultMessage: 'TÌM KIẾM THÔNG TIN TRONG TRÍCH TIN' })}
      </PageTitle>
      <div className='card'> 
        <InstantSearch searchClient={searchClientInstance} indexName='reports'> 
          <Configure
            hitsPerPage={9}
            attributesToSnippet={['content_note:30', 'comment:20']} 
            snippetEllipsisText={'...'}
          />
          <div className='card-header border-0 pt-5'>
             <div className='w-100'>
                 <SearchBox
                    placeholder='Nhập UID, nội dung, nhận xét, hành động, username...'
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
                      { value: 'reports', label: 'Liên quan nhất' },
                      { value: 'reports:updated_at:desc', label: 'Cập nhật (mới nhất)' },
                      { value: 'reports:updated_at:asc', label: 'Cập nhật (cũ nhất)' },
                      { value: 'reports:created_at:desc', label: 'Ngày tạo (mới nhất)' },
                      { value: 'reports:created_at:asc', label: 'Ngày tạo (cũ nhất)' },
                    ]}
                    className="mt-4 mb-3"
                  />
                  <h5 className='mt-4 mb-2'>UID Tài khoản MXH</h5>
                  <RefinementList
                    attribute='social_account_uid'
                    searchable={true}
                    searchablePlaceholder="Tìm UID..."
                    showMore
                    limit={5}
                    showMoreLimit={15}
                    translations={{
                        noResultsText: 'Không có UID nào.',
                        showMoreButtonText: ({ isShowingMore }) => isShowingMore ? 'Ẩn bớt' : 'Xem thêm',
                    }}
                  />
                  <h5 className='mt-4 mb-2'>Người quản lý (Username)</h5>
                  <RefinementList
                    attribute='username' 
                    searchable={true}
                    searchablePlaceholder="Tìm username..."
                    showMore
                    limit={5}
                    showMoreLimit={15}
                     translations={{
                        noResultsText: 'Không có username nào.',
                        showMoreButtonText: ({ isShowingMore }) => isShowingMore ? 'Ẩn bớt' : 'Xem thêm',
                    }}
                  />
                </div>
              </div>
              <div className='col-lg-9'>
                <div className="report-hits-container"> 
                    <Hits hitComponent={HitComponent} 
                    classNames={{ 
                        list: 'p-0 m-0 list-unstyled', // UL là danh sách bình thường
                        item: 'd-block w-100 mb-7', // Quan trọng: Mỗi LI là một Bootstrap row và có margin bottom
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

export { TrichTinSearch };
