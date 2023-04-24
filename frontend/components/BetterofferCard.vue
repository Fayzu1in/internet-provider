<template lang="pug">
section.tariffCard
  .hotFlag(v-if='hot')
    MaterialIcon(:icon="mdiFire")
  .tariffCard__top 
    .topLeftLogo
      img.logo(:src='image')
    .topRight 
      p.name(:name='name') {{ this.name || 'Не указано' }}
      div.type 
        p.typeSubtitle {{ $t('type') }} :
        p.typeTitle(:tech='tech') {{this.tech || 'Не указано'}}
  .tariffCard__middle
    .speed 
      .tech__title {{ $t('dailySpeed') }}
      .tech__text(:speed='speed') {{ this.speed || 'Не указано'}}
    .nightSpeed
      p.nightSpeed__title {{ $t('nightSpeed') }}
      p.nightSpeed__text(:nSpeed='nSpeed') {{ this.nSpeed || 'Не указано' }}
  .tariffCard__bottom
    .tariffCard__bottom-price 
      p.priceBold(:price='price') {{this.price || 'Не указано'}}
      p {{ $t('priceMonth') }}
    NuxtLink.connectButton(:to='localePath(`/request/${this.message}` )', :message='message') {{ $t('connect') }} 
</template>
<script>
import { mdiSpeedometer, mdiCashMultiple, mdiFire } from '@mdi/js'
export default {
  props: {
    hot: {
      type: Boolean,
      default: false,
    },
    message: {
      type: Number,
      default: null,
    },

    image: {
      type: String,
      default: undefined,
    },
    name: {
      type: String,
      default: null,
    },
    speed: {
      type: String,
      default: null,
    },
    bonus: {
      type: String,
      default: null,
    },
    price: {
      type: String,
      default: null,
    },
    nSpeed: {
      type: String,
      default: null,
    },
    tech: {
      type: String,
      default: null,
    },
  },
  data() {
    return {
      mdiSpeedometer,
      mdiCashMultiple,
      mdiFire,
      offers: null,
    }
  },
}
</script>

<style lang="scss" scoped>
.tariffCard {
  display: flex;
  flex-direction: column;
  align-items: normal;
  justify-content: space-between;
  background: #fff;
  padding: 10px;
  border-radius: 5px;
  color: #000;
  width: 250px;
  height: 250px;
  margin-bottom: 15px;
  position: relative;
  .hotFlag {
    position: absolute;
    padding: 0 5px;
    display: flex;
    justify-content: center;
    align-items: center;
    border-radius: 5px;
    top: 3px;
    right: -18px;
    box-shadow: rgb(38, 57, 77) 0px 20px 30px -10px;
    // left: 30px;
    /* left: 10px; */
    /* height: 20px; */
    background: #ec9f1b;
    color: #fff;
  }

  &__top {
    display: flex;
    // justify-content: space-between;
    flex-direction: column;
    .topLeftLogo {
      // max-width: 50%;
      width: 230px;
      height: 60px;
      display: flex;
      justify-content: center;

      .logo {
        height: 100%;
        width: 100%;
        object-fit: contain;
      }
    }
    .topRight {
      // max-width: 50%;
      width: 100%;
      .type {
        padding-top: 10px;
        display: flex;
        align-items: center;
      }
      p {
        margin: 0;
      }
      .name {
        font-size: 22px;
        font-weight: bold;
        text-align: center;
        padding-top: 15px;
        padding-bottom: 10px;
      }
      .typeSubtitle {
        font-size: 12px;
        color: rgb(193, 191, 191);
        padding-right: 10px;
      }
    }
  }
  &__middle {
    display: flex;
    justify-content: space-between;
    .nightSpeed {
      &__title {
        font-size: 12px;
        margin: 0;
        color: rgb(193, 191, 191);
      }
      &__text {
        font-size: 18px;
        margin: 0;
        padding-top: 5px;
      }
    }
    .tech {
      text-align: start;
      padding-right: 10px;
      &__title {
        font-size: 12px;
        margin: 0;
        color: rgb(193, 191, 191);
      }
      &__text {
        text-align: start;
        font-size: 18px;
        margin: 0;
        padding-top: 5px;
      }
    }
  }
  &__bottom {
    display: flex;
    align-items: center;
    justify-content: space-between;

    &-price {
      font-size: 18px;
      .priceBold {
        font-weight: bold;
      }
      /* stylelint-disable-next-line no-descending-specificity */
      p {
        margin: 0;
      }
    }
    .connectButton {
      text-decoration: none;
      cursor: pointer;
      border: none;
      font-size: 18px;
      color: #fff;
      padding: 5px;
      border-radius: 5px;
      background: linear-gradient(to right, #d1b88c 0%, #ec9f1b 100%);
    }
  }
}
</style>
