<template>
  <div>
    <div class="question-list">
      <v-card v-for="question in questions" :key="question.id" class="mb-2">
        <v-card-title primary-title class="question-title">
          <div>
            <div class="headline">{{ question.title }}</div>
            <span class="grey--text"> {{ question.time }} 提出, 已有 {{ question.answerCount }} 个回答</span>
          </div>
        </v-card-title>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn flat color="success" :to="/question/ +user_id ">查看详情</v-btn>
        </v-card-actions>
      </v-card>
    </div>
  </div>
</template>

<script>
export default {
  data:() => ({
    user_id: 0,
    questions: [
      {
        title: '什么是直答？',
        time: '2019/2/17',
        answerCount: '1',
      },
      {
        title: '如何使用Python入门，进行机器学习？',
        time: '2019/2/18',
        answerCount: '0',
      },
      {
        title: '请问这段代码出了什么问题？',
        time: '2019/2/14',
        answerCount: '2',
      }
   ]
  })
}
</script>

<style scoped>
  /* Add a right padding to separate text and image */
  .question-text {
    padding-right: 20px;
  }

  /* Decrease default padding between card-title and card-text */
  .question-title {
    padding-bottom: 0;
  }
</style>
