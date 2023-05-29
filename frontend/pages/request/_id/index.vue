<template lang="pug">
section.request.container-fluid(@click='showModal = false' )
  //- .modalOverlay
  //- transition(name='slide' appear)

  .top

    form.request__form(action="" method="post", @submit.prevent="formSubmit")
      input(:placeholder=`$t('name')` required type="text" id="name" name="name" v-model='post.name' )
      input(:placeholder=`$t('phoneNumber')`, v-maska data-maska='+998 (##) ### ## ##', pattern=".{19,}"  required  id="phone" name="phone" v-model='post.phone' )
      input(:placeholder=`$t('city')` required type="text" id="city" name="city" v-model='post.city' )
      input(:placeholder=`$t('district')` required type="text" id="district" name="district" v-model='post.district' )
      input(:placeholder=`$t('street')`  type="text" id="street" name="street" v-model='post.street' )
      input(:placeholder=`$t('house')` required type="text" id="house" name="house" v-model='post.house' )
      input(type="hidden" name="plan_id"  id='tariff' :value='this.$route.params.id' )
      button.request__form-button(type="submit" value="submit") {{ $t('send') }}
    .iformation
      .iformationList
        .iformationList__left  
          p.title {{ $t('provider') }} 
        .iformationList__right
          p.subtitle {{ providerName }}
      .iformationList
        .iformationList__left  
          p.title {{ $t('tariff') }} 
        .iformationList__right
          p.subtitle {{ tariff }}
      .iformationList
        .iformationList__left.speedTime  
          p.title {{ daily_speed_time}} 
          MaterialIcon(:icon='mdiClockOutline' size='25px')
        .iformationList__right
          p.subtitle {{ speed }}
      .iformationList
        .iformationList__left.speedTime  
          p.title {{ nightly_speed_time }}
          MaterialIcon(:icon='mdiClockOutline' size='25px')

        .iformationList__right
          p.subtitle {{ nightSpeed }}
      .iformationList
        .iformationList__left  
          p.title {{ $t('price') }} 
        .iformationList__right
          p.subtitle {{ price }} {{ $t('priceMonth') }}
      .iformationList
        .iformationList__left  
          p.title {{ $t('limit') }} 
        .iformationList__right
          p.subtitle {{ limit }}
      .iformationList
        .iformationList__left  
          p.title {{ $t('type') }} 
        .iformationList__right
          p.subtitle {{ tech }}
      .iformationList.info
        .info__logo(:style=`routerText?.length ? 'cursor: context-menu' : 'cursor: no-drop'`)
          MaterialIcon.info__logo-image(:icon='mdiRouterWireless' :color=`router ? '#fff' : '#000'` size='30px')
          p.infoText(v-if='routerText?.length') {{ routerText }}
        .info__logo(:style=`tvText?.length ? 'cursor: context-menu' : 'cursor: no-drop'`)
          MaterialIcon.info__logo-image(:icon='mdiTelevisionBox' :color=`tv ? '#fff' : '#000'` size='30px')
          p.infoText.mobileinfoText2(v-if='tvText?.length')  {{ tvText }}
        .info__logo(:style=`cableText?.length ? 'cursor: context-menu' : 'cursor: no-drop'`)
          MaterialIcon.info__logo-image(:icon='mdiCableData' :color=`cable ? '#fff' : '#000'` size='30px')
          p.infoText.mobileinfoText2(v-if='cableText?.length') {{ cableText }}
        .info__logo(:style=`additionallyInfo?.length ? 'cursor: context-menu' : 'cursor: no-drop'`)
          MaterialIcon.info__logo-image(:icon='mdiInformation' :color=`additionallyInfo?.length ? '#fff' : '#000'` size='30px')
          p.infoText.mobileinfoText(v-if='additionallyInfo?.length') {{ additionallyInfo }}
      .iformationList.actions(v-if="this.tariffInfo.info?.length")
        .iformationList__right
          p.actionsTitle {{ $t('action') }}
        .informationList__left 
          p.actionsSubtitle {{ actions }}

  
    
    
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
    this.actions = this.tariffInfo.info
    this.router = this.tariffInfo.router
    this.routerText = this.tariffInfo.router_text
    this.tv = this.tariffInfo.tv
    this.tvText = this.tariffInfo.tv_text
    this.cable = this.tariffInfo.cabel
    this.cableText = this.tariffInfo.cabel_text
    this.additionallyInfo = this.tariffInfo.more_info
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
<style lang="scss">
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
  // border-radius: 5px;
  // overflow: hidden;
}

