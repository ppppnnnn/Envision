<template>
  <div>
    <v-text-field label="填写文章标题:"></v-text-field>
    <envision-editor></envision-editor>
    <v-layout row wrap>
      <v-flex class="px-4">
        <v-btn block>保存为草稿</v-btn>
      </v-flex>
      <v-flex class="px-4">
        <v-btn color="info" block>发表文章</v-btn>
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

    })
  }
</script>