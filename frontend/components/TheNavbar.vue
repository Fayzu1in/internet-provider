<template lang="pug">
nav.Navbar(:class='{stuck}')
  .Navbar__container
    NuxtLink.Navbar__left(to='/') 
      img.logo(src='@/static/logo-full.svg')
    .Navbar__mobile
      button.burgerMenu(@click='mobileNav = true')
        MaterialIcon(:icon='mdiMenu')
    transition-group(name='fade')
      .mobileNavbar(v-if="mobileNav" key='dynamic' class='animated')  
        button.mobileNavbar__btnClose(@click='mobileNav = false') 
          MaterialIcon(:icon='mdiClose')
        NuxtLink.mobileNavbar__link(to="/")
          p Главная 
          MaterialIcon.icon(:icon='mdiHome')
        NuxtLink.mobileNavbar__link(to="/providers")  
          p Провайдеры
          MaterialIcon.icon(:icon='mdiWeb')
        NuxtLink.mobileNavbar__link(to="/news")  
          p Новости
          MaterialIcon.icon(:icon='mdiNewspaperVariantOutline')
        NuxtLink.mobileNavbar__link(to="/speedtest")  
          p Тест скорости интернета
          MaterialIcon.icon(:icon='mdiSpeedometer')  
        a.mobileNavbar__link(href='https://telegram.me/InternetBor') 
          p Техническая поддержка
          MaterialIcon.icon(:icon='mdiFaceAgent')

    .Navbar__right
      NuxtLink.Navbar__link(to="/providers")  Провайдеры
      NuxtLink.Navbar__link(to="/news")  Новости
      NuxtLink.Navbar__link(to="/speedtest")  Тест скорости интернета
      a.Navbar__link(href='https://telegram.me/InternetBor') Техническая поддержка

        
      


</template>
<script>
import {
  mdiPhone,
  mdiMenu,
  mdiHome,
  mdiWeb,
  mdiNewspaperVariantOutline,
  mdiSpeedometer,
  mdiClose,
  mdiFaceAgent,
} from '@mdi/js'

export default {
  data() {
    return {
      mdiPhone,
      mdiMenu,
      mdiHome,
      mdiWeb,
      mdiNewspaperVariantOutline,
      mdiSpeedometer,
      mdiClose,
      mdiFaceAgent,
      stuck: false,
      mobileNav: false,
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
<style lang="scss" scoped>
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
  a.nuxt-link-exact-active {
    font-weight: bold;
  }
  &__container {
    display: flex;
    align-items: center;
    justify-content: space-between;
    max-width: 1200px;
    width: 100%;
    margin: 0 auto;
    // padding-left: 20px;
    // padding-right: 20px;
    @media only screen and (max-width: 420px) {
      padding: 0 20px;
    }
  }

  &__center {
    display: flex;
    // @media only screen and (max-width: 420px) {
    //   display: none;
    // }
  }
  &__left {
    display: flex;
    text-decoration: none;
    color: #fff;
    .logo {
      height: 45px;
      @media only screen and (max-width: 420px) {
        height: 30px;
      }
    }
  }
  &__right {
    display: flex;
    align-items: center;
    &-call {
      display: flex;
      align-items: center;
      text-decoration: none;
      color: #fff;
      margin-left: 30px;
    }
    p {
      margin-right: 7px;
    }
    @media only screen and (max-width: 420px) {
      display: none;
    }
  }
  &__link {
    display: inline-block;
    align-items: center;
    text-decoration: none;
    margin-left: 25px;
    color: #fff;
    transition: color 0.3s;
    line-height: 1.5;

    &::after {
      content: '';
      display: block;
      width: 0;
      height: 2px;
      background: #fff;
      transition: width 0.3s;
    }
    &:hover::after {
      width: 100%;
      transition: width 0.3s;
    }
  }
  &__mobile {
    display: none;
    // position: absolute;
    @media only screen and (max-width: 420px) {
      display: block;
    }
  }
}
.burgerMenu {
  background: none;
  border: none;
  position: absolute;
  top: 18px;
  right: 11px;
}
.stuck {
  background: #000;
}
.mobileNavbar {
  background: #000;
  position: absolute;
  // border-bottom: 2px solid #fdb931;
  top: 0;
  left: 0;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  width: 100%;
  padding: 18px 20px 20px 20px;
  padding-bottom: 50px;

  &__link {
    color: #fff;
    text-decoration: none;
    display: flex;
    align-items: center;
    margin-bottom: 15px;
    p {
      padding-right: 5px;
      // line-height: 0.5;
      margin: 0;
    }
    .icon {
      height: 25px;
    }
  }
  &__btnClose {
    position: absolute;
    top: 18px;
    right: 11px;
    border: none;
    background: none;
  }
  a.nuxt-link-exact-active {
    border-bottom: 1px solid #fff;
  }
}
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.5s;
}

.fade-enter,
.fade-leave-active {
  opacity: 0;
}
</style>
