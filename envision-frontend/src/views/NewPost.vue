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

  export default {
    components: {
      envisionEditor
    },
    data: () => ({
      sectionSelect: ['测试板块1', '测试板块2', '测试板块3', '测试板块4']
    })
  }
</script>