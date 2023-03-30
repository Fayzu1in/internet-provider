<template lang="pug">
section.tariffCard
  p.tariffCard__provider(:provider='provider') {{this.provider.toUpperCase()}}
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
  // background-color: #00000096;
  box-shadow: rgb(38, 57, 77) 0px 20px 30px -10px;
  font-size: 22px;
  padding: 15px 0;
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
  &:hover {
    transform: scale(1.1);
  }

  @media only screen and (max-width: 420px) {
    margin-left: 0;
  }
  &__provider {
    margin: 0;
    font-weight: 500;
    padding-bottom: 15px;
  }
  &__name {
    margin: 0;
    padding-bottom: 15px;

    @media only screen and (max-width: 420px) {
      margin: 0;
    }
  }
  &__speed {
    display: flex;
    align-items: center;
    padding-bottom: 15px;

    p {
      margin: 0;
      margin-right: 5px;
    }
    display: flex;
    align-items: center;
  }
  &__price {
    display: flex;
    align-items: center;

    p {
      margin: 0;
      margin-right: 5px;
    }
  }
}
</style>
