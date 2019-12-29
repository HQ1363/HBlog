<template>
  <div style="width: 100%; height: 100%; display: block; position: relative">
    <el-tabs type="border-card" style="min-height: calc(100% - 10px)" v-model="activeTab" @tab-click="handlerTabChange">
      <el-tab-pane name="blogList">
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
            <template slot-scope="scope">
              {{ scope.row.status | blogStatus }}
            </template>
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
              <el-button type="warning" size="mini" round>{{ scope.row.comments.length }}</el-button>
            </template>
          </el-table-column>
          <el-table-column
            prop="visitors"
            width="80"
            label="访问">
            <template slot-scope="scope">
              <el-button type="info" size="mini" round>{{ scope.row.visitors }}</el-button>
            </template>
          </el-table-column>
          <el-table-column
            prop="created_time"
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
                @click="handleSetting(scope.$index, scope.row)">设置</el-button>
              <el-button
                size="mini"
                type="info"
                @click="handleSetting(scope.$index, scope.row)">查看</el-button>
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
      <el-tab-pane name="addBlog">
        <span slot="label"><i class="el-icon-document-add" style="margin-right: 3px"></i>新增博文</span>
        <div>
          <el-input
            type="text"
            placeholder="请输入文章标题"
            v-model="blogForm.title"
            maxlength="100"
            show-word-limit
          />
        </div>
        <el-divider />
        <div class="mavonEditor">
          <mavon-editor v-model="blogForm.content" :ishljs="true" style="z-index: 3" />
        </div>
        <el-divider />
        <div style="text-align: left; margin-top: 15px; display: flex; align-items: center">
          <div style="display: inline-block">
            <span>文章标签：</span>
          </div>
          <div style="display: inline-block">
            <el-tag
              :key="tag"
              v-for="(tag, index) in blogForm.tags"
              closable
              :disable-transitions="false"
              :style="{ marginRight: index !== blogForm.tags.length ? '10px' : '0px' }"
              @close="handleNewAddTagClose(tag)">
              {{tag}}
            </el-tag>
            <el-input
              class="input-new-tag"
              v-if="blogForm.newAddTagVisible"
              v-model="blogForm.newAddTagValue"
              ref="saveTagInput"
              size="small"
              :style="{ marginRight: blogForm.tags.length > 0 ? '10px' : '0px' }"
              @keyup.enter.native="handleNewAddTagInputConfirm"
              @blur="handleNewAddTagInputConfirm"
            >
            </el-input>
            <el-button v-else class="button-new-tag" size="small" :style="{ marginRight: blogForm.tags.length > 0 ? '10px' : '0px' }" @click="showNewAddTagInput">+ New Tag</el-button>
          </div>
        </div>
        <el-divider />
        <div style="text-align: left; margin-top: 10px;">
          <div style="display: inline-block"><span>分类管理：</span></div>
          <div style="display: inline-block">
            <el-select
              v-model="blogForm.categories"
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
          <el-button type="primary" @click="submitOrUpdateBlog('publish')">发布博客</el-button>
          <el-button type="info" @click="submitOrUpdateBlog('draft')">存为草稿</el-button>
        </div>
      </el-tab-pane>
    </el-tabs>
    <h-drawer
      title="文章设置"
      :visible.sync="openDrawer"
      :showClose="false"
      :modal="false"
      size="25%"
      :append-to-body="false"
      ref="drawer"
      :modal-append-to-body="false">
      <div class="drawer-content">
        <el-form :model="blogForm">
          <el-form-item label="标题" :label-width="blogForm.labelWidth">
            <el-input v-model="blogForm.title" autocomplete="off"></el-input>
          </el-form-item>
          <el-form-item label="摘要" :label-width="blogForm.labelWidth">
            <el-input type="textarea" v-model="blogForm.summary" autocomplete="off"></el-input>
          </el-form-item>
          <el-form-item label="类别" :label-width="blogForm.labelWidth">
            <el-checkbox-group v-model="blogForm.categories">
              <el-checkbox label="美食/餐厅线上活动" name="type"></el-checkbox>
              <el-checkbox label="地推活动" name="type"></el-checkbox>
              <el-checkbox label="线下主题活动" name="type"></el-checkbox>
              <el-checkbox label="单纯品牌曝光" name="type"></el-checkbox>
            </el-checkbox-group>
          </el-form-item>
          <div class="draw-tags">
            <label>标签</label>
            <el-tag
              :key="tag"
              v-for="(tag, index) in blogForm.tags"
              closable
              :disable-transitions="false"
              :style="{ marginRight: index !== blogForm.tags.length ? '10px' : '0px', marginTop: '10px' }"
              @close="handleNewAddTagClose(tag)">
              {{tag}}
            </el-tag>
            <el-input
              class="input-new-tag"
              v-if="blogForm.newAddTagVisible"
              v-model="blogForm.newAddTagValue"
              ref="saveTagInput"
              size="small"
              :style="{ marginRight: blogForm.tags.length > 0 ? '10px' : '0px', marginTop: '10px' }"
              @keyup.enter.native="handleNewAddTagInputConfirm"
              @blur="handleNewAddTagInputConfirm"
            >
            </el-input>
            <el-button v-else class="button-new-tag" size="small" :style="{ marginRight: blogForm.tags.length > 0 ? '10px' : '0px', marginTop: '10px' }" @click="showNewAddTagInput">+ New Tag</el-button>
          </div>
          <el-form-item label="更新状态">
            <el-radio-group v-model="blogForm.status" size="medium">
              <el-radio-button label="发布上线" ></el-radio-button>
              <el-radio-button label="存为草稿"></el-radio-button>
              <el-radio-button label="归档废弃"></el-radio-button>
            </el-radio-group>
          </el-form-item>
          <el-form-item label="开启评论">
            <el-switch v-model="blogForm.commentTable"></el-switch>
          </el-form-item>
          <el-form-item label="是否置顶">
            <el-switch v-model="blogForm.isTop"></el-switch>
          </el-form-item>
        </el-form>
        <div class="drawer-footer">
          <el-button @click="() => {}">取 消</el-button>
          <el-button type="primary" @click="$refs.drawer.closeDrawer()">确 定</el-button>
        </div>
      </div>
    </h-drawer>
  </div>
