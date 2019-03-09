<template>
  <v-toolbar :color="userColorTheme" app clipped-left fixed>
    <span class="title ml-3 mr-5">Envision&nbsp;<span class="slim-text">Web</span></span>
    <v-spacer></v-spacer>

    <v-menu>
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
  
    <v-tooltip bottom>
      <v-btn icon slot="activator">
        <v-badge left overlap color=red>
          <span slot="badge">!</span>
            <v-icon>notifications</v-icon>
        </v-badge>
      </v-btn>
      <span>通知</span>
    </v-tooltip>

    <v-menu>
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
  data: () => ({
    isUserLogged: true,
    avatarHash: 'https://vuetifyjs.com/apple-touch-icon-180x180.png',
    userColorTheme: 'amber',
    username: 'Owen Tsai',
    userDescription: '2015级自动化3班',
    menuItems: [
      { title: '个人中心', icon: 'person' },
      { title: '我的草稿', icon: 'subject' },
      { title: '关注内容', icon: 'stars' },
      { title: '系统设置', icon: 'settings' },
      { title: '退出登录', icon: 'exit_to_app' },
    ],
    createItems: [
      { title: '新文章', link: '/articles/new' },
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
