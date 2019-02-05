import Vue from 'vue'
import {
  Button,
  Table,
  Menu,
  Backtop,
  Aside,
  Card,
  Upload,
  Alert,
  Container,
  Submenu,
  Breadcrumb,
  Col,
  Row,
  Dialog,
  Divider,
  Icon,
  Popover,
  Tag,
  DatePicker,
  Footer,
  Header,
  Main,
  Form,
  FormItem,
  Select,
  Switch,
  MenuItem,
  TableColumn,
  Pagination,
  Avatar,
  Dropdown,
  DropdownItem,
  DropdownMenu,
  Input,
  Option,
  TabPane,
  Tabs,
  Drawer,
  Checkbox,
  CheckboxGroup,
  RadioButton,
  RadioGroup,
  Message,
  MessageBox,
  Loading,
  Notification
} from 'element-ui'

Vue.use(RadioGroup)
Vue.use(RadioButton)
Vue.use(CheckboxGroup)
Vue.use(Checkbox)
Vue.use(Drawer)
Vue.use(TabPane)
Vue.use(Tabs)
Vue.use(Option)
Vue.use(Input)
Vue.use(Dropdown)
Vue.use(DropdownMenu)
Vue.use(DropdownItem)
Vue.use(Button)
Vue.use(Table)
Vue.use(Menu)
Vue.use(Backtop)
Vue.use(Aside)
Vue.use(Card)
Vue.use(Upload)
Vue.use(Alert)
Vue.use(Menu)
Vue.use(Container)
Vue.use(Submenu)
Vue.use(Breadcrumb)
Vue.use(Col)
Vue.use(Row)
Vue.use(Dialog)
Vue.use(Divider)
Vue.use(Icon)
Vue.use(Popover)
Vue.use(Tag)
Vue.use(DatePicker)
Vue.use(Footer)
Vue.use(Header)
Vue.use(Main)
Vue.use(Form)
Vue.use(FormItem)
Vue.use(Select)
Vue.use(Switch)
Vue.use(MenuItem)
Vue.use(TableColumn)
Vue.use(Pagination)
Vue.use(Avatar)

Vue.prototype.$loading = Loading.service
Vue.prototype.$msgbox = MessageBox
Vue.prototype.$alert = MessageBox.alert
Vue.prototype.$confirm = MessageBox.confirm
Vue.prototype.$prompt = MessageBox.prompt
Vue.prototype.$notify = Notification
Vue.prototype.$message = Message
