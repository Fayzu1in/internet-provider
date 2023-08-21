<template lang="pug">
section.address
  .container-fluid
  .address__top {{ $t('chooseProvider') }}
  .address__middle
     .address__middle-left
        AddressForm
     .address__middle-right
       .manual
         p.title {{ $t('connectInternet3Steps') }}
         ol.manual__list
           li {{ $t('fillOutForm') }}
           li {{ $t('weWillDetermine') }}
           li {{ $t('chooseAndLeaveRequest') }}
  a.phoneCall(href='tel:+998781137071') +998 78 113 70 71
  button.callBack {{ $t('callBack') }}
  ChooseCard
</template>
<script>
export default {}
</script>
<style lang="scss" scoped>
// tetstatsaas
.address {
  padding-top: 100px;
  display: flex;
  flex-direction: column;
  align-items: center;

  @media only screen and (max-width: 431px) {
    padding-top: 70px;
  }

  &__top {
    font-size: 32px;
    font-weight: 600;
    text-align: center;
    @media only screen and (max-width: 431px) {
      font-size: 24px;
      // text-align: left;
    }
  }
  &__middle {
    margin: 0 auto;
    // text-align: center;
    // max-width: 750px;
    margin-top: 30px;
    width: fit-content;
    // color: #ffffff;
    padding: 20px 20px;
    // font-size: 18px;
    background-color: #ffffff93;
    border-radius: 15px;
    display: flex;
    justify-content: space-around;
    align-items: center;
    @media only screen and (max-width: 431px) {
      flex-direction: column-reverse;
      padding: 10px;
    }
    &-left {
      // margin-right: 20px;
    }
    &-right {
      background-color: #0b2249;
      border-radius: 15px;
      margin-left: 20px;
      @media only screen and (max-width: 431px) {
        margin-left: 0;
      }
      .manual {
        // max-width: 400px;
        // width: 100%;
        padding: 10px 20px;
        @media only screen and (max-width: 431px) {
          padding: 10px;
        }
        p {
          font-size: 20px;
        }
        &__list {
          width: 300px;
          @media only screen and (max-width: 431px) {
            font-size: 14px;
            width: 255px;
          }
          li {
            padding-bottom: 20px;
            @media only screen and (max-width: 431px) {
              padding-bottom: 10px;
            }
          }
        }
        .title {
          @media only screen and (max-width: 431px) {
            font-size: 18px;
            text-align: center;
          }
        }
      }
    }
    @media only screen and (max-width: 431px) {
      font-size: 16px;
      // text-align: left;
      padding-top: 10px;
    }
  }
  .phoneCall {
    font-family: LilitaOne-Regular;
    color: #fff;
    font-size: 24px;
    margin-top: 30px;
    text-decoration: none;
    transition: color, 0.3s;

    &:hover {
      color: #d8d3d3;
    }
  }
  .callBack {
    margin-top: 10px;
    color: #fff;
    background: none;
    border: none;
    border-radius: 10px;
    width: 300px;
    cursor: pointer;
    transition: all 0.3s;
    font-size: 16px;
    border-bottom: 3px inset transparent;
    transition: border-bottom, 0.3s;

    &:hover {
      border-bottom: 3px inset #ffff;
    }

    @media only screen and (max-width: 431px) {
      margin-left: 0;
      width: 250px;
      margin-bottom: 0;
    }
  }
}
</style>
