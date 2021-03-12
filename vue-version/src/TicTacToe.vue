<template>
  <div style="width: 100%; margin-top: 350px;">
    <div class="heading">
      <h1>Tic-Tac-Toe</h1>
    </div>
    <div class="tictactoe-board">
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
    </div>
    <!-- <v-row style='height: 260px; position: relative;'>
      <v-col cols='6' align-self='center' style='height: 260px; position: relative;'>
        <TTTtest />
      </v-col>
      <v-col cols='6' align-self='center' style='height: 260px; position: relative;'>
        <TTTtest />
      </v-col>
    </v-row> -->
    <div style="width: 100%; text-align: center;margin-top: 50px;">
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
    <vue-tree
      style="width: 100%; height: 600px;"
      :dataset="graph"
      :config="graphConfig"
      ref="tree"
    >
      <template v-slot:node="{ node, collapsed }">
        <span
          class="tree-node"
          :style="{ border: collapsed ? '2px solid grey' : '' }"
          >{{ node.value }}</span
        >
      </template>
    </vue-tree>
  </div>
</template>
<script>
  import Board from "./Board";
  import Dracula from "graphdracula";
  import TTTtest from "../TicTacToetest"

  export default {
    components: {
      TTTtest
    },
    data() { return {
      gameOver: false,
      gameOverText: '',
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
        if (this.gameOver) {
          return;
        }

        if (! this.board.doMove(x, y, 'x')) {
          // Invalid move.
          return;
        }

        this.$forceUpdate();

        if (this.board.isGameOver()) {
          this.gameOver = true;
          this.gameOverText = this.board.playerHas3InARow('x') ? 'You win!' : 'Draw';
          return;
        }

        this.graph = {value: '0', children: []};
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
          if(depth <= 3){
            var newChild = {value: bestScore.toString(), children: []};
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
    display: inline-block;
    width: 28px;
    height: 28px;
    border-radius: 50%;
    background-color: antiquewhite;
    text-align: center;
    line-height: 28px;
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
  }
</style>
