  <template>
  <transition>
    <div class="modal_wrap" v-if="registrationOpened">
      <div class="modal_background" @click="closeModalRegistration"></div>
      <div class="modal_content">
        <h1>Регистрация</h1>
        <form @submit.prevent ="CloseRegisAndCallModalValidate">
          <input type="text" placeholder="Имя" class="nickname" required v-model="user_data.nickname">
          <input type="tel" placeholder="номер телефона" class="number" required v-model="user_data.phone_number">
          <input type="password" placeholder="Пароль" class="password1" required v-model="user_data.password1">
          <input type="password" placeholder="Потвеждения пароля" class="password2" required v-model="user_data.password2">
          <button class="registration" type="submit">Регистрация</button><br>
        </form>
      </div>
    </div>
  </transition>
</template>
<script>
// eslint-disable-next-line
/* eslint-disable */
export default {
  name: 'registration',
  props: {
    registrationOpened : {
      type : Boolean,
    }
  },
  data () {
    return {
        user_data: {
          nickname: '',
          phone_number: '',
          password1: '',
          password2: ''
      }
    }
  },
  methods: {
    closeModalRegistration () {
      this.$emit('close')
    },
    CloseRegisAndCallModalValidate () {
      this.$store.dispatch('create_user', this.user_data).then(resp => {
        this.$emit('OpenedValidate')
      })
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
.registration{
  font-size: 22px;
  padding: 8px 80px;
  margin: 20px 0px;
}
.registration:hover{
  padding: 7px 80px;
}
.modal_content a{
  display: inline-block;
  color: grey;
}
</style>