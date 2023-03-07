<template lang="pug">
section.Providers.container-fluid
      .provider
        .provider__title Uzonline
        TariffCard 
       



    
    

</template>
<script>
export default {
  async asyncData({ $axios }) {
    const ip = await $axios.$get('http://127.0.0.1:5000/flink-plans')
    return { ip }
  },

  data() {
    return {}
  },
}
</script>
<style lang="scss" scoped>
.Providers {
  background-color: #00000096;
  padding: 15px 10px;
  display: flex;
  border-radius: 5px;
  display: flex;
  flex-direction: column;

  .provider {
    margin-left: 15px;
    margin-bottom: 30px;
    &__title {
      font-size: 28px;
      padding-bottom: 30px;
      text-align: center;
    }
  }
}
</style>
