import Vue from 'vue'
import App from './App.vue'
import ToggleButton from 'vue-js-toggle-button'
import ElementUI from 'element-ui'
import axios from 'axios'

Vue.config.productionTip = false

Vue.prototype.$http = axios
Vue.use(ToggleButton)
Vue.use(ElementUI);
new Vue({
  render: h => h(App),
}).$mount('#app')
