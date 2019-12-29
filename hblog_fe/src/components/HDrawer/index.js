import HDrawer from './src/main'

/* istanbul ignore next */
HDrawer.install = function (Vue) {
  Vue.component(HDrawer.name, HDrawer)
}

// overwrite drawer component
export default HDrawer
