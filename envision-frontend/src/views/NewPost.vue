<template>
  <div>
    <p class="display-1">创建主题帖<span class="font-weight-thin"> New Post</span></p>
    <v-layout wrap row>
      <v-flex class="px-4" xs6>
        <v-text-field label="填写帖子主题:"></v-text-field>
      </v-flex>
      <v-flex class="px-4" xs6>
        <v-select :items="sectionSelect" label="选择发布版块:"></v-select>
      </v-flex>
    </v-layout>


    <envision-editor class="mt-4"></envision-editor>
    <v-layout row wrap>
      <v-flex class="px-4">
        <v-btn block>保存为草稿</v-btn>
      </v-flex>
      <v-flex class="px-4">
        <v-btn color="info" block>发表主题</v-btn>
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
      sectionSelect: ['嵌入式技术交流区', '软件技术交流区', '机器人技术交流区', '生活轶事交流区']
    }),
    methods: {
      NewPost: function() {
        let self = this;
        let myDate = new Date();
        axios.post('http://127.0.0.1:8000/api/ArticleCommentViewSet/', {
          'author_id': storage.state.uid,
          'create_time': myDate.toLocaleString('chinese', {hour12: false}).replace(/\//g,"-"),
          'section_id': null,//根据分区名找
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