<template>
  <header>
    <div id="logo">
      <a href="http://localhost:8080/#/turkmenistan/"><img src="../assets/greenLogo.png" alt="Logo"><h2>AFMOON</h2></a>
    </div>
    <div id="search">
      <form>
        <input type="search" placeholder="Поиск по имени товара" class="search">
        <button type="submit">Искать</button>
      </form>
    </div>
    <div class="user_profile" v-if="authorization">
      <a href="http://localhost:8080/#/profile/">
        <section id="user_avatar">
          <img :src="'http://127.0.0.1:8000' + profile.avatar">
        </section>
        <section id="user_nickname">
          <h4>{{ profile.nickname }}</h4>
        </section>
      </a>
    </div>
    <div id="auth" v-else>
      <button type="button" id="regis" @click="show_registration()">Регистрация</button>
      <registration :registrationOpened="registrationOpened" @close="closeModalRegistration" @OpenedValidate="show_validate"></registration>
      <button type="button" @click="show_login()">Вход</button>
      <login :loginOpened="loginOpened" @close="closeModalLogin"></login>
      <validate :validateOpened="validateOpened" @close="closeModalValidate"></validate>
    </div>
  </header>
</template>
<script>
import login from './Login.vue'
import registration from './Registration.vue'
import validate from './Validate.vue'
// eslint-disable-next-line
/* eslint-disable */
import {mapGetters} from 'vuex'
export default{
  name: 'header1',
  components: {
    login,
    registration,
    validate,
  },
  computed: {
    status () {
        return  this.$store.getters.authStatus
      },
      profile () {
        return this.$store.getters.profile
      }
  },
  data () {
    return {
      loginOpened : false,
      registrationOpened : false,
      validateOpened : false,
      authorization : false,
    }
  },
  methods: {
    show_login () {
        this.loginOpened = true;
    },
    closeModalLogin () {
      this.loginOpened = false;
    },
    show_registration () {
        this.registrationOpened = true;
    },
    closeModalRegistration () {
      this.registrationOpened = false;
    },
    show_validate () {
      this.registrationOpened = false;
      this.validateOpened = true;
    },
    closeModalValidate () {
      this.validateOpened = false;
    }
  },
  beforeMount () {
    const token = localStorage.getItem('user-token')
    if (token) {
      this.$store.dispatch('getOwner',)
      this.authorization = true
    }
  }
}
</script>
<style>
login {
  position: absolute;
}
#logo {
  flex-grow: 1;
}
#logo h2{
  display: inline-block;
}
#logo img{
  width: 30px;
  height: 30px;
  max-width: 100%;
  max-height: 100%;
  border: 0px solid white;
  border-radius: 4px;
}
#search {
  flex-grow: 3;
}
#auth{
  flex-grow: 1;
}
header {
  border: 2px solid black;
  border-radius: 5px;
  display: flex;
  padding: 7px;
  background-color: white;
  justify-content: center;
  align-items: center;
  max-height: 70px;
  flex-flow: row nowrap;
}
.search {
  width: 80%;
  padding: 7px;
  font-size: 15px;

}
#regis{
  margin-right: 5px;
}
.user_profile {
  margin-right: 20px;
}
.user_profile a {
  display: flex;
  align-items: center;
}
#user_avatar img{
  width: 40px;
  height: 40px;
  border-radius: 50%;
  padding: 2px;
}
</style>