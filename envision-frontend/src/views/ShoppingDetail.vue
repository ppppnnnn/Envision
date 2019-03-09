<template>
  <div>
    <span>
      <v-btn icon :to="'/giftshop'">
        <v-icon>keyboard_arrow_left</v-icon>
      </v-btn>
      返回礼品店
    </span>
    <v-checkbox v-model="selected" primary hide-details :on="toggleAll"></v-checkbox>
    <v-card  @click="items.selected = !items.selected">
      <!-- <v-subheader>
        {{header}}
      </v-subheader> -->
      <v-checkbox :input-value="items.selected" primary hide-details></v-checkbox>
      <v-card-title v-for="item in items" :key="item.id">
        
        <v-list-tile-avatar>
          <img :src="item.posterAvatar" alt="avatar">
        </v-list-tile-avatar>
        <v-list-tile-content style="font-size:20px">
          <v-list-tile-title>{{ item.poster }}</v-list-tile-title>
        </v-list-tile-content>
      </v-card-title>
    </v-card>
  </div>
</template>

<script>

export default {

  data() {
    return {
      header: '购物车',
      selected: [],
      items:[
        {
          posterAvatar: 'https://vuetifyjs.com/apple-touch-icon-180x180.png',
          poster: 'XiaoMing', 
          action: '2019/1/7',
          postDetail: '<p>帖子一的内容</p>'
        },
        {
          posterAvatar: 'https://vuetifyjs.com/apple-touch-icon-180x180.png',
          poster: 'XiaoMing', 
          action: '2019/1/6',
          postDetail: '<p>帖子二的内容</p>'
        },
        {
          posterAvatar: 'https://vuetifyjs.com/apple-touch-icon-180x180.png',
          poster: 'XiaoMing', 
          action: '2019/1/5',
          postDetail: '<p>帖子三的内容</p>'
        },
        {
          posterAvatar: 'https://vuetifyjs.com/apple-touch-icon-180x180.png',
          poster: 'XiaoMing', 
          action: '2019/1/4',
          postDetail: '<p>帖子四的内容</p>'
        },
        {
          posterAvatar: 'https://vuetifyjs.com/apple-touch-icon-180x180.png',
          poster: 'XiaoMing', 
          action: '2019/1/3',
          postDetail: '<p>帖子五的内容</p>'
        },
        {
          posterAvatar: 'https://vuetifyjs.com/apple-touch-icon-180x180.png',
          poster: 'XiaoMing', 
          action: '2019/1/2',
          postDetail: '<p>帖子六的内容</p>'
        },
        {
          posterAvatar: 'https://vuetifyjs.com/apple-touch-icon-180x180.png',
          poster: 'XiaoMing', 
          action: '2019/1/1',
          postDetail: '<p>帖子七的内容</p>'
        },
      ]
    }
  },
  methods: {
    toggleAll () {
      if (this.selected.length) this.selected = []
      else this.selected = this.items.slice()
    },
  }
}
</script>
