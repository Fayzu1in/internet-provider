<template lang="pug">
section.addressFormSection.container-fluid
  .modalBckg(v-if="modalHelp || switc" @click='modalHelp = false, switc = false')
  .modalRequest(v-if="modalHelp")
    .modalRequest__top 
      .closeModal(@click="modalHelp = false")
        MaterialIcon(:icon='mdiCloseCircleOutline')
      p.title Не можете выбрать тариф ?
      p.subtitle Свяжитесь с нашим оператором и вам помогут
      .modalRequest__help 
        a.helpLink(href="tel:+998909113086") 
          span Позвонить
          MaterialIcon(:icon='mdiPhone')
        a.helpLink(href='https://telegram.me/InternetBor')
          span Телеграм
          img(src='/telegram.svg')
      .modalRequest__bottomLogo 
        img(src="/logo-full.svg")
  .modalRequest(v-if='switc')
    .modalRequest__top
      .closeModal(@click='switc = false')
        MaterialIcon(:icon='mdiCloseCircleOutline')
      p.title Поздравляем!  
      p.subtitle Доступные провайдеры по вашему адресу 
    .modalRequest__middle
      div(v-for="available in availableProviders" ) 
        NuxtLink.availableProvider(:to='(`/provider/${available.provider_id}/`)') 
          img.providerLogo(:src="`${available.provider_picture}`")
    .modalRequest__bottom
      p.subtitle Выгодные тарифы из доступных провайдеров 
      .help
        p Позвоните нам, и наш консультант бесплатно поможет выбрать подходящий вам тариф 
        a.help__phone(href="tel:+998909113086")
          p Позвонить
          MaterialIcon(:icon='mdiPhone')
  form.addressForm(action="" method="post", @submit.prevent="formSubmit")
    label.inputWrapper(for='city')
      input.addressForm__field(type='text' placeholder='Укажите город' v-model="selectedCity" @click="showCities = !showCities, showSuggestions = false" )
      ul.suggestionList(v-if='showCities')
        li.suggestionItem(v-for="word in cities" @click="selectCity(word)") {{ word }}

    label.inputWrapper(for='street')
      input.addressForm__field(type='text' placeholder='Укажите улицу' v-model="inputText" @input="showSuggestions = inputText.length > 0" required @click='suggestion' )
      ul.suggestionList(v-if="showSuggestions" )
        li.suggestionItem(v-for="word in filteredWords" :key="word.id" @click="selectSuggestion(word.street)") {{ word.street }}
    label.inputWrapper(for='house')
      input.addressForm__field(type='text' placeholder="Укажите дом" v-model="inputHome")
    button.searchProviders Найти провайдеров
  div
</template>
<script>
import axios from 'axios'
import { mdiCloseCircleOutline, mdiPhone } from '@mdi/js'

