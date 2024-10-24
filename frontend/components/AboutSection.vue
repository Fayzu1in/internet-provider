<template lang="pug">
.container-fluid
  .AboutCompany
    .AboutCompany__top
      .AboutCompany__top-left
        .connect о нас
        .title  InternetBor —  лучший сервис подбора интернет-провайдера по вашему адресу
        .subtitle Быстрый и удобный поиск интернета для вашего дома или офиса
      .AboutCompany__top-right
        img(src='/wiki.png')
    .AboutCompany__bottom
      .AboutCompany__bottom-top
        .aboutTextCard
          .aboutTextCard-top
            img(src='/gayka.png')
          .aboutTextCard-title Удобные инструменты
          .aboutTextCard-subtitle Наша опытная команда и внимательные консультанты быстро и эффективно решат любую вашу проблему.
        .aboutTextCard
          .aboutTextCard-top
            img(src='/cart.png')
          .aboutTextCard-title Выгодные предложения
          .aboutTextCard-subtitle Подберем оптимальный тариф, идеально соответствующий вашему бюджету, без скрытых переплат.
      .AboutCompany__bottom-btm
        .aboutTextCard
          .aboutTextCard-top
            img(src='/location.png')
          .aboutTextCard-title Поиск по адресу
          .aboutTextCard-subtitle Покажем и отфильтруем только актуальные предложения, доступные именно по вашему адресу, чтобы вы могли выбрать лучшее.

        

      
</template>
<script>
export default {}
</script>
<style lang="scss">
.AboutCompany {
  padding-bottom: 45px;
  padding-top: 48px;
  @media only screen and (max-width: 576px) {
    padding-top: 0;
  }
  &__top {
    display: flex;
    padding-top: 65px;
    align-items: center;
    padding-bottom: 93px;
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
        height: 325px;
        width: 353px;
      }
    }
  }
  &__bottom {
    &-top {
      display: flex;
      justify-content: center;
      @media only screen and (max-width: 576px) {
        flex-direction: column;
      }
    }
    &-btm {
      margin-top: 35px;
      display: flex;
      justify-content: center;
    }
  }
}
.aboutTextCard {
  max-width: 380px;
  width: 100%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  background-color: #fff;
  border-radius: 30px;
  text-align: center;
  padding: 40px;
  margin-left: 10px;
  margin-right: 10px;
  &-top {
    width: auto;
    img {
      height: 40px;
      width: auto;
    }
  }
  &-title {
    color: #2e363e;
    font-size: 20px;
    font-weight: 500;
    padding-top: 24px;
    padding-bottom: 10px;
  }
  &-subtitle {
    color: #2e363e;
    font-size: 14px;
  }
}
</style>
