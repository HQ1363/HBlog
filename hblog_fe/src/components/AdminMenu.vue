<template>
  <el-menu
    router
    :collapse="isCollapse"
    default-active="/admin/category/list"
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
        <span slot="title">{{ item.name }}</span>
      </el-menu-item>
      <el-submenu v-else :key="index" :index="item.index">
        <i :class="item.icon"></i>
        <span slot="title">{{ item.name }}</span>
        <el-menu-item v-for="(subItem, subIndex) in item.subMenu" :index="subItem.index" :key="subIndex">
          {{ subItem.name }}
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
          icon: 'el-icon-menu',
          name: '分类管理',
          index: '/admin/category'
        }, {
          icon: 'el-icon-discount',
          name: '标签管理',
          index: '/admin/tag'
        }, {
          icon: 'el-icon-chat-dot-round',
          name: '评论管理',
          index: '/admin/comment'
        }, {
          icon: 'el-icon-document',
          name: '博文管理',
          index: '/admin/blog'
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
