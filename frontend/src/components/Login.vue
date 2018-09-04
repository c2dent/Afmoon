<template>
  <transition>
    <div class="modal_wrap" v-if="loginOpened">
      <div class="modal_background" @click="closeModalLogin"></div>
      <div class="modal_content">
        <h1>Вход</h1>
        <form @submit.prevent = "auth">
          <input type="tel" placeholder="Номер телефона" class="phone_number" v-model="user.phone_number" required>
          <input type="password" placeholder="Пароль" class="password" required v-model="user.password">
          <button class="login" type="submit">Вход</button><br>
          <a href="#">Забыли пароль ?</a>
          <p>phone : {{ user.phone_number }}</p>
          <p>password : {{ user.password }}</p>
        </form>
      </div>
    </div>
  </transition>
</template>
<script>
// eslint-disable-next-line
/* eslint-disable */
// import { mapActions } from 'vuex  '
export default {
  name: 'login',
  props: {
    loginOpened : {
      type : Boolean,
    },
  },
  data () {
    return {
     user : {
      phone_number : "",
      password : ""
     }
    }
  },
  methods: {
    // ...mapActions(['loginUser']),
    closeModalLogin () {
      this.$emit('close')
    },
    auth () {
      this.$store.dispatch('loginUser', this.user).then(() => {
        this.$router.push('/turkmenistan')
      })
      location.reload()
    },
    login () {
      this.$store.dispatch('loginer')
    }
  }
}
</script>
<style scoped>
h1{
  text-align: center;
}
.modal_wrap, .modal_background{
  position: fixed;
  left: 0px;
  top: 0px;
  width: 100%;
  height: 100%;
}
.modal_background {
   z-index: 40;
  background-color: rgba(10, 10, 10, 0.2)
}
.modal_wrap{
  display: flex;
  justify-content: center;
  align-items: center;
}
.modal_content{
  display: flex;
  flex-direction: column;
  background-color: white;
  border:  2px solid black;
  border-radius: 5px;
  padding: 60px 60px;
  z-index: 50;
}
input::placeholder {
  line-height: 18px;
}
input {
  padding: 9px;
  vertical-align: bottom;
  font-size: 18px;
  font-weight: bold;
  min-width: 350px;
  display: block;
  margin-bottom: 20px;
  border:  1px solid black;
  border-radius: 3px;
}
input:focus{
  border:  2px solid green;
  padding: 8px;
}
.login{
  font-size: 22px;
  padding: 8px 80px;
  margin: 20px 0px;
}
.login:hover{
  padding: 7px 80px;
}
.modal_content a{
  display: inline-block;
  color: grey;
}
</style>