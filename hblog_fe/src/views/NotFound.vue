<template>
  <div>
    <div class="forbidden">
      <p>很抱歉，您当前访问的页面不存在。
        <el-button @click="goBack" type="text" size="large">
          返回上页
        </el-button>
      </p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'NotFound',
  methods: {
    goBack () {
      this.$router.go(-1)
    }
  }
}
</script>

<style scoped>
  .forbidden {
    position: absolute;
    top: 40%;
    left: 50%;
    transform: translate(-50%, -50%);
  }
</style>
