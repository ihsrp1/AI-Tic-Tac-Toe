// Tic Tac Toe AI with Minimax Algorithm
// The Coding Train / Daniel Shiffman
// https://thecodingtrain.com/CodingChallenges/154-tic-tac-toe-minimax.html
// https://youtu.be/I64-UTORVfU
// https://editor.p5js.org/codingtrain/sketches/0zyUhZdJD


let edges = [];

function bestMove() {
  // AI to make its turn
  edges = []
  let bestScore = -Infinity;
  let move;
  for (let i = 0; i < 3; i++) {
    for (let j = 0; j < 3; j++) {
      // Is the spot available?
      if (board[i][j] == '') {
        edges.push({p: {x: 0, y: 0}, c: {x: i, y: j}});
        board[i][j] = ai;
        let score = minimax(board, 0, false, -Infinity, Infinity, {x: i, y: j});
        board[i][j] = '';
        if (score > bestScore) {
          bestScore = score;
          move = { i, j };
        }
      }
    }
  }
  board[move.i][move.j] = ai;
  currentPlayer = human;
  return edges;
}

let scores = {
  X: 10,
  O: -10,
  tie: 0
};

function minimax(board, depth, isMaximizing, alpha, beta, from) {
  let result = checkWinner();
  if (result !== null) {
    return scores[result];
  }

  if (isMaximizing) {
    let bestScore = -Infinity;
    for (let i = 0; i < 3; i++) {
      for (let j = 0; j < 3; j++) {
        // Is the spot available?
        if (board[i][j] == '') {
          edges.push({p: from, c: {x: i, y: j}});
          board[i][j] = ai;
          let score = minimax(board, depth + 1, false, alpha, beta, {x: i, y: j});
          board[i][j] = '';
          bestScore = max(score, bestScore);
          alpha = max(score, alpha)
          if (beta <= alpha) {
            break;
          }
        }
      }
    }
    return bestScore;
  } else {
    let bestScore = Infinity;
    for (let i = 0; i < 3; i++) {
      for (let j = 0; j < 3; j++) {
        // Is the spot available?
        if (board[i][j] == '') {
          edges.push({p: from, c: {x: i, y: j}});
          board[i][j] = human;
          let score = minimax(board, depth + 1, true, alpha, beta, {x: i, y: j});
          board[i][j] = '';
          bestScore = min(score, bestScore);
          alpha = min(score, alpha)
          if (beta <= alpha) {
            break;
          }
        }
      }
    }
    return bestScore;
  }
}
