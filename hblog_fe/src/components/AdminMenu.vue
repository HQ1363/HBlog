<template>
  <el-menu
    router
    :collapse="isCollapse"
    default-active="/admin/category/list"
    background-color="#545c64"
    text-color="#fff"
    style="border-right: none"
    active-text-color="#ffd04b">
    <template v-for="(item, index) in menu">
      <el-menu-item v-if="!item.subMenu" :index="item.index" :key="index">
        <template slot="title">
          <i :class="item.icon"></i>
          <span slot="title">{{ item.name }}</span>
        </template>
      </el-menu-item>
      <el-submenu v-else :key="index" :index="item.index">
        <template slot="title">
          <i :class="item.icon"></i>
          <span slot="title">{{ item.name }}</span>
        </template>
        <el-menu-item v-for="(subItem, subIndex) in item.subMenu" :index="subItem.index" :key="subIndex">
          {{ subItem.name }}
        </el-menu-item>
      </el-submenu>
    </template>
  </el-menu>
</template>

<script>
export default {
  name: 'AdminMenu',
  data () {
    return {
      isCollapse: false,
      menu: [
        {
          icon: 'el-icon-menu',
          name: '分类管理',
          index: '/admin/category',
          subMenu: [
            {
              name: '分类列表',
              index: '/admin/category/list'
            }, {
              name: '新增分类',
              index: '/admin/category/add'
            }, {
              name: '更新分类',
              index: '/admin/category/update'
            }
          ]
        }, {
          icon: 'el-icon-discount',
          name: '标签管理',
          index: '/tags'
        }, {
          icon: 'el-icon-chat-dot-round',
          name: '评论管理',
          index: '/comments'
        }, {
          icon: 'el-icon-document',
          name: '博文管理',
          index: '/blogs'
        }
      ]
    }
  }
}
</script>

<style scoped>

</style>
