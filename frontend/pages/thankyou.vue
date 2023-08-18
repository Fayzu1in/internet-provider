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
<style lang="scss">
.thanksPage {
  height: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}
.thanks {
  background-color: #000000b4;
  backdrop-filter: blur(10px);
  text-align: center;
  padding: 30px;
  border-radius: 5px;
  font-size: 24px;
  //   color: #eba026;
}
</style>
