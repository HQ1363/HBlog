<template>
  <div style="width: 100%; height: 100%; display: block">
    <el-tabs type="border-card">
      <el-tab-pane>
        <span slot="label"><i class="el-icon-tickets" style="margin-right: 3px"></i>博文列表</span>
        <el-form :inline="true" :model="formInline" style="text-align: left">
          <el-form-item label="关键词">
            <el-input v-model="formInline.keyword" placeholder=""></el-input>
          </el-form-item>
          <el-form-item label="状态">
            <el-select v-model="formInline.status" placeholder="">
              <el-option label="已发布" value="shanghai"></el-option>
              <el-option label="草稿箱" value="beijing"></el-option>
              <el-option label="已下线" value="beijing"></el-option>
            </el-select>
          </el-form-item>
          <el-form-item label="类别">
            <el-select v-model="formInline.categories" placeholder="">
              <el-option label="学习笔记" value="shanghai"></el-option>
              <el-option label="日常反思" value="beijing"></el-option>
              <el-option label="娱乐八卦" value="beijing"></el-option>
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
                @click="handleDelete(scope.$index, scope.row)">回收站</el-button>
              <el-button
                size="mini"
                type="primary"
                @click="handleDelete(scope.$index, scope.row)">设置</el-button>
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
      <el-tab-pane>
        <span slot="label"><i class="el-icon-document-add" style="margin-right: 3px"></i>新增博文</span>
        <div>
          <el-input
            type="text"
            placeholder="请输入文章标题"
            v-model="newAddBlog.title"
            maxlength="100"
            show-word-limit
          />
        </div>
        <el-divider />
        <div class="mavonEditor">
          <mavon-editor v-model="newAddBlog.content" :ishljs="true" style="z-index: 3" />
        </div>
        <el-divider />
        <div style="text-align: left; margin-top: 15px; display: flex; align-items: center">
          <div style="display: inline-block">
            <span>文章标签：</span>
          </div>
          <div style="display: inline-block">
            <el-tag
              :key="tag"
              v-for="(tag, index) in newAddBlog.tags"
              closable
              :disable-transitions="false"
              :style="{ marginRight: index !== newAddBlog.tags.length ? '10px' : '0px' }"
              @close="handleNewAddTagClose(tag)">
              {{tag}}
            </el-tag>
            <el-input
              class="input-new-tag"
              v-if="newAddBlog.newAddTagVisible"
              v-model="newAddBlog.newAddTagValue"
              ref="saveTagInput"
              size="small"
              @keyup.enter.native="handleNewAddTagInputConfirm"
              @blur="handleNewAddTagInputConfirm"
            >
            </el-input>
            <el-button v-else class="button-new-tag" size="small" @click="showNewAddTagInput">+ New Tag</el-button>
          </div>
        </div>
        <el-divider />
        <div style="text-align: left; margin-top: 10px;">
          <div style="display: inline-block"><span>分类管理：</span></div>
          <div style="display: inline-block">
            <el-select
              v-model="newAddBlog.categories"
              multiple
              filterable
              allow-create
              default-first-option
              style="min-width: 600px;"
              placeholder="请选择文章分类">
              <el-option
                v-for="item in initCategories"
                :key="item.value"
                :label="item.label"
                :value="item.value">
              </el-option>
            </el-select>
          </div>
        </div>
        <el-divider />
        <div style="text-align: right">
          <el-button type="primary">发布博客</el-button>
          <el-button type="info">存为草稿</el-button>
        </div>
      </el-tab-pane>
    </el-tabs>
  </div>
</template>

<script>

import blogAPi from '@/api/blog'

export default {
  name: 'Blog',
  computed: {
    initCategories () {
      return [{
        value: '测试数据1',
        label: '测试数据1'
      }, {
        value: '测试数据2',
        label: '测试数据2'
      }, {
        value: '测试数据3',
        label: '测试数据3'
      }, {
        value: '测试数据4',
        label: '测试数据4'
      }]
    }
  },
  created () {
    blogAPi.getBlogs()
  },
  data () {
    return {
      newAddBlog: {
        title: '',
        content: '',
        tags: [],
        categories: [],
        newAddTagVisible: false,
        newAddTagValue: ''
      },
      formInline: {
        keyword: '',
        status: '',
        categories: []
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
    handleNewAddTagClose (tag) {
      this.newAddBlog.tags.splice(this.newAddBlog.tags.indexOf(tag), 1)
    },
    showNewAddTagInput () {
      this.newAddBlog.newAddTagVisible = true
      this.$nextTick(_ => {
        this.$refs.saveTagInput.$refs.input.focus()
      })
    },
    handleNewAddTagInputConfirm () {
      let inputValue = this.newAddBlog.newAddTagValue
      if (inputValue) {
        this.newAddBlog.tags.push(inputValue)
      }
      this.newAddBlog.newAddTagVisible = false
      this.newAddBlog.newAddTagValue = ''
    },
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
  .mavonEditor {
    width: 100%;
    height: 100%;
    margin-top: 10px;
  }
  .mavonEditor .markdown-body {
    min-height: 700px;
  }
  .button-new-tag {
    margin-left: 10px;
    height: 32px;
    line-height: 30px;
    padding-top: 0;
    padding-bottom: 0;
  }
  .input-new-tag {
    width: 90px;
    margin-left: 10px;
    vertical-align: bottom;
  }
</style>
