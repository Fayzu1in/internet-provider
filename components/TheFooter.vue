<template lang="pug">
section.theFooter
  hr.hrLine
  .container-fluid
    .footer 
      .footer__left 
        .socialNetwork
          p  Социальные сети
          a(href="//www.instagram.com" target="_blank" rel='noopener noreferrer') 
            MaterialIcon(:icon='mdiInstagram')
          a(href="//www.instagram.com" target="_blank" rel='noopener noreferrer') 
            MaterialIcon(:icon='mdiFacebook')
          a(href="//www.instagram.com" target="_blank" rel='noopener noreferrer') 
            MaterialIcon(:icon='mdiYoutube')
        .news 
          NuxtLink(to="/news") Новости
      .footer__center LOGO
      .footer__right 
        a.footer__right-phone(href='tel:+998909113086' target="_blank" rel='noopener noreferrer')
          p Позвонить
          MaterialIcon(:icon='mdiPhone')

</template>
<script>
import { mdiInstagram, mdiFacebook, mdiYoutube, mdiPhone } from '@mdi/js'
export default {
  data() {
    return {
      mdiInstagram,
      mdiFacebook,
      mdiYoutube,
      mdiPhone,
    }
  },
}
</script>
<style lang="scss" scoped>
.theFooter {
  width: 100%;
  background: #000;
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
  justify-content: space-around;
  align-items: center;
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
}
</style>
