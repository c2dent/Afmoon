<template>
  <transition>
    <div class="modal_wrap" v-if="validateOpened">
      <div class="modal_background" @click="closeModalValidate"></div>
      <div class="modal_content">
        <h1>Потверждение номера</h1>
        <form action="validate">
          <input type="text" placeholder="111-111" class="code_validate" v-model="code_validate" required >
          <button class="validate" type="submit">Потвердить</button><br>
        </form>
      </div>
    </div>
  </transition>
</template>
<script>
// eslint-disable-next-line
/* eslint-disable */
export default {
  name: 'validate',
  props: {
    validateOpened : {
      type : Boolean,
    }
  },
  methods: {
    closeModalValidate () {
      this.$emit('close')
    },

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
.validate{
  font-size: 22px;
  padding: 8px 80px;
  margin: 20px 0px;
}
.validate:hover{
  padding: 7px 80px;
}
.modal_content a{
  display: inline-block;
  color: grey;
}
</style>