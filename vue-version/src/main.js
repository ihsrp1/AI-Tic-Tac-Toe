import Vue from 'vue'
import App from './App.vue'
import VueTree from '@ssthouse/vue-tree-chart'
import TicTacToe from './TicTacToe';
import Cell from './Cell';

Vue.component('tic-tac-toe', TicTacToe);
Vue.component('vue-tree', VueTree)
Vue.component('cell', Cell);

new Vue({
  el: '#app',
  render: h => h(App)
});
