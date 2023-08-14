<template>
  <div
    class="ScrollTop"
    :class="{ visible: scrolledEnough && !transitioning }"
    @click="toTop"
  >
    <material-icon :icon="mdiChevronUp" size="2.5rem"></material-icon>
  </div>
</template>
<script>
import { mdiChevronUp } from '@mdi/js'
export default {
  data() {
    return {
      mdiChevronUp,
      scrolledEnough: false,
      transitioning: false,
    }
  },

  mounted() {
    window.addEventListener('scroll', this.handleScroll, { passive: true })
  },

  beforeDestroy() {
    window.removeEventListener('scroll', this.handleScroll, { passive: true })
  },
  methods: {
    handleScroll(event) {
      this.scrolledEnough = event.currentTarget.scrollY > 250
    },

    toTop() {
      this.transitioning = true
      clearTimeout(this.transitioningTimeout)
      this.transitioningTimeout = setTimeout(() => {
        this.transitioning = false
      }, 500)

      window.scrollTo({
        top: 0,
        behavior: 'smooth',
      })
    },
  },
}
</script>

<style lang="scss" scoped>
.ScrollTop {
  position: fixed;
  background: #56c1ff;
  border-radius: 50%;
  padding: 5px;
  height: 50px;
  cursor: pointer;
  z-index: 1100;
  bottom: -5rem;
  right: 1.25rem;
  transition: bottom 0.3s ease-in-out;
  pointer-events: none;

  &.visible {
    bottom: 1rem;
    pointer-events: auto;
  }
}
</style>
