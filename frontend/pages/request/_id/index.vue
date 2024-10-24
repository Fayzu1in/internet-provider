<template lang="pug">
section.request.container-fluid(@click='showModal = false' )
  //- .modalOverlay
  //- transition(name='slide' appear)

  .top
    .top__left
      .formManual
        .formManual__title {{ $t('congratsTariff') }}
        .formManual__subtitle
          p {{ $t('fillOut') }}
      form.request__form(action="" method="post", @submit.prevent="formSubmit")
        input(:placeholder=`$t('name')` required type="text" id="name" name="name" v-model='post.name' )
        input(:placeholder=`$t('phoneNumber')`, v-maska data-maska='+998 (##) ### ## ##', pattern=".{19,}"  required  id="phone" name="phone" v-model='post.phone' )
        input(:placeholder=`$t('city')` required type="text" id="city" name="city" v-model='post.city' )
        input(:placeholder=`$t('district')` required type="text" id="district" name="district" v-model='post.district' )
        input(:placeholder=`$t('street')`  type="text" id="street" name="street" v-model='post.street' )
        input(:placeholder=`$t('house')` required type="text" id="house" name="house" v-model='post.house' )
        input(type="hidden" name="plan_id"  id='tariff' :value='this.$route.params.id' )
        button.request__form-button(type="submit" value="submit") {{ $t('send') }}
    .information
      .tariff
        .tariff__title
          p {{ $t('yourTariff') }}
        .tariff__bottom 
          .tariff__left
            .name {{ tariff }}
            .price {{ price + $t('priceMonth')}}
          .tariff__right
            img(:src='image')
      .tariffInfo
        .leftSide
          .type 
            .type__title {{ $t('type') }}:
            .type__subtitle {{ tech }}
          .dailySpeed 
            .dailySpeed__title 
              MaterialIcon(:icon='mdiClockOutline' size='25px' color='black')
              p {{ daily_speed_time }}
            .dailySpeed__subtitle 
              //- img(src='')
              p {{ speed }}

        .rightSide
          .limit 
            .limit__title {{ $t('limit') }}:
            .limit__subtitle {{ limit }}
          .nightlySpeed 
            .nightlySpeed__title 
              MaterialIcon(:icon='mdiClockOutline' size='25px' color='black')
              p {{ nightly_speed_time }}
            .nightlySpeed__subtitle 
              //- img(src='')
              p {{ nightSpeed }}
      .informationList(v-if='routerText?.length')
        .informationList__left
          img(src='/icon_tarriff.png')
        .informationList__right
          p {{ routerText }}
      .informationList(v-if='tvText?.length')
        .informationList__left
          img(src='/icon_tarriff.png')
        .informationList__right
          p {{ tvText }}
      .informationList(v-if='cableText?.length')
        .informationList__left
          img(src='/icon_tarriff.png')
        .informationList__right
          p {{ cableText }}
      .informationList(v-if='actions?.length')
        .informationList__left
          img(src='/icon_tarriff.png')
        .informationList__right
          p {{ actions }}

  
    
    
  .bottom
    yandex-map(:coords="location", :zoom='18', :scroll-zoom='false'  class="map", @actionend='onActionEnd' @map-was-initialized='mapInit')



</template>

<script>
import axios from 'axios'
import {
  mdiClose,
  mdiClockOutline,
  mdiInformation,
  mdiTelevisionBox,
  mdiRouterWireless,
  mdiCableData,
} from '@mdi/js'

