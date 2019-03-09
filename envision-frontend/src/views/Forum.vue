<template>
  <v-card>
    <v-list two-line subheader>
      <div v-for="group in groups" :key="group.id">
        <v-subheader inset>
          {{ group.name }}
        </v-subheader>
        <v-list-tile v-for="item in group.items" :key="item.id" :to="item.link" avatar>
          <v-list-tile-avatar>
            <v-icon :class="[item.iconClass]">{{ item.icon }}</v-icon>
          </v-list-tile-avatar>
          <v-list-tile-content>
            <v-list-tile-title>{{ item.title }}</v-list-tile-title>
            <v-list-tile-sub-title>
              {{ item.subtitle }} &nbsp;&nbsp;&nbsp;&nbsp;{{ item.action }}
            </v-list-tile-sub-title>
          </v-list-tile-content>
          <v-list-tile-action>
            <v-btn icon ripple>
              <v-icon color="grey lighten-1">keyboard_arrow_right</v-icon>
            </v-btn>
          </v-list-tile-action>
        </v-list-tile>
        <v-divider inset v-if="groups.indexOf(group) < groups.length - 1"></v-divider>
      </div>
    </v-list>
  </v-card>
</template>

<script>

export default {
  data(){
    return {
      groups: [
        {
          id: 0,
          name: '公告 / 新闻',
          items: [
            {id: 0, title: '公告', subtitle: '公告一', action: '2019/1/7', iconClass: 'info white--text', icon: 'announcement', link: '/announmentcelists/new'},
            {id: 1, title: '活动与新闻', subtitle: '活动与新闻一', action: '2019/1/7', iconClass: 'info white--text', icon: 'local_activity', link: '/activitynews/new'},
          ]
        },
        {
          id: 1,
          name: '技术交流',
          items: [
            {id: 0, title: '嵌入式技术交流区', subtitle: '帖子一', action: '2019/1/7', iconClass: 'info white--text', icon: 'settings_input_composite', link: '/postlist/0'},
            {id: 1, title: '软件技术交流区', subtitle: '帖子一', action: '2019/1/7', iconClass: 'info white--text', icon: 'code', link: '/postlist/1'},
            {id: 2, title: '机器人技术交流区', subtitle: '帖子一', action: '2019/1/7', iconClass: 'info white--text', icon: 'adb', link: '/postlist/2'},
            {id: 3, title: '生活轶事交流区', subtitle: '帖子一', action: '2019/1/7', iconClass: 'info white--text', icon: 'free_breakfast', link: '/postlist/3'},
          ]
        },
      ]
    }
  },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
