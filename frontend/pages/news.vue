<template lang="pug">
section.newsSection.container-fluid
  .cardSection(v-for="item in news" :key='news.id')
    .card(v-if='item.published === true')
      .date {{item.created}}
      .newsCard  
        .newsCard__title {{item.title}}
        .newsCard__subtitle {{ item.text }}

</template>
<script>
export default {
  data() {
    return {
      news: [],
    }
  },
  async fetch() {
    this.news = await this.$axios.$get('https://internetbor.uz/api/v1/news')
    // console.log(this.news)
  },
}
</script>
<style lang="scss" scoped>
.card {
  margin-bottom: 30px;
}
.newsSection {
  padding-top: 100px;
  @media only screen and (max-width: 431px) {
    padding-top: 80px;
  }
  .date {
    font-size: 18px;
    padding-bottom: 5px;
    padding-left: 10px;
  }
  .newsCard {
    background-color: #00000096;
    // box-shadow: rgb(38, 57, 77) 0px 20px 30px -10px;
    padding: 15px 10px;
    display: flex;
    border-radius: 5px;
    display: flex;
    flex-direction: column;
    font-size: 18px;
    @media only screen and (max-width: 431px) {
      font-size: 16px;
      padding: 10px 5px;
    }
    &__title {
      font-size: 22px;
      padding-bottom: 10px;
      @media only screen and (max-width: 431px) {
        font-size: 18px;
      }
    }
  }
}
</style>
