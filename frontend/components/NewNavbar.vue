<template lang="pug">
nav.Navbar(:class='{stuck}')
  .Navbar__container
    .Navbar__top.container-fluid
      .Navbar__top-lists
        NuxtLink.list(:to='localePath("/")', style="padding-bottom: 12px;")
          img.logo(src='/new_logo.svg')
        NuxtLink.list(:to='localePath("/providers")') {{ $t('providers') }}
        a.list(href="https://t.me/InternetBorNews") {{ $t('news') }}
        NuxtLink.list(:to='localePath("/speedtest")') Speed test
        .list.langs
          a.lang(
          :href='switchLocalePath("ru")',
          :class='{ active: $i18n.locale === "ru" }'
          ) РУ
          a.lang(
          :href='switchLocalePath("en")',
          :class='{ active: $i18n.locale === "en" }'
          ) EN
          a.lang(
          :href='switchLocalePath("uz")',
          :class='{ active: $i18n.locale === "uz" }'
          ) O'Z
      .Navbar__mobile
        NuxtLink.list(:to='localePath("/")', style="padding-bottom: 12px;")
          img.MobileLogo(src='/new_logo.svg')
        .burgerMenu
          MaterialIcon(:icon='mdiMenu')
</template>
<script>
import { mdiMenu } from '@mdi/js'
export default {
  data() {
    return {
      stuck: false,
      mdiMenu,
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
}
</script>
<style lang="scss" scoped>
.stuck {
  box-shadow: rgba(50, 50, 93, 0.25) 0px 13px 27px -5px,
    rgba(0, 0, 0, 0.3) 0px 8px 16px -8px;
}
.Navbar {
  width: 100%;
  background-color: rgb(124, 213, 230);
  position: fixed;
  z-index: 1000;
  border-bottom-left-radius: 15px;
  border-bottom-right-radius: 15px;
  transition: all 0.3s;

  &__container {
    padding-top: 45px;
    @media only screen and (max-width: 576px) {
      padding-top: 20px;
    }
  }
  &__top {
    padding-bottom: 39px;
    @media only screen and (max-width: 576px) {
      padding-bottom: 20px;
    }
    .logo {
      width: 149px;
      height: 25px;
    }
    &-lists {
      display: flex;
      justify-content: space-between;
      align-items: center;
      text-align: center;
      width: 100%;
      @media only screen and (max-width: 576px) {
        display: none;
      }
      .list {
        color: #fff;
        white-space: nowrap;
        transition: color 0.3s;
        &:hover {
          text-decoration: none;
          color: #3f62a7;
        }
      }
      a {
        width: fit-content;
      }
      .langs {
        gap: 5px;
        display: flex;

        width: auto;
        a {
          color: #fff;
          text-decoration: none;
        }
      }
    }
  }
  &__mobile {
    display: none;
    @media only screen and (max-width: 576px) {
      display: flex;
      justify-content: space-between;
    }
    .list {
      width: auto;
    }
    .burgerMenu {
      width: auto;
    }
    .MobileLogo {
      width: 149px;
      height: 25px;
    }
  }
  &__bottom {
    width: 100%;
    padding-bottom: 10px;
  }
  .active {
    color: #3f62a7 !important;
    font-weight: bold !important;
  }
}
</style>
