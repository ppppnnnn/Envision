<template>
  <div>
    <div class="article-list">
      <v-card v-for="item in items" :key="item.id" :to="item.link" class="mb-2">
        <v-card-title primary-title class="article-title">
          <div style="font-size:10px">{{ item.partition }} &nbsp;|&nbsp;{{ item.action }}</div>
        </v-card-title>
        <v-card-text v-html="item.postDetail">
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="info" flat :to="/person/ + user_id">阅读</v-btn>
        </v-card-actions>
      </v-card>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import storage from '@/plugins/storage';

export default {
  data() {
    return {

      user_id:0,
      items:[
        {
          partition:'嵌入式技术交流区',
          action: '2019/1/7',
          postDetail: '<p>帖子一的内容</p>', 
          link: '/postdetail'
        },
        {
          partition:'软件技术交流区',
          action: '2019/1/6',
          postDetail: '<p>帖子二的内容</p>', 
          link: '/postdetail'
        },
        {
          partition:'机器人技术交流区',
          action: '2019/1/5',
          postDetail: '<p>帖子三的内容</p>', 
          link: '/postdetail'
        },
        {
          partition:'嵌入式技术交流区',
          action: '2019/1/4',
          postDetail: '<p>帖子四的内容</p>', 
          link: '/postdetail'
        },
        {
          partition:'嵌入式技术交流区', 
          action: '2019/1/3',
          postDetail: '<p>帖子五的内容</p>', 
          link: '/postdetail'
        },
        {
          partition:'嵌入式技术交流区', 
          action: '2019/1/2',
          postDetail: '<p>帖子六的内容</p>', 
          link: '/postdetail'
        },
        {
          partition:'嵌入式技术交流区',
          action: '2019/1/1',
          postDetail: '<p>帖子七的内容</p>', 
          link: '/postdetail'
        },
      ]
    }
  },
  // methods: {
  //   PersonPostListGet: function() {
  //     let self = this;
  //     let pid = storage.state.uid;
  //     axios.get('http://127.0.0.1:8000/api/PostViewSet/?author_id=pid'
  //     ).
  //     then(function(response) {
  //       console.log(response.data)
  //       self.items=response.data;
  //     }).
  //     catch(function(error) {
  //       console.log(error);
  //     });
  //   }
  // },
  // mounted() {
  //   this.PersonPostListGet();
  // }
}
</script>