export default {
  data() {
    return {
      tariffID: this.$route.params.id,
      tariffInfo: [],
      providerName: '',
      tariff: '',
      speed: '',
      nightSpeed: '',
      tech: '',
      price: '',
      limit: '',
      locationText: '',
      showModal: false,
      yData: '',
      daily_speed_time: '08:00 - 00:00',
      nightly_speed_time: '00:00 - 08:00',
      mdiClockOutline,
      mdiInformation,
      mdiTelevisionBox,
      mdiRouterWireless,
      mdiCableData,
      router: false,
      routerText: '',
      tv: false,
      tvText: '',
      cable: false,
      cableText: '',
      actions: '',
      infoText: '',
      additionallyInfo: '',
      image: '',
      location: [41.311151, 69.279737],
      mdiClose,
      post: {
        name: '',
        phone: '+998',
        city: '',
        district: '',
        street: '',
        house: '',
        plan_id: this.$route.params.id,
      },
    }
  },
  async fetch() {
    this.tariffInfo = await this.$axios.$get(
      `https://internetbor.uz/api/v1/plans/${this.tariffID}`
    )
    // console.log(this.tariffInfo)
    this.providerName = this.tariffInfo.provider_name
    this.tariff = this.tariffInfo.title
    this.speed = this.tariffInfo.speed
    this.nightSpeed = this.tariffInfo.night
    this.price = this.tariffInfo.price
    this.limit = this.tariffInfo.limit
    this.tech = this.tariffInfo.tech
    this.daily_speed_time = this.tariffInfo.daily_speed_time
    this.nightly_speed_time = this.tariffInfo.nightly_speed_time
    this.actions = this.tariffInfo.info.replace(/&#32;/g, ' ')
    this.router = this.tariffInfo.router
    this.routerText = this.tariffInfo.router_text.replace(/&#32;/g, ' ')
    this.tv = this.tariffInfo.tv
    this.tvText = this.tariffInfo.tv_text.replace(/&#32;/g, ' ')
    this.cable = this.tariffInfo.cabel
    this.cableText = this.tariffInfo.cabel_text.replace(/&#32;/g, ' ')
    this.additionallyInfo = this.tariffInfo.more_info.replace(/&#32;/g, ' ')
    this.image = this.tariffInfo.provider_picture
    // console.log(this.tariffInfo)
  },

  methods: {
    formSubmit() {
      axios
        .post('https://internetbor.uz/api/v1/callbacks', this.post)
        .then((response) => {
          if (this.post.phone.length < 4) {
            alert('Введите номер телефона')
          }
          this.post.name = ''
          this.post.phone = '+998'
          this.post.city = ''
          this.post.district = ''
          this.post.street = ''
          this.post.house = ''
          this.showModal = true
          // this.$router.push('/thankyou')
          window.location.href = '/thankyou'
        })
    },
    mapInit(e) {
      // console.log(e)
      window.ymaps.geolocation.get().then((res) => {
        e.geoObjects.add(res.geoObjects)
        this.location = res.geoObjects.position
      })
    },

    onActionEnd(event) {
      const coords = event.get('target').getCenter()
      window.ymaps.geocode(coords).then((result) => {
        const firstGeoObject = result.geoObjects.get(0)
        this.locationText = firstGeoObject.getAddressLine()
        const [city, district, street] = this.locationText.split(', ')
        this.post.city = city
        this.post.district = district
        this.post.street = street
      })
    },
  },
}
</script>
<style lang="scss" scoped>
* {
  width: auto;
}
.map {
  max-width: 1000px;
  width: 100%;
  height: 454px;
  border-radius: 5px;
  overflow: hidden;
  @media only screen and (max-width: 431px) {
    height: 300px;
    margin-bottom: 30px;
  }
}
.ymap-container {
  border-radius: 15px;
  // overflow: hidden;
}

.request {
  padding-top: 160px;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  @media only screen and (max-width: 431px) {
    padding-bottom: 30px;
    padding-top: 70px;
  }
  .top {
    padding-top: 50px;
    width: 100%;
    display: flex;
    justify-content: center;
    align-items: flex-start;
    @media only screen and (max-width: 431px) {
      flex-direction: column-reverse;
      align-items: center;
      padding-bottom: 30px;
    }
    &__left {
      background-color: #fff;
      outline: 7px solid #1bb8d1;
      border-radius: 15px;
      padding: 10px 15px;
      margin-right: 48px;
      @media only screen and (max-width: 431px) {
        margin-right: 0;
      }
      .formManual {
        padding: 10px 20px;
        color: #2e363e;
        border-radius: 15px;
        width: 350px;
        text-align: center;
        display: flex;
        flex-direction: column;
        align-items: center;
        @media only screen and (max-width: 431px) {
          width: 100%;
        }
        &__title {
          font-size: 1.375rem;
          font-weight: 600;
          max-width: 216px;
          width: 100%;
          text-align: center;
          line-height: 30px;
        }
        &__subtitle {
          padding-top: 10px;
          display: flex;
          align-items: center;
          font-weight: 200;
          font-size: 0.75rem;
          line-height: 25px;
          max-width: 268px;
          width: 100%;
          &-number {
            font-size: 28px;
            padding-right: 15px;
          }
          p {
            font-size: 16px;
          }
        }
      }
    }
    .information {
      background-color: #fff;
      outline: 7px solid #1bb8d1;
      border-radius: 15px;
      padding: 10px 15px;
      margin-left: 48px;
      display: flex;
      flex-direction: column;
      align-items: center;

      @media only screen and (max-width: 431px) {
        margin-left: 0;
        margin-bottom: 20px;
      }

      .tariff {
        border-radius: 15px;
        padding: 10px 20px;
        padding-bottom: 0;
        color: #2e363e;
        &__title {
          padding-bottom: 22px;
          display: flex;
          align-items: center;
          justify-content: center;
          p {
            font-size: 1.375rem;
            font-weight: 600;
            max-width: 216px;
            width: 100%;
            text-align: center;
            line-height: 30px;
          }
        }
        &__bottom {
          display: flex;
          align-items: center;
          justify-content: center;
        }
        &__left {
          width: 100%;
          margin-right: 5px;
          display: flex;
          flex-direction: column;
          justify-content: center;
          align-items: center;
          .name,
          .price {
            color: #001b48;
            text-align: center;
            background-color: #f0f8ff;
            border-radius: 15px;
            padding: 10px 10px;
            margin-bottom: 10px;
            width: 100%;
            font-size: 18px;
          }
          .price {
            padding: 10px 60px;
          }
        }
        &__right {
          margin-left: 5px;
          background-color: #f0f8ff;
          display: flex;
          justify-content: center;
          border-radius: 15px;
          align-items: center;
          padding: 10px 10px;
          height: 90px;
          margin-bottom: 10px;
          img {
            height: 25px;
          }
        }
      }
      .tariffInfo {
        display: flex;
        width: 100%;
        justify-content: center;
        .leftSide {
          width: 48%;
          margin-right: 5px;
          .type,
          .dailySpeed {
            margin-top: 10px;
            color: #001b48;
            padding: 10px 10px;
            border-radius: 15px;
            background-color: #f0f8ff;
            height: 80px;
            display: flex;
            align-items: center;
            flex-direction: column;
            justify-content: space-around;
          }
          .type {
            &__title {
              font-size: 20px;
            }
            &__subtitle {
              text-align: center;
              font-size: 18px;
            }
          }
          .dailySpeed {
            text-align: center;
            &__title {
              display: flex;
              align-items: center;
              justify-content: center;
              font-size: 20px;
            }
            &__subtitle {
              font-size: 18px;
            }
            p {
              margin: 0;
            }
          }
        }
        .rightSide {
          width: 48%;
          margin-left: 5px;
          .limit,
          .nightlySpeed {
            margin-top: 10px;
            color: #001b48;
            padding: 10px 10px;
            border-radius: 15px;
            background-color: #f0f8ff;
            align-items: center;

            height: 80px;
            display: flex;
            flex-direction: column;
            justify-content: space-around;
          }
          .limit {
            &__title {
              font-size: 20px;
            }
            &__subtitle {
              text-align: center;
              text-transform: uppercase;
              font-size: 18px;
            }
          }
          .nightlySpeed {
            text-align: center;
            &__title {
              font-size: 20px;
              display: flex;
              align-items: center;
              justify-content: center;
            }
            &__subtitle {
              font-size: 18px;
            }
            p {
              margin: 0;

              padding-left: 5px;
            }
          }
        }
      }
      .informationList {
        max-width: 350px;
        width: 100%;
        color: #000;
        padding: 10px 20px;
        background-color: #f0f8ff;
        border-radius: 15px;
        padding: 10px 20px;
        margin-top: 10px;
        display: flex;
        align-items: center;
        justify-content: flex-start;
        &__left {
          img {
            height: 22px;
          }
        }
        &__right {
          padding-left: 15px;
        }
      }
    }
    // .iformation {
    //   // backdrop-filter: blur(10px);
    //   // background-color: #00000096;
    //   max-width: 350px;
    //   width: 100%;
    //   display: flex;
    //   justify-content: center;
    //   align-items: center;
    //   // padding: 0 20px;
    //   flex-direction: column;
    //   border-radius: 5px;
    //   margin-left: 15px;
    //   @media only screen and (max-width: 431px) {
    //     // padding: 10px 20px;
    //     margin-bottom: 15px;
    //     margin-right: 0;
    //     margin-left: 0;
    //   }
    //   .iformationList {
    //     display: flex;
    //     max-width: 700px;
    //     align-items: center;
    //     width: 100%;
    //     justify-content: space-between;
    //     // border-bottom: 1px solid rgba(128, 128, 128, 0.417);
    //     // font-size: 18px;
    //     // padding: 7px 0;
    //     border: 1px solid rgba(128, 128, 128, 0.417);
    //     background: #00000096;
    //     border-radius: 5px;
    //     font-size: 20px;
    //     color: #fff;

    //     margin-bottom: 5px;
    //     padding: 7px 20px;
    //     @media only screen and (max-width: 431px) {
    //       font-size: 18px;
    //       border-bottom: none;
    //       padding: 10px 15px;
    //     }
    //     .title {
    //       color: rgb(193, 191, 191);
    //       margin: 0;
    //     }
    //     .subtitle {
    //       margin: 0;
    //     }
    //     .speedTime {
    //       display: flex;
    //       p {
    //         margin-right: 10px;
    //       }
    //     }
    //   }
    //   .actions {
    //     display: flex;
    //     flex-direction: column;
    //     .actionsTitle {
    //       color: #eba026;
    //       font-weight: bold;
    //       margin: 0;
    //     }
    //     .actionsSubtitle {
    //       margin: 0;
    //       padding-top: 5px;
    //       white-space: pre-wrap;
    //     }
    //   }
    //   .info {
    //     &__logo {
    //       position: relative;
    //       cursor: context-menu;

    //       &-image {
    //         &:hover + .infoText {
    //           display: block;
    //         }
    //       }
    //       .infoText {
    //         display: none;
    //         position: absolute;
    //         bottom: 45px;
    //         background: rgba(246, 246, 246, 0.606);
    //         backdrop-filter: blur(10px);
    //         border-radius: 15px;
    //         color: #000;
    //         width: 250px;
    //         margin: 0;
    //         padding: 10px;
    //         z-index: 1;
    //         white-space: pre-wrap;
    //       }
    //       .mobileinfoText {
    //         @media only screen and (max-width: 431px) {
    //           right: 0;
    //         }
    //       }
    //       .mobileinfoText2 {
    //         @media only screen and (max-width: 431px) {
    //           right: -100px;
    //           // left: 0;
    //         }
    //       }
    //     }
    //   }
    // }
  }
  .bottom {
    display: flex;
    justify-content: space-evenly;
    width: 100%;
    align-items: center;
    margin-top: 30px;
    @media only screen and (max-width: 431px) {
      flex-direction: column-reverse;
      margin-top: 0;
    }
  }
  &__form {
    display: flex;
    flex-direction: column;
    max-width: 350px;
    width: 100%;
    // margin-right: 15px;
    @media only screen and (max-width: 431px) {
      margin-right: 0;
    }
    &-title {
      font-size: 22px;
    }
    input {
      // border: 1px solid rgba(128, 128, 128, 0.417);
      // background: #00000096;
      // border-radius: 5px;
      // color: #fff;

      // font-size: 20px;
      // margin-bottom: 5px;
      // padding: 7px 20px;
      // height: 50px;
      // padding: 8px 20px;
      background-color: #f0f8ff;
      border: none;
      backdrop-filter: blur(10px);
      color: #000;
      // font-size: 22px;
      border-radius: 10px;
      max-width: 350px;
      width: 100%;
      text-align: center;
      margin-top: 10px;
      font-size: 1rem;
      padding: 9px 20px;
      @media only screen and (max-width: 431px) {
        font-size: 18px;
        margin-bottom: 5px;
        // test
        border-bottom: 1px solid grey;
        padding: 10px 15px;
      }
    }
    &-label {
      font-size: 20px;
      padding-bottom: 10px;
    }
    &-button {
      // border: none;
      // font-size: 22px;
      // cursor: pointer;
      // text-decoration: none;
      // color: #fff;
      // background: linear-gradient(to right, #d1b88c 0%, #ec9f1b 100%);
      // padding: 5px 20px;
      // border-radius: 5px;
      // padding: 0 20px;
      // height: 50px;
      background: #1bb8d1;
      color: #fff;
      border: none;
      border-radius: 10px;
      max-width: 350px;
      width: 100%;
      margin-top: 17px;
      // margin-left: 20px;
      // font-size: 22px;
      cursor: pointer;
      transition: all 0.3s;
      font-size: 20px;
      // margin-bottom: 10px;
      padding: 17px 75px;
      @media only screen and (max-width: 431px) {
        font-size: 18px;
      }
    }
  }
}
.modal {
  position: fixed;
  top: 50%;
  left: 50%;
  background: #000;
  color: #fff;
  transform: translate(-50%, -50%);
  z-index: 99;
  width: 100%;
  max-width: 400px;
  text-align: center;
  padding: 30px;
  border-radius: 5px;
  // box-shadow: rgba(50, 50, 93, 0.25) 0px 50px 100px -20px,
  //   rgba(0, 0, 0, 0.3) 0px 30px 60px -30px;
  @media only screen and (max-width: 431px) {
    width: 80%;
    padding: 20px;
    border: 1px solid rgb(193, 191, 191);
  }
  &__title {
    color: #eba026;
    font-size: 28px;
    padding-bottom: 15px;
    @media only screen and (max-width: 431px) {
      font-size: 24px;
      padding-top: 30px;
    }
  }
  &__subtitle {
    font-size: 18px;
    // color: rgb(193, 191, 191);
    color: #eba026;
  }
  &__closeBtn {
    position: absolute;
    top: 5px;
    right: 5px;
    background: none;
    border: none;
    cursor: pointer;
  }
  &__hrLine {
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
      padding: 0 0.5em;
      color: #818078;
      background-color: #fcfcfa;
    }
  }
}

.slide-enter-active,
.slide-leave-active {
  transition: transform 0.5s;
}

.slide-enter,
.slide-leave-to {
  transform: translateY(-50%) translateX(100vw);
}
</style>
