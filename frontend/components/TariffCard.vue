<template lang="pug">
section.tariff
  .tariff__card
    .tariff__card-name.column(:tariffName='tariffName') 
      p {{tariffName}}
    .tariff__card-traffic.column
      p(:traffic='traffic') {{ traffic }}
      MaterialIcon(:icon='mdiAllInclusive')
    .tariff__card-speed.column
      p(:speed='speed') {{ this.speed }}
      MaterialIcon(:icon='mdiSpeedometer' )
    .tariff__card-cost
      p(:cost='cost') {{ cost }}  сум/мес
      MaterialIcon(:icon='mdiCashMultiple' color='green')
    NuxtLink.tariff__card-button(:to='(`/request/${plan}`)',) Подключить
  hr.hrLine
</template>
<script>
import { mdiSpeedometer, mdiCashMultiple, mdiAllInclusive } from '@mdi/js'
export default {
  props: {
    plan: {
      type: Number,
      default: null,
    },
    traffic: {
      type: String,
      default: null,
    },
    speed: {
      type: String,
      default: null,
    },
    cost: {
      type: String,
      default: null,
    },
    tariffName: {
      type: String,
      default: null,
    },
  },
  data() {
    return {
      mdiSpeedometer,
      mdiCashMultiple,
      mdiAllInclusive,
    }
  },
}
</script>
<style lang="scss" scoped>
.tariff {
  //   padding-top: 30px;
  &__card {
    display: flex;
    justify-content: space-between;
    border-radius: 5px;
    align-items: center;
    font-size: 22px;
    @media only screen and (max-width: 420px) {
      flex-direction: column;
      font-size: 18px;
      padding-bottom: 15px;
    }

    &-name,
    &-speed,
    &-cost,
    &-traffic {
      display: flex;
      align-items: center;
      p {
        padding-right: 10px;
        @media only screen and (max-width: 420px) {
          margin: 0;
        }
      }
      @media only screen and (max-width: 420px) {
        padding-bottom: 15px;
      }
    }
    .column {
      max-width: 200px;

      width: 100%;
      text-align: start;
      @media only screen and (max-width: 420px) {
        text-align: unset;
        width: unset;
      }
    }
    &-name {
      p {
        border-bottom: 1px solid #fff;
        padding-bottom: 5px;
        @media only screen and (max-width: 420px) {
          margin: 0;
        }
      }
    }
    &-button {
      text-decoration: none;
      color: #fff;
      background: linear-gradient(to right, #aeb2b6 0%, #283c4c 100%);
      box-shadow: rgb(38, 57, 77) 0px 20px 30px -10px;
      padding: 7px 15px;
      border-radius: 5px;
    }
  }
}
.hrLine {
  position: relative;
  outline: 0;
  border: 0;
  color: black;
  opacity: 0.5;
  &:before {
    content: '';
    background: linear-gradient(to right, transparent, #818078, transparent);
    position: absolute;
    left: 0;
    // top: 50%;
    width: 100%;
    height: 1px;
  }
  &:after {
    content: '';
    position: relative;
    display: inline-block;
    color: black;

    padding: 0 0.5em;
    // line-height: 1.5em;
    color: #818078;
    background-color: #fcfcfa;
  }
}
</style>
