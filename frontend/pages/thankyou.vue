<template lang="pug">
section.thanksPage
    .thanks
      .thanks__title {{ $t('requestSent') }}
      hr.thanks__hrLine
      .thanks__subtitle {{ $t('youWillBeContacted') }}


</template>
<script>
export default {
  data() {
    return {}
  },
  // computed: {
  //   reload() {
  //     return this.$store.state.location.reload
  //   },
  // },
  // mounted() {
  //   this.refreshPage()
  // },
  // methods: {
  //   refreshPage() {
  //     // Use location.reload() to refresh the page

  //   },
  // },
}
</script>
<style lang="scss" scoped>
* {
  width: auto;
}
.thanksPage {
  height: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}
.thanks {
  text-align: center;
  color: #000;
  background-color: #fff;
  outline: 7px solid #1bb8d1;
  border-radius: 15px;
  padding: 20px 40px;
  font-size: 24px;
  &__title {
    padding-bottom: 20px;
  }
  &__subtitle {
    padding: 20px 0;
    font-size: 1rem;
  }
  //   color: #eba026;
}
</style>
