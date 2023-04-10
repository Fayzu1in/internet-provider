// https://stackoverflow.com/a/71329842

import Vue from 'vue'
import { Swiper, SwiperSlide } from 'swiper/vue/swiper-vue'
import 'swiper/swiper-bundle.css'
// eslint-disable-next-line vue/multi-word-component-names
Vue.component('SwiperContainer', Swiper)
Vue.component('SwiperSlide', SwiperSlide)
