  <template>
     <v-card raised style="max-height: 1000px;">
        <v-toolbar color="pink" dark dense height="80px">
          <v-toolbar-side-icon></v-toolbar-side-icon>
            <v-menu :nudge-width="100">

          <template v-slot:activator="{ on }">
            <v-toolbar-title v-on="on">
                <span>学习清单</span>
                    <v-icon dark>arrow_drop_down</v-icon>
            </v-toolbar-title>
          </template>

          <v-list>
            <v-list-tile
                        v-for="item in items"
                        :key="item"
                        @click=""
            >
              <v-list-tile-title v-text="item"></v-list-tile-title>
            </v-list-tile>
            </v-list>
                  </v-menu>

          <v-spacer></v-spacer>
            <v-tooltip bottom>
                <v-btn icon slot="activator">
                    <v-icon>notifications</v-icon>
                </v-btn>
                    <span>开启“监督我”功能</span>
              </v-tooltip>
              <Addlist></Addlist> 
            </v-toolbar>
          
          <v-expansion-panel focusable>
              <v-expansion-panel-content
                v-for="(item,i) in 6"
                :key="i"
              >
            <template v-slot:header>
              <div> 
                <div>
                  <v-btn icon>
                  <v-icon>check_circle_outline</v-icon>
                  </v-btn>
                  Top1
                </div>
                <span class="grey--text">截止日期：2019-03-09</span>
              </div>

            <v-card-actions >
              <v-spacer></v-spacer>
                <v-btn icon>
                  <v-icon>edit</v-icon>
                </v-btn>
                <v-btn icon>
                  <v-icon>delete</v-icon>
                </v-btn>
              </v-card-actions>
            </template>

            <v-card>
              <v-card-text class="grey lighten-3">Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.</v-card-text>
                </v-card>
              </v-expansion-panel-content>
          </v-expansion-panel>
     </v-card>
  </template>

<script>
import Addlist from '@/components/Addlist'
import axios from 'axios'
export default {
    components: {
    Addlist
  },
 data: () => ({
    items: [
      '学习清单', '学习目标'
    ],
     methods:{
          AddlistGet: function() {
            let self = this;
            axios.get('http://127.0.0.1:8000/api/LearningTaskViewSet/')
            .then(function(response) {
              console.log(response)
            self.items=response.data;
            })
            .catch(function(error) {
              console.log(error)
            })
          },
          mounted() {
            this.AddlistGet();
          }
        }
  }),
}
</script>
