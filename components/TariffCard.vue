<template lang="pug">
section.tariff
  .tariff__card
    //- .tariff__card-name(:tariffName='tariffName') {{this.tariffName}}
    .tariff__card-traffic
      p Безлимит
      MaterialIcon(:icon='mdiAllInclusive')
    .tariff__card-speed 
      p 10 мб
      MaterialIcon(:icon='mdiSpeedometer' color='red')
    .tariff__card-cost
      p 109.000
      MaterialIcon(:icon='mdiCashMultiple' color='green')
    NuxtLink.tariff__card-button(to='/') Подключить
  hr.hrLine
</template>
<script>
import { mdiSpeedometer, mdiCashMultiple, mdiAllInclusive } from '@mdi/js'
export default {
  props: {},
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

    &-name,
    &-speed,
    &-cost,
    &-traffic {
      display: flex;
      align-items: center;
      p {
        padding-right: 10px;
      }
    }
    &-name {
      font-size: 32px;
      font-weight: bold;
    }
    &-button {
      text-decoration: none;
      color: #fff;
      background: radial-gradient(
          ellipse farthest-corner at right bottom,
          #fedb37 0%,
          #fdb931 8%,
          #9f7928 30%,
          #8a6e2f 40%,
          transparent 80%
        ),
        radial-gradient(
          ellipse farthest-corner at left top,
          #ffffff 0%,
          #ffffac 8%,
          #d1b464 25%,
          #5d4a1f 62.5%,
          #5d4a1f 100%
        );
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
