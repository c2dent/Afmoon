<template>
  <section>
    <h1>Page PROFILE</h1>
    <div id="profile">
      <ul id="owner">
        <li class="Nickname">
          df
        </li>
        <li class="phoneNumber">
          dscd
        </li>
        <li class="password">
          sdc
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
      return this.$store.getters.owner
    }
  },
  beforeMount () {
    this.$store.dispatch('getOwner',)
  }
}
</script>
<style>
section {
  background-color: white;
  border: 2px solid black;
  border-radius: 5px;
  margin:  6px 0px ;
}
#owner {
  background-color: #EEE7E7;
  border-radius: 6px;
  margin: 10px 20px;
}
li {
  list-style-type: none;
}
</style>