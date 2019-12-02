<template>
  <div id="header-logout">
    <div @click="handlerCollapseChange" style="font-size: 30px; position: absolute; left: 0; z-index: 10; margin-top: 12px; cursor: pointer">
      <i class="el-icon-s-fold"></i>
    </div>
    <el-menu
      mode="horizontal"
      background-color="#545c64"
      text-color="#fff"
      style="border-right: none; z-index: 9"
      active-text-color="#ffd04b"
      router>
      <el-submenu v-if="name" style="padding: 0 0 !important;" index="#">
        <template slot="title">
          <el-avatar>{{ name }}</el-avatar>
        </template>
        <el-menu-item index="/logout">退出登陆</el-menu-item>
      </el-submenu>
    </el-menu>
  </div>
</template>

<script>
export default {
  props: {
    isCollapse: {
      type: Boolean
    }
  },
  name: 'AdminHeader',
  data () {
    return {
      name: 'HQ'
    }
  },
  methods: {
    handlerCollapseChange () {
      this.$emit('handlerCollapseChange', !this.isCollapse)
    }
  }
}
</script>

<style scoped>
  #header-logout {
    height: 100%;
    display: block;
    position: relative;
  }
  #header-logout .el-menu--horizontal>.el-submenu {
    float: right;
  }
</style>
