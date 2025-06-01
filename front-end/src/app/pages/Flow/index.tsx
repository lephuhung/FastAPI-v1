import React, {useCallback, useEffect, useState} from 'react'
import {ReactFlow, MiniMap, Controls, Background, applyEdgeChanges, applyNodeChanges,addEdge,
    type Node,
    type Edge,
    type FitViewOptions,
    type OnConnect,
    type OnNodesChange,
    type OnEdgesChange,
    type OnNodeDrag,
    type DefaultEdgeOptions} from '@xyflow/react'
import axios from 'axios'
import '@xyflow/react/dist/style.css'
const URL = process.env.REACT_APP_API_URL

interface NodeData {
  id: string
  name: string
  type: string
}

interface EdgeData {
  from: string
  to: string
  relationship_id: number
  relationship_name: string
}

interface FlowResponse {
  nodes: NodeData[]
  edges: EdgeData[]
}

const nodeTypeColor = (type: string) => {
  switch (type) {
    case 'administrator':
      return '#007bff'
    case 'social_account':
      return '#28a745'
    default:
      return '#888'
  }
}

const Flow: React.FC<{uid_administrator: string}> = ({uid_administrator}) => {
  const [nodes, setNodes] = useState<Node[]>([])
  const [edges, setEdges] = useState<Edge[]>([])

  useEffect(() => {
    axios.get<FlowResponse>(`${URL}/administrators/flow/${uid_administrator}`).then((res) => {
      const {nodes: nodeData, edges: edgeData} = res.data

      // Map nodes for React Flow
      const rfNodes: Node[] = nodeData.map((n, idx) => ({
        id: n.id,
        data: {label: `${n.id.includes('-') ? 'Đối tượng: ' : 'Tài khoản: '} ${n.name}`},
        position: {x: 100 + idx * 200, y: 100},
        style: {background: nodeTypeColor(n.type), color: '#fff', borderRadius: 8, padding: 10},
        type: 'default',
      }))

      // Map edges for React Flow
      const rfEdges: Edge[] = edgeData.map((e) => ({
        id: `e${e.from}-${e.to}`,
        source: e.from,
        target: e.to,
        label: e.relationship_name || `ID: ${e.relationship_id}`,
        animated: true,
        style: {stroke: '#333'},
        labelStyle: {fill: '#333', fontWeight: 700},
        type: 'default',
      }))

      setNodes(rfNodes)
      setEdges(rfEdges)
    })
  }, [uid_administrator])
  const fitViewOptions: FitViewOptions = {
    padding: 0.2,
  };
   
  const defaultEdgeOptions: DefaultEdgeOptions = {
    animated: true,
  };
   
  const onNodesChange: OnNodesChange = useCallback(
    (changes) => setNodes((nds) => applyNodeChanges(changes, nds)),
    [setNodes],
  );
  const onEdgesChange: OnEdgesChange = useCallback(
    (changes) => setEdges((eds) => applyEdgeChanges(changes, eds)),
    [setEdges],
  );
  const onConnect: OnConnect = useCallback(
    (connection) => setEdges((eds) => addEdge(connection, eds)),
    [setEdges],
  );
  return (
    <div style={{width: '100%', height: '600px'}}>
      <ReactFlow
        nodes={nodes}
        edges={edges}
        fitView={true}
        defaultEdgeOptions={defaultEdgeOptions}
        onNodesChange={onNodesChange}
        onEdgesChange={onEdgesChange}
        onConnect={onConnect}
        snapToGrid={true}
        snapGrid={[16, 16]}
        defaultViewport={{zoom: 0.5, x: 0, y: 0}}
      >
        <MiniMap nodeColor={(n) => nodeTypeColor((n.data as any)?.label?.split(':')[0] || '')} />
        <Controls />
        <Background color='#aaa' gap={16} />
      </ReactFlow>
    </div>
  )
}

export default Flow
