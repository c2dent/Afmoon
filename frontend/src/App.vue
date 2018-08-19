<template>
  <div id="app">
    <header1></header1>
    <router-view/>
    <footer1></footer1>
  </div>
</template>

<script>
import header1 from './components/Header.vue'
import footer1 from './components/Footer.vue'
export default {
  name: 'App',
  components: {
    header1,
    footer1
  }
}
</script>

<style>
body{
  padding: 0px;
  margin: 0px;
  color: black;
  background-color: #F4F4F4;
}
button {
  color: white;
  background-color: #00B900;
  border: none;
  border-radius: 5px;
  padding: 8px 11px;
  font-weight: bold;
  font-size: 16px;
}
button:hover{
  color:  black;
  background-color: white;
  border: 1px solid black;
  padding: 7px 10px;
}

a{
  text-decoration: none;
  font-weight: bold;
}
a:hover {
  color: #00B900;
}
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
  max-width: 1080px;
  margin: auto;
}
img{
  max-height: 100%;
  max-width: 100%;
  border-radius: 3px;
  padding: 0px;
  margin: 0px;
}
</style>
