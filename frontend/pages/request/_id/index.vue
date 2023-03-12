<template lang="pug">
section.request.container-fluid
  form.request__form(action="" method="post", @submit.prevent="formSubmit")
    p.request__form-title Заявка на подключение интернета
    //- label.request__form-label(for='name') Введите имя
    input(placeholder="Введите имя" required type="text" id="name" name="name" v-model='post.name')
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
    button.request__form-button(type="submit" value="submit") Отправить
  LocationPicker
</template>
<script>
import axios from 'axios'
export default {
  data() {
    return {
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
  methods: {
    formSubmit() {
      axios
        .post('http://127.0.0.1:8000/api/v1/callbacks/', this.post)
        .then((response) => {
          console.log(response)
        })
    },
  },
}
</script>
<style lang="scss">
.about {
  // padding-top: 60px;
}
.request {
  padding-top: 60px;
  // padding-bottom: 60px;
  display: flex;
  // justify-content: flex-start;
  justify-content: space-between;
  align-items: center;
  &__form {
    display: flex;
    flex-direction: column;
    // padding-top: 60px;
    max-width: 400px;
    width: 100%;
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
</style>
