<template lang="pug">
ModalDialog(@close='$emit("close")')
  .NeedHelpSection
    .NeedHelp
      .NeedHelp__top {{ $t('cantChoose') }}
      .NeedHelp__middle
        p {{ $t('contactSupportAndGetHelp') }}
        .helpLink.phone(@click='callCatcher') 
          span 78 113 70 71 
        span.helpLink(@click='telegram')
          span {{ $t('telegram') }}
      .NeedHelp__bottom
        p(style='text-wrap: nowrap;') {{ $t('providingConsultation') }}
        p {{ $t('workDaily') }}
        p {{ $t('contactTommorow') }}
</template>
<script>
export default {
  data() {
    return {}
  },
  methods: {
    async telegram() {
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
<style lang="scss">
.NeedHelpSection {
  z-index: 1001;
}
.NeedHelp {
  color: #000;
  background-color: #fff;
  outline: 7px solid #1bb8d1;
  border-radius: 15px;

  position: absolute;
  left: 50%;
  top: 50%;
  transform: translate(-50%, -50%);
  display: flex;
  flex-direction: column;
  align-items: center;
  width: unset;
  @media only screen and (max-width: 431px) {
    width: 95%;
    padding: 5px;
  }
  img {
    height: 50px;
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
    width: 100%;
    color: #000;
    font-size: 1.875rem;
    font-weight: 600;
    text-align: center;
    padding: 58px 55px;
    text-wrap: nowrap;
    padding-bottom: 0;

    @media only screen and (max-width: 431px) {
      font-size: 18px;
      width: 200px;
      display: flex;
      justify-content: center;
    }
  }
  &__middle {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 0px 43px 48px 43px;
    p {
      margin: 0;
      font-size: 1rem;
      margin-top: 10px;
      font-weight: 200;
      margin-bottom: 30px;
      @media only screen and (max-width: 431px) {
        display: none;
      }
    }
    .helpLink {
      text-decoration: none;
      color: #fff;
      font-size: 1.125rem;
      padding: 13px 82px;
      border-radius: 15px;
      text-decoration: none;
      transition: all, 0.3s;
      background-color: #1bb8d1;
      margin-top: 10px;
      display: flex;
      justify-content: center;
      width: 70%;
      text-wrap: nowrap;
      cursor: pointer;

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
  }
  &__bottom {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 15px 43px;
    background-color: #41aacf;
    width: 100%;
    color: #fff;

    @media only screen and (max-width: 431px) {
      padding-top: 20px;
    }

    p {
      font-size: 1rem !important;
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
