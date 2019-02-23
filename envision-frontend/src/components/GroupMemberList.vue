<template>
  <v-card flat>
    <v-layout row wrap>
      <v-flex xs10 class="pr-3">
        <v-text-field
          label="搜索成员"
          box
        ></v-text-field>
      </v-flex>
      <v-flex xs2>
        <v-btn block color="primary">
          搜索
        </v-btn>
      </v-flex>
    </v-layout>

    <v-list three-line>
      <template v-for="(member, index) in members">
        <v-subheader
          v-if="item.header"
          :key="item.header"
        >
          {{ item.header }}
        </v-subheader>

        <v-divider
          v-else-if="item.divider"
          :key="index"
          :inset="item.inset"
        ></v-divider>

        <v-list-tile
          v-else
          :key="item.title"
          avatar
          @click=""
        >
          <v-list-tile-avatar>
            <img :src="item.avatar">
          </v-list-tile-avatar>

          <v-list-tile-content>
            <v-list-tile-title v-html="item.title"></v-list-tile-title>
            <v-list-tile-sub-title v-html="item.subtitle"></v-list-tile-sub-title>
          </v-list-tile-content>
        </v-list-tile>
      </template>
    </v-list>
  </v-card>
</template>

<script>
  export default {
    data: () => ({
      members: [
        {  }
      ]
    })
  }
</script>