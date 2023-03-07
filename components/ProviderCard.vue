<template lang="pug">
section.Providers.container-fluid
      .provider
        .provider__title Uzonline
        TariffCard(v-for='index in 10')



    
    

</template>
<script>
export default {
  data() {
    return {
      tariff: [
        {
          name: 'yangi',
          costfrom: '100.000',
        },
        {
          name: 'yangi 2',
          costfrom: '102.000',
        },
        {
          name: 'yangi 3',
          costfrom: '103.000',
        },
      ],
      options: {
        rewind: true,

        perPage: 6,
        // gap: '0rem',
        perMove: 2,
        type: 'loop',
      },
    }
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
