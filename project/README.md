XO Game
Video Demo:  <https://www.youtube.com/watch?v=HZdw9fZTBtw>

Description:

Hi there!
This is an XO GAME representing my final project, the ending of CS50 track. I find it useful to write code in javascript along with HTML, and CSS. Although, Javascript wasn't taught and included in the curriculum of the course, I was eager to to use it in building a webiste application (XO GAME !!).

Contents:

- Introduction (why, challenges, and everything to know in the journey, and more..)
- html file along with CSS file
- javascript along with HTML AND CSS files

First Intro:

Introduction:
The project idea isn’t the best thing to do at the end of the course. Yet the thing is I am a starter in the field of programming. Thus, at least for me coding with Javascript and even knowing my passion in computer science is the best outcome to get out of the course. I wouldn’t know that web applications will be my focus and area of interest later hopefully. Loving web applications pushes me towards the motion of implementing any web design thinking although XO isn’t fair enough for the staff to be satisfied; however, let the way guide me more and more. And not just that, I am originally studying Electronics & Communication Engineering in my current university. Imagining the weight of knowledge given and taught within this course to be part of my educational endeavours is really great and beneficial. Why Javascript? I knew from my colleagues and other educational institutions students the importance of Javascript on this track. That’s why I wanted to do something with language of course along with HTML and CSS files. The time and effort I assigned for the project depended on different factors such as, choosing the idea, implementing the idea, and testing it. It is a bit challenging due to the fact of not teaching Javascript by Dr. Malan throughout the course. HTML and CSS were much easier than Javascript code. Thanks to the effort of Dr. Malan, I want to thank each and every one contributed in this journey and helped guided millions of students their way to computer science and programming.

Explaining the code in detail:
Index.html
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>XO Game</title>
    <link rel="stylesheet" href="style.css">

This part is the content of the head tag.
First meta tag to set the character for encoding “UTF-8”. The second meta tag is to make the website adjustable to multiple screen sizes with the initial-scale = 1.0. The title as well is there and the link tag to reference the style.css but should be within the same folder directory within which included all the other coded files.
<div class="title"><span>X O</span> GAME</div>

Notice span here for X O, the inline container used to make up specific text.
<div onclick="yourTurn(this.id)" class="square" id="item1"></div>

This part is repeated within the body for each square of the XO game, calling the build-in onclick that just passes the action of clicking with id to yourTurn function defined in mine.js file. Div tag is featured with the class square and the id item1. Class “square” is defined in the CSS file and item1 will be used later in javascript.
<script src="mine.js"></script>

I added script tag at the end of the body to reference mine.js.
Second javaScript:
let title = document.querySelector('.title');
let games = document.querySelectorAll('.game');
let turn = 'x'; // by default
let square = []; // empty list


This part is at the very beginning of the mine.js file. Document.querySelector is a built-in inside javascript to let the programmer select all the elements of the unique id title or class game. Turn is x by default and square is an empty list to store all the clicked Xs, or Os.

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

Gameover function to identify the winner and reload the page afterwards. Title.innerhtml allows the user to alter the title text whenever needed to inform the final winner. Document.getElementById built-n as well to get all the elements of the ids item and do style its background to a yellow. SetInterval and SetTimeout is both built-in which iterates and call themselves every specified number of milliseconds. Location.relaod() is to reload the location of the webpage whenever called so the user can replay again.





 function winner(){
    for(let i = 1; i < 10; i++){
        square[i]= document.getElementById('item'+i).innerHTML;
    }

    if(square[1] == square[2] && square[2] == square[3] && square[1] != ''){
        gameOver(1, 2, 3);
    }

Winner function is to define the winner of the game. For the body of the for loop, after the document is loaded, get the element by the id, for example document.getElementById (item2) as defined back in html to get its content by innerhtml and store that value to square [i] index in the list. Then, we need to check all of the different possibilities in multiple ifs statements to identify the winner whenever Xs only or Os only fills up any three squares diagonally, horizontally, or vertically first.
else {
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

Final else is for the draw case.  Crjoin variable is assigned to the concatenation of the all the indices of the square list. When it becomes 9, it means no one has won the game, and the title is needed to updated to Draw.








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


Yourturn method is called with the id argument, Turn is a variable which is x by default as indicated in the first part of the code. Whenever the box is empty and the turn is X element.innerhtml is updated to X. Remember innerhtml gives us access to the content of the element variable in javascript.
CSS file is using different attributes to specialize the appearance of each and every class or id of t=both html and javascript file.


