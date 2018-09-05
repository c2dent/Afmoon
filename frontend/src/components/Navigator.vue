<template>
  <section id="nav">
    <form>
      <select name="region" id="region" placeholder="men">
        <option value="" v-for="region in regions" :key="region.id">{{ region.name }}</option>
      </select>
      <select name="categories" id="categories">
        <option value="" v-for="category in categories" :key="category.id">{{ category.name }}</option>
      </select>
      <button>Искать</button>
    </form>
  </section>
</template>
<script>
// eslint-disable-next-line
/* eslint-disable */
import {mapGetters} from 'vuex'
export default {
  name: 'navigation',
  computed: {
    regions () {
      return this.$store.getters.regions
    },
    categories () {
      return this.$store.getters.categories
    }
  },
  beforeMount () {
    this.$store.dispatch('region',).then(() => {
      console.log('All OK ')
    })
    this.$store.dispatch('category',).then(() => {
      console.log('All OK ')
    })
  }
}
</script>
<style>
#nav {
  border: 2px solid black;
  border-radius: 5px;
  margin:  5px 0px;
  padding: 5px;
  display: flex;
  background-color: white;
  align-content: center;
  justify-content: center
}
</style>