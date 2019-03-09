<template>
  <v-layout>
    <v-flex>
      <v-toolbar flat color="white" white>
        <v-toolbar-title ><b><font>礼品店</font></b></v-toolbar-title>
        <v-spacer></v-spacer>
        <v-tooltip bottom>
          <v-btn icon slot="activator">
            <v-badge right overlap color=red>
              <span slot="badge">6</span>
              <v-icon large color="black" >shopping_cart</v-icon>
            </v-badge>
          </v-btn>
          <span>“购物车”功能暂未上线，正在完善之中</span>
        </v-tooltip>
      </v-toolbar>
      <v-divider></v-divider>
      <v-card flat>
        <v-container fluid grid-list-md>
          <v-layout row wrap>
            <v-flex v-for="card in cards" :key="card.title" v-bind="{ [`xs${card.flex}`]: true }">
              <v-card flat>
                <v-img :src="card.src" height="200px">
                </v-img>
                <v-card-text style="text-align: center">
                  {{ card.name }}
                  ( {{ card.points }} 积分)
                </v-card-text>
                <v-card-actions>
                <v-toolbar dense flat color="white">    
                  <v-btn icon ripple>
                    <v-icon>remove</v-icon>
                  </v-btn>
                  <v-text-field label=" " solo ></v-text-field>
                  <v-btn icon ripple>
                    <v-icon>add</v-icon>
                  </v-btn>
                </v-toolbar>
                </v-card-actions>
              </v-card>
            </v-flex>
          </v-layout>
        </v-container>
      </v-card>
    </v-flex>
  </v-layout>
</template>

<script>

  export default {
    data: () => ({
      cards: [
      { name: "签字笔", points: 100, src: 'https://cdn.vuetifyjs.com/images/cards/house.jpg', flex: 3},
      { name: "笔记本", points: 200, src: 'https://cdn.vuetifyjs.com/images/cards/house.jpg', flex: 3},
      { name: "水杯", points: 300, src: 'https://cdn.vuetifyjs.com/images/cards/road.jpg', flex: 3 },
      { name: "32G U盘", points: 400, src: 'https://cdn.vuetifyjs.com/images/cards/road.jpg', flex: 3 },
      { name: "零食大礼包", points: 500, src: 'https://cdn.vuetifyjs.com/images/cards/plane.jpg', flex: 3}
      ]
    })
  }
</script>