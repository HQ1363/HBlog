<template>
  <el-container class="admin-page">
    <el-container>
      <template>
        <el-aside width="250px" id="admin-menu">
          <AdminMenu />
        </el-aside>
        <el-container>
          <el-header id="admin-header">
            <AdminHeader />
          </el-header>
          <el-main id="admin-main">
            <div>这里是管理后台页面主体</div>
            <!-- 顶层admin page router-view -->
            <router-view></router-view>
          </el-main>
          <el-footer id="admin-footer">
            <AdminFooter></AdminFooter>
          </el-footer>
        </el-container>
      </template>
    </el-container>
  </el-container>
</template>

<script>

import AdminMenu from '@components/AdminMenu'
import AdminFooter from '@components/AdminFooter'
import AdminHeader from '@components/AdminHeader'

export default {
  name: 'Index',
  components: {
    AdminMenu,
    AdminFooter,
    AdminHeader
  },
  created () {
  },
  mounted () {
  },
  watch: {
  },
  computed: {
  },
  methods: {
  }
}
</script>

<style scoped>
  .admin-page {
    height: 100%;
  }
  #admin-footer {
    padding: 0 0 !important;
    /*height: 50px;*/
  }
  #admin-menu {
    background: #545c64;
  }
  #admin-header {
    color: white;
    background: #545c64;
    height: 40px !important;
  }
</style>
