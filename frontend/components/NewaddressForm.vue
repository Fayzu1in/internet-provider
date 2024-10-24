<template lang="pug">
div
  form.addressForm(action="" method="post", @submit.prevent="formSubmit")
    .addressForm__district
      label.inputWrapper(for='city')
        input.addressForm__field(type='text' :placeholder=`$t('city')` required v-model="inputCity" @input="showCities = inputCity.length > 0" @click="showCities = !showCities, showDistrict = false, showStreets = false" )
        ul.suggestionList(v-if="showCities" )
          li.suggestionItem(v-for="city in city" @click="selectCity(city.city)") {{ city.city }}
    .addressForm__district
      label.inputWrapper(for='district')
        input.addressForm__field(type='text' :placeholder=`$t('district')` required v-model="inputDistrict" @input="showDistrict = inputDistrict.length > 0" @click='suggestion' :disabled="isSecondDisabled" )
        ul.suggestionList(v-if="showDistrict" )
          li.suggestionItem(v-for="district in district"  @click="selectDistrict(district.district)") {{ district.district }}
    .addressForm__street
      label.inputWrapper(for='street')
        input.addressForm__field(type='text' :placeholder=`$t('street')` required v-model="inputStreets" @input="showStreets = inputStreets.length > 0" @click="showStreets = !showStreets, showCities = false, showHouses = false, showDistrict = false" :disabled="isThirdDisabled" )
        ul.suggestionList(v-if="showStreets")
          li.suggestionItem(v-for="str in street"  @click="selectStreet(str.street)") {{ str.street }}
    .addressForm__house 
      label.inputWrapper(for='house')
        input.addressForm__field(type='text' :placeholder=`$t('house')` required v-model="inputHouse" @click='showHouses = !showHouses, showStreets = false, showDistrict=false, showCities= false' :disabled="isForthDisabled", style="border-right: none")
        ul.suggestionList(v-if="showHouses")
          li.suggestionItem(v-for="house in this.housesByStreets" @click="selectHouse(house)" ) {{ house }}
    button.addressForm__search {{ $t('search') }}
  FoundedProviders(:availableProviders='availableProviders', :bestOfAvailable='bestOfAvailable', v-if='showFoundedProviders', @hide='showFoundedProviders = false')

