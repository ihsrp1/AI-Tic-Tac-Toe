<template>
  <div class="BodyContainer">
    <div class="heading">
      <h1>Tic-Tac-Toe</h1>
    </div>
    <!-- <div class="tictactoe-board">
      <div v-for="(n, i) in 3" :key="i">
        <div v-for="(n, j) in 3" :key="j">
          <cell @click="performMove(j, i)"
                :value="board.cells[j][i]"
          />
        </div>
      </div>
      <div class="game-over-text" v-if="gameOver">
        {{ gameOverText }}
      </div>
    </div> -->
    <v-row no-gutters class='GameRow' style='position: relative;'>
      <v-col v-if='$vuetify.breakpoint.smAndUp' xs='12' sm='12' md='6' align-self='center' style='position: relative;'>
        <BotBob :gameOver='gameOver' :gameOverText='gameOverText' :gameNotStarted='gameNotStarted'/>
      </v-col>
      <v-col xs='12' sm='12' md='6' align-self='center' style='position: relative; height: 264px;'>
        <div class="container">
          <div v-for="(n, i) in 3" :key="i" class="TTTflex">
            <div v-for="(n, j) in 3" :key="j" class="cube">
              <div class="wall front">
                <cell @click="performMove(j, i)"
                  :value="board.cells[j][i]"
                />
              </div>
              <div class="wall back"></div>
              <div class="wall left"></div>
              <div class="wall right"></div>
              <div class="wall top"></div>
              <div class="wall bottom"></div>
            </div>
          </div>
        </div>
      </v-col>
    </v-row>
    <div class='ButtonRow'>
      <button @click="zoom(0)" class='btnClass' style='background-color: #3f51b5; border-color: #3f51b5;' type="button">
        <div class='btnContentClass'>
          <span class='btnIconClass' aria-hidden="true">-</span>
        </div>
      </button>
      <button @click="zoom(2)" class='btnClass' style='background-color: #3f51b5; border-color: #3f51b5;' type="button">
        <div class='btnContentClass'>
          <span class='btnIconClass' style='font-size: 20px;' aria-hidden="true">1:1</span>
        </div>
      </button>
      <button @click="zoom(1)" class='btnClass' style='background-color: #3f51b5; border-color: #3f51b5;' type="button">
        <div class='btnContentClass'>
          <span class='btnIconClass' aria-hidden="true">+</span>
        </div>
      </button>
    </div>
    <div class='TreeRow'>
      <div class='shape-outer'>
        <vue-tree
          class='shape-inner'
          :dataset="graph"
          :config="graphConfig"
          ref="tree"
        >
          <template v-slot:node="{ node, collapsed }">
            <div
              class="tree-node"
              :style="{ border: collapsed ? '2px solid grey' : '' }"
              >
              <div style='height: 80px; background: white; border-top-left-radius: 4px; border-top-right-radius: 4px; margin: 0 auto; display: flex; flex-wrap: wrap; align-items: center; justify-content: center; width: 100%;'>
                <div v-for="(n, i) in 3" :key="i">
                  <div v-for="(n, j) in 3" :key="j" style='border: 1px solid black;'>
                    <div style='height: 20px; width: 20px; color: black;'>{{node.boardCells ? node.boardCells[i][j] : board.cells[i][j]}}</div>
                  </div>
                </div>
              </div>
              <span>{{ node.value }}</span>
            </div>
          </template>
        </vue-tree>
      </div>
    </div>
  </div>
