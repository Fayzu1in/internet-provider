<template lang="pug">
section.provider
  .provider__title 
    //- TariffCard(:tariffName='link.title', :cost='link.price', :speed='link.speed' traffic='Безлимит', :plan='link.id')
  

</template>
<script>
export default {
  //   props: {
  //     message: {
  //       type: Array,
  //       required: true,
  //     },
  //   },
  fetch() {
    // this.topProviders = await this.$axios.$get(
    //   'http://127.0.0.1:8000/api/v1/top-providers'
    // )
    console.log(this.$route.params.id)
  },
}
</script>
<style lang="scss" scoped></style>
