<template>
  <div>
    <span>
      <v-btn icon :to="'/announmentceDetails/new'">
        <v-icon>keyboard_arrow_left</v-icon>
      </v-btn>
      返回帖子列表
    </span>
    <v-card class="mb-3">
      <v-card-title primary-title>   
        <v-Detail-tile-content style="font-size:20px">
          <v-Detail-tile-title>{{ topic }}</v-Detail-tile-title>
          <v-Detail-tile-sub-title class="grey--text" style="font-size:10px">
            {{ create_time }}
          </v-Detail-tile-sub-title>
        </v-Detail-tile-content>
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
      create_time: '',
      vote: 28,
      content: '',
    }),
    methods:{
      AnnoucementDetailGet: function() {
      let aid = this.$route.params.id;
      let self = this;
      axios.get('http://127.0.0.1:8000/api/AnnouncementViewSet/${aid}/'
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