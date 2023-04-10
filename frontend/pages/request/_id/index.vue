<template lang="pug">
section.request.container-fluid(@click='showModal = false' )
  .modalOverlay
  transition(name='slide' appear)
    .modal(v-if='showModal')
      .modal__title Заявка отправлена
      hr.modal__hrLine
      .modal__subtitle С вами свяжутся в течении 15-20 минут
      button(@click='showModal = false').modal__closeBtn 
        MaterialIcon(:icon='mdiClose')
  .top
    .iformation
      .iformationList
        .iformationList__left  
          p.title Провайдер 
        .iformationList__right
          p.subtitle {{ providerName }}
      .iformationList
        .iformationList__left  
          p.title Тариф 
        .iformationList__right
          p.subtitle {{ tariff }}
      .iformationList
        .iformationList__left  
          p.title Скорость 
        .iformationList__right
          p.subtitle {{ speed }}
      .iformationList
        .iformationList__left  
          p.title Ночная скорость 
        .iformationList__right
          p.subtitle {{ nightSpeed }}
      .iformationList
        .iformationList__left  
          p.title Цена 
        .iformationList__right
          p.subtitle {{ price }} сум
      .iformationList
        .iformationList__left  
          p.title Лимит 
        .iformationList__right
          p.subtitle {{ limit }}
      .iformationList
        .iformationList__left  
          p.title Тип 
        .iformationList__right
          p.subtitle {{ tech }}

  
    
    
  .bottom
    form.request__form(action="" method="post", @submit.prevent="formSubmit")
      input(placeholder="Введите имя" required type="text" id="name" name="name" v-model='post.name' )
      input(placeholder="Введите номер телефона" required type="tel"  id="phone" name="phone" v-model='post.phone' )
      input(placeholder="Введите город" required type="text" id="city" name="city" v-model='post.city' )
      input(placeholder="Введите район" required type="text" id="district" name="district" v-model='post.district' )
      input(placeholder="Введите улицу"  type="text" id="street" name="street" v-model='post.street' )
      input(placeholder="Введите дом" required type="text" id="house" name="house" v-model='post.house' )
      input(type="hidden" name="plan_id"  id='tariff' :value='this.$route.params.id' )
      button.request__form-button(type="submit" value="submit") Отправить
    yandex-map(:coords="location", :zoom='18'  class="map", @actionend='onActionEnd' @map-was-initialized='mapInit')



</template>

<script>
import axios from 'axios'
import { mdiClose } from '@mdi/js'

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

      location: [41.311151, 69.279737],
      mdiClose,
      post: {
        name: '',
        phone: '',
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
    this.providerName = this.tariffInfo.provider_name.toUpperCase()
    this.tariff = this.tariffInfo.title
    this.speed = this.tariffInfo.speed
    this.nightSpeed = this.tariffInfo.night
    this.price = this.tariffInfo.price
    this.limit = this.tariffInfo.limit.toUpperCase()
    this.tech = this.tariffInfo.tech
    // console.log(this.tariffInfo)
  },

  methods: {
    formSubmit() {
      axios
        .post('https://internetbor.uz/api/v1/callbacks', this.post)
        .then((response) => {
          this.post.name = ''
          this.post.phone = ''
          this.post.city = ''
          this.post.district = ''
          this.post.street = ''
          this.post.house = ''

          this.showModal = true
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
  max-width: 550px;
  width: 100%;
  height: 492px;
  border-radius: 5px;
  overflow: hidden;
  @media only screen and (max-width: 420px) {
    height: 300px;
    margin-bottom: 30px;
  }
}
.ymap-container {
  // border-radius: 5px;
  // overflow: hidden;
}

.request {
  padding-top: 60px;

  display: flex;

  justify-content: center;
  align-items: center;
  flex-direction: column;
  .top {
    width: 100%;
    display: flex;
    justify-content: center;
    padding-bottom: 60px;
    padding-top: 60px;
    .iformation {
      backdrop-filter: blur(10px);
      background-color: #00000096;
      max-width: 600px;
      width: 100%;
      display: flex;
      justify-content: center;
      align-items: center;
      padding: 20px 20px;
      flex-direction: column;
      border-radius: 5px;
      .iformationList {
        display: flex;
        max-width: 700px;
        align-items: center;
        width: 100%;
        justify-content: space-between;
        border-bottom: 1px solid rgba(128, 128, 128, 0.417);
        font-size: 20px;
        padding: 15px 0;
        @media only screen and (max-width: 420px) {
          font-size: 18px;
          padding: 15px;
          border-bottom: none;
        }
        .title {
          color: rgb(193, 191, 191);
          margin: 0;
        }
        .subtitle {
          margin: 0;
        }
      }
    }
  }
  .bottom {
    display: flex;
    justify-content: space-around;
    width: 100%;
    align-items: center;
    @media only screen and (max-width: 420px) {
      flex-direction: column-reverse;
    }
  }
  &__form {
    display: flex;
    flex-direction: column;

    max-width: 400px;
    width: 100%;
    &-title {
      font-size: 22px;
    }
    input {
      border: 1px solid rgba(128, 128, 128, 0.417);
      background: #00000096;
      border-radius: 5px;
      font-size: 24px;
      color: #fff;

      margin-bottom: 15px;
      padding: 15px 20px;
      @media only screen and (max-width: 420px) {
        font-size: 18px;
        margin-bottom: 10px;
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
      padding: 10px 20px;
      border-radius: 5px;

      @media only screen and (max-width: 420px) {
        font-size: 18px;
      }
    }
  }
}

.modalOverlay {
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
  @media only screen and (max-width: 420px) {
    width: 70%;
    padding: 20px;
  }
  &__title {
    font-size: 28px;
    padding-bottom: 15px;
    @media only screen and (max-width: 420px) {
      font-size: 18px;
      padding-top: 30px;
    }
  }
  &__subtitle {
    color: rgb(193, 191, 191);
  }
  &__closeBtn {
    position: absolute;
    top: 5px;
    right: 5px;
    background: none;
    border: none;
    cursor: pointer;
    @media only screen and (max-width: 420px) {
    }
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
      color: black;

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
