import Vue from 'vue'
import App from './App.vue'
import VueTree from '@ssthouse/vue-tree-chart'
import TicTacToe from './TicTacToe';
import Cell from './Cell';

import vuetify from './plugins/vuetify'

// ES6
import VueTyperPlugin from 'vue-typer'

Vue.use(VueTyperPlugin)

Vue.component('tic-tac-toe', TicTacToe);
Vue.component('vue-tree', VueTree)
Vue.component('cell', Cell);

new Vue({
  el: '#app',
  vuetify,
  render: h => h(App)
});
