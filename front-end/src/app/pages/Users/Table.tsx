/* eslint-disable jsx-a11y/anchor-is-valid */
import React, { useEffect, useState, useCallback } from 'react';
import axios from 'axios';
import { ToastContainer, toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';

interface User {
  id: string;
  username: string;
  is_active: boolean;
  roles: Array<{
    id: string;
    name: string;
  }>;
  unit_id: string;
  unit?: {
    id: string;
    name: string;
  };
}

interface Role {
  id: string;
  name: string;
}

const styles = {
  container: {
    width: '100%',
    overflowX: 'auto' as const,
  },
  table: {
    width: '100%',
    borderCollapse: 'collapse' as const,
    margin: '20px 0',
  },
  th: {
    padding: '12px',
    textAlign: 'center' as const,
    borderBottom: '1px solid #ddd',
    backgroundColor: '#f7f7f7',
    fontWeight: 500,
    color: '#333',
    letterSpacing: '0.5px',
  },
  td: {
    padding: '12px',
    textAlign: 'center' as const,
    borderBottom: '1px solid #ddd',
  },
  tr: {
    backgroundColor: 'transparent',
  },
  trHover: {
    backgroundColor: '#f9f9f9',
  },
  switch: {
    position: 'relative' as const,
    display: 'inline-block',
    width: '44px',
    height: '24px',
  },
  switchInput: {
    opacity: 0,
    width: 0,
    height: 0,
  },
  slider: {
    position: 'absolute' as const,
    cursor: 'pointer',
    top: 0,
    left: 0,
    right: 0,
    bottom: 0,
    backgroundColor: '#e0e0e0',
    transition: '.3s',
    borderRadius: '24px',
  },
  sliderChecked: {
    backgroundColor: '#4CAF50',
  },
  knob: {
    position: 'absolute' as const,
    top: '3px',
    left: '3px',
    width: '18px',
    height: '18px',
    backgroundColor: '#fff',
    borderRadius: '50%',
    boxShadow: '0 2px 4px rgba(0,0,0,0.2)',
    transition: 'transform .3s',
  },
  knobChecked: {
    transform: 'translateX(20px)',
  },
  button: {
    padding: '8px 16px',
    border: 'none',
    borderRadius: '4px',
    cursor: 'pointer',
    marginRight: '8px',
    fontSize: '14px',
  },
  primaryButton: {
    backgroundColor: '#2196F3',
    color: 'white',
  },
  secondaryButton: {
    backgroundColor: '#f5f5f5',
    color: '#333',
  },
  modal: {
    position: 'fixed' as const,
    top: 0,
    left: 0,
    width: '100%',
    height: '100%',
    backgroundColor: 'rgba(0, 0, 0, 0.5)',
    display: 'flex',
    justifyContent: 'center',
    alignItems: 'center',
    zIndex: 1000,
  },
  modalContent: {
    backgroundColor: 'white',
    padding: '20px',
    borderRadius: '8px',
    minWidth: '300px',
    maxWidth: '500px',
  },
  formGroup: {
    marginBottom: '20px',
  },
  input: {
    width: '100%',
    padding: '8px',
    border: '1px solid #ddd',
    borderRadius: '4px',
    fontSize: '14px',
  },
  select: {
    width: '100%',
    padding: '8px',
    border: '1px solid #ddd',
    borderRadius: '4px',
    fontSize: '14px',
    height: '120px',
  },
  formActions: {
    display: 'flex',
    justifyContent: 'flex-end',
    gap: '8px',
  },
  loading: {
    textAlign: 'center' as const,
    padding: '20px',
    fontSize: '16px',
    color: '#666',
  },
  actionButtons: {
    display: 'flex',
    gap: '8px',
  },
};

const UserTable: React.FC = () => {
  const [users, setUsers] = useState<User[]>([]);
  const [roles, setRoles] = useState<Role[]>([]);
  const [loading, setLoading] = useState(false);
  const [passwordModalVisible, setPasswordModalVisible] = useState(false);
  const [roleModalVisible, setRoleModalVisible] = useState(false);
  const [selectedUser, setSelectedUser] = useState<User | null>(null);
  const [newPassword, setNewPassword] = useState('');
  const [selectedRoles, setSelectedRoles] = useState<string[]>([]);
  const [hoveredRow, setHoveredRow] = useState<string | null>(null);
  const [error, setError] = useState<string | null>(null);
  const URL = process.env.REACT_APP_API_URL
  const fetchUsers = useCallback(async () => {
    try {
      setLoading(true);
      setError(null);
      console.log('Fetching all users');
      const response = await axios.get(`${URL}/users`);
      console.log('Users response:', response.data);
      setUsers(response.data);
    } catch (error) {
      console.error('Error fetching users:', error);
      setError('Failed to fetch users. Please try again.');
      if (axios.isAxiosError(error)) {
        console.error('API Error:', error.response?.data);
      }
    } finally {
      setLoading(false);
    }
  }, []);

  const fetchRoles = useCallback(async () => {
    try {
      setError(null);
      console.log('Fetching roles');
      const response = await axios.get(`${URL}/roles`);
      console.log('Roles response:', response.data);
      setRoles(response.data);
    } catch (error) {
      console.error('Error fetching roles:', error);
      setError('Failed to fetch roles. Please try again.');
      if (axios.isAxiosError(error)) {
        console.error('API Error:', error.response?.data);
      }
    }
  }, []);

  useEffect(() => {
    console.log('Component mounted');
    fetchUsers();
    fetchRoles();
  }, [fetchUsers, fetchRoles]);

  const handleToggleActive = async (userId: string) => {
    try {
      setError(null);
      console.log('Toggling active state for user:', userId);
      await axios.put(`${URL}/users/${userId}/toggle-active`);
      console.log('Toggle successful');
      toast.success('User status updated');
      fetchUsers();
    } catch (error) {
      console.error('Error toggling user status:', error);
      setError('Failed to update user status. Please try again.');
      if (axios.isAxiosError(error)) {
        console.error('API Error:', error.response?.data);
      }
    }
  };

  const handlePasswordChange = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!selectedUser) return;
    try {
      setError(null);
      console.log('Changing password for user:', selectedUser.id);
      await axios.put(`${URL}/users/${selectedUser.id}/password`, { password: newPassword });
      console.log('Password change successful');
      toast.success('Password updated successfully');
      setPasswordModalVisible(false);
      setNewPassword('');
    } catch (error) {
      console.error('Error changing password:', error);
      setError('Failed to update password. Please try again.');
      if (axios.isAxiosError(error)) {
        console.error('API Error:', error.response?.data);
      }
    }
  };

  const handleRoleUpdate = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!selectedUser) return;
    try {
      setError(null);
      console.log('Updating roles for user:', selectedUser.id);
      await axios.put(`${URL}/users/${selectedUser.id}/roles`, { role_ids: selectedRoles });
      console.log('Role update successful');
      toast.success('Roles updated successfully');
      setRoleModalVisible(false);
      setSelectedRoles([]);
      fetchUsers();
    } catch (error) {
      console.error('Error updating roles:', error);
      setError('Failed to update roles. Please try again.');
      if (axios.isAxiosError(error)) {
        console.error('API Error:', error.response?.data);
      }
    }
  };

  return (
    <div style={styles.container}>
      {error && (
        <div style={{ 
          padding: '10px', 
          margin: '10px 0', 
          backgroundColor: '#ffebee', 
          color: '#c62828', 
          borderRadius: '4px' 
        }}>
          {error}
        </div>
      )}
      {loading ? (
        <div style={styles.loading}>Loading...</div>
      ) : users.length === 0 ? (
        <div style={{ textAlign: 'center', padding: '20px' }}>
          No users found.
        </div>
      ) : (
        <table style={styles.table}>
          <thead>
            <tr>
              <th style={styles.th}> Tên tài khoản</th>
              <th style={styles.th}>Đơn vị</th>
              <th style={styles.th}>Trạng thái</th>
              <th style={styles.th}>Vai trò</th>
              <th style={styles.th}>Hành động</th>
            </tr>
          </thead>
          <tbody>
            {users.map((user) => (
              <tr 
                key={user.id} 
                style={{
                  ...styles.tr,
                  ...(hoveredRow === user.id ? styles.trHover : {})
                }}
                onMouseEnter={() => setHoveredRow(user.id)}
                onMouseLeave={() => setHoveredRow(null)}
              >
                <td style={styles.td}>{user.username}</td>
                <td style={styles.td}>{user.unit?.name || 'No Unit'}</td>
                <td style={styles.td}>
                  <label style={styles.switch}>
                    <input
                      type="checkbox"
                      checked={user.is_active}
                      onChange={() => handleToggleActive(user.id)}
                      style={styles.switchInput}
                    />
                    <span style={{
                      ...styles.slider,
                      ...(user.is_active ? styles.sliderChecked : {})
                    }} />
                    <span style={{
                      ...styles.knob,
                      ...(user.is_active ? styles.knobChecked : {})
                    }} />
                  </label>
                </td>
                <td style={styles.td}>{user.roles.map(role => role.name).join(', ')}</td>
                <td style={styles.td} >
                  <div style={styles.actionButtons}>
                    <button
                      style={{...styles.button, ...styles.primaryButton}}
                      onClick={() => {
                        setSelectedUser(user);
                        setPasswordModalVisible(true);
                      }}
                    >
                      Change Password
                    </button>
                    <button
                      style={{...styles.button, ...styles.secondaryButton}}
                      onClick={() => {
                        setSelectedUser(user);
                        setSelectedRoles(user.roles.map(role => role.id));
                        setRoleModalVisible(true);
                      }}
                    >
                      Edit Roles
                    </button>
                  </div>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      )}

      {passwordModalVisible && (
        <div style={styles.modal}>
          <div style={styles.modalContent}>
            <h2>Change Password</h2>
            <form onSubmit={handlePasswordChange}>
              <div style={styles.formGroup}>
                <input
                  type="password"
                  value={newPassword}
                  onChange={(e) => setNewPassword(e.target.value)}
                  placeholder="New Password"
                  required
                  style={styles.input}
                />
              </div>
              <div style={styles.formActions}>
                <button type="submit" style={{...styles.button, ...styles.primaryButton}}>
                  Update Password
                </button>
                <button
                  type="button"
                  style={{...styles.button, ...styles.secondaryButton}}
                  onClick={() => {
                    setPasswordModalVisible(false);
                    setNewPassword('');
                  }}
                >
                  Cancel
                </button>
              </div>
            </form>
          </div>
        </div>
      )}

      {roleModalVisible && (
        <div style={styles.modal}>
          <div style={styles.modalContent}>
            <h2>Edit Roles</h2>
            <form onSubmit={handleRoleUpdate}>
              <div style={styles.formGroup}>
                <select
                  multiple
                  value={selectedRoles}
                  onChange={(e) => {
                    const values = Array.from(e.target.selectedOptions, option => option.value);
                    setSelectedRoles(values);
                  }}
                  required
                  style={styles.select}
                >
                  {roles.map((role) => (
                    <option key={role.id} value={role.id}>
                      {role.name}
                    </option>
                  ))}
                </select>
                <small style={{ display: 'block', marginTop: '4px', color: '#666' }}>
                  Hold Ctrl/Cmd to select multiple roles
                </small>
              </div>
              <div style={styles.formActions}>
                <button type="submit" style={{...styles.button, ...styles.primaryButton}}>
                  Update Roles
                </button>
                <button
                  type="button"
                  style={{...styles.button, ...styles.secondaryButton}}
                  onClick={() => {
                    setRoleModalVisible(false);
                    setSelectedRoles([]);
                  }}
                >
                  Cancel
                </button>
              </div>
            </form>
          </div>
        </div>
      )}
      <ToastContainer />
    </div>
  );
};

export default UserTable;