<template>
  <div>
    <span>
      <v-btn icon :to="'/forum/new'">
        <v-icon>keyboard_arrow_left</v-icon>
      </v-btn>
      返回论坛首页
    </span>
    <v-card >
      <v-list two-line>
        <div v-for="(item, index) in items" :key="index">
          <v-list-tile :to="item.link">
            <v-list-tile-avatar>
              <img :src="item.posterAvatar" alt="avatar">
            </v-list-tile-avatar>
            <v-list-tile-content>
              <v-list-tile-title>{{ item.poster }}</v-list-tile-title>
              <v-list-tile-sub-title style="font-size:10px">
                {{ item.action }}
              </v-list-tile-sub-title>
              <v-list-tile-sub-title class="text--primary" style="font-size:12px" v-html="item.postDetail">
              </v-list-tile-sub-title>
            </v-list-tile-content>

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
      items:[
        {
          posterAvatar: 'https://vuetifyjs.com/apple-touch-icon-180x180.png',
          poster: 'XiaoMing', 
          action: '2019/1/7',
          postDetail: '<p>帖子一的内容</p>', 
          link: '/postdetail'
        },
        {
          posterAvatar: 'https://vuetifyjs.com/apple-touch-icon-180x180.png',
          poster: 'XiaoMing', 
          action: '2019/1/6',
          postDetail: '<p>帖子二的内容</p>', 
          link: '/postdetail'
        },
        {
          posterAvatar: 'https://vuetifyjs.com/apple-touch-icon-180x180.png',
          poster: 'XiaoMing', 
          action: '2019/1/5',
          postDetail: '<p>帖子三的内容</p>', 
          link: '/postdetail'
        },
        {
          posterAvatar: 'https://vuetifyjs.com/apple-touch-icon-180x180.png',
          poster: 'XiaoMing', 
          action: '2019/1/4',
          postDetail: '<p>帖子四的内容</p>', 
          link: '/postdetail'
        },
        {
          posterAvatar: 'https://vuetifyjs.com/apple-touch-icon-180x180.png',
          poster: 'XiaoMing', 
          action: '2019/1/3',
          postDetail: '<p>帖子五的内容</p>', 
          link: '/postdetail'
        },
        {
          posterAvatar: 'https://vuetifyjs.com/apple-touch-icon-180x180.png',
          poster: 'XiaoMing', 
          action: '2019/1/2',
          postDetail: '<p>帖子六的内容</p>', 
          link: '/postdetail'
        },
        {
          posterAvatar: 'https://vuetifyjs.com/apple-touch-icon-180x180.png',
          poster: 'XiaoMing', 
          action: '2019/1/1',
          postDetail: '<p>帖子七的内容</p>', 
          link: '/postdetail'
        },
      ]
    }
  }
}
</script>
