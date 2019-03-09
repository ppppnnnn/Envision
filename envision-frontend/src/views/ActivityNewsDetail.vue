<template>
  <div>
    <span>
      <v-btn icon :to="'/activitynews/new'">
        <v-icon>keyboard_arrow_left</v-icon>
      </v-btn>
      返回帖子列表
    </span>
    <v-card class="mb-3">
      <v-card-title primary-title>   
        <v-list-tile-content style="font-size:20px">
          <v-list-tile-title>{{ title }}</v-list-tile-title>
          <v-list-tile-sub-title class="grey--text" style="font-size:10px">
            {{ time }}
          </v-list-tile-sub-title>
        </v-list-tile-content>
      </v-card-title>
      <v-card-text v-html="announcementDetail"></v-card-text>    
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn disabled flat color="grey" class="mx-2">
          <span >阅读量：</span>
          <span class="font-weight-bold mx-2">{{ vote }}</span>
        </v-btn>
      </v-card-actions>
    </v-card>
  </div>
</template>

<script>

  export default {
    data: () => ({
      title: '活动与新闻一',
      time: '2019/2/17',
      vote: 46,
      announcementDetail: '<p>活动与新闻一的内容</p>',
    })
  }
</script>