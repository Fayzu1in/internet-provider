<template lang="pug">
section.choose
  .chooseCard(v-for='i in tariff', @click.stop.prevent='$emit("showCallBackModal")')
    .chooseCard__img
      img(:src='i.image')
    .chooseCard__text 
      p.top {{ $t('internet') }}
      p.chooseCard__title {{ i.dwelling }}
    p.chooseCard__cost 
      span {{ $t('from') }} 
      span.price(style="font-family: 'LilitaOne-Regular';") {{ i.priceFrom }} 
      span {{ $t('sum') }}
    p.chooseCard__subtitle {{ $t('selectOptimal') }}

      

</template>
<script>
export default {
  data() {
    return {
      tariff: [
        {
          dwelling: this.$t('flat'),
          priceFrom: '90.000',
          image: '/flat.png',
        },
        {
          dwelling: this.$t('home'),
          priceFrom: '90.000',
          image: '/house.png',
        },
        {
          dwelling: this.$t('office'),
          priceFrom: '120.000',
          image: '/office.png',
        },
      ],
    }
  },
}
</script>
<style lang="scss" scoped>
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
