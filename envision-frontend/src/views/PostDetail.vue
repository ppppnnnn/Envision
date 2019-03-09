<template>
  <div>
    <span>
      <v-btn icon :to="/postlist/ +id">
        <v-icon>keyboard_arrow_left</v-icon>
      </v-btn>
      返回帖子列表
    </span>
    <v-card class="mb-3">
      <v-card-title primary-title>
        <v-avatar color="grey lighten-4" :size=40 slot="activator">
          <img :src="posterAvatar" alt="avatar">
        </v-avatar>
        <v-list-tile-content style="font-size:20px">
          <v-list-tile-title>{{ poster }}</v-list-tile-title>
          <v-list-tile-sub-title class="grey--text" style="font-size:10px">
            {{ partition }} &nbsp;|&nbsp; {{ time }}
          </v-list-tile-sub-title>
        </v-list-tile-content>
      </v-card-title>
      <v-card-text v-html="postDetail"></v-card-text>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn small flat color="info" @click="dialog = !dialog">评论</v-btn>
      </v-card-actions>
    </v-card>      
    <v-card v-for="answer in answers" :key="answer.id" class="mb-1">
      <v-card-title>
        <v-list-tile-avatar>
          <img :src="answer.responderAvatar" alt="avatar">
        </v-list-tile-avatar>
        <v-list-tile-content style="font-size:20px">
          <v-list-tile-title>{{ answer.responder }}</v-list-tile-title>
          <v-list-tile-sub-title class="grey--text" style="font-size:10px">
            {{ answer.floornum }} &nbsp;|&nbsp; {{ answer.time }}
          </v-list-tile-sub-title>
        </v-list-tile-content>
      </v-card-title>
      <v-card-text>
        <span v-html="answer.content"></span>
      </v-card-text>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-tooltip top>
          <v-btn flat color="success" icon slot="activator">
            <v-icon>sentiment_satisfied_alt</v-icon>
          </v-btn>
          <span>点赞</span>
        </v-tooltip>
        <span class="font-weight-bold mx-2">{{ answer.vote }}</span>
        <v-btn outline color="grey" slot="activator" @click="dialog = !dialog" class="mx-2">
          <v-icon>insert_comment</v-icon> 回复
        </v-btn>
      </v-card-actions>
    </v-card>
    <v-dialog v-model="dialog" max-width="780">
      <v-card>
        <envision-editor></envision-editor>
        <v-layout row wrap>
          <v-flex class="px-4">
            <v-btn block @click="dialog = false">确认</v-btn>
          </v-flex>
          <v-flex class="px-4">
            <v-btn color="info" block @click="dialog = false">取消</v-btn>
          </v-flex>
        </v-layout>
      </v-card>  
    </v-dialog>
  </div>
</template>

<script>
  import envisionEditor from '@/components/TextEditorFull'

  export default {
    components: {
      envisionEditor
    },
    data: () => ({
      posterAvatar: 'https://vuetifyjs.com/apple-touch-icon-180x180.png',
      poster: 'XiaoMing',
      id: 0,
      partition: '嵌入式技术交流区',
      time: '2019/2/17',
      postDetail: '<p>帖子一的内容</p>',
      dialog: false,
      answers: [
        {
          id: 1,
          responder: 'XiaoPeng',
          responderAvatar: 'https://vuetifyjs.com/apple-touch-icon-180x180.png',
          floornum: '第一楼',
          time: '2019/2/18',
          content: '<p>我是一楼</p>',
          vote: 177
        },
        {
          id: 2,
          responder: '  Bill',
          responderAvatar: 'https://vuetifyjs.com/apple-touch-icon-180x180.png',
          floornum: '第二楼',
          time: '2019/2/18',
          content: '<p>我是二楼</p>',
          vote: 94
        },
        {
          id: 3,
          responder: 'XiaoHong',
          responderAvatar: 'https://vuetifyjs.com/apple-touch-icon-180x180.png',
          floornum: '第三楼',
          time: '2019/2/18',
          content: '<p>我是三楼</p>',
          vote: 84
        },
      ]
    })
  }
</script>