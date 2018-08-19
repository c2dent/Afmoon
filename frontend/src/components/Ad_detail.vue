<template>
  <div id="ad">

    <div id="main_block">
      <div class="ad_detail_header">
        <p class="ad_title">{{ads.title}}</p>
        <p class="ad_price">{{ads.price}} TM</p>
        </div>
      <div id="img">
        <div class="ad_img_list">
          <p v-for="img in ads.images" :key="img" class="images">
            <img  :src="'http://127.0.0.1:8000/media/' + img" alt="" @click="image=img">
          </p>
        </div>
        <div class="main_img">
          <img :src="'http://127.0.0.1:8000/media/' + image" alt="">
          <!-- <p>image :{{  image }}</p> -->
        </div>
      </div>
      <div id="ad_description">
        <p class="description">
          {{ ads.description }}
        </p>
      </div>
    </div>
    <div id="ad_info_block">
      <div class="seller">
        <div class="seller_avatar_name">
          <p class="seller_avatar">
           <!-- -->
          </p>
          <p class="seller_name">
          <!-- -->
          </p>
        </div>
        <div class="seller_adress">
        <!-- -->
        </div>
      </div>
      <div id="ad_info">
        <p class="ad_phone_number">
          <span>Тел.номер : {{ ads.phone_number }}</span>
        </p>
        <p class="ad_adress">
          {{ ads.region }}
        </p>
        <p class="ad_category">
          {{ ads.category }}
        </p>
        <p class="ad_date_create">
          {{ ads.date_create }}
        </p>
        <p class="ad_view">
          Просмотр : {{ ads.view }}
        </p>
      </div>
    </div>
  </div>
</template>
<script>
// eslint-disable-next-line
/* eslint-disable */
import { mapGetters } from 'vuex'
export default {
  name: 'ad_detail',
  computed: mapGetters(['ads']),
  data: function ()  {
    return  {
      image : ''
    }
  },
  methods: {
  },
  beforeMount () {
      this.$store.dispatch('getAds', [this.$route.params.region, this.$route.params.category, this.$route.params.id])
    },
}

</script>
<style>
h3{
  overflow: hidden;
}
#ad{
  width: 100%;
  background-color: white;
  border-radius: 5px;
  border:  1px solid black;
  display: flex;
  margin-top: 6px;
  margin-bottom: 6px;
}
#main_block{
  max-width: 750px;
  flex-grow: 1;
  flex-direction: column;
  flex-direction: row;
}
.ad_img_list{
  display: flex;
  width: 100%;
  flex-wrap: wrap;
  border-bottom: 1px solid black;
}
#img{
  border: 1px solid black;
  border-radius: 5px;
  margin: 3px;
}
.main_img{
  margin: 3px;
  display: flex;
  justify-content: center;
  align-content: center;
  max-width: 750px;
  max-height: 550px;
  min-height: 550px;
}
.main_img img{
  max-width: 750px;
  max-height: 540px;
  margin: auto;
  padding: 10px;
}
.images{
  display: flex;
  max-height: 80px;
  max-width: 80px;
  align-self: center;
  margin: 3px;
  justify-content: end;
}
.images:hover{
  border: 2px solid green;
  border-radius: 3px;
  margin: 1px;
}
.ad_title{
  text-align: center;
  font-size: 23px;
  font-weight: bold;
  margin: 10px;
}
.ad_price{
  font-size: 23px;
  font-weight: bold;
  border: 2px solid black;
  border-radius: 5px;
  padding: 2px 8px;
  margin: 10px;
}
.ad_detail_header{
  display: flex;
  justify-content: space-between;
  margin:  0px 15px;
}
.seller{
  border: 1px solid black;
  border-radius: 5px;
  margin: 5px;
  padding: 5px;
  min-height: 160px;
}
#ad_info_block{
  display: flex;
  flex-direction: column;
  text-align: center;
  min-width: 325px;
}
.ad_phone_number {
  margin:  15px 0px;
  font-size: 20px;
  font-weight: bold;
}
.ad_phone_number span{
  display: inline-block;
  border-radius: 3px;
  border:  1px solid black;
  padding: 2px 8px;
}
#ad_description{
  border: 1px solid black;
  border-radius: 3px;
  padding: 15px;
  font-size: 16px;
  font-weight: bold;
}
</style>