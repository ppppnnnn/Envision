<template>
    <v-card
          class="mx-auto"
          max-width="1000"
        >
      <div id="app">
        <v-app id="inspire">
          <v-container>     
            <v-sheet class="pa-3 primary lighten-2">
              <v-text-field
                v-model="search"
                label="搜索"
                dark
                flat
                solo-inverted
                hide-details
                clearable
                clear-icon="search"
              ></v-text-field>
            </v-sheet>
            <v-layout row wrap>
              <v-flex xs12 >
                <h3 ref="radio" class="headline"></h3>          
                <v-radio-group v-model="type" row>
                  <v-radio label="所有器材" value="allequipment"></v-radio>
                  <v-radio label="借还记录" value="Loanrecord"></v-radio> 
                </v-radio-group>
              </v-flex>
            </v-layout>
            <Allequipment v-if="type==='allequipment'" v-model="allequipment" type="allequipment" label="所有器材"></Allequipment>
            <Loanrecord v-if="type==='Loanrecord'" v-model="Loanrecord" type="Loanrecord" label="借还记录"></Loanrecord>
          </v-container>
        </v-app>
      </div>
    </v-card>
</template>

<script>
import Allequipment from '@/views/Allequipment.vue';
import Loanrecord from '@/views/Loanrecord.vue';
import axios from 'axios'
  export default {
  components:{
    Allequipment,
    Loanrecord
  },
    data () {
        
      return {
        type: '所有器材',
        loanrecord: '借还记录',
      }
    },
  }
</script>