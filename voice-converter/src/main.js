import Vue from 'vue'
import App from './App.vue'
import AudioRecorder from 'vue-audio-recorder'
import axios from 'axios'

Vue.config.productionTip = false

Vue.prototype.$http = axios

Vue.use(AudioRecorder)
new Vue({
  render: h => h(App),
}).$mount('#app')
