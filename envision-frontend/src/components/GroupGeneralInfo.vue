<template>
  <v-layout class="basic-info" row wrap>
    <v-flex xs5>
      <p class="font-weight-bold" v-for="info in infoList" :key="info.head">{{ info.head }}
        <span class="font-weight-regular"> {{ info.body }}</span>
      </p>
    </v-flex>
    <v-flex xs7>
      <v-card color="purple darken-2" class="white--text">
        <v-layout>
          <v-flex xs4 class="pa-4">
            <v-img
              src="https://cdn.vuetifyjs.com/images/cards/foster.jpg"
              aspect-ratio="1"
            ></v-img>
          </v-flex>
          <v-flex xs8>
            <v-card-title primary-title>
              <div>
                <div class="headline">{{ memberID[0] }}</div>
                <div>{{ memberID[1] }}</div>
                <br>
                <div class="font-weight-thin">{{ memberID[2] }}</div>
              </div>
            </v-card-title>
          </v-flex>
        </v-layout>
        <v-divider light></v-divider>
        <v-card-actions class="pa-3">
          AAIT - NO. ac201801001
          <v-spacer></v-spacer>
          <v-btn outline small color="white">导出</v-btn>
        </v-card-actions>
      </v-card>
    </v-flex>
    <v-flex xs12>
      <p class="font-weight-bold">群组介绍 <br><span class="font-weight-regular">{{ groupIntro }}</span></p>
    </v-flex>
  </v-layout>
</template>

<script>
  export default {
    data: () => ({
      infoList: [
        {head: '群组性质', body: '常规学习交流'},
        {head: '创建时间', body: '2017年11月11日'},
        {head: '管理员', body: '张三, 李四'},
        {head: '活跃度', body: '177'},
        {head: '当前期数', body: '2'},
        {head: '成员数量', body: '99'},
      ],
      groupIntro: 'C语言学习交流小组是由人工智能技术协会创建的，旨在于不拉不拉不拉的群组C语言学习交流小组是由人工智能技术协会创建的，旨在于不拉不拉不拉的群组C语言学习交流小组是由人工智能技术协会创建的，旨在于不拉不拉不拉的群组.C语言学习交流小组是由人工智能技术协会创建的，旨在于不拉不拉不拉的群组C语言学习交流小组是由人工智能技术协会创建的，旨在于不拉不拉不拉的群组C语言学习交流小组是由人工智能技术协会创建的，旨在于不拉不拉不拉的群组.',
      memberID: [
        'Owen Tsai',
        'C语言学习交流群组 - 合格证明',
        '该同学已经完成了人工智能技术协会的活动，可以予以学分认定。',
      ]
    })
  }
</script>

<style scoped>

</style>