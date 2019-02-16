<template>
  <div>
    <p class="display-1">直答<span class="font-weight-thin"> Direct Answer</span></p>

    <div class="question-list">
      <v-card v-for="item in questions" :key="item.id">
        <v-card-title primary-title>
          <div>
            <div class="headline">{{ item.title }}</div>
            <span class="grey--text">由 {{ item.po }} 在 {{ item.time }} 提出</span>
          </div>
        </v-card-title>

        <v-card-content>
          <v-layout row wrap>
            <v-flex xs8>占位文字 placeholder 占位文字 placeholder 占位文字 placeholder 占位文字 placeholder 占位文字 placeholder 占位文字 placeholder 占位文字 placeholder 占位文字 placeholder 占位文字 placeholder 占位文字 placeholder 占位文字 placeholder 占位文字 placeholder </v-flex>
            <v-flex xs4>
              <img src="https://unity3d.com/sites/default/files/styles/frontpage_promo_large_background/public/unity-front-header_1.jpg?itok=KK6yypMW">
            </v-flex>
          </v-layout>
        </v-card-content>
      </v-card>
    </div>
  </div>
</template>

<script>
export default {
  
}
</script>

<style scoped>

</style>
