<template lang="pug">
section.address
  form.addressForm(action="" method="post", @submit.prevent="formSubmit")
    label(for='city')
      select.addressForm__field(id='type' name='type' required)
        option(value='' disable selected) Выберите город
        option(value='Tashkent') Tashkent
    label.inputWrapper(for='street')
      input.addressForm__field(type='text' placeholder='Укажите улицу' v-model="inputText" @input="showSuggestions = inputText.length > 0" required @click='suggestion' )
      ul.suggestionList(v-if="showSuggestions")
        li.suggestionItem(v-for="word in filteredWords" :key="word.id" @click="selectSuggestion(word.street)") {{ word.street }}
    button.searchProviders Найти провайдеров

</template>
<script>
export default {
  data() {
    return {
      streets: [],
      inputText: '',
      showSuggestions: false,
      // SuggestionList: true,
      topProviders: null,
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
  // watch: {
  // inputText(newValue) {
  //   if (newValue.length > 0) {
  //     this.showSuggestions = true
  //   }
  // },
  // },

  methods: {
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
.address {
  display: flex;
  justify-content: center;
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
    border-bottom: 2px solid #fdb931;
    // position: relative;
    width: 100%;
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
    border: 1px solid #fdb931;
    border-top: none;
    border-radius: 5px;
    box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
    list-style: none;
    padding: 5px 10px;
    margin: 0;
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
