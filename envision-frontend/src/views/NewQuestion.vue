<template>
  <div>
    <p class="display-1">创建问题<span class="font-weight-thin"> New Question</span></p>
    <v-text-field label="填写问题标题:"></v-text-field>
    <v-combobox
      color="success"
      flat
      v-model="tags"
      label="输入问题所属的标签，每输入一个标签后按下Enter键确认"
      append-icon=""
      messages="为你的问题添加合适的话题标签，有助于更多对该话题感兴趣的人浏览到问题"
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
        <v-btn color="info" block>发表问题</v-btn>
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
      tags: []
    })
  }
</script>