<template>
  <div>
    <span>
      <v-btn icon :to="'/activitynews/new'">
        <v-icon>keyboard_arrow_left</v-icon>
      </v-btn>
      返回帖子列表
    </span>
    <v-card class="mb-3">
      <v-card-title primary-title>   
        <v-list-tile-content style="font-size:20px">
          <v-list-tile-title>{{ topic }}</v-list-tile-title>
          <v-list-tile-sub-title class="grey--text" style="font-size:10px">
            {{ start_time }}
          </v-list-tile-sub-title>
        </v-list-tile-content>
      </v-card-title>
      <v-card-text v-html="content"></v-card-text>    
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn disabled flat color="grey" class="mx-2">
          <span >阅读量：</span>
          <span class="font-weight-bold mx-2">{{ vote }}</span>
        </v-btn>
      </v-card-actions>
    </v-card>
  </div>
</template>

<script>
import axios from 'axios'

  export default {
    data: () => ({
      topic: '',
      start_time: '',
      vote: 46,
      content: '',
    }),
    methods:{
      AnnoucementDetailGet: function() {
      let aid = this.$route.params.id;
      let self = this;
      axios.get('http://127.0.0.1:8000/api/GroupActivityViewSet/${aid}/'
      ).
      then(function(response) {
        console.log(response)
        self.content = response.data.content;
        self.topic = response.data.topic;
        self.create_time = response.data.create_time;
      }).
      catch(function(error) {
        console.log(error);
      });
    }
  },
  mounted() {
    this.AnnoucementDetailGet();
  }
}
</script>