<template>
  <v-app>
    <app-toolbar></app-toolbar>
    <app-side-menu></app-side-menu>
    <app-right-side-panel></app-right-side-panel>

    <v-content>
      <v-container>
        <question></question>
      </v-container>
    </v-content>
  </v-app>
</template>

<script>
import AppToolbar from './components/AppToolbar'
import AppSideMenu from './components/AppSideMenu'
import AppRightSidePanel from './components/AppRightSidePanel'
import Question from './views/Questions'
import axios from 'axios'

export default {
  name: 'App',
  components: {
    AppToolbar,
    AppSideMenu,
    AppRightSidePanel,
    Question,
  },
  data () {
    return {
      //
    }
  },
  mounted() {
    axios.get('http://127.0.0.1:8000/index/')
    .then(function(response) {
      console.log(response)
    })
    .catch(function(error) {
      console.log(error)
    })
  },
}
</script>