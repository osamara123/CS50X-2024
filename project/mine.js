let title = document.querySelector('.title');
let games = document.querySelectorAll('.game');
let turn = 'x'; // by default
let square = []; // empty list 

// Game Over

function gameOver(num1, num2, num3,){
    
    title.innerHTML = `${square[num1]} Winner`
    document.getElementById('item' + num1, 'item' + num2, 'item' + num3).style.backgroundColor = '#fa0'; 

    setInterval(function(){
        title.innerHTML += '.';
    },1000);

    setTimeout(function(){
        location.reload();
    },3500);

}

// Winner

function winner(){
    for(let i = 1; i < 10; i++){
        square[i]= document.getElementById('item'+i).innerHTML;
    }

    if(square[1] == square[2] && square[2] == square[3] && square[1] != ''){
        gameOver(1, 2, 3);
    }
    else if(square[4] == square[5] && square[5] == square[6] && square[4] != ''){
        gameOver(4, 5, 6);
    }
    else if(square[7] == square[8] && square[8] == square[9] && square[7] != ''){
        gameOver(7, 8, 9);
    }
    else if(square[1] == square[4] && square[4] == square[7] && square[7] != ''){
        gameOver(1, 4, 7);
    }
    else if(square[2] == square[5] && square[5] == square[8] && square[8] != ''){
        gameOver(2, 5, 8);
    }
    else if(square[3] == square[6] && square[6] == square[9] && square[9] != ''){
        gameOver(3, 6, 9);
    }
    else if(square[1] == square[5] && square[5] == square[9] && square[9] != ''){
        gameOver(1, 5, 9);
    }
    else if(square[3] == square[5] && square[5] == square[7] && square[7] != ''){
        gameOver(3, 5, 7);
    } else {
        let crJoin = square.reduce((acc, el) => acc + el);
            if(crJoin.length === 9) {
                title.innerHTML = `Draw`
                setInterval(function(){
                    title.innerHTML += '.';
                },1000);
            
                setTimeout(function(){
                    location.reload();
                },3500);
            }
    }

}

// Your Turn

function yourTurn(id){
    let element = document.getElementById(id);
    if(turn === 'x' && element.innerHTML == ''){
        element.innerHTML = 'x';
        turn = 'o';
        title.innerHTML = 'o';
    }
    else if(turn === 'o' && element.innerHTML == ''){
        element.innerHTML = 'o';
        turn = 'x';
        title.innerHTML = 'x';
    }
    
    winner();
}




