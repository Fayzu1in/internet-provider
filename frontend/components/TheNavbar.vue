<template lang="pug">
nav.Navbar(:class='{stuck}')
  .Navbar__container
    NuxtLink.Navbar__left(:to='localePath("/")') 
      img.logo(src='@/static/logo-full.svg')
    .mobilePhone
      a(href='tel:+998781137071') 
        MaterialIcon(:icon='mdiPhone' size='25px' color='#eba026')
        p 78 113 70 71
    .mobileLang 
      .globus(@click='globusLang = !globusLang')
        MaterialIcon(:icon='mdiWeb' size='25px')
        
        .languages(v-if='globusLang')
          a.lang(
          :href='switchLocalePath("uz")',
          :class='{ active: $i18n.locale === "uz" }'
          ) O'Z
          a.lang(
          :href='switchLocalePath("ru")',
          :class='{ active: $i18n.locale === "ru" }'
          ) РУ

          a.lang(
          :href='switchLocalePath("en")',
          :class='{ active: $i18n.locale === "en" }'
          ) EN


    .Navbar__mobile
      button.burgerMenu(@click='mobileNav = true')
        MaterialIcon(:icon='mdiMenu')
    transition-group(name='fade')
      .mobileNavbar(v-if="mobileNav" key='dynamic' class='animated')  
        button.mobileNavbar__btnClose(@click='mobileNav = false') 
          MaterialIcon(:icon='mdiClose')
        NuxtLink.mobileNavbar__link(:to='localePath("/")')
          p(@click='mobileNav = false') {{ $t('homePage') }} 
          //- MaterialIcon.icon(:icon='mdiHome')
        NuxtLink.mobileNavbar__link(:to='localePath("/providers")')  
          p(@click='mobileNav = false') {{ $t('providers') }}
          //- MaterialIcon.icon(:icon='mdiWeb')
        a.mobileNavbar__link(href="https://t.me/InternetBorNews")  
          p(@click='mobileNav = false') {{ $t('news') }}
          //- MaterialIcon.icon(:icon='mdiNewspaperVariantOutline')
        NuxtLink.mobileNavbar__link(:to='localePath("/speedtest")')  
          p(@click='mobileNav = false') {{ $t('speedtest') }}
          //- MaterialIcon.icon(:icon='mdiSpeedometer')  
        a.mobileNavbar__link(href='https://telegram.me/InternetBor') 
          p {{ $t('support') }}
          //- MaterialIcon.icon(:icon='mdiFaceAgent')

    .Navbar__right
      NuxtLink.Navbar__link(:to='localePath("/providers")')  {{ $t('providers') }}
      a.Navbar__link(href="https://t.me/InternetBorNews")  {{ $t('news') }}
      NuxtLink.Navbar__link(:to='localePath("/speedtest")')   {{ $t('speedtest') }}
      a.Navbar__link.navbarPhone(href='tel:+998781137071') 
        MaterialIcon(:icon='mdiPhone')
        p 78 113 70 71
      .languages 
      
        a.lang(
          :href='switchLocalePath("uz")',
          :class='{ active: $i18n.locale === "uz" }'
        ) O'Z
        a.lang(
          :href='switchLocalePath("ru")',
          :class='{ active: $i18n.locale === "ru" }'
        ) РУ

        a.lang(
          :href='switchLocalePath("en")',
          :class='{ active: $i18n.locale === "en" }'
        ) EN

        
      


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
      globusLang: false,
    }
  },
  mounted() {
    console.log(this.$i18n.locale)
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
  z-index: 1000;
  top: 0;
  left: 0;
  width: 100%;
  height: 70px;
  display: flex;
  align-items: center;
  font-size: 18px;
  transition: background 0.3s;
  padding: 0 20px;
  @media only screen and (max-width: 431px) {
    padding: 0 10px;
  }
  a.nuxt-link-exact-active {
    color: #eba026;
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
    @media only screen and (max-width: 431px) {
      padding: 0;
    }
  }

  &__center {
    display: flex;
    // @media only screen and (max-width: 431px) {
    //   display: none;
    // }
  }
  &__left {
    display: flex;
    text-decoration: none;
    color: #fff;
    .logo {
      height: 45px;
      @media only screen and (max-width: 431px) {
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
    @media only screen and (max-width: 431px) {
      display: none;
    }
    .languages {
      border-left: 1px solid #fff;
      margin-left: 10px;

      a.lang {
        color: #fff;
        text-decoration: none;
        margin-left: 10px;
        transition: color 0.3s;
        &:hover {
          color: #eba026;
        }
        &.active {
          color: #eba026;
        }
      }
    }
    .navbarPhone {
      display: flex;
      align-items: center;
      color: #eba026;
      font-weight: bold;
      p {
        margin-left: 5px;
      }
      .MaterialIcon {
        :deep(path) {
          transition: all 0.3s;
          fill: #eba026;
        }
      }
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

    &:hover {
      color: #eba026;
      .MaterialIcon {
        :deep(path) {
          fill: #eba026;
        }
      }
    }

    // &::after {
    //   content: '';
    //   display: block;
    //   width: 0;
    //   height: 2px;
    //   background: #fff;
    //   transition: width 0.3s;
    // }
    // &:hover::after {
    //   width: 100%;
    //   transition: width 0.3s;
    // }
  }
  .mobilePhone {
    display: none;
    @media only screen and (max-width: 431px) {
      display: flex;
    }
    a {
      display: flex;
      align-items: center;
      text-decoration: none;
      color: #eba026;
      font-weight: bold;
      p {
        margin-left: 5px;
      }
    }
  }
  .mobileLang {
    display: none;

    @media only screen and (max-width: 431px) {
      display: flex;
      align-items: center;
      .languages {
        background: #000;
        display: flex;
        flex-direction: column;
        position: absolute;
        top: 30px;
        left: -10px;
        padding: 5px;
        .lang {
          margin-bottom: 10px;
          margin-left: 6px;
          margin-right: 6px;
          text-decoration: none;
          color: #fff;
          font-size: 20px;
          @media only screen and (max-width: 431px) {
            &:active {
              color: #eba026;
            }
          }
          &.active {
            color: #eba026;
          }
        }
      }
    }
    .globus {
      position: relative;
    }
  }

  &__mobile {
    display: none;
    // position: absolute;
    @media only screen and (max-width: 431px) {
      display: block;
    }
  }
}
.burgerMenu {
  background: none;
  border: none;
  position: absolute;
  top: 15px;
  right: 10px;
  padding: 0;
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
  border-bottom-left-radius: 10px;
  border-bottom-right-radius: 10px;

  &__link {
    color: #fff;
    text-decoration: none;
    display: flex;
    align-items: center;
    margin-bottom: 15px;
    /* stylelint-disable-next-line no-descending-specificity */
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
    top: 15px;
    right: 0px;
    border: none;
    background: none;
  }
  // a.nuxt-link-exact-active {
  //   border-bottom: 1px solid #fff;
  // }
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
