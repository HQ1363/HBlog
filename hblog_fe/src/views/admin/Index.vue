<template>
  <el-container class="admin-page">
    <el-container>
      <template>
        <el-aside id="admin-menu" style="max-width: 250px !important; width: auto !important;">
          <AdminMenu :isCollapse="isCollapse" />
        </el-aside>
        <el-container>
          <el-header id="admin-header">
            <AdminHeader @handlerCollapseChange="handlerCollapseChange" :isCollapse="isCollapse" />
          </el-header>
          <el-main id="admin-main">
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
  data () {
    return {
      isCollapse: false
    }
  },
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
    handlerCollapseChange (val) {
      console.log('value: ', this.isCollapse)
      this.isCollapse = val
    }
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
  #admin-main {
    padding: 0 0 !important;
  }
  #admin-header {
    color: white;
    background: #545c64;
    height: 56px !important;
    padding: 0 0 !important;
  }
</style>
