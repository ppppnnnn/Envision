<template>
  <div>
    <div class="article-list">
      <v-card v-for="article in articles" :key="article.id" class="mb-2">
        <v-card-title primary-title class="article-title">
          <div>
            <h3 class="headline mb-0">{{ article.title }}</h3>
            <div>作者 | 
              {{ article.user_name }}
            </div>
            <div>
            {{article.article_time}}
            </div>
          </div>
        </v-card-title>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-tooltip bottom>
            <v-btn icon flat slot="activator" color="grey">
              <v-icon>favorite</v-icon>{{ article.applaud }}
            </v-btn>
            <span>“赞同”功能暂未上线，正在完善之中</span>
          </v-tooltip>
          <v-btn color="info" flat :to="/article/ + article.article_id">阅读</v-btn>
        </v-card-actions>
      </v-card>
    </div>
  </div>
</template>

<script>
//import axios from 'axios'
export default {
  data() {
    return {
      articles:[
          {
              article_id: 0 ,
              title: '0',
              user_name: 'Xiaoming',
              article_time: '2019/1/1',
          },
          {
              article_id: 1 ,
              title: '1',
              user_name: 'Xiaoming',
              article_time: '2019/1/1',
          },
          {
              article_id: 2 ,
              title: '2',
              user_name: 'Xiaoming',
              article_time: '2019/1/1',
          },
      ]
    }
  },
//   methods: {
//     AddArticleToFav: function(article_id) {
//       // this.articles[article_id].isLiked = !this.articles[article_id].isLiked;
//       // if(this.articles[article_id].isLiked === false) {
//       //   this.articles[article_id].likes -= 1;
//       // } else {
//       //   this.articles[article_id].likes += 1;
//       // }
//     },
//     ArticleListGet: function() {
//       let self = this;
//       axios.get(`${'https://cors-anywhere.herokuapp.com/'}http://www.aait-suse.cn/api/ArticleViewSet/`
//       ).
//       then(function(response) {
//         console.log(response.data)
//         self.articles=response.data;
//       }).
//       catch(function(error) {
//         console.log(error);
//       });
//     }
//   },
//   props: {
//     showCtrlBtns: Boolean
//   },
//   mounted() {
//     this.ArticleListGet();
//   }
}
</script>
