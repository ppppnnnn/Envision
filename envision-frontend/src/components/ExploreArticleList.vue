<template>
  <div>
    <div class="article-list">
      <v-card v-for="article in articles" :key="article.id" class="mb-2">
        <v-card-title primary-title class="article-title">
          <div>
            <h3 class="headline mb-0">{{ article.topic }}</h3>
            <div>作者 | 
              {{ article.author_id }}
            </div>
            <div>
            {{article.create_time}}
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
import axios from 'axios'

export default {
  data() {
    return {
      articles:[]
    }
  },
  methods: {
    ArticleListGet: function() {
      let self = this;
      axios.get('http://127.0.0.1:8000/api/ArticleViewSet/'
      ).
      then(function(response) {
        console.log(response)
        self.articles=response.data;
      }).
      catch(function(error) {
        console.log(error);
      });
    }
  },
  mounted() {
    this.ArticleListGet();
  }
}
</script>
