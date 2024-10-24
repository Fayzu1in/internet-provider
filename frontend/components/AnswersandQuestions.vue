<template lang="pug">
section.container-fluid
  .faqSection
    .faq 
      //- .faq__title {{ $t('questionsAndAnswers') }}
      .faq__list(v-for='item in faq' :key='item.id')
        .question(@click="toggleDropdown(item.id)")
          p {{ item.question }}
          MaterialIcon(:icon='show === item.id ? mdiChevronUp : mdiChevronDown' color='#001b48')
        SmoothReflow(tag='section',)
          .answer(v-show='show === item.id', key="dropdown")
            p {{item.answer}}
</template>
<script>
import { mdiChevronDown, mdiChevronUp } from '@mdi/js'
export default {
  data() {
    return {
      mdiChevronDown,
      mdiChevronUp,
      show: false,
      faq: null,
    }
  },
  async fetch() {
    this.faq = await this.$axios.$get('https://internetbor.uz/api/v1/q&a/')
  },
  methods: {
    toggleDropdown(itemId) {
      this.show = this.show === itemId ? null : itemId
    },
  },
}
</script>
<style lang="scss">
.faqSection {
  display: flex;
  justify-content: center;
  padding-top: 30px;
  .faq {
    max-width: 800px;
    width: 100%;
    display: flex;
    flex-direction: column;
    align-items: center;
    background-color: #fff;
    border-radius: 15px;
    color: #001b48;
    padding: 15px;
    &__title {
      font-size: 32px;
    }
    &__list:not(:last-child) {
      border-bottom: 1px solid #001b48;
    }
    &__list {
      width: 100%;
      font-size: 24px;
      cursor: pointer;
      .question {
        display: flex;
        align-items: center;
        justify-content: space-between;
        width: 100%;
        p {
          margin: 0;
          padding: 10px 0;
        }
      }
      .answer {
        p {
          font-size: 20px;
          margin: 0;
          padding-bottom: 10px;
        }
      }
    }
  }
}
</style>
