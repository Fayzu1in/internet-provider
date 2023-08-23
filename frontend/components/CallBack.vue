<template lang="pug">
ModalDialog(@close='$emit("close")')
  .callBackSection
    .callBackModal 
      MaterialIcon.closeModal(:icon='mdiClose' color='#001b48' )
      .callBackModal__top 
        p Заявка на консультацию специалиста
      .callBackModal__middle
        p.youCanCall Для консультации вы можете позвонить по телефону:
        a.phoneCallFromModal(href='tel:+998781137071') +998 78 113 70 71
        p или заполнить форму заявки обратного звонка
        .callBackForm 
          input(placeholder="Ваше ФИО...")
          input(placeholder="Ваш телефон")
          input(placeholder="Когда вам перезвонить")
          button(type="submit") ЗАКАЗАТЬ КОНСУЛЬТАЦИЮ
      .callBackModal__bottom 
        p ПОЛЕЗНО ЗНАТЬ:
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
    }
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

  .closeModal {
    position: absolute;
    top: 5px;
    right: 5px;
    border-radius: 50%;
    border: 3px solid #001b48;
  }
  &__top {
    background-color: #0b2249;
    width: 100%;
    position: absolute;
    top: 0;
    left: 0;
    border-top-left-radius: 15px;
    border-top-right-radius: 15px;
  }
  &__middle {
    .callBackForm {
      display: flex;
      flex-direction: column;
      align-items: center;
    }
  }
  &__bottom {
    display: flex;
    flex-direction: column;
    align-items: center;
  }
}
</style>
