<template>
  <div>
    <span>
      <v-btn icon :to="'/forum/new'">
        <v-icon>keyboard_arrow_left</v-icon>
      </v-btn>
      返回论坛首页
    </span>
    <v-card >
      <v-list two-line>
        <div v-for="(item, index) in items" :key="index">
          <v-list-tile :to="/postDetail/ +item.post_id">
            <v-list-tile-avatar>
              <img :src="item.posterAvatar" alt="avatar">
            </v-list-tile-avatar>
            <v-list-tile-content>
              <v-list-tile-title>{{ item.autnor_name }}</v-list-tile-title>
              <v-list-tile-sub-title style="font-size:10px">
                {{ item.create_time }}
              </v-list-tile-sub-title>
              <v-list-tile-sub-title class="text--primary" style="font-size:12px" v-html="item.content">
              </v-list-tile-sub-title>
            </v-list-tile-content>

          </v-list-tile>
          <v-divider v-if="index + 1 < items.length" :key="`divider-${index}`">
          </v-divider>
        </div>
      </v-list>
    </v-card>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  data() {
    return {
      items:[
      ]
    }
  },
    methods:{
      PostListGet: function() {
      let aid = this.$route.params.id;
      let self = this;
      axios.get('http://127.0.0.1:8000/api/PostVieweSet/?seaction_id=${aid}/'
      ).
      then(function(response) {
        console.log(response)
        self.items=response.data;
      }).
      catch(function(error) {
        console.log(error);
      });
    }
  },
  mounted() {
    this.PostListGet();
  }
}
</script>
