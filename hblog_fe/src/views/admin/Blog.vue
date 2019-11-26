<template>
  <div style="width: 100%; height: 100%; display: block">
    <el-tabs type="border-card">
      <el-tab-pane>
        <span slot="label"><i class="el-icon-date"></i>博文列表</span>
        <el-form :inline="true" :model="formInline" style="text-align: left">
          <el-form-item label="审批人">
            <el-input v-model="formInline.user" placeholder="审批人"></el-input>
          </el-form-item>
          <el-form-item label="活动区域">
            <el-select v-model="formInline.region" placeholder="活动区域">
              <el-option label="区域一" value="shanghai"></el-option>
              <el-option label="区域二" value="beijing"></el-option>
            </el-select>
          </el-form-item>
          <el-form-item>
            <el-button type="primary" @click="onSubmit">查询</el-button>
          </el-form-item>
        </el-form>
        <el-table
          stripe
          border
          :data="tableData"
          class="rightTableStyles"
          :row-class-name="tableRowClassName">
          <el-table-column
            prop="title"
            label="标题"
            width="180">
          </el-table-column>
          <el-table-column
            prop="status"
            label="状态"
            width="180">
          </el-table-column>
          <el-table-column
            prop="categories"
            label="分类"
            width="300"
            :filters="[{ text: '家', value: '家' }, { text: '公司', value: '公司' }]"
            :filter-method="filterTag"
            filter-placement="bottom-end">
            <template slot-scope="scope">
              <el-tag v-for="(category, index) in scope.row.categories" :key="index" :type="tagTypes[index%5]" effect="dark" :style="index !== scope.row.categories.length ? { marginRight: '5px' } : {}">{{category}}</el-tag>
            </template>
          </el-table-column>
          <el-table-column
            prop="tags"
            label="标签"
            width="400"
            :filters="[{ text: '家', value: '家' }, { text: '公司', value: '公司' }]"
            :filter-method="filterTag"
            filter-placement="bottom-end">
            <template slot-scope="scope">
              <el-tag v-for="(tag, index) in scope.row.tags" :key="index" :type="tagTypes[index%5]" effect="dark" :style="index !== scope.row.tags.length ? { marginRight: '5px' } : {}">{{tag}}</el-tag>
            </template>
          </el-table-column>
          <el-table-column
            prop="comments"
            width="80"
            label="评论">
            <template slot-scope="scope">
              <el-button type="warning" size="mini" round>{{ scope.row.comments }}</el-button>
            </template>
          </el-table-column>
          <el-table-column
            prop="visit"
            width="80"
            label="访问">
            <template slot-scope="scope">
              <el-button type="info" size="mini" round>{{ scope.row.visit }}</el-button>
            </template>
          </el-table-column>
          <el-table-column
            prop="date"
            label="发布时间"
            width="180">
          </el-table-column>
          <el-table-column label="操作">
            <template slot-scope="scope">
              <el-button
                size="mini"
                @click="handleEdit(scope.$index, scope.row)">编辑</el-button>
              <el-button
                size="mini"
                type="danger"
                @click="handleDelete(scope.$index, scope.row)">删除</el-button>
            </template>
          </el-table-column>
        </el-table>
        <div class="pagination">
          <el-pagination
            layout="total, sizes, prev, pager, next"
            :current-page.sync="pageNum"
            :page-sizes="[10, 20, 50, 100]"
            :page-size="pageSize"
            @size-change="handlePageSizeChange"
            @current-change="handlePageNumChange"
            :total="tableData.length">
          </el-pagination>
        </div>
      </el-tab-pane>
      <el-tab-pane label="新增博文">新增博文</el-tab-pane>
    </el-tabs>
  </div>
</template>

