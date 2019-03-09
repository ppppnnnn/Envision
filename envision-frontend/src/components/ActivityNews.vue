<template>
  <div>
    <span>
      <v-btn icon :to="'/forum/new'">
        <v-icon>keyboard_arrow_left</v-icon>
      </v-btn>
      返回论坛首页
    </span>
    <v-card>
      <v-subheader>
        {{header}}
      </v-subheader>
      <v-list two-line subheader>  
        <div v-for="(item, index) in items" :key="index">
          <v-list-tile avatar ripple :to="item.link">
            <v-list-tile-content>
              <v-list-tile-title>{{ item.title }}</v-list-tile-title>    
            </v-list-tile-content>
            <v-list-tile-action>
              <v-list-tile-action-text>{{ item.action }}</v-list-tile-action-text>
            </v-list-tile-action>
          </v-list-tile>
          <v-divider v-if="index + 1 < items.length" :key="`divider-${index}`">
          </v-divider>
        </div>
      </v-list>
    </v-card>
  </div>
</template>

<script>

export default {
  data() {
    return {
      header: '活动与新闻',
      items:[
        {title: '活动与新闻一', action: '2019/1/7', link: '/activitynewsdetail'},
        {title: '活动与新闻二', action: '2019/1/6', link: '/activitynewsdetail'},
        {title: '活动与新闻三', action: '2019/1/5', link: '/activitynewsdetail'},
        {title: '活动与新闻四', action: '2019/1/4', link: '/activitynewsdetail'},
        {title: '活动与新闻五', action: '2019/1/3', link: '/activitynewsdetail'},
        {title: '活动与新闻六', action: '2019/1/2', link: '/activitynewsdetail'},
        {title: '活动与新闻七', action: '2019/1/1', link: '/activitynewsdetail'},
      ]
    }
  }
}
</script>
