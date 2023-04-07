<template lang="pug">
section.tariffCard
  .tariffCard__top 
    .topLeftLogo
      img.logo(:src='image')
    .topRight 
      p.name(:name='name') {{ this.name }}
      P.speed(:speed='speed') {{this.speed}}
  .tariffCard__middle
    .nightSpeed
      p.nightSpeed__title Ночная скорость
      p.nightSpeed__text(:nSpeed='nSpeed') {{ this.nSpeed }}
    .tech 
      .tech__title Тип
      .tech__text(:tech='tech') {{ this.tech }}
  .tariffCard__bottom
    .tariffCard__bottom-price 
      p.priceBold(:price='price') {{this.price}}
      p сум/мес 
    NuxtLink.connectButton(:to='(`/request/${this.message}` )', :message='message') Подключить 
 
    
  //- p.tariffCard__provider(:provider='provider') {{this.provider.toUpperCase()}}
  //- p.tariffCard__name(:title='title') {{this.title}}
  //- .tariffCard__speed
  //-   p(:speed='speed') {{this.speed}} 
  //-   MaterialIcon(:icon='mdiSpeedometer')
  //- .tariffCard__price
  //-   p(:price='price') {{this.price}}
  //-   MaterialIcon(:icon='mdiCashMultiple')
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
      .speed {
        padding-top: 10px;
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
        color: grey;
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
        color: grey;
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
      // background: #000;
      background: linear-gradient(to right, #d1b88c 0%, #ec9f1b 100%);

      // border: 1px solid rgba(128, 128, 128, 0.417);
      // background: radial-gradient(
      //     ellipse farthest-corner at right bottom,
      //     #fedb37 0%,
      //     #fdb931 8%,
      //     #9f7928 30%,
      //     #8a6e2f 40%,
      //     transparent 80%
      //   ),
      //   radial-gradient(
      //     ellipse farthest-corner at left top,
      //     #ffffff 0%,
      //     #ffffac 8%,
      //     #d1b464 25%,
      //     #5d4a1f 62.5%,
      //     #5d4a1f 100%
      //   );
    }
  }
}
// .tariffCard {
//   text-decoration: none;
//   color: #fff;
//   display: flex;
//   flex-direction: column;
//   align-items: center;
//   justify-content: center;
//   border-radius: 5px;
//   width: 180px;
//   cursor: pointer;
//   transition: transform 0.3s;
//   // background-color: #00000096;
//   box-shadow: rgb(38, 57, 77) 0px 20px 30px -10px;
//   font-size: 22px;
//   padding: 15px 0;
//   background: radial-gradient(
//       ellipse farthest-corner at right bottom,
//       #fedb37 0%,
//       #fdb931 8%,
//       #9f7928 30%,
//       #8a6e2f 40%,
//       transparent 80%
//     ),
//     radial-gradient(
//       ellipse farthest-corner at left top,
//       #ffffff 0%,
//       #ffffac 8%,
//       #d1b464 25%,
//       #5d4a1f 62.5%,
//       #5d4a1f 100%
//     );
//   // &:hover {
//   //   transform: scale(1.1);
//   // }

//   @media only screen and (max-width: 420px) {
//     margin-left: 0;
//   }
//   &__provider {
//     margin: 0;
//     font-weight: 500;
//     padding-bottom: 15px;
//   }
//   &__name {
//     margin: 0;
//     padding-bottom: 15px;

//     @media only screen and (max-width: 420px) {
//       margin: 0;
//     }
//   }
//   &__speed {
//     display: flex;
//     align-items: center;
//     padding-bottom: 15px;

//     p {
//       margin: 0;
//       margin-right: 5px;
//     }
//     display: flex;
//     align-items: center;
//   }
//   &__price {
//     display: flex;
//     align-items: center;

//     p {
//       margin: 0;
//       margin-right: 5px;
//     }
//   }
// }
</style>
