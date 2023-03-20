<template lang="pug">
section.request.container-fluid
  .modalOverlay(@click='showModal = false' v-if='showModal')
  transition(name='slide' appear)
    .modal(v-if='showModal')
      .modal__title Заявка отправлена
      hr.modal__hrLine
      .modal__subtitle С вами свяжутся в течении 15-20 минут
      button(@click='showModal = false').modal__closeBtn 
        MaterialIcon(:icon='mdiClose')
  .request__detail
    h1 Detail
  .bottom
    form.request__form(action="" method="post", @submit.prevent="formSubmit")
      p.request__form-title Заявка на подключение интернета
      //- label.request__form-label(for='name') Введите имя
      input(placeholder="Введите имя" required type="text" id="name" name="name" v-model='post.name' )
      //- label.request__form-label(for='phone') Введите номер телефона
      input(placeholder="Введите номер телефона" required type="tel"  id="phone" name="phone" v-model='post.phone' )
      //- label.request__form-label(for='city') Введите город
      input(placeholder="Введите город" required type="text" id="city" name="city" v-model='post.city' )
      //- label.request__form-label(for='district') Введите район
      input(placeholder="Введите район" required type="text" id="district" name="district" v-model='post.district' )
      //- label.request__form-label(for='street') Введите улицу
      input(placeholder="Введите улицу"  type="text" id="street" name="street" v-model='post.street' )
      //- label.request__form-label(for='house') Введите дом
      input(placeholder="Введите дом" required type="text" id="house" name="house" v-model='post.house' )
      //- button(@click='test()') Найти меня на карте
      button.request__form-button(type="submit" value="submit") Отправить
    yandex-map(:coords="location", :zoom='18'  class="map", @actionend='onActionEnd' @map-was-initialized='mapInit')
  //- @autopanbegin='mapEvent'


</template>
<!-- <script
  src="https://api-maps.yandex.ru/2.1/?apikey=257d086b-7f6d-4767-b170-0073c6f47bd0&lang=ru_RU"
  type="text/javascript"
></script> -->
<script>
import axios from 'axios'
import { mdiClose } from '@mdi/js'
// import { log } from 'console'
// import { loadYmap } from 'vue-yandex-maps'

export default {
  data() {
    return {
      locationText: '',
      showModal: false,
      yData: '',
      // newBound: [41.311151, 69.279737],
      location: [41.311151, 69.279737],
      mdiClose,
      post: {
        name: '',
        phone: '',
        city: '',
        district: '',
        street: '',
        house: '',
      },
    }
  },
  // mounted() {
  //   loadYmap().then(() => {
  //     window.ymaps.geolocation.get()
  //     console.log(window.ymaps.Map('map'))
  //   })
  // this.location = ymaps.geolocation.get()
  // },
  methods: {
    formSubmit() {
      axios
        .post('http://127.0.0.1:8000/api/v1/callbacks', this.post)
        .then((response) => {
          this.post.name = ''
          this.post.phone = ''
          this.post.city = ''
          this.post.district = ''
          this.post.street = ''
          this.post.house = ''
          this.showModal = true
          // console.log(response)
        })
    },
    mapInit(e) {
      console.log(e)
      window.ymaps.geolocation.get().then((res) => {
        e.geoObjects.add(res.geoObjects)
        this.location = res.geoObjects.position
      })
    },
    mapEvent(e) {
      // this.some = window.ymaps.Map('map', {
      //   center: this.location,
      //   zoom: 18,
      // })
      // console.log(e)
    },
    onActionEnd(event) {
      const coords = event.get('target').getCenter()
      window.ymaps.geocode(coords).then((result) => {
        const firstGeoObject = result.geoObjects.get(0)
        this.locationText = firstGeoObject.getAddressLine()
        // const strings = this.locationText.split(', ')
        const [city, district, street] = this.locationText.split(', ')
        console.log(this.locationText)
        this.post.city = city
        this.post.district = district
        this.post.street = street
        // console.log(this.city)
      })
    },
  },
  // test() {
  //   // eslint-disable-next-line no-undef
  //   this.yData = ymaps.geolocation.get()
  //   console.log(this.yData)
  // },
}
</script>
<style lang="scss">
.map {
  max-width: 600px;
  width: 100%;
  height: 400px;
}
.about {
  // padding-top: 60px;
}
.request {
  padding-top: 60px;
  // padding-bottom: 60px;
  display: flex;
  // justify-content: flex-start;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  .bottom {
    display: flex;
    justify-content: space-around;
    width: 100%;
    align-items: center;
  }
  &__form {
    display: flex;
    flex-direction: column;
    // padding-top: 60px;
    max-width: 400px;
    width: 100%;
    &-title {
      font-size: 22px;
    }
    input {
      border: none;
      background: #00000096;
      // text-align: left;
      font-size: 24px;
      color: #fff;
      // border-radius: 5px;
      margin-bottom: 15px;
      padding: 15px 20px;
    }
    &-label {
      font-size: 20px;
      padding-bottom: 10px;
      // color: grey;
    }
    &-button {
      border: none;
      font-size: 22px;
      cursor: pointer;
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
      padding: 7px 30px;
      border-radius: 5px;
    }
  }
}
.modalOverlay {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  z-index: 98;
  background: rgba(0, 0, 0, 0.4);
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
  box-shadow: rgba(50, 50, 93, 0.25) 0px 50px 100px -20px,
    rgba(0, 0, 0, 0.3) 0px 30px 60px -30px;
  &__title {
    font-size: 28px;
    padding-bottom: 15px;
  }
  &__subtitle {
    color: grey;
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
      color: black;

      padding: 0 0.5em;
      // line-height: 1.5em;
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
