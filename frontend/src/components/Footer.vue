<template>
  <footer>
     <p>© Shamyrat Babanazarow</p>
     <a href="#">Обратный связь</a>
     <a href="#">Помочь</a>
     <a href="#">Лицензионное соглашение</a>
  </footer>
</template>
<script>
export default{
  name: 'footer1'
}
</script>
<style>
footer {
  text-align: center;
  border: 2px solid black;
  border-radius: 5px;
  padding: 5px;
  display: flex;
  justify-content: space-around;
  align-items: center;
  background-color: white;
}
footer a {
  display: inline-block;
  font-size: 12px;
  color:  grey;
}
</style>
