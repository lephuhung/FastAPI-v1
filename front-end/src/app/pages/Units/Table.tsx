import React, { useEffect, useState } from 'react';
import axios from 'axios';

interface Unit {
  id: string;
  name: string;
  user_count: number;
}

const UnitTable: React.FC = () => {
  const [units, setUnits] = useState<Unit[]>([]);
  const [loading, setLoading] = useState(false);

  const URL = process.env.REACT_APP_API_URL;

  useEffect(() => {
    const fetchUnits = async () => {
      setLoading(true);
      try {
        const res = await axios.get(`${URL}/units`);
        setUnits(res.data);
      } catch (err) {
        setUnits([]);
      }
      setLoading(false);
    };
    fetchUnits();
  }, [URL]);

  return (
    <div style={{ width: '100%', overflowX: 'auto' }}>
      <h2>Units</h2>
      {loading ? (
        <div>Loading...</div>
      ) : (
        <table
          style={{
            width: '100%',
            borderCollapse: 'separate',
            borderSpacing: 0,
            margin: '20px 0',
            background: '#fff',
            borderRadius: '8px',
            boxShadow: '0 2px 8px rgba(0,0,0,0.06)',
            overflow: 'hidden'
          }}
        >
          <thead>
            <tr>
              <th
                style={{
                  padding: '16px',
                  borderBottom: '2px solid #f0f0f0',
                  background: '#f7f7f7',
                  color: '#222',
                  fontWeight: 600,
                  textAlign: 'left'
                }}
              >
                Tên đơn vị
              </th>
              <th
                style={{
                  padding: '16px',
                  borderBottom: '2px solid #f0f0f0',
                  background: '#f7f7f7',
                  color: '#222',
                  fontWeight: 600,
                  textAlign: 'center'
                }}
              >
                Số lượng người dùng
              </th>
            </tr>
          </thead>
          <tbody>
            {units.map((unit, idx) => (
              <tr
                key={unit.id}
                style={{
                  background: idx % 2 === 0 ? '#fafbfc' : '#fff',
                  transition: 'background 0.2s'
                }}
              >
                <td style={{ padding: '14px 16px', borderBottom: '1px solid #f0f0f0' }}>
                  {unit.name}
                </td>
                <td
                  style={{
                    padding: '14px 16px',
                    borderBottom: '1px solid #f0f0f0',
                    textAlign: 'center'
                  }}
                >
                  {unit.user_count}
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </div>
  );
};

export default UnitTable;