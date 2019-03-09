<template>
  <v-toolbar color="amber" app clipped-left fixed>
    <span class="title ml-3 mr-5">Envision&nbsp;<span class="slim-text">Web</span></span>
    <v-spacer></v-spacer>

    <v-menu v-if="isUserLogged == true">
      <v-btn icon slot="activator">
        <v-icon>create</v-icon>
      </v-btn>
      <v-list dense>
        <v-list-tile
          v-for="(item, index) in createItems"
          :key="index"
          :to="item.link"
        >
          <v-list-tile-title>{{ item.title }}</v-list-tile-title>
        </v-list-tile>
      </v-list>
    </v-menu>
  
    <v-tooltip bottom v-if="isUserLogged == true">
      <v-btn icon slot="activator">
        <v-badge left overlap color=red>
          <span slot="badge">!</span>
            <v-icon>notifications</v-icon>
        </v-badge>
      </v-btn>
      <span>通知</span>
    </v-tooltip>

    <v-btn outline large @click="ShowLoginDialog" v-if="isUserLogged == false">
      <v-icon>account_circle</v-icon> 
      <span class="font-weight-bold"> &nbsp;登录/注册</span>
    </v-btn>

    <v-menu v-if="isUserLogged == true">
      <v-btn slot="activator" fab flat small>
        <v-tooltip bottom>
          <v-avatar color="grey lighten-4" :size=40 slot="activator">
            <img :src="avatarHash" alt="avatar">
          </v-avatar>
          <span>我的</span>
        </v-tooltip>
      </v-btn>
      <v-list dense>
        <v-list-tile avatar class="my-2">
          <v-list-tile-avatar>
            <img :src="avatarHash" alt="avatar" :size=40>
          </v-list-tile-avatar>

          <v-list-tile-content>
            <v-list-tile-title>{{ username }}</v-list-tile-title>
            <v-list-tile-sub-title>{{ userDescription }}</v-list-tile-sub-title>
          </v-list-tile-content>
        </v-list-tile>
        <v-list-tile
          v-for="(item, index) in menuItems"
          :key="index"
          avatar
          @click=";"
          :to="item.link"
        >
          <v-list-tile-avatar>
            <v-icon>{{ item.icon }}</v-icon>
          </v-list-tile-avatar>
          <v-list-tile-title>{{ item.title }}</v-list-tile-title>
        </v-list-tile>
      </v-list>
    </v-menu>
      
  </v-toolbar>
</template>

<script>
export default {
  props: {
    isUserLogged: Boolean,
    ShowLoginDialog: Function,
    username: String,
    userDescription: String,
    avatarHash: String
  },
  data: () => ({
    userDescription: '2015级自动化3班',
    menuItems: [
      { title: '个人中心', icon: 'person', link: '/user/new' },
      { title: '我的草稿', icon: 'subject' , link: '/home/new' },
      { title: '关注内容', icon: 'stars' , link: '/giftshop/new'},
      { title: '系统设置', icon: 'settings' , link: '/explore/new'},
      { title: '退出登录', icon: 'exit_to_app' , link: '/home/new'},
    ],
    createItems: [
      { title:'新文章', link: '/articles/new' },
      { title: '新帖子', link: '/posts/new' },
      { title: '新问题', link: '/questions/new' },
      { title: '从草稿创建', link: '/draft' }
    ]
  })
}
</script>

<style>
.slim-text {
  font-weight: 300;
}
</style>
