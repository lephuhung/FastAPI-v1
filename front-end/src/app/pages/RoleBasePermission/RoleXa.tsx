/* eslint-disable jsx-a11y/anchor-is-valid */
import React, {useState, useEffect} from 'react'
import {KTSVG, toAbsoluteUrl} from '../../../_metronic/helpers'
import {useQuery, useQueryClient} from 'react-query'
import Avatar from 'react-avatar'
import {useSearchParams} from 'react-router-dom'
import { ToastContainer, toast } from 'react-toastify'
import axios from 'axios'
const URL = process.env.REACT_APP_API_URL

interface Permission {
  id: number
  name: string
}

interface PermissionGroup {
  category: string
  permissions: Permission[]
}

type Props = {
  className: string
}

const RoleXa: React.FC<Props> = ({className}) => {
  const [selectedPermissions, setSelectedPermissions] = useState<number[]>([])
  const [permissionGroups, setPermissionGroups] = useState<PermissionGroup[]>([])
  const [isUpdating, setIsUpdating] = useState<boolean>(false)
  const queryClient = useQueryClient()

  // Fetch all permissions
  const {isLoading: isLoadingAllPermissions, data: allPermissions} = useQuery({
    queryKey: ['permissions'],
    queryFn: async () => {
      const response = await axios.get(`${URL}/permissions`)
      return response.data
    },
  })

  // Fetch role permissions
  const {isLoading: isLoadingRolePermissions, data: rolePermissions} = useQuery({
    queryKey: ['rolePermissionsXa'],
    queryFn: async () => {
      const response = await axios.get(`${URL}/role-permissions/roles/cax`)
      return response.data.permissions
    },
  })

  useEffect(() => {
    if (allPermissions) {
      // Group permissions by their category (before the dot)
      const groups: {[key: string]: Permission[]} = {}
      allPermissions.forEach((permission: Permission) => {
        const [category] = permission.name.split('.')
        if (!groups[category]) {
          groups[category] = []
        }
        groups[category].push(permission)
      })

      // Convert groups object to array of PermissionGroup
      const formattedGroups = Object.entries(groups).map(([category, perms]) => ({
        category,
        permissions: perms,
      }))

      setPermissionGroups(formattedGroups)
    }
  }, [allPermissions])

  // Set initial selected permissions when role permissions are loaded
  useEffect(() => {
    if (rolePermissions) {
      const selectedIds = rolePermissions.map((permission: Permission) => permission.id)
      setSelectedPermissions(selectedIds)
    }
  }, [rolePermissions])

  const handleCheckboxChange = (permissionId: number) => {
    setSelectedPermissions((prev) => {
      if (prev.includes(permissionId)) {
        return prev.filter((id) => id !== permissionId)
      } else {
        return [...prev, permissionId]
      }
    })
  }

  const handleUpdatePermissions = async () => {
    try {
      setIsUpdating(true)
      await axios.put(`${URL}/role-permissions/roles/cax/permissions`, {
        permission_ids: selectedPermissions,
      })
      
      // Invalidate and refetch queries
      await queryClient.invalidateQueries('rolePermissionsXa')
      
      toast.success('Cập nhật quyền thành công')
    } catch (error) {
      console.error('Error updating permissions:', error)
      toast.error('Có lỗi xảy ra khi cập nhật quyền')
    } finally {
      setIsUpdating(false)
    }
  }

  if (isLoadingAllPermissions || isLoadingRolePermissions) {
    return <div>Loading...</div>
  }

  return (
    <div className={`card ${className}`}>
      {/* begin::Header */}
      <div className='card-header border-0 pt-5'>
        <h3 className='card-title align-items-start flex-column'>
          <span className='card-label fw-bold fs-3 mb-1'>DANH SÁCH QUYỀN TRONG ROLE</span>
        </h3>
        <div className='card-toolbar'>
          <button
            type='button'
            className='btn btn-sm btn-light-primary'
            onClick={handleUpdatePermissions}
            disabled={isUpdating}
          >
            {isUpdating ? (
              <span className='spinner-border spinner-border-sm' role='status' aria-hidden='true'></span>
            ) : (
              <KTSVG path='/media/icons/duotune/arrows/arr075.svg' className='svg-icon-2' />
            )}
            {isUpdating ? 'Đang cập nhật...' : 'Cập nhật lại quyền'}
          </button>
        </div>
      </div>
      {/* end::Header */}
      {/* begin::Body */}
      <div className='card-body py-3'>
        {/* begin::Permissions */}
        <div className='row g-9'>
          {permissionGroups.map((group) => (
            <div key={group.category} className='col-md-4'>
              <div className='card card-flush h-md-100'>
                <div className='card-header'>
                  <div className='card-title'>
                    <h2 className='text-capitalize'>{group.category}</h2>
                  </div>
                </div>
                <div className='card-body pt-1'>
                  <div className='d-flex flex-column gap-2'>
                    {group.permissions.map((permission) => (
                      <div key={permission.id} className='d-flex align-items-center'>
                        <label className='form-check form-check-custom form-check-solid me-5'>
                          <input
                            className='form-check-input'
                            type='checkbox'
                            checked={selectedPermissions.includes(permission.id)}
                            onChange={() => handleCheckboxChange(permission.id)}
                            disabled={isUpdating}
                          />
                          <span className='form-check-label'>{permission.name}</span>
                        </label>
                      </div>
                    ))}
                  </div>
                </div>
              </div>
            </div>
          ))}
        </div>
        {/* end::Permissions */}
      </div>
      {/* end::Body */}
      <ToastContainer />
    </div>
  )
}

export {RoleXa}
