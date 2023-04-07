<template lang="pug">
#app
  TheNavbar
  HeroBackground
  Nuxt.wrapper
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
  // background: linear-gradient(to right, #d7d2cc 0%, #304352 100%);
  color: #fff;
}
#app {
}
.container-fluid {
  max-width: 1200px;
  width: 100%;
  margin: 0 auto;
  @media only screen and (max-width: 420px) {
    padding-left: 20px;
    padding-right: 20px;
  }
}
.wrapper {
  min-height: 83vh;
}
</style>
