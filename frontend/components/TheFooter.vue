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
        p.logoText InternetBor
        
        p.copyright 2023
      .footer__right 
        a.feetback(href="https://t.me/InternetBor") 
          img.feetback__image(src='/telegram.svg')
          p {{ $t('feedback') }}
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
  margin-left: -7px;
  margin-right: -7px;
  margin-bottom: -10px;
  margin-top: 30px;
  @media only screen and (max-width: 431px) {
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
  @media only screen and (max-width: 431px) {
    flex-direction: column;
    justify-content: center;
    align-items: center;
    padding-left: 20px;
    padding-right: 20px;
    padding-bottom: 20px;
    padding-top: 20px;
    font-size: 16px;
  }
  a {
    text-decoration: none;
    color: #fff;
    cursor: pointer;
  }

  &__center {
    margin: 0;
    display: flex;
    align-items: center;
    margin-right: 10px;
    p {
      margin: 0;
    }
    @media only screen and (max-width: 431px) {
      margin-right: 0;
      padding-bottom: 10px;
    }
    .copyright {
      padding-right: 5px;
      color: rgb(193, 191, 191);
      padding-left: 5px;
    }
  }
  &__right {
    display: flex;
    .feetback {
      display: flex;
      align-items: center;
      transition: color 0.3s;
      &:hover {
        color: #eba026;
      }

      &__image {
        height: 25px;
        margin-left: 10px;
        margin-right: 10px;
        @media only screen and (max-width: 431px) {
          margin-left: 0;
        }
      }
      p {
        margin: 0;
      }
    }
  }
}
</style>
