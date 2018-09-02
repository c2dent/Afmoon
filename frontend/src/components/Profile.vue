<template>
  <section id="profile_wrap">
    <div id="profile_info">
      <ul id="owner">
        <li class="Nickname">
          <img :src="'http://127.0.0.1:8000' + owner.avatar" alt="">
          <h2>{{ owner.nickname }}</h2>
        </li>
        <li class="location">
          <p>Место : </p><span>{{ owner.region }}</span>
        </li>
        <li class="phoneNumber">
          <p>Телефон номер :</p><span>{{ owner.phone_number }}</span>
        </li>
        <li class="password">
          <p>Пароль :</p><button>Изменить</button>
        </li>
        <li class="logout">
          <form action="#" @submit="logout">
            <button type="submit">Выйти</button>
          </form>
        </li>
      </ul>
    </div>
    <div class="user_ads">
      <div class="switching_ads">
        <span class="ad_active active_hover" v-bind:class="{ active: is_active }" @click="active">
          Актывные
        </span>
        <span class="ad_old active_hover" v-bind:class="{ active: is_active_old }" @click="active_old">
          Не активные
        </span>
      </div>
      <ul>
        <li v-for='ad in owner.ads' :key = 'ad.id'>
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
    </div>
  </section>
</template>
<script>
// eslint-disable-next-line
/* eslint-disable */
import { mapGetters } from 'vuex'
export default {
  name: 'profile',
  computed :{
    owner () {
      return this.$store.getters.profile
    }
  },
  data () {
    return {
      is_active: true,
      is_active_old: false
    }
  },
  methods: {
    active () {
      this.is_active = true,
      this.is_active_old = false
    },
    active_old () {
      this.is_active_old = true,
      this.is_active = false
    },
    logout () {
      this.$store.dispatch('logout',).then(() => {
        this.$router.push(/turkmenistan/)
      })
    }
  },
  beforeMount () {
    this.$store.dispatch('getOwner',)
  }
}
</script>
<style>
#profile_wrap {
  background-color: white;
  border: 2px solid black;
  border-radius: 5px;
  margin:  6px 0px ;
  padding: 10px;
}
#owner {
  max-width: 800px;
  background-color: #EEE7E7;
  border-radius: 6px;
  margin: auto;
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  text-align: left;
}
#owner li {
  list-style-type: none;
  margin: 10px 15px;
}
.Nickname {
  display: flex;
  align-items: center;
}
.Nickname img {
  width: 100px;
  height: auto;
  border-radius: 50%;
  margin-right: 20px;
}
#owner li p {
  display: inline-block;
  margin-right: 15px;
}
.logout {
  text-align: center;
}
.logout button {
  background-color: #EEE7E7;
  border: 1px solid red;
  color: red;
  border-color: red;
  padding: 5px 15px;
}
.logout button:hover {
  border: 1px solid red;
  background-color: red;
  color: white;
}

.user_ads {
  max-width: 838px;
  margin:  auto;
  /* border: 2px solid black; */
  border-radius: 5px;
  margin-top: 10px;
}
.user_ads ul {
  max-width: 700px;
  margin:  auto;
  padding: 0px;
}
.switching_ads {
  display: flex;
}
.switching_ads span {
  display: inline-block;
  width: 50%;
  text-align: center;
  margin-bottom: 10px;
  border-bottom: 2px solid black;
  font-weight: bold;
  padding: 3px;
  background-color: #EEE7E7;
  /* border: 2px solid black; */
}
.ad_active {
  border-bottom-right-radius: 6px;
  border: 2px solid black;
}
.ad_old {
  border-bottom-left-radius: 6px;
  border: 2px solid black;
}
.active_hover:hover {
  color: #00B900;
  cursor: pointer;
}
.switching_ads .active {
  background-color: white;
  color: #00B900;
  border-top: 2px solid black;
  border-left: none;
  border-bottom: none;
  border-right: none;
}
.user_ads li {
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