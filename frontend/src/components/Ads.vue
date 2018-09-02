<template>
  <div id="content">
    <ul>
      <li v-for='ad in ads' :key = 'ad.id'>
        <div class="ad">
          <div class="ad_img">
            <p>
              <img :src="'http://127.0.0.1:8000/media/' + ad.images[0]" :alt="ad.title">
            </p>
          </div>
          <div class="ad_detail">
            <a href="#">
                {{ ad.title }}
            </a>
            <br>
            <p class="price">
              <b>Цена : {{ ad.price }} TM</b>
            </p>
            <p class="region">
              <b>Место : </b>{{ ad.region }}
            </p>
            <p>
              {{ ad.date_create }}
            </p>
          </div>
        </div>
      </li>
    </ul>
    <div class="reklama">
    </div>
  </div>
</template>

<script>
// eslint-disable-next-line
/* eslint-disable */
import axios from 'axios'

import {mapGetters} from 'vuex'
  export default {
    name: 'ad',
    computed : {
      ads () {
        return  this.$store.getters.ads
      },
      status () {
        return  this.$store.getters.status
      },
      region () {
        return this.$route.params.region
      }
    },
    methods : {
  
    },
    beforeMount () {
      this.$store.dispatch('getAds', [this.$route.params.region, this.$route.params.category, this.$route.params.id])
    },
  }
</script>
<style>
#content ul {
  max-width: 750px;
  padding: 0px;
}
#content li {
  padding: 5px;
  list-style-type: none;
  border: 1px solid black;
  border-radius: 7px;
  background-color: white;
  margin-bottom: 7px;
}
.ad{
  display: flex;
  display: -webkit-box;
  display: -moz-box;
  display: -ms-flexbox;
  display: -webkit-flex;
  flex-flow: row nowrap;
  align-items: center;
}
.ad .ad_img{
  height: 160px;
  width: 150px;
  flex-basis: 220px;
  display: flex;
}

 .ad .ad_img p {
  margin: 0px;
  padding: 0px;
  display: inline-block;
}
.ad .ad_detail {
  text-align: left;
  flex-grow: 1;
  padding: 0px 15px;
}
.ad .ad_detail p {
  margin: 5px 0px;
}
.price {
  border: 1px solid black;
  border-radius: 5px;
  display: inline-block;
  padding: 3px;
}
</style>