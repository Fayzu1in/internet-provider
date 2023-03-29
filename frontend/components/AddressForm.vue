<template lang="pug">
section.addressFormSection.container-fluid
  form.addressForm(action="" method="post", @submit.prevent="formSubmit")
    label(for='city')
      select.addressForm__field(id='type' name='type' required v-model='selectedCity')
        option(value='' disable selected) Выберите город
        option(value='Tashkent') Tashkent
    label.inputWrapper(for='street')
      input.addressForm__field(type='text' placeholder='Укажите улицу' v-model="inputText" @input="showSuggestions = inputText.length > 0" required @click='suggestion' )
      ul.suggestionList(v-if="showSuggestions")
        li.suggestionItem(v-for="word in filteredWords" :key="word.id" @click="selectSuggestion(word.street)") {{ word.street }}
    button.searchProviders Найти провайдеров
  div
    transition-group(name='fade')
      div.availableProviders(v-if='switc' key='dynamic' class='animated')
        p.availableProviders__title Доступные провайдеры на вашей улице
        div(v-for='available in availableProviders')
          NuxtLink.availableProviders__names(:to='(`/providers/${available}`)') {{ available.toUpperCase() }}
        
      //- div(key='main-content')

      

</template>
<script>
import axios from 'axios'

export default {
  data() {
    return {
      selectedCity: '',
      streets: [],
      inputText: '',
      showSuggestions: false,
      // SuggestionList: true,
      topProviders: null,
      response: null,
      switc: false,
      availableProviders: '',
    }
  },
  async fetch() {
    this.streets = await this.$axios.$get(
      'http://127.0.0.1:8000/api/v1/coverage/'
    )
    // console.log(this.streets)
  },

  computed: {
    filteredWords() {
      const uniqueWords = this.streets.reduce((acc, word) => {
        if (!acc[word.street]) {
          acc[word.street] = word
        }
        return acc
      }, {})
      return Object.values(uniqueWords).filter((word) => {
        return word.street.toLowerCase().includes(this.inputText.toLowerCase())
      })
    },
  },

  methods: {
    formSubmit() {
      axios
        .get(`http://127.0.0.1:8000/api/v1/coverage/?street=${this.inputText}`)
        .then((response) => {
          this.response = response.data[0]
          console.log(this.response)
          this.availableProviders = this.response.providers.split(',')
          console.log(this.availableProviders)

          if (this.response != null) {
            this.switc = true
          }
          // console.log(this.inputText)
        })
    },

    selectSuggestion(word) {
      this.inputText = word
      this.SuggestionList = false
      this.showSuggestions = false
    },
    suggestion() {
      this.showSuggestions = !this.showSuggestions
    },
  },
}
</script>
<style lang="scss" scoped>
.addressFormSection {
  display: flex;
  justify-content: center;
  flex-direction: column;
  align-items: center;
  padding-top: 50px;
}
.inputWrapper {
  position: relative;
}
.addressForm {
  max-width: 800px;
  width: 100%;
  // margin-top: 60px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  @media only screen and (max-width: 420px) {
    flex-direction: column;
    align-items: center;
  }
  &__field {
    height: 50px;
    padding: 8px 16px;
    background-color: #00000081;
    color: #fff;
    border: none;
    border-radius: 5px;
    // width: 250px;
    // margin-bottom: 20px;
    margin-left: 20px;
    font-size: 20px;
    box-shadow: rgb(38, 57, 77) 0px 20px 30px -10px;

    // border-bottom: 2px solid #fdb931;
    // border-bottom: 2px solid #fff;

    // position: relative;
    width: 100%;
    @media only screen and (max-width: 420px) {
      margin-left: 0;
      margin-bottom: 10px;
      width: 250px;
    }
  }
  .suggestionList {
    position: absolute;
    font-size: 18px;
    top: 50px;
    left: 20px;
    width: 100%;
    max-height: 200px;
    overflow-y: auto;
    background-color: #00000096;
    // border: 1px solid #fdb931;
    border-top: none;
    border-radius: 5px;
    box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
    list-style: none;
    padding: 5px 10px;
    margin: 0;
    @media only screen and (max-width: 420px) {
      left: 0;
    }
  }
}
.searchProviders {
  padding: 0 20px;
  height: 50px;
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
  // background: #00000096;
  background: linear-gradient(to right, #aeb2b6 0%, #283c4c 100%);
  box-shadow: rgb(38, 57, 77) 0px 20px 30px -10px;

  color: #fff;
  border: none;
  border-radius: 5px;
  width: 250px;
  margin-left: 20px;
  font-size: 20px;
  cursor: pointer;
  transition: all 0.3s;
  &:hover {
    background: #000;
  }
  @media only screen and (max-width: 420px) {
    margin-left: 0;
  }
}
.fade-enter,
.fade-leave-active {
  opacity: 0;
  transform: translateX();
}
.fade-leave-active {
  position: absolute;
}

.animated {
  transition: all 0.5s;
  display: flex;
  flex-direction: column;
  width: 100%;
}
.availableProviders {
  background-color: #00000096;
  border-radius: 5px;
  margin-top: 30px;
  padding: 20px 30px;
  @media only screen and (max-width: 420px) {
    max-width: 300px;
    width: 100%;
  }

  &__title {
    font-size: 20px;
    // line-height: 0;
    margin: 0;
    // padding-bottom: 50px
    color: grey;
    @media only screen and (max-width: 420px) {
      font-size: 18px;
      line-height: 1;
      text-align: center;
      padding-bottom: 10px;
    }
  }
  &__names {
    color: #fff;
    text-decoration: none;
    display: flex;
    justify-content: space-around;
    font-size: 24px;
    transition: color 0.3s;
    margin-top: 30px;
    margin-bottom: 10px;
    &:hover {
      color: grey;
    }

    @media only screen and (max-width: 420px) {
      flex-direction: column;
      align-items: center;
      // margin-bottom: 10px;
    }
  }
}
</style>
