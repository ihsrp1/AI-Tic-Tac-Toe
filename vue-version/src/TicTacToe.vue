<template>
  <div style="width: 100%;">
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
    <input type="button" @click="zoom(1)" value="Zoom +"/>
    <input type="button" @click="zoom(2)" value="1:1"/>
    <input type="button" @click="zoom(0)" value="Zoom -"/>
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

  export default {

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
            score: board.getScore() + depth,
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
          if(depth <= 2){
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
    width: 320px;
    color: white;
  }
</style>