.request {
  padding-top: 100px;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  @media only screen and (max-width: 431px) {
    padding-bottom: 30px;
    padding-top: 70px;
  }
  .top {
    width: 100%;
    display: flex;
    justify-content: center;
    align-items: flex-start;
    @media only screen and (max-width: 431px) {
      flex-direction: column-reverse;
      align-items: center;
      padding-bottom: 30px;
    }
    .iformation {
      // backdrop-filter: blur(10px);
      // background-color: #00000096;
      max-width: 350px;
      width: 100%;
      display: flex;
      justify-content: center;
      align-items: center;
      // padding: 0 20px;
      flex-direction: column;
      border-radius: 5px;
      margin-left: 15px;
      @media only screen and (max-width: 431px) {
        // padding: 10px 20px;
        margin-bottom: 15px;
        margin-right: 0;
        margin-left: 0;
      }
      .iformationList {
        display: flex;
        max-width: 700px;
        align-items: center;
        width: 100%;
        justify-content: space-between;
        // border-bottom: 1px solid rgba(128, 128, 128, 0.417);
        // font-size: 18px;
        // padding: 7px 0;
        border: 1px solid rgba(128, 128, 128, 0.417);
        background: #00000096;
        border-radius: 5px;
        font-size: 20px;
        color: #fff;

        margin-bottom: 5px;
        padding: 7px 20px;
        @media only screen and (max-width: 431px) {
          font-size: 18px;
          border-bottom: none;
          padding: 10px 15px;
        }
        .title {
          color: rgb(193, 191, 191);
          margin: 0;
        }
        .subtitle {
          margin: 0;
        }
        .speedTime {
          display: flex;
          p {
            margin-right: 10px;
          }
        }
      }
      .actions {
        display: flex;
        flex-direction: column;
        .actionsTitle {
          color: #eba026;
          font-weight: bold;
          margin: 0;
        }
        .actionsSubtitle {
          margin: 0;
          padding-top: 5px;
          white-space: pre-wrap;
        }
      }
      .info {
        &__logo {
          position: relative;
          cursor: context-menu;

          &-image {
            &:hover + .infoText {
              display: block;
            }
          }
          .infoText {
            display: none;
            position: absolute;
            bottom: 45px;
            background: rgba(246, 246, 246, 0.606);
            backdrop-filter: blur(10px);
            border-radius: 15px;
            color: #000;
            width: 250px;
            margin: 0;
            padding: 10px;
            z-index: 1;
            white-space: pre-wrap;
          }
          .mobileinfoText {
            @media only screen and (max-width: 431px) {
              right: 0;
            }
          }
          .mobileinfoText2 {
            @media only screen and (max-width: 431px) {
              right: -100px;
              // left: 0;
            }
          }
        }
      }
    }
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
    margin-right: 15px;
    @media only screen and (max-width: 431px) {
      margin-right: 0;
    }
    &-title {
      font-size: 22px;
    }
    input {
      border: 1px solid rgba(128, 128, 128, 0.417);
      background: #00000096;
      border-radius: 5px;
      color: #fff;

      font-size: 20px;
      margin-bottom: 5px;
      padding: 7px 20px;
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
      border: none;
      font-size: 22px;
      cursor: pointer;
      text-decoration: none;
      color: #fff;
      background: linear-gradient(to right, #d1b88c 0%, #ec9f1b 100%);
      padding: 5px 20px;
      border-radius: 5px;

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
