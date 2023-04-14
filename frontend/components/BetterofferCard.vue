<template lang="pug">
section.tariffCard
  .tariffCard__top 
    .topLeftLogo
      img.logo(:src='image')
    .topRight 
      p.name(:name='name') {{ this.name || 'Не указано' }}
      p.typeSubtitle Тип
      p.typeTitle(:tech='tech') {{this.tech || 'Не указано'}}
  .tariffCard__middle
    .speed 
      .tech__title Дневная скорость
      .tech__text(:speed='speed') {{ this.speed || 'Не указано'}}
    .nightSpeed
      p.nightSpeed__title Ночная скорость
      p.nightSpeed__text(:nSpeed='nSpeed') {{ this.nSpeed || 'Не указано' }}
  .tariffCard__bottom
    .tariffCard__bottom-price 
      p.priceBold(:price='price') {{this.price || 'Не указано'}}
      p сум/мес 
    NuxtLink.connectButton(:to='(`/request/${this.message}` )', :message='message') Подключить 
</template>
<script>
import { mdiSpeedometer, mdiCashMultiple } from '@mdi/js'
export default {
  props: {
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

  &__top {
    display: flex;
    justify-content: space-between;
    .topLeftLogo {
      max-width: 50%;

      .logo {
        height: 70px;
        width: 70px;
      }
    }
    .topRight {
      max-width: 50%;
      width: 100%;
      p {
        margin: 0;
      }
      .name {
        font-size: 22px;
        font-weight: bold;
      }
      .typeSubtitle {
        padding-top: 10px;
        font-size: 12px;
        color: rgb(193, 191, 191);
      }
    }
  }
  &__middle {
    display: flex;
    justify-content: space-between;
    padding-top: 20px;
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
