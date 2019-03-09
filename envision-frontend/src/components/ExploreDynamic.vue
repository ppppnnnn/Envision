<template>
  <div>
    <div class="dynamic-list">
      <v-card v-for="dynamic in dynamics" :key="dynamic.id" class="mb-2">
        <v-card-text>
          <v-layout row wrap>
            <v-flex xs12  class="dynamic-text">
              <span class="font-weight-bold">{{ dynamic.name }}</span> : {{ dynamic.content }}
            </v-flex>
            <v-flex xs6 v-if="dynamic.image != null">
              <v-img
                :src="dynamic.image"
                aspect-ratio="2.5"
                style="margin-top:20px"
              ></v-img>
            </v-flex>

          </v-layout>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn 
            flat
            :color="dynamic.isInFav ? 'success' : 'grey'"
            @click="dynamic.isInFav = !dynamic.isInFav"
          >
            <v-icon>star</v-icon>
          </v-btn>
          <v-btn 
            flat
            :color="dynamic.isLiked ? 'red' : 'info'"
            @click="AddFeedToFav(dynamic.dynamic_id)"
          >
            <v-icon>favorite</v-icon>{{ dynamic.applaud }}
          </v-btn>
        </v-card-actions>
      </v-card>
    </div>
  </div>
</template>

<script>

export default {
  data() {
    return {
      dynamics:[
          {
             dynamic_id: 0,
             image: 'https://picsum.photos/500/300?image=11',
             name: 'XiaoMing',
             content: 'asfafsasvavasdasfafa',
             applaud: 12, 
          },
          {
              dynamic_id: 1,
              image: null,
              name: 'XiaoMing',
              content: 'daffewfvwvsdsdfsfsdasdasd',
              applaud: 45,
          },
          {
              dynamic_id: 2,
              image: null,
              name: 'XiaoMing',
              content: 'dqwqrfewwegwewerrwefwevwevwewefefwefwf',
              applaud: 41,
          }
      ]
    }
  },
//   methods: {
//     AddFeedToFav: function(feed_id) {
//       this.feeds[feed_id].isLiked = !this.feeds[feed_id].isLiked;
//       if(this.feeds[feed_id].isLiked === false) {
//         this.feeds[feed_id].likes -= 1;
//       } else {
//         this.feeds[feed_id].likes += 1;
//       }
//     },
//     FeedListGet: function() {
//       let self = this;
//       axios.get(`${'https://cors-anywhere.herokuapp.com/'}http://www.aait-suse.cn/api/FeedViewSet/`
//       ).
//       then(function(response) {
//         self.feeds=response.data;
//       }).
//       catch(function(error) {
//         console.log(error);
//       });
//     },
//   },
//   props: {
//     showCtrlBtns: Boolean
//   },
//   mounted() {
//     this.FeedListGet();
//   }
}
</script>
