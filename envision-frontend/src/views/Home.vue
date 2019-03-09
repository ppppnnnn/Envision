<template>
  <div>
    <v-carousel>
      <v-carousel-item
        v-for="(item,i) in items"
        :key="i"
        :src="item.src"
      ></v-carousel-item>
    </v-carousel>

    <v-card>
      <v-card-title primary-title>
        <h3 class="headline mb-0">“发现杯”全国大学生互联网软件设计大赛</h3>
      </v-card-title>
    </v-card>

    <v-layout row wrap>
      <v-flex xs6 v-for="post in posts" :key="post.id" >
        <v-card raised class="ma-4">
          <v-img v-if="post.img"
            :src="post.img"
            aspect-ratio="2.75"
          ></v-img>
          <v-card-title primary-title v-if="post.title">
            <h3 class="headline mb-0">{{ post.title }}</h3>
          </v-card-title>
          <v-card-text v-if="post.content">
            {{ post.content }}
          </v-card-text>
        </v-card>
      </v-flex>
    </v-layout>
  </div>
</template>


<script>
  export default {
    data () {
      return {
        items: [
          {
            src: 'https://cdn.vuetifyjs.com/images/carousel/squirrel.jpg'
          },
          {
            src: 'https://cdn.vuetifyjs.com/images/carousel/sky.jpg'
          },
          {
            src: 'https://cdn.vuetifyjs.com/images/carousel/bird.jpg'
          },
          {
            src: 'https://cdn.vuetifyjs.com/images/carousel/planet.jpg'
          }
        ],
        posts:[
          {
          id: 1,
          title:'赛项主题',
          content: ' 发现杯大赛分设“互联网应用开发与设计”、“网络营销技能”、“艺术设计”和“大数据”四个比赛项目。旨在提升高校学生积极参与互联网领域的研究兴趣，激发学生团队创新创业意识，提高高校在互联网技术开发应用和电子商务营销方向的成果转化能力。',
          },
          {
          id: 2,
          title: '互联网应用开发与设计',
          content: ' 参赛者根据大赛组委会提供的规范，确定创意设计的主题，针对互联网技术特点，围绕互联网应用的开发，围绕互联网应用场景进行研究和设计，编制创意设计方案，完成设计与开发。并按照大赛组委会的要求提交作品，参赛作品的内容包含作品简介、软件创意设计文档、云端作品部署、软件项目源码、视频短片等。',
         },
        ]
      }
    }
  }
</script>