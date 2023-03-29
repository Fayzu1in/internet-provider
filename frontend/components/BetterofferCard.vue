<template lang="pug">
section.tariffCard
  p.tariffCard__provider(:provider='provider') {{this.provider}}
  p.tariffCard__name(:title='title') {{this.title}}
  .tariffCard__speed
    p(:speed='speed') {{this.speed}} 
    MaterialIcon(:icon='mdiSpeedometer')
  .tariffCard__price
    p(:price='price') {{this.price}}
    MaterialIcon(:icon='mdiCashMultiple')
</template>
<script>
import { mdiSpeedometer, mdiCashMultiple } from '@mdi/js'
export default {
  props: {
    provider: {
      type: String,
      default: null,
    },
    title: {
      type: String,
      default: null,
    },
    speed: {
      type: String,
      default: null,
    },
    price: {
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
  text-decoration: none;
  color: #fff;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  border-radius: 5px;
  width: 180px;
  cursor: pointer;
  transition: transform 0.3s;
  background-color: #00000096;
  box-shadow: rgb(38, 57, 77) 0px 20px 30px -10px;
  &:hover {
    transform: scale(1.1);
  }

  @media only screen and (max-width: 420px) {
    margin-left: 0;
  }
  &__provider {
    font-size: 32px;
    line-height: 0;
    font-weight: 600;
  }
  &__name {
    font-size: 26px;
    // line-height: 0;
    @media only screen and (max-width: 420px) {
      // line-height: 0;
      margin: 0;
    }
  }
  &__speed {
    p {
      margin-right: 5px;
    }
    display: flex;
    align-items: center;
    font-size: 20px;
    // line-height: 0;
  }
  &__price {
    display: flex;
    font-size: 20px;
    padding-bottom: 10px;
    line-height: 0;
    p {
      margin-right: 5px;
    }
  }
  &:hover {
    // transform: scale(1.1);
  }
}
</style>
