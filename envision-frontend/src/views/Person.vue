<template>
  <v-layout row wrap> 
    <v-flex xl12 lg12 md12 sm12 xs12 order-sm2 order-xs2 order-lg1 order-md1 order-xl1>
      <v-card>
        <v-layout align-center justify-center style="
          height: 300px; 
          background-image: url('https://raw.githubusercontent.com/AAIT-SUSE/forum/master/src/assets/img/profile-bg.jpg');
          background-repeat: no-repeat;
          background-size: conver; 
          z-index: -99
        ">
          <v-flex xs3>
            <v-img
              :src='userAvatar'
              height="125px"
              contain
              style="border-radius:10%"
            ></v-img>
          </v-flex>
          <v-flex xs9>
            <v-card-title primary-title class="white--text">
              <div>
                <div class="headline">{{ username }}
                  <v-btn icon @click="mini = !mini">
                    <v-icon color="white" v-if="mini">chevron_left</v-icon>
                    <v-icon color="white" v-if="!mini">chevron_right</v-icon>
                  </v-btn>  
                </div>
                <div>
                  <v-icon></v-icon>
                  {{ userSignature }}
                </div>
                <br>
                <div>
                  <v-tooltip right>
                    <v-chip color="white" slot="activator">
                      <v-avatar>
                        <v-icon color="primary">local_offer</v-icon>
                      </v-avatar>
                      {{ userCredits }} 积分
                    </v-chip>
                    <span>
                      积分可以通过以下途径获得: <br>
                      <li>热心帮助他人</li>
                      <li>对社区做出贡献</li>
                      <li>积极参加活动</li>
                      <li>参与其他活动、赛事等</li>
                      <br>
                      使用积分可以提出"直答"问题，或在礼品店兑换礼品
                    </span>
                  </v-tooltip>
                </div>
              </div>
              <div>
                <v-timeline dense v-if=" mini == true ">
                  <v-timeline-item
                    v-for="item in items"
                    :key="item.index"
                    color="red lighten-2"
                    small
                    left
                    fill-dot
                  >
                    <span>{{ item.time }}&nbsp;&nbsp;&nbsp;{{ item.assignment }}</span>                
                  </v-timeline-item>
                </v-timeline> 
              </div>
            </v-card-title>
          </v-flex>
        </v-layout>
      </v-card> 
    </v-flex>
    <v-flex xl12 lg12 md12 sm12 xs12 order-sm2 order-xs2 order-lg1 order-md1 order-xl1>
      <div>  
        <v-tabs
          slot="extension" v-model="tab" color="warning" grow>
          <v-tab>我的文章</v-tab>
          <v-tab>我的帖子</v-tab>
          <v-tab>我的直答</v-tab>
          <v-tab>我的关注</v-tab>
          <v-tab>我的学习</v-tab>
        </v-tabs>
        <v-tabs-items>
          <v-tab-item>
            <router-view></router-view>
          </v-tab-item>
        </v-tabs-items>
      </div>
    </v-flex>
  </v-layout>
</template>

<script>

export default {

  data() {
    return {
      mini: false,
      username: 'Owen Tsai',
      userCredits: '666',
      userSignature: 'Envision 项目发起人',
      userAvatar: 'https://randomuser.me/api/portraits/men/85.jpg',
      tab: null,
      items:[
        {
          time: "2019/1/1",
          assignment: "掌握c语言函数",
        },
        {
          time: "2019/1/2",
          assignment: "掌握c语言指针" 
        }
      ],
      groups: [
        {
          message: '我的文章',
          value: 'Article',
          link: '/postlist/' +user_id
        },
        {
          message: '我的帖子',
          value: 'Post',
          link: '/postlist/ +user_id'
        },
        {
          message: '我的直答',
          value: 'Answer',
          link: '/postlist/ +user_id'
        },
        {
          message:'我的关注',
          value:'MyAttention',
          link: '/postlist/ +user_id'
        },
        {
          message:'我的学习',
          value:'MyStudy',
          link: '/postlist/ +user_id'
        },
      ]
    }
  },
  methods: {
  }
}
</script>
<style scoped>
</style>