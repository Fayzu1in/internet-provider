<template lang="pug">
.container-fluid
  .questionsSection
    .questionsSection__top
      .questionsSection__top-left
        .connect вопросы и ответы
        .title  Ответы на часто задаваемые вопросы
        .subtitle Все, что вам нужно знать: быстрые ответы на популярные вопросы
      .questionsSection__top-right
        img(src='/internet-devices.png')
    .questionsSection__bottom
      AnswersandQuestions
</template>
<script>
export default {}
</script>
<style lang="scss">
.questionsSection {
  padding-bottom: 45px;
  padding-top: 48px;
  &__top {
    display: flex;
    padding-top: 65px;
    align-items: center;
    padding-bottom: 50px;
    @media only screen and (max-width: 576px) {
      flex-direction: column;
    }

    &-left {
      color: #fff;
      .connect {
        width: fit-content;
        font-size: 11px;
        color: #2e363e;
        padding: 10px 18px;
        background-color: #fff;
        border-radius: 5px;
        box-shadow: rgba(0, 0, 0, 0.25) 0px 54px 55px,
          rgba(0, 0, 0, 0.12) 0px -12px 30px, rgba(0, 0, 0, 0.12) 0px 4px 6px,
          rgba(0, 0, 0, 0.17) 0px 12px 13px, rgba(0, 0, 0, 0.09) 0px -3px 5px;
      }
      .title {
        font-size: 45px;
        padding-top: 24px;
        font-weight: bold;
        line-height: 60px;
        padding-bottom: 14px;
      }
      .subtitle {
        font-size: 20px;
        font-weight: 200;
      }
    }
    &-right {
      display: flex;
      justify-content: flex-end;
      img {
        height: 274px;
        width: 421px;
      }
    }
  }
  &__bottom {
  }
}
</style>
