<template>
  <div>
    <v-toolbar
      color="pink"
      dark
      tabs
    >
      <v-tooltip bottom>
        <v-btn icon slot="activator">
          <v-icon>keyboard_arrow_left</v-icon>
        </v-btn>
        <span>查看所有群组</span>
      </v-tooltip>

      <v-toolbar-title>{{ groupName }}<span class="font-weight-thin"> 群组</span></v-toolbar-title>

      <v-tabs
        slot="extension"
        centered
        color="pink"
        slider-color="yellow"
      >
        <v-tab to="/group/general">群组概览</v-tab>
        <v-tab to="/group/members">群组成员</v-tab>
        <v-tab>活动与公告</v-tab>
        <v-tab>学习资料</v-tab>
        <v-tab>学习任务</v-tab>
      </v-tabs>
    </v-toolbar>
    <v-tabs-items>
      <v-tab-item>
        <v-card class="pa-3">
          <router-view></router-view>
        </v-card>
      </v-tab-item>
    </v-tabs-items>
  </div>
</template>

<script>
  export default {
    data: () => ({
      groupName: 'C语言学习交流',

    })
  }
</script>