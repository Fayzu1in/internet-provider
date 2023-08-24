<template lang="pug">
ModalDialog(@close='$emit("close")')
  .callBackSection
    .callBackModal 
      .closeModal(@click='$emit("close")')
        MaterialIcon(:icon='mdiClose')
      .callBackModal__top 
        p Заявка на консультацию специалиста
      .callBackModal__middle
        p Для консультации вы можете позвонить по телефону:
        a.phoneCallFromModal(href='tel:+998781137071') +998 78 113 70 71
        p или заполнить форму заявки обратного звонка
        form(method="post", @submit.prevent="postCallBackForm").callBackForm 
          input(placeholder="Ваше ФИО..." required  id="phone" name="phone" v-model='name')
          input(placeholder="Ваш телефон" v-maska data-maska='+998 (##) ### ## ##', pattern=".{19,}" required  id="phone" name="phone" v-model='phone')
          input(placeholder="Когда вам перезвонить" required  id="preferrable_time" name="preferrable_time" v-model='preferrableTime')
          button.callBackForm__submit(type="submit" value="submit") ЗАКАЗАТЬ КОНСУЛЬТАЦИЮ
      .callBackModal__bottom 
        p.title ПОЛЕЗНО ЗНАТЬ:
        p Предоставление консультации не обязывает Вас к подключению.
        p Консультанты работают Ежедневно, с 9:00 до 22:00.
        p Если свою заявку Вы отправили после 22:00, - консультант свяжется с Вами завтра в первой половине дня.
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
    }
  },
  methods: {
    postCallBackForm() {
      this.$api.postCallBack(this.name, this.phone, this.preferrableTime)
    },
  },
}
</script>
<style lang="scss" scoped>
.callBackSection {
  z-index: 1001;
}
.callBackModal {
  background-color: rgba(255, 255, 255, 0.7647058824);
  color: #001b48;
  backdrop-filter: blur(10px);
  border-radius: 15px;
  position: absolute;
  left: 50%;
  top: 50%;
  transform: translate(-50%, -50%);
  padding: 15px;
  display: flex;
  flex-direction: column;
  align-items: center;
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
        margin-top: 10px;
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
      font-size: 24px;
      padding: 5px 10px;
      border-radius: 15px;
      text-decoration: none;
      transition: all, 0.3s;
      background-color: #001b48;
      margin-top: 15px;
      @media only screen and (max-width: 431px) {
        font-size: 18px;
        margin-top: 20px;
      }
      &:hover {
        background-color: #fff;
        color: #001b48;
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
