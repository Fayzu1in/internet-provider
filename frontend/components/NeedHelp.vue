<template lang="pug">
ModalDialog(@close='$emit("close")')
  .NeedHelpSection
    .NeedHelp
      .closeModal(@click='$emit("close")')
        MaterialIcon(:icon='mdiClose')
      .NeedHelp__top 
        p {{ $t('cantChoose') }}
      .NeedHelp__middle
        p {{ $t('contactSupportAndGetHelp') }}
        p.helpLink.phone(@click='call_button_click') 
          img(src='/phone.png')
          span +998(78)113-70-71
        span.helpLink(@click='telegram')
          img(src='/telegram.svg')
          span {{ $t('telegram') }}
      .NeedHelp__bottom
        p.title {{ $t('googToKnow') }}
        p {{ $t('providingConsultation') }}
        p {{ $t('workDaily') }}
        p {{ $t('contactTommorow') }}
</template>
<!-- (v-if="modalHelp || switc" @click='modalHelp = false, switc = false') -->
<script>
import { mdiClose } from '@mdi/js'
import axios from 'axios'
export default {
  data() {
    return {
      mdiClose,
    }
  },
  methods: {
    call_button_click() {
      const phoneNumber = '+998781137071'
      window.dataLayer = window.dataLayer || []
      window.dataLayer.push({
        event: 'phoneCallClick', // Custom event name
        phoneNumber, // Push phone number to the data layer
      })
      window.location.href = `tel:${phoneNumber}`
    },
    telegram() {
      axios
        .post('https://internetbor.uz/api/v1/click/', {
          title: 'telegram ',
        })
        .then((response) =>
          window.open('https://telegram.me/InternetBor', '_blank')
        )
    },
  },
}
</script>
<style lang="scss">
.NeedHelpSection {
  z-index: 1001;
}
.NeedHelp {
  background-color: rgba(255, 255, 255, 0.7647058824);
  color: #001b48;
  border-radius: 15px;
  position: absolute;
  left: 50%;
  top: 50%;
  transform: translate(-50%, -50%);
  padding: 15px;
  display: flex;
  flex-direction: column;
  align-items: center;
  img {
    height: 50px;
  }
  @media only screen and (max-width: 431px) {
    width: 85%;
  }
  .closeModal {
    cursor: pointer;
    position: absolute;
    top: 5px;
    right: 5px;
    border-radius: 50%;
    border: 3px solid #fff;
    z-index: 1;
    display: flex;
  }
  &__top {
    background-color: #0b2249;
    width: 100%;
    position: absolute;
    top: 0;
    left: 0;
    border-top-left-radius: 15px;
    border-top-right-radius: 15px;
    @media only screen and (max-width: 431px) {
      display: flex;
      justify-content: center;
    }
    p {
      color: #fff;
      font-size: 20px;
      text-align: center;
      @media only screen and (max-width: 431px) {
        font-size: 18px;
        width: 200px;
      }
    }
  }
  &__middle {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding-top: 50px;
    p {
      margin: 0;
      font-size: 18px;
      margin-top: 15px;
      @media only screen and (max-width: 431px) {
        display: none;
      }
    }
    .helpLink {
      text-decoration: none;
      color: #fff;
      font-size: 24px;
      padding: 5px 10px;
      border-radius: 15px;
      text-decoration: none;
      transition: all, 0.3s;
      background-color: #001b48;
      margin-top: 15px;
      display: flex;
      justify-content: center;
      width: 70%;
      cursor: pointer;
      &:hover {
        background-color: #fff;
        color: #001b48;
      }
      @media only screen and (max-width: 431px) {
        font-size: 20px;
        margin-top: 20px;
        width: 100%;
      }
      img {
        height: 30px;
        @media only screen and (max-width: 431px) {
          display: none;
        }
      }
    }
    .helpLink.phone {
      font-family: LilitaOne-Regular;
      @media only screen and (max-width: 431px) {
        margin-top: 30px;
      }
    }
  }
  &__bottom {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding-top: 15px;
    max-width: 450px;
    width: 100%;
    @media only screen and (max-width: 431px) {
      padding-top: 20px;
    }

    .title {
      font-size: 20px;
      @media only screen and (max-width: 431px) {
        font-size: 18px;
        padding-bottom: 10px;
      }
    }
    p {
      margin: 0;
      text-align: center;
      line-height: 24px;
      @media only screen and (max-width: 431px) {
        font-size: 14px;
        line-height: 18px;
      }
    }
  }
}
</style>
