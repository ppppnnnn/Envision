<template>
  <div>
    <v-text-field label="填写问题:"></v-text-field>
    <envision-editor></envision-editor>
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

    })
  }
</script>