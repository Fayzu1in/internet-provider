<template lang="pug">
nav.Navbar(:class='{stuck}')
  .Navbar__container
    NuxtLink.Navbar__left(:to='localePath("/")') 
      img.logo(src='/new_logo.svg')
    .mobilePhone(@click='callCatcher') 
      div
       img(src='/phone.png')
       span 78 113 70 71 
    .mobileLang 
      .globus(@click='globusLang = !globusLang')
        MaterialIcon(:icon='mdiWeb' size='25px')
        
        .languages(v-if='globusLang')
          a.lang(
          v-if='this.$i18n.locale !== "uz"'
          :href='switchLocalePath("uz")',
          :class='{ active: $i18n.locale === "uz" }'
          ) O'Z
          a.lang(
            v-if='this.$i18n.locale !== "ru"'
          :href='switchLocalePath("ru")',
          :class='{ active: $i18n.locale === "ru" }'
          ) РУ

          a.lang(
            v-if='this.$i18n.locale !== "en"'
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
        NuxtLink.mobileNavbar__link(:to='localePath("/providers")')  
          p(@click='mobileNav = false') {{ $t('providers') }}
        a.mobileNavbar__link(href="https://t.me/InternetBorNews")  
          p(@click='mobileNav = false') {{ $t('news') }}
        NuxtLink.mobileNavbar__link(:to='localePath("/speedtest")')  
          p(@click='mobileNav = false') {{ $t('speedtest') }}
        span.mobileNavbar__link(@click='redirectToTelegram') 
          p {{ $t('support') }}

    .Navbar__right
      NuxtLink.Navbar__link(:to='localePath("/providers")')  {{ $t('providers') }}
      a.Navbar__link(href="https://t.me/InternetBorNews")  {{ $t('news') }}
      NuxtLink.Navbar__link(:to='localePath("/speedtest")')   {{ $t('speedtest') }}
      .Navbar__link.navbarPhone(@click='callCatcher') 
        img(src='/phone.png')
        span 78 113 70 71 
      .languages 
        img.verticalLine(src='/vertical-line.png')
        a.lang(
          v-if='this.$i18n.locale !== "uz"'
          :href='switchLocalePath("uz")',
          :class='{ active: $i18n.locale === "uz" }'
        ) O'Z
        a.lang(
          v-if='this.$i18n.locale !== "ru"'
          :href='switchLocalePath("ru")',
          :class='{ active: $i18n.locale === "ru" }'
        ) РУ

        a.lang(
          v-if='this.$i18n.locale !== "en"'
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
    window.document.onscroll = () => {
      const navBar = document.querySelector('.Navbar')
      if (window.scrollY > navBar.offsetTop) {
        this.stuck = true
      } else {
        this.stuck = false
      }
    }
  },
  methods: {
    async redirectToTelegram() {
      try {
        await this.$api.clickCatcher('telegram')
      } catch (error) {
        console.error('Error occured', error)
      } finally {
        window.open('https://telegram.me/InternetBor', '_blank')
      }
    },
    async callCatcher() {
      try {
        await this.$api.clickCatcher('phone call')
      } catch (error) {
        console.error('Error occured', error)
      } finally {
        const phoneNumber = '+998781137071'
        window.location.href = `tel:${phoneNumber}`
      }
    },
  },
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
  padding: 0 100px;
  @media only screen and (max-width: 431px) {
    padding: 0 10px;
  }
  a.nuxt-link-exact-active {
    color: #56c1ff;
  }
  &__container {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin: 0 auto;
  }

  &__center {
    display: flex;
  }
  &__left {
    display: flex;
    text-decoration: none;
    color: #fff;
    .logo {
      height: 25px;
      @media only screen and (max-width: 431px) {
        height: 15px;
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
      // margin-left: 10px;
      display: flex;
      align-items: center;
      .verticalLine {
        height: 35px;
      }

      a.lang {
        color: #56c1ff;
        text-decoration: none;
        margin-left: 10px;
        transition: color 0.3s;
        &:hover {
          color: #eba026;
        }
        &.active {
          color: #fff;
        }
      }
    }
    .navbarPhone {
      display: flex;
      align-items: center;
      color: #56c1ff;
      font-weight: bold;
      cursor: pointer;
      img {
        height: 35px;
      }
      p {
        margin-left: 5px;
      }
      // .MaterialIcon {
      //   :deep(path) {
      //     transition: all 0.3s;
      //     fill: #eba026;
      //   }
      // }
    }
  }

  &__link {
    display: inline-block;
    align-items: center;
    text-decoration: none;
    margin-left: 25px;
    color: #56c1ff;
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
      text-decoration: none;
    }
    div {
      display: flex;
      align-items: center;
      text-decoration: none;
      color: #56c1ff;
      font-weight: bold;
      p {
        margin-left: 5px;
      }
      img {
        height: 30px;
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
  background: #02234c;
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
