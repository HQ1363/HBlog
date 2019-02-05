export const applyStatus = {
  0: '待审核',
  1: '审核中',
  2: '审核通过',
  3: '审核失败'
}

// 成功, 通知, 警告, 失败
export const statusColor = {
  0: '#00b5ad',
  1: '#909399',
  2: '#e6a23c',
  3: '#f56c6c'
}

// 博文状态
export const blogStatus = {
  1: '草稿箱',
  2: '已发布',
  3: '已下线'
}

export const permissionTypeText = {
  0: 'code',
  1: 'token',
  2: 'role'
}

export const branchStatusText = {
  1: '新建',
  2: '删除',
  3: '更新'
}

const filters = {
  'applyStatus': (key) => { return applyStatus[key] },
  'statusColor': (key) => { return statusColor[key] },
  'permissionTypeText': (key) => { return permissionTypeText[key] },
  'branchStatusText': (key) => { return branchStatusText[key] },
  'blogStatus': (key) => { return blogStatus[key] }
}

export default (Vue) => {
  Object.keys(filters).forEach((key) => {
    Vue.filter(key, filters[key])
  })
}
