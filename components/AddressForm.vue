<template lang="pug">
section.addressForm
  label(for='city')
    select.addressForm__field(id='type' name='type')
      option(value='' disable selected) Выберите город
      option(value='Tashkent') Tashkent
      option(value='Samarqand') Samarqand
      option(value='Nukus') Nukus
  label(for='street')
    input.addressForm__field(type='text' placeholder='Укажите улицу')
  //- select.addressForm__field(id='type' name='type')
  //-   option(value='' disable selected) Выберите улицу
  //-   option(value='flat') test1
  //-   option(value='office') test2
  //-   option(value='cottage') tes3

  label(for='type')
    select.addressForm__field(id='type' name='type')
      option(value='' disable selected) Тип подключения
      option(value='flat') Квартира
      option(value='office') Офис
      option(value='cottage') Дача
  button.searchProviders Найти провайдеров

</template>
<script>
export default {
  data() {
    return {}
  },
}
</script>
<style lang="scss">
.addressForm {
  margin-top: 60px;
  display: flex;
  // flex-direction: column;
  align-items: center;
  justify-content: center;
  &__field {
    height: 50px;
    padding: 0 15px;
    background-color: #00000081;
    color: #fff;
    border: none;
    border-radius: 5px;
    // width: 250px;
    // margin-bottom: 20px;
    margin-left: 20px;
    font-size: 20px;
    border-bottom: 2px solid #fdb931;
  }
}
.searchProviders {
  padding: 0 20px;
  height: 50px;
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
  color: #fff;
  border: none;
  border-radius: 5px;
  width: 250px;
  margin-left: 20px;
  font-size: 20px;
  cursor: pointer;
  transition: all 0.3s;
}
</style>