</template>
<script>
  import Board from "./Board";
  import Dracula from "graphdracula";
  import BotBob from "../src/components/BotBob"

  export default {
    components: {
      BotBob
    },
    data() { return {
      gameOver: false,
      gameOverText: '',
      gameNotStarted: true,
      board: new Board(),
      graph: {},
      graphConfig: { nodeWidth: 120, nodeHeight: 80, levelHeight: 200 }
    } },

    methods: {
      zoom(controll) {
        if (controll === 1) {
          console.log(this.$refs)
          this.$refs.tree.zoomIn();
        } else if (controll === 0) {
          this.$refs.tree.zoomOut();
        } else {
          this.$refs.tree.restoreScale();
        }
      },
      fromMatrixToString(board) {
        let string = [];
        for(let i = 0; i < 3; i++){
          for(let j = 0; j < 3; j++) {
            if (board[i][j] != '') {
              string.push(board[i][j]);
            } else {
              string.push('_');
            }
            string.push('|')
          }
          string.push('\n')
        }
        return string;
      },
      performMove(x, y) {
        this.gameNotStarted = false
        if (this.gameOver) {
          return;
        }

        if (! this.board.doMove(x, y, 'x')) {
          // Invalid move.
          return;
        }

        let newBoard = this.board.clone();

        this.$forceUpdate();

        if (this.board.isGameOver()) {
          this.gameOver = true;
          this.gameOverText = this.board.playerHas3InARow('x') ? 'You win!' : 'Draw';
          return;
        }

        this.graph = {value: '0', boardCells: newBoard.cells, children: []};
        // this.graph.addEdge(this.board.clone().toString(), '')

        let aiMove = this.minimax(this.board.clone(), 'o', this.graph, -Infinity, Infinity);
        this.board.doMove(aiMove.move.x, aiMove.move.y, 'o');
        this.graph.value = aiMove.score

        if (this.board.isGameOver()) {
          this.gameOver = true;
          this.gameOverText = this.board.playerHas3InARow('o') ? 'You lose!' : 'Draw';
        }

        this.$forceUpdate();
      },

      minimax(board, player, parent, alpha, beta, depth = 1) {

        // If the board has 3 in a row return the score of the board.
        if (board.isGameOver()) {
          return {
            score: board.getScore(),
            move: null
          }
        }

        // The 'o' player wants to maximize its score, the 'x' player wants to
        // minimize its score.
        let bestScore = player === 'o' ? -10000 : 10000;
        let bestMove = null;

        let moves = board.getPossibleMoves();
        for (let i = 0; i < moves.length; i++) {
          let move = moves[i];
          let newBoard = board.clone();
          newBoard.doMove(move.x, move.y, player);
          if(depth <= 10 - moves.length){
            var newChild = {value: bestScore.toString(), boardCells: newBoard.cells, children: []};
            parent.children.push(newChild);
          } else {
            var newChild = parent
          }

          // Recursively call the minimax function for the new board.
          const score = this.minimax(newBoard, player === 'x' ? 'o' : 'x', newChild, alpha, beta, depth + 1).score;

          // If the score is better than the best saved score update the best saved
          // score to this move.
          if ((player === 'o' && score > bestScore) || (player === 'x' && score < bestScore)) {
            bestScore = score;
            bestMove = move;
          }
          
          parent.value = bestScore
          // parent.board_cells = bestMove
          if (player === 'o') {
            alpha = Math.max(score, alpha);
          } else {
            beta = Math.min(score, beta);
          }
          if (beta <= alpha) {
            break;
          }

        }
        // Return the best found score & move!
        return {
          score: bestScore,
          move: bestMove
        }
      }
    }

  }