</template>

<script>

import blogAPi from '@/api/blog'
import HDrawer from '@/components/HDrawer'

export default {
  name: 'Blog',
  components: {
    HDrawer
  },
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
    this.queryBlogList()
  },
  data () {
    return {
      activeTab: 'blogList',
      blogForm: {
        labelWidth: '50px',
        title: '',
        content: '',
        tags: [],
        categories: [],
        newAddTagVisible: false,
        newAddTagValue: '',
        status: true,
        commentTable: true,
        isTop: false,
        summary: ''
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
      }],
      openDrawer: false,
      pageNum: 1,
      pageSize: 20
    }
  },
  methods: {
    async queryBlogList () {
      const blogList = await blogAPi.getBlogList()
      this.tableData = blogList.results
    },
    handleNewAddTagClose (tag) {
      this.blogForm.tags.splice(this.blogForm.tags.indexOf(tag), 1)
    },
    showNewAddTagInput () {
      this.blogForm.newAddTagVisible = true
      this.$nextTick(_ => {
        this.$refs.saveTagInput.$refs.input.focus()
      })
    },
    handleNewAddTagInputConfirm () {
      let inputValue = this.blogForm.newAddTagValue
      if (inputValue) {
        this.blogForm.tags.push(inputValue)
      }
      this.blogForm.newAddTagVisible = false
      this.blogForm.newAddTagValue = ''
    },
    onSubmit () {
      console.log('submit!')
    },
    filterTag (value, row) {
      return row.tag === value
    },
    handlerTabChange (tab, event) {
      this.activeTab = tab._props.name
    },
    tableRowClassName ({ row, rowIndex }) {
      if (rowIndex === 1) {
        return 'warning-row'
      } else if (rowIndex === 3) {
        return 'success-row'
      }
      return ''
    },
    async handleEdit (index, row) {
      console.log(index, row)
      console.log('activeTab: ', this.activeTab)
      this.$message({
        type: 'info',
        message: '正前往编辑页面'
      })
      this.activeTab = 'addBlog'
      const blogDetail = await blogAPi.getBlogDetail(row.id)
      console.log('blog detail: ', blogDetail)
      this.blogForm = {
        ...blogDetail
      }
    },
    handleDelete (index, row) {
      console.log(index, row)
    },
    handleSetting (index, row) {
      this.openDrawer = true
    },
    handlePageSizeChange (val) {
      console.log(val)
    },
    handlePageNumChange (val) {
      console.log(val)
    },
    submitOrUpdateBlog (type) {
      console.log('hello world')
      this.$confirm('立即前往文章列表页?', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning',
        center: true
      }).then(() => {
        this.$message({
          type: 'success',
          message: '提交成功!'
        })
      }).catch(() => {
        this.$message({
          type: 'info',
          message: '操作已取消'
        })
      })
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
    height: 32px;
    line-height: 30px;
    padding-top: 0;
    padding-bottom: 0;
  }
  .input-new-tag {
    width: 90px;
    vertical-align: bottom;
  }
  .drawer-content {
    padding: 20px 20px;
    height: 100%;
  }
  .drawer-content .drawer-footer {
    display: block;
    position: absolute;
    bottom: 20px;
    right: 20px;
  }
  .drawer-content .draw-tags {
    margin-top: -20px;
    margin-bottom: 20px;
    display: block;
    & > label {
      text-align: right;
      vertical-align: middle;
      float: left;
      font-size: 14px;
      width: 50px;
      color: #606266;
      line-height: 40px;
      padding: 0 12px 0 0;
      -webkit-box-sizing: border-box;
      box-sizing: border-box;
      margin-top: 5px;
    }
  }
</style>
