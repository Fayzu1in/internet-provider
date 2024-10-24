<template lang="pug">
.container-fluid
  .TopProviders
    .TopProviders__top
      .TopProviders__top-left
        .connect тарифы
        .title  Тарифы месяца по версии INTERNETBOR
        .subtitle Тарифы по выгодным ценам: оптимальные решения для любого бюджета
      .TopProviders__top-right
        img(src='/rocket.png')
    .TopProviders__bottom
      betterOffers
</template>
<script>
export default {}
</script>
<style lang="scss" scoped>
.TopProviders {
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
      padding-top: 0;
      padding-bottom: 0;
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
        font-size: 2.75rem;
        padding-top: 24px;
        font-weight: bold;
        line-height: 60px;
        padding-bottom: 14px;
        @media only screen and (max-width: 576px) {
          font-size: 2rem;
          line-height: 35px;
        }
      }
      .subtitle {
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
        height: 256px;
        width: 238px;
      }
    }
  }
  &__bottom {
    display: flex;
    justify-content: space-between;
    .providerCard {
      border-radius: 13px;
      max-width: 146px;
      width: 100%;
      box-shadow: rgba(0, 0, 0, 0.25) 0px 54px 55px,
        rgba(0, 0, 0, 0.12) 0px -12px 30px, rgba(0, 0, 0, 0.12) 0px 4px 6px,
        rgba(0, 0, 0, 0.17) 0px 12px 13px, rgba(0, 0, 0, 0.09) 0px -3px 5px;

      .topProviders {
        display: flex;
        justify-content: center;
        align-items: center;
        // padding-bottom: 30px;
        // transition: all 0.6s;
        @media only screen and (max-width: 431px) {
          flex-direction: column;
          padding-bottom: 0;
        }
        .topCard {
          width: 250px;
          height: 125px;
          margin-left: 10px;
          margin-right: 10px;
          @media only screen and (max-width: 431px) {
            display: flex;
            justify-content: center;

            margin: 0 0;
            height: unset;
          }
        }
        &__card {
          &-img {
            background-color: #ffffff;
            height: 100%;
            width: 100%;
            object-fit: contain;
            padding: 30px;

            border-radius: 15px;
            // box-shadow: rgba(50, 50, 93, 0.25) 0px 50px 100px -20px,
            //   rgba(0, 0, 0, 0.3) 0px 30px 60px -30px;
            // box-shadow: rgb(38, 57, 77) 0px 20px 30px -10px;

            transition: transform 0.3s;
            &:hover {
              transform: scale(1.1);
            }
            @media only screen and (max-width: 431px) {
              margin-left: 0;
              padding: 20px;
              height: 200px;
              width: 200px;
              margin-bottom: 15px;
            }
          }
        }
      }
    }
  }
}
</style>
