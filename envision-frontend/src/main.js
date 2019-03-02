import Vue from 'vue'
import './plugins/vuetify'
import App from './App.vue'
import router from './plugins/router'
import './plugins/editor'

Vue.config.productionTip = false;

new Vue({
  router,
  render: h => h(App),
}).$mount('#app');