export default {
  data() {
    return {
      mdiCloseCircleOutline,
      mdiPhone,
      selectedCity: '',
      streets: [],
      cities: ['Ташкент'],
      inputCity: '',
      inputText: '',
      inputHome: '',
      showSuggestions: false,
      showCities: false,
      // SuggestionList: true,
      topProviders: null,
      response: null,
      switc: false,
      modalHelp: false,
      availableProviders: [],
      currentIndex: 0,
      hotTariff: null,
      modalBckg: false,
      options: {
        rewind: true,
        width: '250px',
        gap: '20px',
        perPage: 1,
      },
    }
  },
  async fetch() {
    this.streets = await this.$axios.$get(
      'https://internetbor.uz/api/v1/coverage/'
    )
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

  mounted() {
    let clicked = false
    const timer = setInterval(() => {
      if (!clicked) {
        this.modalHelp = true
        this.modalBckg = true
      }
    }, 30000)
    window.addEventListener('click', () => {
      clicked = true
      clearInterval(timer)
    })
  },

  methods: {
    formSubmit() {
      axios
        .get(`https://internetbor.uz/api/v1/coverage/?street=${this.inputText}`)
        .then((response) => {
          this.response = response.data[0]
          this.availableProviders = this.response.providers
          if (this.response != null) {
            this.switc = true
          }

          this.hotTariff = this.availableProviders.map('provider_id')
        })
    },

    selectCity(word) {
      this.selectedCity = word
      this.showCities = false
    },

    selectSuggestion(word) {
      this.inputText = word
      this.SuggestionList = false
      this.showSuggestions = false
    },
    suggestion() {
      this.showSuggestions = !this.showSuggestions
      this.showCities = false
    },
    nextSlide() {
      this.currentIndex = Math.min(
        this.currentIndex + 1,
        this.cards.length - this.itemsToShow
      )
    },
    prevSlide() {
      this.currentIndex = Math.max(this.currentIndex - 1, 0)
    },
  },
}
</script>

<style lang="scss" scoped>
.modalBckg {
  position: fixed;
  top: 0;
  bottom: 0;
  right: 0;
  left: 0;
  background: #0000005f;
}
.modalRequest {
  border: 1px solid rgba(128, 128, 128, 0.417);
  position: fixed;
  max-width: 600px;
  width: 100%;
  border-radius: 5px;
  top: 50%;
  transform: translateY(-50%);
  z-index: 999;
  background-color: #00000096;
  backdrop-filter: blur(10px);
  padding: 10px 20px;
  text-align: center;
  max-height: 100%;
  overflow: scroll;
  transform: translateY(-50%);
  @media only screen and (max-width: 420px) {
    overscroll-behavior: contain;
    top: 50%;
    max-height: 60vh;
    width: 90%;
  }

  .closeModal {
    position: absolute;
    right: 10px;
    top: 10px;
    cursor: pointer;
  }

  .subtitle {
    margin: 0;
    padding-top: 10px;
    font-size: 18px;
    padding-bottom: 15px;
    @media only screen and (max-width: 420px) {
      font-size: 16px;
      padding-top: 10px;
      padding-bottom: 10px;
    }
  }
  &__top {
    @media only screen and (max-width: 420px) {
      padding-top: 30px;
    }
    .title {
      font-size: 32px;
      margin: 0;
      @media only screen and (max-width: 420px) {
        font-size: 24px;
      }
    }
  }
  &__middle {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    .availableProvider {
      border-radius: 5px;
      display: flex;
      flex-direction: column;
      justify-content: center;
      padding: 3px;
      border: 1px solid rgba(128, 128, 128, 0.417);
      margin-left: 10px;
      margin-right: 10px;
      cursor: pointer;
      &:hover {
        border: 1px dashed #fff;
      }
      @media only screen and (max-width: 420px) {
        margin-left: 0;
        margin-right: 0;
        margin-bottom: 10px;
      }
      .providerLogo {
        height: 140px;
        background: #fff;
        width: 140px;
        border-radius: 5px;
      }
      .selectBtn {
        border: none;
        font-size: 18px;
        padding: 5px 0;
        color: #fff;
        background: linear-gradient(to right, #d1b88c 0%, #ec9f1b 100%);
      }
    }
  }
  &__bottom {
    display: flex;
    justify-content: center;
    flex-direction: column;
    align-items: center;
    .splide {
      // margin-top: 20px;
      margin-bottom: 15px;
    }
  }
  &__help {
    display: flex;
    flex-direction: column;
    align-items: center;
    border-top: 1px solid grey;
    padding-top: 10px;
    padding-bottom: 10px;
    .helpLink {
      display: flex;
      align-items: center;
      text-decoration: none;
      color: #fff;
      max-width: 180px;
      width: 100%;
      justify-content: space-around;
      margin-top: 10px;
      margin-bottom: 10px;
      transition: color 0.3s;
      &:hover {
        color: rgb(193, 191, 191);
      }
      @media only screen and (max-width: 420px) {
        justify-content: center;
        margin-bottom: 5px;
        margin-top: 5px;
      }

      span {
        font-size: 26px;
        @media only screen and (max-width: 420px) {
          font-size: 20px;
          padding-right: 10px;
        }
      }
      img {
        height: 30px;
      }
    }
  }

  &__bottomLogo {
    border-top: 1px solid grey;
    img {
      margin-top: 20px;
      height: 40px;
    }
  }
  .help {
    display: flex;
    border-top: 1px solid grey;
    flex-direction: column;
    align-items: center;
    p {
      margin: 10px 0;
    }
    &__phone {
      font-size: 22px;

      display: flex;
      align-items: center;
      justify-content: center;
      color: #fff;
      text-decoration: none;
    }
  }
}
.addressFormSection {
  display: flex;
  justify-content: space-around;
  flex-direction: column;
  align-items: center;
  padding-top: 50px;
  @media only screen and (max-width: 420px) {
    padding-top: 30px;
  }
}
.inputWrapper {
  position: relative;
}
.addressForm {
  max-width: 1030px;
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
    border: 1px solid rgba(128, 128, 128, 0.417);
    backdrop-filter: blur(10px);
    color: #fff;
    // border: none;
    border-radius: 5px;
    // width: 250px;
    // margin-bottom: 20px;
    margin-left: 20px;
    font-size: 18px;
    // box-shadow: rgb(38, 57, 77) 0px 20px 30px -10px;

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
    z-index: 999;
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
    // box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
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
  background: linear-gradient(to right, #d1b88c 0%, #ec9f1b 100%);
  color: #fff;
  border: none;
  border-radius: 5px;
  width: 250px;
  margin-left: 20px;
  font-size: 18px;
  cursor: pointer;
  transition: all 0.3s;

  @media only screen and (max-width: 420px) {
    margin-left: 0;
  }
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
    font-size: 18px;
    margin: 0;
    color: rgb(193, 191, 191);
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
    align-items: center;
    font-size: 24px;
    transition: color 0.3s;
    margin-top: 30px;
    margin-bottom: 10px;
    &:hover {
      color: rgb(193, 191, 191);
    }

    @media only screen and (max-width: 420px) {
      flex-direction: column;
      align-items: center;
    }
  }
}
</style>
