  <template>
    <v-layout row wrap>
      <v-flex>
        <div>
          <v-toolbar color="yellow darken-1" tabs>
            <v-text-field
              class="mx-3"
              flat
              label="搜索功能暂不可用"
              prepend-inner-icon="search"
              solo-inverted
            ></v-text-field>
            <v-tabs slot="extension" left color="transparent" slider-color="red">
              <v-tab to="/explore/dynamic">动态</v-tab>
              <v-tab to="/explore/articlelist">文章</v-tab>
              <v-tab to="/explore/questionslist">直答</v-tab>
            </v-tabs>            
          </v-toolbar>
          <v-tabs-items>
            <v-tab-item>
              <router-view></router-view>
            </v-tab-item>
          </v-tabs-items>
        </div>
      </v-flex>
    </v-layout>
</template>

<script>

export default {
    
  data() {
    return {

    }
  }
}

</script>
