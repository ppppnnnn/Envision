<template>
  <div>
    <span>
      <v-btn icon :to="'/explore/articlelist'">
        <v-icon>keyboard_arrow_left</v-icon>
      </v-btn>
      返回文章列表
    </span>
    <v-layout row wrap>
      <v-flex>
        <v-card>
          <v-card-title primary-title>
            <div>
              <h3 class="headline mb-0">{{ title }}</h3>
              <div>作者 {{ author }} , 发表于 {{ time }}</div>
            </div>
          </v-card-title>
          <v-card-text v-html="content"></v-card-text>
        </v-card>
      </v-flex>
    </v-layout>
  </div>
</template>

<script>
import axios from 'axios'

export default {

  data() {
    return {
      title: '',
      author: '',
      content: '',
      time: '',
    }
  },
  methods: {
    GetArticleContent: function() {
      let aid = this.$route.params.id;
      let self = this;
      axios.get('http://127.0.0.1:8000/api/ArticleViewSet/${aid}/')
      .then(function(response) {
        self.content = response.data.content;
        self.author = response.data.anthor_name;
        self.title = response.data.topic;
        self.time = response.data.create_time;
      })
      .catch(function(error) {
        alert('获取文章出现错误。请将以下内容发送给 @蔡仲晨 进行分析：\n' + error);
      });
    }
  },
  mounted() {
    this.GetArticleContent();
  }
}
</script>