<script>
export default {
  name: 'Blog',
  data () {
    return {
      formInline: {
        user: '',
        region: ''
      },
      tagTypes: ['', 'success', 'info', 'danger', 'warning'],
      tableData: [{
        title: '测试数据',
        tags: ['Python', 'Java', 'Node', 'H5', 'Go'],
        categories: ['前端', '博客'],
        status: 'publish',
        comments: 10,
        visit: 100,
        date: '2016-05-02',
        id: 2
      }, {
        title: '测试数据',
        tags: ['Python', 'Java', 'Node', 'H5', 'Go'],
        categories: ['前端', '博客'],
        status: 'publish',
        comments: 10,
        visit: 100,
        date: '2016-05-02',
        id: 1
      }, {
        title: '测试数据',
        tags: ['Python', 'Java', 'Node', 'H5', 'Go'],
        categories: ['前端', '博客'],
        status: 'publish',
        comments: 10,
        visit: 100,
        date: '2016-05-02',
        id: 4
      }, {
        title: '测试数据',
        tags: ['Python', 'Java', 'Node', 'H5', 'Go'],
        categories: ['前端', '博客'],
        status: 'publish',
        comments: 10,
        visit: 100,
        date: '2016-05-02',
        id: 1
      }, {
        title: '测试数据',
        tags: ['Python', 'Java', 'Node', 'H5', 'Go'],
        categories: ['前端', '博客'],
        status: 'publish',
        comments: 10,
        visit: 100,
        date: '2016-05-02',
        id: 4
      }, {
        title: '测试数据',
        tags: ['Python', 'Java', 'Node', 'H5', 'Go'],
        categories: ['前端', '博客'],
        status: 'publish',
        comments: 10,
        visit: 100,
        date: '2016-05-02',
        id: 1
      }, {
        title: '测试数据',
        tags: ['Python', 'Java', 'Node', 'H5', 'Go'],
        categories: ['前端', '博客'],
        status: 'publish',
        comments: 10,
        visit: 100,
        date: '2016-05-02',
        id: 4
      }, {
        title: '测试数据',
        tags: ['Python', 'Java', 'Node', 'H5', 'Go'],
        categories: ['前端', '博客'],
        status: 'publish',
        comments: 10,
        visit: 100,
        date: '2016-05-02',
        id: 1
      }, {
        title: '测试数据',
        tags: ['Python', 'Java', 'Node', 'H5', 'Go'],
        categories: ['前端', '博客'],
        status: 'publish',
        comments: 10,
        visit: 100,
        date: '2016-05-02',
        id: 4
      }, {
        title: '测试数据',
        tags: ['Python', 'Java', 'Node', 'H5', 'Go'],
        categories: ['前端', '博客'],
        status: 'publish',
        comments: 10,
        visit: 100,
        date: '2016-05-02',
        id: 1
      }, {
        title: '测试数据',
        tags: ['Python', 'Java', 'Node', 'H5', 'Go'],
        categories: ['前端', '博客'],
        status: 'publish',
        comments: 10,
        visit: 100,
        date: '2016-05-02',
        id: 4
      }, {
        title: '测试数据',
        tags: ['Python', 'Java', 'Node', 'H5', 'Go'],
        categories: ['前端', '博客'],
        status: 'publish',
        comments: 10,
        visit: 100,
        date: '2016-05-02',
        id: 1
      }, {
        title: '测试数据',
        tags: ['Python', 'Java', 'Node', 'H5', 'Go'],
        categories: ['前端', '博客'],
        status: 'publish',
        comments: 10,
        visit: 100,
        date: '2016-05-02',
        id: 4
      }, {
        title: '测试数据',
        tags: ['Python', 'Java', 'Node', 'H5', 'Go'],
        categories: ['前端', '博客'],
        status: 'publish',
        comments: 10,
        visit: 100,
        date: '2016-05-02',
        id: 1
      }, {
        title: '测试数据',
        tags: ['Python', 'Java', 'Node', 'H5', 'Go'],
        categories: ['前端', '博客'],
        status: 'publish',
        comments: 10,
        visit: 100,
        date: '2016-05-02',
        id: 4
      }, {
        title: '测试数据',
        tags: ['Python', 'Java', 'Node', 'H5', 'Go'],
        categories: ['前端', '博客'],
        status: 'publish',
        comments: 10,
        visit: 100,
        date: '2016-05-02',
        id: 1
      }, {
        title: '测试数据',
        tags: ['Python', 'Java', 'Node', 'H5', 'Go'],
        categories: ['前端', '博客'],
        status: 'publish',
        comments: 10,
        visit: 100,
        date: '2016-05-02',
        id: 4
      }, {
        title: '测试数据',
        tags: ['Python', 'Java', 'Node', 'H5', 'Go'],
        categories: ['前端', '博客'],
        status: 'publish',
        comments: 10,
        visit: 100,
        date: '2016-05-02',
        id: 1
      }, {
        title: '测试数据',
        tags: ['Python', 'Java', 'Node', 'H5', 'Go'],
        categories: ['前端', '博客'],
        status: 'publish',
        comments: 10,
        visit: 100,
        date: '2016-05-02',
        id: 4
      }, {
        title: '测试数据',
        tags: ['Python', 'Java', 'Node', 'H5', 'Go'],
        categories: ['前端', '博客'],
        status: 'publish',
        comments: 10,
        visit: 100,
        date: '2016-05-02',
        id: 3
      }],
      pageNum: 1,
      pageSize: 20
    }
  },
  methods: {
    onSubmit () {
      console.log('submit!')
    },
    filterTag (value, row) {
      return row.tag === value
    },
    tableRowClassName ({ row, rowIndex }) {
      if (rowIndex === 1) {
        return 'warning-row'
      } else if (rowIndex === 3) {
        return 'success-row'
      }
      return ''
    },
    handleEdit (index, row) {
      console.log(index, row)
    },
    handleDelete (index, row) {
      console.log(index, row)
    },
    handlePageSizeChange (val) {
      console.log(val)
    },
    handlePageNumChange (val) {
      console.log(val)
    }
  }
}
</script>

<style scoped lang="less">
  .rightTableStyles {
    width: 100%;
  }
</style>
