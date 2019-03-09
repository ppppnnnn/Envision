<template>
  <div>
    <span>
      <v-btn icon :to="'/explore/questionslist'">
        <v-icon>keyboard_arrow_left</v-icon>
      </v-btn>
      返回直答列表
    </span>

    <v-card class="mb-3">
      <v-card-title primary-title>
        <div class="headline">{{ questionTitle }}</div>
        <span class="grey--text">由 {{ poster }} 在 {{ time }} 提出</span>
      </v-card-title>

      <v-card-text v-html="questionDetail"></v-card-text>

      <v-card-actions>
        <v-btn small flat color="info" @click="dialog = !dialog">我来回答</v-btn>
      </v-card-actions>
    </v-card>
    <v-card v-for="answer in answers" :key="answer.id" class="mb-1">
      <v-card-title>
        <v-avatar color="grey lighten-4" :size=40 slot="activator">
          <img :src="answer.responderAvatar" alt="avatar">
        </v-avatar>
        <span class="ml-3 font-weight-bold">{{ answer.responder }}, </span>
        <span class="ml-3">回答于 {{ answer.time }}</span>
      </v-card-title>
      <v-card-text>
        <span v-html="answer.content"></span>
      </v-card-text>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-tooltip top>
          <v-btn flat color="success" icon slot="activator">
            <v-icon>arrow_drop_up</v-icon>
          </v-btn>
          <span>赞成该答案</span>
        </v-tooltip>
        <span class="font-weight-bold mx-2">{{ answer.vote }}</span>
        <v-tooltip top>
          <v-btn flat color="error" icon slot="activator">
            <v-icon>arrow_drop_down</v-icon>
          </v-btn>
          <span>反对该答案</span>
        </v-tooltip>
        <v-btn outline color="grey" slot="activator" class="mx-2">
          <v-icon>flag</v-icon> 举报
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
      dialog: false,
      questionTitle: '什么是直答？',
      poster: 'James White',
      time: '2019/2/17',
      questionDetail: '<p>最近在浏览 Envision 的时候，发现了有一个模块叫做【直答】。所以我想请问一下，直答这个模块的主要功能是什么呢？</p>',
      answers: [
        {
          id: 1,
          responder: 'Owen Tsai',
          responderAvatar: 'https://vuetifyjs.com/apple-touch-icon-180x180.png',
          time: '2019/2/18',
          content: '<p>「直答」是 Envision 最新推出的一项服务，旨在为了在保证人工智能技术协会热情互助的氛围的前提下，<strong>鼓励大家自己探索解决问题的方式方法</strong>。</p><p>在「直答」中任何用户都可以提出一个问题，并就这个问题邀请另外的 Envision 用户进行回答。被邀请的用户会受到系统的提醒通知。同时，<b>任何人都可以回答「直答」中的问题</b>，其中也包括自己提出的。但是提问者在提出该问题时如果邀请了某一位用户进行回答，那么被邀请者的答案将会置顶显示在其他所有回答的上面，被更多的人看到。<p>如果被邀请者回答了提问者提出的问题，那么提问者将要支付一定数额的积分作为赏金。如果在提出问题前，提问者的积分余额不足以支付赏金，那么提问将无法发布。</p>',
          vote: 177
        },
        {
          id: 2,
          responder: '错误示范',
          responderAvatar: 'https://vuetifyjs.com/apple-touch-icon-180x180.png',
          time: '2019/2/18',
          content: '<p>楼上说得很好，我完全同意楼上的说法。</p>',
          vote: -94
        }
      ]
    })
  }
</script>