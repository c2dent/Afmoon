<template>
  <div>
    <ul>
      <!-- <li v-for="region in regions" :key="region.id"> -->
      <li >
        {{ regions }}
      </li>
    </ul>
  </div>
</template>

<script>
// eslint-disable-next-line
/* eslint-disable */
import { mapGetters } from 'vuex'
import axios from 'axios'

export default {
  name: 'AdList',
  computed: mapGetters(['regions']),
  data: function () {
    return {
    title : '' ,
    description : ''
    }
  },
  methods: {
    createAd () {
      this.$store.dispatch('createAds', {title:this.title, description:this.description})
    },
    createAdss () {
        axios.post('http://127.0.0.1:8000/turkmenistan/ad/', {
          title: this.title,
          description: this.description
        })
        .then(response => console.log(response))
        .catch(error => console.log(error));
    }
  },
  beforeMount () {
    // Перед тем как загрузить страницу, нам нужно получить список всех
    // имеющихся заметок. Для этого мы вызываем действие `getNotes` из
    // нашего хранилища
    this.$store.dispatch('getRegs')
  }
}

// eslint-disable-next-line
/* eslint-disable */
</script>
<style>
</style>