<template lang="pug">
section.theFooter
  //- hr.hrLine
  .container-fluid
    .footer 
      //- .footer__left 
      //-   .socialNetwork
      //-     p  Социальные сети
      //-     .socialNetwork__links
      //-       a(href="//www.instagram.com" target="_blank" rel='noopener noreferrer') 
      //-         MaterialIcon(:icon='mdiInstagram')
      //-       a(href="//www.instagram.com" target="_blank" rel='noopener noreferrer') 
      //-         MaterialIcon(:icon='mdiFacebook')
      //-       a(href="//www.instagram.com" target="_blank" rel='noopener noreferrer') 
      //-         MaterialIcon(:icon='mdiYoutube')
        //- NuxtLink.news(to="/news") Новости
      .footer__center 
        p.copyright Copyright &#169 
        //- span Internetbor 
        //- img.footerLogo(src='@/static/logo-full.svg')
        p.logoText Internetbor
        
        p.copyright 2023
      //- .footer__right 
      //-   .phoneCall
      //-     a(href='tel:+998909113086'  rel='noopener noreferrer') Позвонить
      //-     MaterialIcon(:icon='mdiPhone', size='1.5rem')
      //-   NuxtLink.footer__right-phone(to='/speedtest')
      //-     p Измерить скорость интернета
      //-     MaterialIcon(:icon='mdiSpeedometerSlow', size='1.5rem')
        

</template>
<script>
import {
  mdiInstagram,
  mdiFacebook,
  mdiYoutube,
  mdiPhone,
  mdiSpeedometerSlow,
} from '@mdi/js'
export default {
  data() {
    return {
      mdiInstagram,
      mdiFacebook,
      mdiYoutube,
      mdiPhone,
      mdiSpeedometerSlow,
    }
  },
}
</script>
<style lang="scss" scoped>
.theFooter {
  // left: 0;
  border-top: 1px solid rgba(128, 128, 128, 0.417);
  background: #000;
  margin-left: -10px;
  margin-right: -10px;
  margin-bottom: -10px;
  margin-top: 50px;
  @media only screen and (max-width: 420px) {
    margin-right: -8px;
    margin-top: 0;
  }
  .hrLine {
    position: relative;
    outline: 0;
    border: 0;
    color: black;
    opacity: 0.5;
    &:before {
      content: '';
      background: linear-gradient(to right, transparent, #818078, transparent);
      position: absolute;
      left: 0;
      top: 50%;
      width: 100%;
      height: 1px;
    }
    &:after {
      content: '';
      position: relative;
      display: inline-block;
      color: black;

      padding: 0 0.5em;
      line-height: 1.5em;
      color: #818078;
      background-color: #fcfcfa;
    }
  }
}
.footer {
  display: flex;
  justify-content: center;
  align-items: center;
  line-height: 1;
  padding-bottom: 30px;
  padding-top: 20px;
  font-size: 18px;
  @media only screen and (max-width: 420px) {
    flex-direction: column;
    padding-left: 20px;
    padding-right: 20px;
    padding-bottom: 10px;
    padding-top: 10px;
    font-size: 12px;
  }
  a {
    text-decoration: none;
    color: #fff;
    cursor: pointer;
  }
  &__right {
    &-phone {
      display: flex;
      align-items: center;
    }
  }
  &__left {
    .socialNetwork {
      p {
        // padding: 20px 0;
        margin: unset;
        padding-bottom: 20px;
        color: grey;
      }
      &__links {
        // padding-bottom: 20px;
        a {
          margin-right: 10px;
        }
      }
    }
  }
  &__center {
    margin: 0;
    display: flex;
    align-items: center;
    .copyright {
      padding-right: 5px;
      color: grey;
      padding-left: 5px;
    }
    .logoText {
      @media only screen and (max-width: 420px) {
        color: #fff;
      }
    }
    .footerLogo {
      height: 40px;
      @media only screen and (max-width: 420px) {
        height: 30px;
      }
    }
    @media only screen and (max-width: 420px) {
      // display: none;
    }
  }
  &__right {
    .phoneCall {
      display: flex;
      align-items: center;
      padding-bottom: 20px;
      @media only screen and (max-width: 420px) {
        padding-top: 20px;
      }
      a {
        margin-right: 10px;
      }
    }
    &-phone {
      padding-bottom: 20px;
      p {
        margin: 0;
        margin-right: 10px;
      }
    }
  }
}
</style>
