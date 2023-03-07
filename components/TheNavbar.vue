<template lang="pug">
nav.Navbar(:class='{stuck}')
  .Navbar__container
    .Navbar__left LOGO
    .Navbar__center
      NuxtLink.Navbar__link(to="/providers")  Провайдеры
      NuxtLink.Navbar__link(to="/news")  Новости
      NuxtLink.Navbar__link(to="/speedtest")  Тест скорости интернета
    .Navbar__right
      a.Navbar__link(href='tel:998909113086')  
        p Позвонить
        MaterialIcon(:icon='mdiPhone', size='1.5rem', color='#fff')

</template>
<script>
import { mdiPhone } from '@mdi/js'

export default {
  data() {
    return {
      mdiPhone,
      stuck: false,
    }
  },
  mounted() {
    window.document.onscroll = () => {
      const navBar = document.querySelector('.Navbar')
      if (window.scrollY > navBar.offsetTop) {
        this.stuck = true
      } else {
        this.stuck = false
      }
    }
  },

  methods: {},
}
</script>
<style lang="scss">
.Navbar {
  position: fixed;
  z-index: 999;
  top: 0;
  left: 0;
  width: 100%;
  height: 70px;
  display: flex;
  align-items: center;
  font-size: 18px;
  transition: background 0.3s;

  &__container {
    display: flex;
    align-items: center;
    justify-content: space-between;
    width: 1200px;
    margin: 0 auto;
  }

  &__center {
    display: flex;
  }
  &__right {
    p {
      margin-right: 7px;
    }
  }
  &__link {
    display: flex;
    align-items: center;
    text-decoration: none;
    margin-left: 25px;
    color: #fff;
    transition: color 0.3s;
  }
}
.stuck {
  background: #000;
}
</style>
