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
import { KTSVG } from '../../../_metronic/helpers';
import Avatar from 'react-avatar'; 
import { toast } from 'react-toastify';

import 'instantsearch.css/themes/algolia-min.css';

const MEILISEARCH_HOST = process.env.REACT_APP_MEILI_HOST || 'http://localhost:7700'; 
const MEILISEARCH_API_KEY = process.env.REACT_APP_MEILI_KEY || 'TODO_SECURE_MASTER_KEY'; 

let searchClientInstance: SearchClient | null = null;
let searchClientInitializationError: string | null = null;

try {
  if (!MEILISEARCH_HOST ) {
    // Kiểm tra nếu đang dùng giá trị fallback và biến env không được set
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



interface IndividualHit {
  objectID: string; 
  id: string; 
  full_name: string;
  national_id?: string | null; 
  citizen_id?: string | null;  
  image_url?: string | null;
  date_of_birth?: string | null; 
  is_male?: boolean | null;
  hometown?: string | null;
  additional_info?: string | null;
  phone_number?: string | null;
  is_kol?: boolean | null;
  created_at: number; // Unix timestamp
  updated_at?: number | null; // Unix timestamp

  _highlightResult?: any;
  _snippetResult?: any;
  __position: number;
  __queryID?: string;
}

const DoituongSearch: FC = () => {
  const intl = useIntl();

  const HitComponent: FC<{ hit: IndividualHit }> = ({ hit }) => {
 
    const handleDetail = (individualId: string) => {
      console.log(`View Detail for Individual ID: ${individualId}`);
      // setdoituongItem(hit); // Cần điều chỉnh để set đúng kiểu dữ liệu nếu modal dùng kiểu khác
      // setshowModalDoituong(true);
      toast.info(`Xem chi tiết đối tượng ID: ${individualId}`);
    };

    const handleEdit = (individualId: string) => {
      console.log(`Edit Individual ID: ${individualId}`);
      // setdoituongItemUpdate(hit);
      // setshowModalDoituongupdate(true);
      toast.info(`Chỉnh sửa đối tượng ID: ${individualId}`);
    };

    const handleDelete = async (individualId: string, individualName: string) => {
      if (window.confirm(`Bạn có chắc chắn muốn xóa đối tượng "${individualName}" không?`)) {
        console.log(`Delete Individual ID: ${individualId}`);
        // try {
        //   const response = await instance.delete(`${URL_API}/individuals/${individualId}`);
        //   if (response.status === 200 || response.status === 204) {
        //     toast.success(`Xóa đối tượng "${individualName}" thành công!`);
        //     // Cần cách để refresh lại danh sách Hits, ví dụ dùng refresh prop của InstantSearch
        //     // Hoặc nếu xóa thành công, Meilisearch sẽ tự cập nhật index và kết quả sẽ thay đổi
        //   } else {
        //     toast.error(`Xóa đối tượng thất bại: ${response.data.message || 'Lỗi không xác định'}`);
        //   }
        // } catch (error: any) {
        //   toast.error(`Lỗi khi xóa đối tượng: ${error.response?.data?.message || error.message || 'Lỗi không xác định'}`);
        // }
        toast.warn(`Chức năng xóa cho ID: ${individualId} cần được triển khai.`);
      }
    };


    return (
      <div className='mb-7'> 
        <div className='card card-custom gutter-b shadow-sm'>
          <div className='card-header align-items-center'>
            <div className='card-title d-flex align-items-center'>
              <div className='symbol symbol-50px symbol-circle me-4'>
                {hit.image_url ? (
                  <img src={hit.image_url} alt={hit.full_name} onError={(e) => (e.currentTarget.style.display = 'none')} />
                ) : (
                  <Avatar name={hit.full_name} round={true} size="50px" />
                )}
              </div>
              <div className='flex-grow-1'>
                <h3 className='card-label text-dark fw-bold text-hover-primary fs-6 mb-0'>
                  <Highlight attribute='full_name' hit={hit} />
                </h3>
          
                {hit.is_kol ? (
                  <span className='badge badge-light-primary fs-7 fw-bold'>KOL</span>
                ) : (
                  <span className='badge badge-light-danger fs-7 fw-bold'>-</span>
                )}
  
              </div>
            </div>
            <div className='card-toolbar'>
              {/* Các nút hành động */}
              <button
                title='Chi tiết'
                className='btn btn-icon btn-sm btn-light-primary me-2'
                onClick={() => handleDetail(hit.id)}
              >
                <KTSVG path='/media/icons/duotune/general/gen005.svg' className='svg-icon-3' />
              </button>
              <button
                title='Chỉnh sửa'
                className='btn btn-icon btn-sm btn-light-warning me-2'
                onClick={() => handleEdit(hit.id)}
              >
                <KTSVG path='/media/icons/duotune/art/art005.svg' className='svg-icon-3' />
              </button>
              <button
                title='Xóa'
                className='btn btn-icon btn-sm btn-light-danger'
                onClick={() => handleDelete(hit.id, hit.full_name)}
              >
                <KTSVG path='/media/icons/duotune/general/gen027.svg' className='svg-icon-3' />
              </button>
            </div>
          </div>
          <div className='card-body p-5'>
            {hit.national_id && (
              <div className='mb-3'>
                <span className='fw-bold text-gray-800 fs-7'>CCCD: </span>
                <span className='text-gray-600 fs-7'>
                  <Highlight attribute='national_id' hit={hit} />
                </span>
              </div>
            )}
            {hit.citizen_id && (
              <div className='mb-3'>
                <span className='fw-bold text-gray-800 fs-7'>CMND: </span>
                <span className='text-gray-600 fs-7'>
                  <Highlight attribute='citizen_id' hit={hit} />
                </span>
              </div>
            )}

            {hit.phone_number && (
              <div className='mb-3'>
                <span className='fw-bold text-gray-800 fs-7'>SĐT: </span>
                <span className='text-gray-600 fs-7'>
                  <Highlight attribute='phone_number' hit={hit} />
                </span>
              </div>
            )}
            {hit.hometown && (
              <div className='mb-3'>
                <span className='fw-bold text-gray-800 fs-7'>Quê quán: </span>
                <span className='text-gray-600 fs-7'>
                  <Highlight attribute='hometown' hit={hit} />
                </span>
              </div>
            )}
            
             {hit.additional_info && (
              <div className='mb-3'>
                <p className='text-gray-800 fw-bold fs-7 mb-1'>Thông tin thêm:</p>
                <div className='text-gray-600 fs-7 report-card-snippet'> 
                  <Snippet attribute='additional_info' hit={hit} />
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

  // Nếu có lỗi khi khởi tạo searchClient, hiển thị thông báo lỗi
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
        {intl.formatMessage({ id: 'MENU.DOITUONG.SEARCH', defaultMessage: 'TÌM KIẾM THÔNG TIN ĐỐI TƯỢNG' })}
      </PageTitle>
      <div className='card'> 
        <InstantSearch searchClient={searchClientInstance} indexName='individuals'> 
          <Configure
            hitsPerPage={5} 
            attributesToSnippet={['additional_info:50']} 
            snippetEllipsisText={'...'}
          />
          <div className='card-header border-0 pt-5'>
             <div className='w-100'>
                 <SearchBox
                    placeholder='Nhập tên, CCCD, SĐT, quê quán...'
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
                      { value: 'individuals', label: 'Liên quan nhất' },
                      { value: 'individuals:full_name:asc', label: 'Tên (A-Z)' },
                      { value: 'individuals:full_name:desc', label: 'Tên (Z-A)' },
                      { value: 'individuals:created_at:desc', label: 'Ngày tạo (mới nhất)' },
                      { value: 'individuals:created_at:asc', label: 'Ngày tạo (cũ nhất)' },
                      { value: 'individuals:updated_at:desc', label: 'Cập nhật (mới nhất)' },
                    ]}
                    className="mb-3"
                  />
                  <h5 className='mt-4 mb-2'>Trạng thái KOL</h5>
                  <RefinementList
                    attribute='is_kol' 
                    transformItems={(items) =>
                        items.map((item) => ({
                          ...item,
                          label: item.label === 'true' ? 'Là KOL' : 'Không phải KOL',
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

export { DoituongSearch  };
