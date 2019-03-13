import Vue from 'vue'
import './plugins/vuetify'
import App from './App.vue'
import router from './plugins/router'
import './plugins/editor'
import axios from 'axios'

Vue.config.productionTip = false;
Vue.prototype.$axios = axios;
Vue.use(axios);

new Vue({
  router,
  render: h => h(App),
}).$mount('#app');
