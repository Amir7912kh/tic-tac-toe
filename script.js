document.addEventListener('DOMContentLoaded', () => {
    const boardElement = document.getElementById('game-board');
    const statusElement = document.getElementById('status');
    const newGameButton = document.getElementById('new-game-button');
    const cells = document.querySelectorAll('.cell');

    let board = ['', '', '', '', '', '', '', '', ''];
    let currentPlayer = 'X';
    let isGameActive = true;

    const winningConditions = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ];

    function checkWinner() {
        for (let i = 0; i < winningConditions.length; i++) {
            const [a, b, c] = winningConditions[i];
            if (board[a] && board[a] === board[b] && board[a] === board[c]) {
                return { winner: board[a], line: [a, b, c] };
            }
        }
        if (!board.includes('')) {
            return { winner: 'draw', line: [] };
        }
        return null;
    }

    function handleCellClick(e) {
        const clickedCell = e.target;
        const clickedCellIndex = parseInt(clickedCell.getAttribute('data-index'));

        if (board[clickedCellIndex] !== '' || !isGameActive || currentPlayer !== 'X') {
            return;
        }

        makeMove(clickedCellIndex, 'X');

        const gameResult = checkWinner();
        if (gameResult) {
            endGame(gameResult);
            return;
        }

        currentPlayer = 'O';
        statusElement.textContent = `AI's turn (O)`;

        // AI's turn
        setTimeout(aiMove, 500); // Add a small delay for better UX
    }

    function makeMove(index, player) {
        board[index] = player;
        cells[index].textContent = player;
        cells[index].classList.add(player.toLowerCase());
    }

    function endGame(result) {
        isGameActive = false;
        if (result.winner === 'draw') {
            statusElement.textContent = "It's a draw!";
        } else {
            statusElement.textContent = `${result.winner} wins!`;
            result.line.forEach(index => {
                cells[index].classList.add('win');
            });
        }
    }

    function startGame() {
        board = ['', '', '', '', '', '', '', '', ''];
        currentPlayer = 'X';
        isGameActive = true;
        statusElement.textContent = `Your turn (X)`;
        cells.forEach(cell => {
            cell.textContent = '';
            cell.classList.remove('x', 'o', 'win');
        });
    }

    // AI Logic
    function aiMove() {
        if (!isGameActive) return;

        const bestMove = minimax(board, 'O');
        makeMove(bestMove.index, 'O');

        const gameResult = checkWinner();
        if (gameResult) {
            endGame(gameResult);
            return;
        }

        currentPlayer = 'X';
        statusElement.textContent = `Your turn (X)`;
    }

    function minimax(newBoard, player) {
        const availableSpots = newBoard.map((val, idx) => val === '' ? idx : null).filter(val => val !== null);

        if (checkWinnerForMinimax(newBoard, 'X')) {
            return { score: -10 };
        } else if (checkWinnerForMinimax(newBoard, 'O')) {
            return { score: 10 };
        } else if (availableSpots.length === 0) {
            return { score: 0 };
        }

        const moves = [];
        for (let i = 0; i < availableSpots.length; i++) {
            const move = {};
            move.index = availableSpots[i];
            newBoard[availableSpots[i]] = player;

            if (player === 'O') {
                const result = minimax(newBoard, 'X');
                move.score = result.score;
            } else {
                const result = minimax(newBoard, 'O');
                move.score = result.score;
            }

            newBoard[availableSpots[i]] = '';
            moves.push(move);
        }

        let bestMove;
        if (player === 'O') {
            let bestScore = -10000;
            for (let i = 0; i < moves.length; i++) {
                if (moves[i].score > bestScore) {
                    bestScore = moves[i].score;
                    bestMove = i;
                }
            }
        } else {
            let bestScore = 10000;
            for (let i = 0; i < moves.length; i++) {
                if (moves[i].score < bestScore) {
                    bestScore = moves[i].score;
                    bestMove = i;
                }
            }
        }
        return moves[bestMove];
    }

    function checkWinnerForMinimax(currentBoard, player) {
        for (let i = 0; i < winningConditions.length; i++) {
            const [a, b, c] = winningConditions[i];
            if (currentBoard[a] === player && currentBoard[b] === player && currentBoard[c] === player) {
                return true;
            }
        }
        return false;
    }


    cells.forEach(cell => cell.addEventListener('click', handleCellClick));
    newGameButton.addEventListener('click', startGame);
});
