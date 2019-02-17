<template>
  <v-app>
    <app-toolbar></app-toolbar>
    <app-side-menu></app-side-menu>

    <v-content style="padding-right: 300px;">
      <v-container fluid>
        <v-layout>
          <v-flex shrink style="width: 100%;">
            <question></question>
          </v-flex>
        </v-layout>
      </v-container>
    </v-content>

    <app-right-side-panel></app-right-side-panel>
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

<style>
  * {
    font-family: 等线, Serif,sans-serif;
  }
</style>