<template lang="pug">
#app
  NewNavbar
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
  methods: {
    async redirectToTelegram() {
      try {
        await this.$api.clickCatcher('telegram')
      } catch (error) {
        this.$error('Error occured', error)
      } finally {
        window.open('https://telegram.me/InternetBor', '_blank')
      }
    },
  },
}
</script>
<style lang="scss">
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  width: 100%;
}
a {
  text-decoration: none;
}
html {
  font-family: 'Poppins', sans-serif;

  // background: linear-gradient(to right, #d7d2cc 0%, #304352 100%);
  color: #fff;
  ::-webkit-scrollbar {
    width: 7px;
    border-radius: 15px;
  }

  /* Track */
  ::-webkit-scrollbar-track {
    background: #0b2249;
    border-radius: 15px;
  }
  ::-webkit-scrollbar-thumb {
    background: #008de5;
    border-radius: 15px;
    // border-radius: 5px;
  }

  /* Handle on hover */
  ::-webkit-scrollbar-thumb:hover {
    background: #006caf;
  }
}
body {
  background-color: rgb(124, 213, 230);
}

.container-fluid {
  display: flex;
  justify-content: center;
  max-width: 1280px;
  width: 100%;
  padding-left: 100px;
  padding-right: 100px;
  margin: 0 auto;
  @media only screen and (max-width: 431px) {
    padding-left: 20px;
    padding-right: 20px;
  }
}
.wrapper {
  min-height: 88vh;
}
.telegramGif {
  position: fixed;
  bottom: 1rem;
  right: 1rem;
  height: 60px;
  background: none;
  cursor: pointer;
}
</style>
