<template>
  <div>
    <div class="article-list">
      <v-card v-for="article in articles" :key="article.id" class="mb-2">
        <v-card-title primary-title class="article-title">
          <div>
            <h3 class="headline mb-0">{{ article.topic }}</h3>
            <div>
            {{article.create_time}}
            </div>
          </div>
        </v-card-title>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-tooltip bottom>
            <v-btn disabled icon flat slot="activator" color="grey">
              <v-icon>favorite</v-icon>{{ article.applaud }}
            </v-btn>
          </v-tooltip>
          <v-btn color="info" flat :to="/article/ + article.article_id">阅读</v-btn>
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
      articles:[
      ]
    }
  },
  methods: {
    PersonArticleListGet: function() {
      let self = this;
      let pid = storage.state.uid;
      axios.get('http://127.0.0.1:8000/api/ArticleViewSet/?author_id=pid'
      ).
      then(function(response) {
        console.log(response.data)
        self.articles=response.data;
      }).
      catch(function(error) {
        console.log(error);
      });
    }
  },
  mounted() {
    this.PersonArticleListGet();
  }
}
</script>
