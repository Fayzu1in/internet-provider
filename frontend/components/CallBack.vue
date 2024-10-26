<template lang="pug">
ModalDialog(@close='$emit("close")')
  .callBackSection
    .callBackModal 
      .callBackModal__top {{$t('applicationSpecialist')}}
      .callBackModal__middle
        p {{ $t('forConsultation') }}
        .phoneCallFromModal(@click='callCatcher') +998 78 113 70 71
        p {{ $t('fillOutCallBack') }}
        form(method="post", @submit.prevent="postCallBackForm").callBackForm 
          input(:placeholder=`$t('yourName')`, required  id="phone" name="phone" v-model='name')
          input(:placeholder=`$t('yourPhone')`, v-maska data-maska='+998 (##) ### ## ##', pattern=".{19,}" required  id="phone" name="phone" v-model='phone')
          input(:placeholder=`$t('whenToCall')`, required  id="preferrable_time" name="preferrable_time" v-model='preferrableTime')
          ActionButton(:loading = `loading`, type='submit' :content='this.$t("orderConsultation")')
      .callBackModal__bottom 
        p {{ $t('providingConsultation') }}
        p {{ $t('workDaily') }}
        p {{ $t('contactTommorow') }}
</template>
<script>
import { mdiClose } from '@mdi/js'
export default {
  data() {
    return {
      mdiClose,
      name: '',
      phone: '',
      preferrableTime: '',
      loading: false,
    }
  },
  methods: {
    postCallBackForm() {
      this.loading = true
      this.$api
        .postCallBack(this.name, this.phone, this.preferrableTime)
        .then((res) => {
          this.name = ''
          this.phone = ''
          this.preferrableTime = ''
          this.loading = false
          console.log(res)
          this.$emit('close')
        })
        .catch((error) => {
          // Handle errors here if needed
          console.error('Error:', error)
          this.loading = false // Set loading to false on error as well
        })
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
.callBackSection {
  z-index: 1001;
}
.callBackModal {
  color: #000;
  background-color: #fff;
  border: 7px solid #1bb8d1;
  border-radius: 15px;
  padding: 58px 43px 28px 43px;
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
    p {
      margin: 0;
      font-size: 1rem;
      margin-top: 15px;
      @media only screen and (max-width: 431px) {
        display: none;
      }
    }
    .callBackForm {
      display: flex;
      flex-direction: column;
      align-items: center;
      width: 100%;
      margin-top: 15px;
      @media only screen and (max-width: 431px) {
        margin-top: 5px;
      }
      input {
        background-color: #ffffffc3;
        border: 1px solid rgba(128, 128, 128, 0.417);
        backdrop-filter: blur(10px);
        color: #000;
        border-radius: 10px;
        width: 100%;
        text-align: center;
        margin-bottom: 10px;
        font-size: 18px;
        padding: 9px 20px;
        @media only screen and (max-width: 431px) {
          margin-bottom: 5px;
          font-size: 16px;
          border-bottom: 1px solid grey;
          padding: 10px 15px;
          margin-top: 3px;
        }
      }
      &__submit {
        background: #008de5;
        color: #fff;
        border: none;
        border-radius: 10px;
        width: 100%;
        margin-top: 10px;
        cursor: pointer;
        transition: all 0.3s;
        font-size: 18px;
        margin-bottom: 10px;
        padding: 10px 20px;
        @media only screen and (max-width: 431px) {
          font-size: 16px;
        }
      }
    }
    .phoneCallFromModal {
      font-family: LilitaOne-Regular;
      color: #fff;
      font-size: 1.125rem;
      padding: 13px 82px;
      border-radius: 15px;
      text-decoration: none;
      transition: all, 0.3s;
      background-color: #1bb8d1;
      margin-top: 24px;
      cursor: pointer;
      @media only screen and (max-width: 431px) {
        font-size: 18px;
        margin-top: 20px;
      }
    }
  }
  &__bottom {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding-top: 15px;
    @media only screen and (max-width: 431px) {
      padding-top: 10px;
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