</template>
<script>
import axios from 'axios'
export default {
  data() {
    return {
      showDistrict: false,
      showCities: false,
      showStreets: false,
      showHouses: false,
      districtByCities: [],
      streets: [],
      inputCity: '',
      inputDistrict: '',
      inputStreets: '',
      inputHouse: '',
      showFoundedProviders: false,
    }
  },
  async fetch() {
    this.streets = await this.$axios.$get(
      'https://internetbor.uz/api/v1/coverage-cities/'
    )
  },
  computed: {
    city() {
      const uniqueWords = this.streets.reduce((acc, cur) => {
        if (!acc[cur.city]) {
          acc[cur.city] = cur
        }
        return acc
      }, {})

      const cities = Object.values(uniqueWords)

      if (cities.some((c) => c.city === this.inputCity)) {
        return cities
      }

      return cities.filter((cur) => {
        return cur.city.toLowerCase().includes(this.inputCity.toLowerCase())
      })
    },

    district() {
      const uniqueWords = this.districtByCities.reduce((acc, cur) => {
        if (!acc[cur.district]) {
          acc[cur.district] = cur
        }
        return acc
      }, {})

      const districts = Object.values(uniqueWords)

      if (districts.some((d) => d.district === this.inputDistrict)) {
        return districts
      }

      return Object.values(uniqueWords).filter((cur) => {
        return cur.district
          .toLowerCase()
          .includes(this.inputDistrict.toLowerCase())
      })
    },
    street() {
      const uniqueWords = this.streetsByDistrict.reduce((acc, cur) => {
        if (!acc[cur.street]) {
          acc[cur.street] = cur
        }
        return acc
      }, {})
      return Object.values(uniqueWords).filter((cur) => {
        return cur.street
          .toLowerCase()
          .includes(this.inputStreets.toLowerCase())
      })
    },
    isSecondDisabled() {
      return !this.inputCity
    },
    isThirdDisabled() {
      return !this.inputDistrict
    },
    isForthDisabled() {
      return !this.inputStreets
    },
  },
  methods: {
    selectCity(word) {
      this.inputDistrict = ''
      this.inputStreets = ''
      this.inputHouse = ''
      this.districtByCities = this.streets.filter((obj) => obj.city === word)
      this.districtByCities = this.districtByCities.reduce((acc, obj) => {
        const foundIndex = acc.findIndex(
          (item) => item.district === obj.district
        )
        if (foundIndex === -1) {
          acc.push(obj)
        } else {
          acc[foundIndex] = obj
        }
        return acc
      }, [])
      this.selectedCity = word
      this.inputCity = word
      this.showCities = false
    },
    selectDistrict(word) {
      this.inputStreets = ''
      this.inputHouse = ''
      this.streetsByDistrict = this.streets.filter(
        (obj) => obj.district === word
      )
      this.streetsByDistrict = this.streetsByDistrict.reduce((acc, obj) => {
        const foundIndex = acc.findIndex((item) => item.street === obj.street)
        if (foundIndex === -1) {
          acc.push(obj)
        } else {
          acc[foundIndex] = obj
        }
        return acc
      }, [])
      // console.log(this.streetsByDistrict)
      this.inputDistrict = word
      this.SuggestionList = false
      this.showDistrict = false
    },
    selectStreet(word) {
      this.inputStreets = word
      this.showStreets = false
      this.housesByStreets = axios
        .get(
          `https://internetbor.uz/api/v1/coverage/?street=${word}&district=${this.inputDistrict}`
        )
        .then((response) => {
          this.housesByStreets = response.data[0].houses
          // console.log(this.housesByStreets)
        })
    },
    selectHouse(word) {
      this.inputHouse = word
      this.showHouses = false
    },

    suggestion() {
      this.showDistrict = !this.showDistrict
      this.showCities = false
      this.showStreets = false
      this.showHouses = false
    },
    formSubmit() {
      this.loading = true
      axios
        .get(
          `https://internetbor.uz/api/v1/coverage-check/?district=${this.inputDistrict}&street=${this.inputStreets}&house=${this.inputHouse}`
        )
        .then((response) => {
          this.response = response.data
          console.dir(this.response)
          // console.log('response', this.response)
          this.inputCity = ''
          this.inputDistrict = ''
          this.inputStreets = ''
          this.inputHouse = ''
          if (this.response.providers !== null) {
            this.availableProviders = this.response.providers
            this.showHouses = false
            this.showCities = false
            this.showDistrict = false
            this.showStreets = false
            let result = []
            for (const obj of this.availableProviders) {
              result = result.concat(obj.provider_best)
              this.bestOfAvailable = result
            }
            this.showFoundedProviders = true
          }

          if (this.response.providers === null) {
            this.notFounded = true
          }
        })
        .catch((error) => {
          console.error('Error:', error)
        })
        .finally(() => {
          this.loading = false
        })
      axios
        .get(
          `https://internetbor.uz/api/v1/coverage/?street=${this.inputStreets}`
        )
        .then((data) => {
          this.providersByStreet = data.data[0].providers
        })
        .catch((error) => {
          console.error('Error:', error)
        })
        .finally(() => {
          this.loading = false
        })
    },
  },
}
</script>
<style lang="scss">
input:focus {
  outline: none;
}
.addressForm {
  display: flex;
  align-items: center;
  background-color: #fff;
  border-radius: 30px;
  overflow: hidden;
  padding: 5px 14px;
  box-shadow: rgba(255, 255, 255, 0.1) 0px 1px 1px 0px inset,
    rgba(50, 50, 93, 0.25) 0px 50px 100px -20px,
    rgba(0, 0, 0, 0.3) 0px 30px 60px -30px;
  overflow: visible;
  @media only screen and (max-width: 576px) {
    flex-direction: column;
  }
  label {
    margin-bottom: 0;
  }
  &__field {
    padding: 30px 10px;
    border: none;
    text-align: center;

    padding-bottom: 25px;
    border-right: 1px solid #3f62a7;
    font-size: 1.125rem;
  }
  &__search {
    border: none;
    background-color: #3f62a7;
    border-radius: 999px;
    font-size: 1.25rem;
    color: #fff;
    padding: 20px 25px;
    cursor: pointer;
  }
  .inputWrapper {
    position: relative;
    .suggestionList {
      list-style: none;
      background-color: #fff;
      position: absolute;
      width: fit-content;
      top: 40px;
      padding: 10px 20px;
      border-bottom-left-radius: 15px;
      border-bottom-right-radius: 15px;
      width: 100%;
      overflow: auto;
      max-height: 270px;
      .suggestionItem {
        font-size: 1rem;
        color: #3f62a7;
        font-weight: 200;
        padding-bottom: 10px;

        text-align: left;
        cursor: pointer;
        &:hover {
          text-decoration: underline;
        }
      }
    }
  }
}
</style>
