<template>
  <el-menu
    router
    :collapse="isCollapse"
    default-active="/admin/document"
    background-color="#545c64"
    text-color="#fff"
    @open="handleOpen"
    @close="handleClose"
    style="border-right: none"
    active-text-color="#ffd04b">
    <el-menu-item key="home" index="/admin" style="padding: 0 0 !important;">
      <img src="../assets/HBlog.png" alt="logo" style="height: 100%; width: 100%" />
    </el-menu-item>
    <template v-for="(item, index) in menu">
      <el-menu-item v-if="!item.subMenu" :index="item.index" :key="index" style="padding: 0 0 !important;">
        <i :class="item.icon"></i>
        <span>{{ item.name }}</span>
      </el-menu-item>
      <el-submenu v-else :key="index" :index="item.index">
        <template slot="title">
          <i :class="item.icon"></i>
          <span>{{ item.name }}</span>
        </template>
        <el-menu-item v-for="(subItem, subIndex) in item.subMenu" :index="subItem.index" :key="subIndex" style="min-width: auto !important; padding: 0 0 !important;">
          <span>{{ subItem.name }}</span>
        </el-menu-item>
      </el-submenu>
    </template>
  </el-menu>
</template>

<script>
export default {
  props: {
    isCollapse: {
      type: Boolean
    }
  },
  name: 'AdminMenu',
  data () {
    return {
      menu: [
        {
          icon: 'el-icon-odometer',
          name: '仪表',
          index: '/admin/statistic'
        }, {
          icon: 'el-icon-document',
          name: '文章',
          index: '/admin/document'
        }, {
          icon: 'el-icon-user',
          name: '用户',
          index: '/admin/user',
          subMenu: [
            {
              icon: 'el-icon-camera',
              name: '相册',
              index: '/admin/user/photos'
            },
            {
              icon: 'el-icon-postcard',
              name: '主页',
              index: '/admin/user/page'
            }
          ]
        }, {
          icon: 'el-icon-setting',
          name: '系统',
          index: '/admin/system'
        }
      ]
    }
  },
  methods: {
    handleOpen (key, keyPath) {
      console.log(key, keyPath)
    },
    handleClose (key, keyPath) {
      console.log(key, keyPath)
    }
  }
}
</script>

<style scoped>

</style>
