<template lang="pug">
#app
  TheNavbar
  HeroBackground
  Nuxt
  TheFooter
</template>
<script>
export default {}
</script>
<style lang="scss">
* {
  box-sizing: border-box;
}
html {
  font-family: sans-serif;
  background: #000;
  color: #fff;
}
.container-fluid {
  max-width: 1200px;
  width: 100%;
  margin: 0 auto;
}
</style>
