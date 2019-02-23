<template>
  <v-navigation-drawer
    clipped
    fixed
    floating
    v-model="drawerRight"
    right
    style="margin-top:64px; z-index: 1"
    class="grey lighten-5 pa-3"
  >
    <v-card class="mb-3">
      <v-img
        class="white--text"
        height="200px"
        :src=topNewsImg
        @click=""
      >
        <v-container fill-height fluid>
          <v-layout fill-height>
            <v-flex xs12 align-end flexbox>
              <span class="headline">{{ topNewsTitle }}</span>
            </v-flex>
          </v-layout>
        </v-container>
      </v-img>
    </v-card>

    <v-card class="blue-grey darken-3 mb-3">
      <v-card-text class="white--text">
        Envision is founded by Owen Tsai, developed and maintained by volunteers. <br>
        Envision is completely free and open source, source code is avaliable to everyone at our
        <a href="https://github.com/AAIT-SUSE/Envision" class="white--text">Github Repo Page</a>.
      </v-card-text>
    </v-card>

    <v-card flat class="grey lighten-5">
      <v-card-text style="padding: 8px;">
        <a class="footer-link" href="https://github.com/AAIT-SUSE/Envision">源代码</a>
        <a class="footer-link">关于我们</a>
        <a class="footer-link">加入我们</a>
        <a class="footer-link">许可协议</a>
        <a class="footer-link">违法违规行为举报</a><br>
        <a class="footer-link">版权所有(c)aait-suse</a>
      </v-card-text>
    </v-card>
  </v-navigation-drawer>
</template>

<script>
  import unityBg from '../assets/unity_bg.jpg'

  export default {
    data: () => ({
      drawerRight: null,
      topNewsTitle: 'Unity 2019 的十大新特性',
      topNewsImg: unityBg
    })
  }
</script>

<style scoped>
  .footer-link {
    display: inline-block;
    margin-right: 12px;
    margin-left: 12px;
    color: grey;
    text-decoration: none;
  }

  .footer-link:hover {
    color:tomato;
  }
</style>
