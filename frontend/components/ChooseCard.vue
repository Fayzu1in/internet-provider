<template lang="pug">
.container-fluid
  .ChooseCard
    .ChooseCard__top
      .ChooseCard__top-left
        .connect {{ $t('connect') }}
        .title  {{ $t('internetForAnyPurpose') }}
        .subtitle {{ $t('limitlessOpportunities') }}
      .ChooseCard__top-right
        img(src='/connect.png')
    .ChooseCard__bottom
      .tariffCard(v-for='item in tariff', @click.stop.prevent='$emit("showCallBackModal")')
        .tariffCard__top
          img(:src='item.image')
          span.text {{ item.dwelling }}
        .tariffCard__middle {{ item.priceFrom }}
        button.tariffCard__button {{ $t('choosePlan') }}
</template>
<script>
export default {
  data() {
    return {
      tariff: [
        {
          dwelling: this.$t('flat'),
          priceFrom: 'From 90.000 sum',
          image: '/home.png',
        },
        {
          dwelling: this.$t('home'),
          priceFrom: 'From 90.000 sum',
          image: '/flat.png',
        },
        {
          dwelling: this.$t('office'),
          priceFrom: 'From 120.000 sum',
          image: '/office.png',
        },
      ],
    }
  },
}
</script>
<style lang="scss" scoped>
.ChooseCard {
  cursor: pointer;
  &__top {
    display: flex;
    padding-top: 65px;
    align-items: center;
    padding-bottom: 93px;
    @media only screen and (max-width: 576px) {
      flex-direction: column;
      padding-top: 20px;
      padding-bottom: 20px;
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
        font-size: 20px;
        font-weight: 200;
        font-family: 'Montserrat', sans-serif;
      }
    }
    &-right {
      display: flex;
      justify-content: flex-end;
      @media only screen and (max-width: 576px) {
        justify-content: center;
      }

      img {
        height: 265px;
        width: 343px;
        @media only screen and (max-width: 576px) {
          height: 190px;
          width: auto;
        }
      }
    }
  }
  &__bottom {
    display: flex;
    justify-content: space-between;
    @media only screen and (max-width: 576px) {
      flex-direction: column;
      align-items: center;
    }
    .tariffCard {
      min-width: 307px;
      width: 100%;
      text-align: center;
      padding-left: 30px;
      padding-right: 30px;
      border-radius: 30px;
      padding-bottom: 14px;
      padding-top: 45px;
      background-color: #fff;
      display: flex;
      color: #3f62a7;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      width: fit-content;
      font-family: 'Montserrat', sans-serif;
      @media only screen and (max-width: 576px) {
        margin-bottom: 10px;
        margin-top: 10px;
      }
      &__top {
        // width: fit-content;
        display: flex;
        justify-content: center;
        align-items: center;
        font-family: 'Raleway', sans-serif;

        .text {
          font-size: 30px;
          font-weight: bold;
          padding-left: 18px;
          width: fit-content;
        }
        img {
          width: 43px;
          height: 43px;
        }
      }
      &__middle {
        padding-top: 43px;
        padding-bottom: 50px;
        font-size: 25px;
      }
      &__button {
        font-size: 20px;
        color: #fff;
        background-color: #3f62a7;
        padding: 20px 30px;
        border-radius: 999px;
        border: none;
        cursor: pointer;
        font-family: 'Montserrat', sans-serif;
      }
    }
  }
}

.choose {
  display: flex;
  justify-content: center;
  width: 100%;
  padding-top: 30px;
  @media only screen and (max-width: 431px) {
    flex-direction: column;
    align-items: center;
  }
  .chooseCard {
    cursor: pointer;
    color: #fff;
    background-color: rgba(255, 255, 255, 0.5764705882);
    text-align: center;
    margin-left: 10px;
    margin-right: 10px;
    border-radius: 15px;
    padding: 15px 10px;
    max-width: 250px;
    width: 100%;
    display: flex;
    flex-direction: column;
    align-items: center;
    @media only screen and (max-width: 431px) {
      margin-left: 0;
      margin-right: 0;
      margin-bottom: 15px;
    }
    &__img {
      margin-bottom: 10px;
      background-color: #fff;
      border-radius: 15px;
      width: 100%;
      img {
        height: 80px;
      }
    }
    &__text {
      color: #001b48;
      font-size: 18px;
      width: 100%;
      padding-top: 10px;
      background-color: #fff;
      border-radius: 15px;
      padding: 10px;
      p {
        margin: 0;
      }
    }
    &__title {
      font-size: 24px;
      font-weight: bold;
      color: #008de5;
      padding-top: 5px;
      margin: 0;
    }
    &__cost {
      margin: 0;
      background-color: #fff;
      color: #001b48;
      margin-top: 10px;
      border-radius: 15px;
      padding: 10px;
      span {
        font-size: 20px;
      }
    }
    &__subtitle {
      margin: 0;
      background-color: #fff;
      color: #001b48;
      margin-top: 10px;
      border-radius: 15px;
      padding: 10px;
    }
  }
}
</style>
