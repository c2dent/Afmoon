<template>
  <transition>
    <div class="modal_wrap" v-if="loginOpened">
      <div class="modal_background" @click="closeModalLogin"></div>
      <div class="modal_content">
        <h1>Вход</h1>
        <form action="login">
          <input type="text" placeholder="Имя пользователя" class="username">
          <input type="password" placeholder="Пароль" class="password">
          <button class="login">Вход</button><br>
          <a href="#">Забыли пароль ?</a>
        </form>
      </div>
    </div>
  </transition>
</template>
<script>
// eslint-disable-next-line
/* eslint-disable */
export default {
  name: 'login',
  props: {
    loginOpened : {
      type : Boolean,
    }
  },
  methods: {
    closeModalLogin () {
      this.$emit('close')
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