<template>
  <div class="error-page">
    <h1>This page could not be found</h1>
    <p>Redirecting to the homepage...</p>
  </div>
</template>

<script>
export default {
  props: {
    error: {
      type: Object,
      default: null,
    },
  },
  mounted() {
    // Redirect immediately for 404 errors
    if (this.error && this.error.statusCode === 404) {
      this.$router.replace('/')
    }
  },
}
</script>

<style scoped>
.error-page {
  text-align: center;
  padding: 2rem;
}
</style>
