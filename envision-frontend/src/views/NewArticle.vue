<template>
  <div>
    <p class="display-1">创建文章<span class="font-weight-thin"> New Article</span></p>
    <v-text-field label="填写文章标题:"></v-text-field>
    <v-combobox
      color="success"
      flat
      v-model="tags"
      label="输入文章所属的标签，每输入一个标签后按下Enter键确认"
      append-icon=""
      messages="为你的文章添加合适的话题标签，有助于更多对该话题感兴趣的人浏览到文章"
      chips
      clearable
      multiple
    >
      <template slot="selection" slot-scope="data">
        <v-chip
          :selected="data.selected"
          close
          @input="remove(data.item)"
        >
          <strong>{{ data.item }}</strong>&nbsp;
        </v-chip>
      </template>
    </v-combobox>
    <envision-editor class="mt-4"></envision-editor>
    <v-layout row wrap>
      <v-flex class="px-4">
        <v-btn block>保存为草稿</v-btn>
      </v-flex>
      <v-flex class="px-4">
        <v-btn color="info" block @click="NewArticle()">发表文章</v-btn>
      </v-flex>
    </v-layout>
  </div>
</template>

<script>
  import envisionEditor from '@/components/TextEditorFull'
  import axios from 'axios'
  import storage from '@/plugins/storage';

  export default {
    components: {
      envisionEditor
    },
    data: () => ({
      tags: [],
    }),
    methods: {
      NewArticle: function() {
        let self = this;
        let myDate = new Date();
        axios.post('http://127.0.0.1:8000/api/ArticleCommentViewSet/', {
          'author_id': storage.state.uid,
          'create_time': myDate.toLocaleString('chinese', {hour12: false}).replace(/\//g,"-"),
          'tag': self.tags,
          'topic': self.articleTitle,
          'content': self.editorContent,
        }).
        then(function(response){
        }).
        catch(function(error) {
          console.log(error);
        });     
      },
    }
  }
</script>