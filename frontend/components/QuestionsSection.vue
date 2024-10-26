<template lang="pug">
.container-fluid
  .questionsSection
    .questionsSection__top
      .questionsSection__top-left
        .connect(style="text-transform: lowercase;") {{ $t('questionsAndAnswers') }}
        .title  {{ $t('faq') }}
        .subtitle {{ $t('faqInfo') }}
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
      padding-top: 0;
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
        font-family: 'Montserrat', sans-serif;
      }
      .title {
        font-size: 45px;
        padding-top: 24px;
        font-weight: bold;
        line-height: 60px;
        padding-bottom: 14px;
        font-family: 'Raleway', sans-serif;
      }
      .subtitle {
        font-family: 'Montserrat', sans-serif;
        font-size: 20px;
        font-weight: 200;
      }
    }
    &-right {
      display: flex;
      justify-content: flex-end;
      @media only screen and (max-width: 576px) {
        display: none;
      }
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
