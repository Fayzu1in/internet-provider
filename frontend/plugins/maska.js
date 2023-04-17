import Vue from 'vue'
import { vMaska } from 'maska'

Vue.directive('maska', vMaska)

// or in case of CDN load
Vue.directive('maska', vMaska.vMaska)
