<template lang="pug">
#app
  TheNavbar
  HeroBackground
  Nuxt.wrapper
  TheFooter
</template>
<script>
export default {
  head() {
    return {
      title: this.$t('browserTitle'),
    }
  },
}
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
  ::-webkit-scrollbar {
    width: 10px;
    border-radius: 5px;
  }

  /* Track */
  ::-webkit-scrollbar-track {
    background: #000;
  }
  ::-webkit-scrollbar-thumb {
    background: linear-gradient(to right, #d1b88c 0%, #ec9f1b 100%);
    // border-radius: 5px;
  }

  /* Handle on hover */
  ::-webkit-scrollbar-thumb:hover {
    background: linear-gradient(to right, #d3b47f 0%, #b17409 100%);
  }
}

.container-fluid {
  max-width: 1200px;
  width: 100%;
  margin: 0 auto;
  @media only screen and (max-width: 431px) {
    padding-left: 20px;
    padding-right: 20px;
  }
}
.wrapper {
  min-height: 83vh;
}
</style>
