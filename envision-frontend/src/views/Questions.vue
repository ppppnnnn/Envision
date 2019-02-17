<template>
  <div>
    <p class="display-1">直答<span class="font-weight-thin"> Direct Answer</span></p>

    <div class="question-list">
      <v-card v-for="item in questions" :key="item.id" class="mb-2">
        <v-card-title primary-title>
          <div>
            <div class="headline">{{ item.title }}</div>
            <span class="grey--text">由 {{ item.po }} 在 {{ item.time }} 提出, 已有 {{ item.answerCount }} 个回答</span>
          </div>
        </v-card-title>

        <v-card-text>
          <v-layout row wrap>
            <v-flex xs12 v-if="item.image == null">
              <span class="font-weight-bold">{{ item.topResponder }}</span> : {{ item.answer }}
            </v-flex>
            <v-flex xs8 v-if="item.image != null">
              {{ item.answer }}
            </v-flex>
            <v-flex xs4 v-if="item.image != null">
              <v-img
                :src="item.image"
                aspect-ratio="2.5"
              ></v-img>
            </v-flex>
          </v-layout>
        </v-card-text>

        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn flat color="success">查看详情</v-btn>
        </v-card-actions>
      </v-card>
    </div>
  </div>
</template>

<script>
export default {
  data:() => ({
    questions: [
      {
        id: 1,
        title: '什么是直答？',
        po: 'James White',
        time: '2019/2/17',
        answerCount: '1',
        image: null,
        topResponder: 'Owen Tsai',
        answer: '「直答」是 Envision 最新推出的一项服务，旨在为了在保证人工智能技术协会热情互助的氛围的前提下，鼓励大家自己探索解决问题的方式方法。在「直答中」任何用户都可以提出一个问题，并就这个问题邀请另外的 Envision 用户进行回答...',
      },
      {
        id: 2,
        title: '如何使用Python入门，进行机器学习？',
        po: '路人甲',
        time: '2019/2/18',
        answerCount: '0',
        image: 'https://picsum.photos/500/300?image=11',
        topResponder: '路人乙',
        answer: '我来举个实际的例子吧。比如你想要写一个Python程序来自动识别图片中是否存在山河风景，那么你首先需要大量的模型用于程序的训练。比如如图所示的这张图片，首先，你需要...'
      },
      {
        id: 3,
        title: '请问这段代码出了什么问题？',
        po: 'Tom Taylor',
        time: '2019/2/14',
        answerCount: '2',
        image: 'http://img3.imgtn.bdimg.com/it/u=4036543105,586481454&fm=11&gp=0.jpg',
        topResponder: 'James White',
        answer: '这个错误反映除了你对指针的了解并不是很充足。你从图中可以看出，这段代码的主要目的在于什么我也不知道，我这段回答主要是为了测试一下显示文字是否是正常的。这个错误反映除了你对指针的了解并不是很充足。你从图中可以看出，这段代码的主要目的在于什么我也不知道，我这段回答主要是为了测试一下显示文字是否是正常的.这个错误反映除了你对指针的了解并不是很充足。你从图中可以看出，这段代码的主要目的在于什么我也不知道...'
      }
   ]
  })
}
</script>

<style scoped>

</style>
