<template lang="pug">
section.tariffCard
  p.tariffCard__provider(:provider='provider') {{this.provider}}
  p.tariffCard__name(:title='title') {{this.title}}
  .tariffCard__speed
    p(:speed='speed') {{this.speed}} МБИТ/С
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
    }
  },
}
</script>

<style lang="scss" scoped>
.tariffCard {
  color: #fff;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  border-radius: 4px;
  max-width: 200px;
  width: 100%;
  // padding: 0 30px;
  cursor: pointer;
  transition: transform 0.3s;
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
  margin-left: 30px;
  &__provider {
    font-size: 32px;
    line-height: 0;

    font-weight: 600;
  }
  &__name {
    font-size: 26px;
    // line-height: 0;
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