</script>
<style>
  .BodyContainer {
    width: 100%;
    height: 100%;
    display: flex;
    flex-flow: column;
  }
  .GameRow {
    flex: 0 1 264px;
  }
  .ButtonRow {
    width: 100%;
    text-align: center;
    margin-top: 2vh;
    flex: 0 1 auto;
  }
  .TreeRow {
    width: 100%;
    flex: 1 1 auto;
    padding: 10px;
  }
  .shape-outer {
    height: 100%;
    width: 100%;
    background-image: linear-gradient(to bottom right, rgb(15, 32, 39), rgb(32, 58, 67), rgb(32, 58, 67));
    padding: 4px;
    border-radius: 6px;
  }

  .shape-inner {	
    height: 100%;
    width: 100%;
    background: radial-gradient(circle at center, #222, #000);;
    background-size: cover;
    margin: auto;
  }
  .btnClass {
    box-shadow: 0 3px 5px -1px rgb(0 0 0 / 20%), 0 6px 10px 0 rgb(0 0 0 / 14%), 0 1px 18px 0 rgb(0 0 0 / 12%);
    will-change: box-shadow;
    min-width: 0;
    height: 45px;
    width: 45px;
    padding: 0;
    border-radius: 50%;
    align-items: center;
    display: inline-flex;
    flex: 0 0 auto;
    font-size: 14px;
    font-weight: 500;
    justify-content: center;
    margin: 6px 8px;
    outline: 0;
    text-transform: uppercase;
    text-decoration: none;
    transition: .3s cubic-bezier(.25,.8,.5,1),color 1ms;
    position: relative;
    vertical-align: middle;
    user-select: none;
    cursor: pointer;
  }
  .btnClass:before {
    border-radius: inherit;
    color: inherit;
    content: "";
    position: absolute;
    left: 0;
    top: 0;
    height: 100%;
    opacity: .12;
    transition: .3s cubic-bezier(.25,.8,.5,1);
    width: 100%;
  }
  .btnContentClass {
    flex: 1 1 auto;
    margin: 0;
    height: 100%;
    align-items: center;
    border-radius: inherit;
    color: inherit;
    display: flex;
    justify-content: center;
    position: relative;
    transition: .3s cubic-bezier(.25,.8,.5,1);
    white-space: nowrap;
    width: inherit;
  }
  .btnIconClass {
    color: inherit;
    height: inherit;
    width: inherit;
    color: #fff !important;
    align-items: center;
    display: inline-flex;
    font-feature-settings: "liga";
    font-size: 24px;
    justify-content: center;
    line-height: 1;
    transition: .3s cubic-bezier(.25,.8,.5,1);
    vertical-align: text-bottom;
    font-family: 'Roboto';
    font-weight: normal;
    font-style: normal;
    letter-spacing: normal;
    text-transform: none;
    white-space: nowrap;
    direction: ltr;
    -webkit-font-smoothing: antialiased;
  }
  .tictactoe-board {
    margin: 0 auto;
    display: flex;
    flex-wrap: wrap;

    width: 204px;
    height: 204px;
  }
  .container {
    display: flex;
    flex-direction: column;
    align-items: center;
  }

  .tree-node {
    text-align: center;
    width: 80px;
    padding-bottom: 8px;
    display: flex;
    flex-direction: column;
    align-items: flex-center;
    justify-content: center;
    color: white;
    background-color: #f7c616;
    border-radius: 4px;
  }

  .game-over-text {
    font-weight: bold;
    color: white;
    width: 204px;
    font-size: 16px;
    text-align: center;
    padding-top: 12px;
  }

  .heading {
    text-align: center;
    width: 100%;
    color: white;
    margin-top: 50px;
    margin-bottom: 4vh;
    flex: 0 1 auto;
  }

  /* Classes TicTacToe animation */

  /* basic style */

  .TTTflex {
    display: flex;
    justify-content: center;
    align-items: center;
  }

  /* cube */
  .cell {
    height: 80px !important;
    width: 80px !important;
    border: none !important;
  }

  .cube {
    position: relative;
    width: 1px;
    height: 1px;
    transform-style: preserve-3d;
  }
  .wall {
    width: 80px;
    height: 80px;
    position: absolute;
    text-align: center;
    line-height: 100px;
    left: calc(-80px / 2);
    top: calc(-80px / 2);
  }
  .front {
    transform: translateZ(calc(80px / 2));
  }
  .back {
    transform: translateZ(calc(-80px / 2)) rotateY(180deg);
  }
  .right {
    transform: translateX(calc(80px / 2)) rotateY(90deg);
  }
  .left {
    transform: translateX(calc(-80px / 2)) rotateY(-90deg);
  }
  .top {
    transform: translateY(calc(-80px / 2)) rotateX(90deg);
  }
  .bottom {
    transform: translateY(calc(80px / 2)) rotateX(-90deg);
  }

  /* animation */

  .TTTflex:nth-of-type(4) .cube:nth-of-type(1) {
    animation: rotation 3s cubic-bezier(0.215, 0.61, 0.355, 1) 0.5s forwards;
  }

  .TTTflex:nth-of-type(3) .cube:nth-of-type(1) {
    animation: rotation 3s cubic-bezier(0.215, 0.61, 0.355, 1) 0.6s forwards;
  }
  .TTTflex:nth-of-type(4) .cube:nth-of-type(2) {
    animation: rotation 3s cubic-bezier(0.215, 0.61, 0.355, 1) 0.6s forwards;
  }

  .TTTflex:nth-of-type(2) .cube:nth-of-type(1) {
    animation: rotation 3s cubic-bezier(0.215, 0.61, 0.355, 1) 0.7s forwards;
  }
  .TTTflex:nth-of-type(3) .cube:nth-of-type(2) {
    animation: rotation 3s cubic-bezier(0.215, 0.61, 0.355, 1) 0.7s forwards;
  }
  .TTTflex:nth-of-type(4) .cube:nth-of-type(3) {
    animation: rotation 3s cubic-bezier(0.215, 0.61, 0.355, 1) 0.8s forwards;
  }

  .TTTflex:nth-of-type(1) .cube:nth-of-type(1) {
    animation: rotation 3s cubic-bezier(0.215, 0.61, 0.355, 1) 0.8s forwards;
  }
  .TTTflex:nth-of-type(2) .cube:nth-of-type(2) {
    animation: rotation 3s cubic-bezier(0.215, 0.61, 0.355, 1) 0.8s forwards;
  }
  .TTTflex:nth-of-type(3) .cube:nth-of-type(3) {
    animation: rotation 3s cubic-bezier(0.215, 0.61, 0.355, 1) 0.8s forwards;
  }
  .TTTflex:nth-of-type(4) .cube:nth-of-type(4) {
    animation: rotation 3s cubic-bezier(0.215, 0.61, 0.355, 1) 0.8s forwards;
  }

  .TTTflex:nth-of-type(1) .cube:nth-of-type(2) {
    animation: rotation 3s cubic-bezier(0.215, 0.61, 0.355, 1) 0.9s forwards;
  }
  .TTTflex:nth-of-type(2) .cube:nth-of-type(3) {
    animation: rotation 3s cubic-bezier(0.215, 0.61, 0.355, 1) 0.9s forwards;
  }
  .TTTflex:nth-of-type(3) .cube:nth-of-type(4) {
    animation: rotation 3s cubic-bezier(0.215, 0.61, 0.355, 1) 0.9s forwards;
  }

  .TTTflex:nth-of-type(1) .cube:nth-of-type(3) {
    animation: rotation 3s cubic-bezier(0.215, 0.61, 0.355, 1) 1s forwards;
  }
  .TTTflex:nth-of-type(2) .cube:nth-of-type(4) {
    animation: rotation 3s cubic-bezier(0.215, 0.61, 0.355, 1) 1s forwards;
  }

  .TTTflex:nth-of-type(1) .cube:nth-of-type(4) {
    animation: rotation 3s cubic-bezier(0.215, 0.61, 0.355, 1) 1.1s forwards;
  }

  @keyframes rotation {
    0% {
      transform: rotateX(270deg) rotateY(270deg);
      margin: 0 0px 0 0;
    }
    100% {
      margin: 0 80px 0 0;
    }
  }

  .wall{
    animation: color 1s linear 0s forwards;
  }

  .TTTflex {
    animation: size 1s linear 0s forwards;
  }

  .container {
    animation: sizes 1s linear 0s forwards;
  }

  @keyframes sizes {
    from {
      padding-left: 80px;
    }
    to {
      padding-left: 0px;
    }
  }

  @keyframes size {
    from {
      width: 0px;
      height: 0px;
      margin: 0 0px 0 0;
    }
    to {
      width: 80px;
      height: 80px;
      margin: 0 -80px 0 0;
    }
  }

  @keyframes color {
    0% {
      background-color: #fff;
      border: none;
      border-radius: none;
    }
    70% {
      background-color: rgba(255,255,255,0);
      border: 2px solid rgb(233,233,233);
      border-radius: 5px;
    }
    100% {
      background-color: rgba(255,255,255,0);
      border: 2px solid rgb(233,233,233);
      border-radius: 5px;
    }
  }

</style>
