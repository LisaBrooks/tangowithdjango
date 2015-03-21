//bao1 - just print things into the canvas for now

/*	our board is represented by two arrays, one for player1's half of the board
	and another for player2's half of the board.

	Each half is represented as a 1 dimentional array of 1 dimentional arrays 
	(where the size of the inner array is the number of balls in that pit)

	the indecies of the pits are arranged as follows

	 0  1  2  3  4  5  6  7
	15 14 13 12 11 10  9  8 

	for each player.  The whole board is therefore arranged as follows

	15 14 13 12 11 10  9  8 
	 0  1  2  3  4  5  6  7
	 0  1  2  3  4  5  6  7
	15 14 13 12 11 10  9  8 

	where the upper numbers refer to the indicies of player2's half of the board.
*/

// Initialize canvas and required variables 
var canvas;
var width = 800;
var height = 400;
var cellWidth = width / 8;
var cellHeight = height / 4;
var ctx;

// Initialize board arrrays and player
var player1Board = [];
var player2Board = [];
var currentPlayer = 1;

window.onload = function () 
{
	// console.log("Got into the js.")

    canvas = document.getElementById('canvas');
    ctx = canvas.getContext('2d');

    canvas.width = width;
    canvas.height = height;

    // When mouse click events are recievedm onCanvasClick will be called
    canvas.onclick = onCanvasClick;

    // Draw game board when the window loads
    // drawGameBoard();
    initBoard();
    
	drawBalls();

    setTimeout(timeoutCheck, 10000);



    // drawPlayerMoves();
};

function timeoutCheck()
{
	console.log("setTimeout");
}

function drawGameBoard() 
{
	var i = 0;

	//This makes the background colour for the board
	ctx.beginPath();    
    //ctx.rect(0, 0, 0, 0);
	ctx.stroke();
	ctx.fillStyle = "#6B4724";
	ctx.fillRect(0, 0, 800, 400);
	ctx.closePath();
 
 	//draw vertical lines
    for (i = 1; i < 8; i++)
    {
    
	    ctx.beginPath();
	    ctx.moveTo(cellWidth * i, 0);
	    ctx.lineTo(cellWidth * i, height);
	    ctx.stroke();

	}
  
    // Drawing horizontal lines
     for (i = 1; i < 4; i++)
    {
	    ctx.beginPath();
 	   	ctx.moveTo(0, cellHeight * i);
 	  	ctx.lineTo(width, cellHeight * i);
 	  	if (i === 2)
 	  	{
 	  		ctx.lineWidth = 5;
 	   	}
 	   	else 
 	   	{
 	   		ctx.lineWidth = 1;
 	   	}
 	   	ctx.stroke();
	}
}

function initBoard()
{
	var i =0;

	//place two balls into each pit
	for (i = 0; i < 17; i++)
	{
		player1Board.push([]);
		for (var j = 0; j < 2; j++)
		{}
		player1Board[i].push(1);
		player1Board[i].push(1);

		player2Board.push([]);
		player2Board[i].push(1);
		player2Board[i].push(1);
	}

	// console.log(player1Board);
	// console.log(player2Board);
}

//just have this draw how many balls are in each position 
function drawBalls()
{
	ctx.clearRect ( 0 , 0 , canvas.width, canvas.height );
	drawGameBoard();


	var i = 0;
	var j = 0;
	var cellMiddleHeight = cellHeight /2;
	ctx.font="40px Arial";
	var coordsX = [ 0, 15, -25, -15, 25, 5];
	var coordsY = [25, -15, 15, -25, 0, 10];


	//draw player1's front row
	for (i = 0; i < 8; i++)
	{
		ctx.fillStyle="#997A5C";
		ctx.beginPath();
		var frontBalls = player1Board[i].length;
		// ctx.fillText("" + i,cellMiddleHeight + (cellHeight * i),(cellWidth * 3) - (cellWidth / 2));
		var pit = ctx.arc(cellMiddleHeight + (cellHeight * i), (cellWidth * 3) - (cellWidth / 2), 40, 0, Math.PI*2, true); 
		ctx.closePath();
		ctx.fill();
		//ctx.fillStyle = "black"; // font color to write the text with
		//ctx.fillText("" + frontBalls,cellMiddleHeight + (cellHeight * i),(cellWidth * 3) - (cellWidth / 2));

		for (j = 0; j < frontBalls; j++){

			if (j <= 6){ //Looping creating balls
			ctx.fillStyle = "black"; // balls colour
			ctx.beginPath();
			ctx.arc(cellMiddleHeight + (cellHeight * i - coordsX[j]),(cellWidth * 3) - (cellWidth / 2 - coordsY[j]),7,0,2*Math.PI),true;
			ctx.closePath();
			ctx.fill();
			ctx.closePath();
			}

			if (j < 300 ){ //this loop prints out now all the numbers, it will be modified only to print larger numbers later
				ctx.beginPath();
				ctx.fillStyle = "purple"; //inside of text colour
				ctx.strokeStyle = "black";
				ctx.textAlign="center"; 
				ctx.fillText("" + frontBalls,cellMiddleHeight + (cellHeight * i),(cellWidth * 3) - (cellWidth / 2));
				ctx.strokeText("" + frontBalls,cellMiddleHeight + (cellHeight * i),(cellWidth * 3) - (cellWidth / 2));
				ctx.stroke();
				ctx.fill ();
				ctx.closePath();
			}
	
		}
		
		//ctx.stroke();
	}
 
	//draw player1's back row
	for (i = 8; i < 16; i++)
	{
		ctx.fillStyle="#997A5C";
		ctx.beginPath();
		var backBalls = player1Board[23 - i].length;
		ctx.arc(cellMiddleHeight + (cellHeight * (i- 8)), (cellWidth * 4) - (cellWidth / 2), 40, 0, Math.PI*2, true); 
		ctx.closePath();
		ctx.fill();
		
		// ctx.fillText("" + (23 - i),cellMiddleHeight + (cellHeight * (i- 8)),(cellWidth * 4) - (cellWidth / 2));
		//ctx.fillText("" + backBalls,cellMiddleHeight + (cellHeight * (i- 8)),(cellWidth * 4) - (cellWidth / 2));

			for (j = 0; j < backBalls; j++){

			if (j <= 6){ //Looping creating balls
			ctx.fillStyle = "black"; // balls colour
			ctx.beginPath();
			ctx.arc(cellMiddleHeight + (cellHeight * (i-8) - coordsX[j]),(cellWidth * 4) - (cellWidth / 2 - coordsY[j]),7,0,2*Math.PI),true;
			ctx.closePath();
			ctx.fill();
			ctx.closePath();
			}

			if (j < 300 ){ //this loop prints out now all the numbers, it will be modified only to print larger numbers later
				ctx.beginPath();
				ctx.fillStyle = "purple"; //inside of text colour
				ctx.strokeStyle = "black";
				ctx.textAlign="center"; 
				ctx.strokeText("" + backBalls,cellMiddleHeight + (cellHeight * (i- 8)),(cellWidth * 4) - (cellWidth / 2));
				ctx.fillText("" + backBalls,cellMiddleHeight + (cellHeight * (i- 8)),(cellWidth * 4) - (cellWidth / 2));
				ctx.stroke();
				ctx.fill ();
				ctx.closePath();
			}
	
		}

	}

	//draw player2's front row
	for (i = 0; i < 8; i++)
	{
		ctx.fillStyle="#997A5C";
		ctx.beginPath();
		var frontBalls = player2Board[i].length;
		ctx.arc(cellMiddleHeight + (cellHeight * i), (cellWidth * 2) - (cellWidth / 2), 40, 0, Math.PI*2, true); 
		ctx.closePath();
		ctx.fill();
		
		// ctx.fillText("" + i,cellMiddleHeight + (cellHeight * i),(cellWidth * 2) - (cellWidth / 2));
		//ctx.fillText("" + frontBalls,cellMiddleHeight + (cellHeight * i),(cellWidth * 2) - (cellWidth / 2));
	

		for (j = 0; j < frontBalls; j++){

			if (j <= 6){ //Looping creating balls
			ctx.fillStyle = "black"; 
			ctx.beginPath();
			ctx.arc(cellMiddleHeight + (cellHeight * i - coordsX[j]),(cellWidth * 2) - (cellWidth / 2 - coordsY[j]),7,0,2*Math.PI),true;
			ctx.closePath();
			ctx.fill();
		}
			//ctx.closePath();

			if (j < 500){ //this loop prints out now all the numbers, it will be modified only to print larger numbers later
				ctx.fillStyle = "red"; 
				//ctx.beginPath();
				ctx.fillText("" + frontBalls,cellMiddleHeight + (cellHeight * i),(cellWidth * 2) - (cellWidth / 2));
				//ctx.closePath();
				//console.log("HAPPENED");
			}

		}

	}

	//draw player2's back row
	for (i = 8; i < 16; i++)
	{
		ctx.fillStyle="#997A5C";
		ctx.beginPath();
		var backBalls = player2Board[23 - i].length;
		ctx.arc(cellMiddleHeight + (cellHeight * (i- 8)), (cellWidth) - (cellWidth / 2), 40, 0, Math.PI*2, true); 
		ctx.closePath();
		ctx.fill();
		ctx.fillStyle = "black"; 

		// ctx.fillText("" + (23 - i),cellMiddleHeight + (cellHeight * (i- 8)),(cellWidth) - (cellWidth / 2));
		//ctx.fillText("" + backBalls,cellMiddleHeight + (cellHeight * (i- 8)),(cellWidth) - (cellWidth / 2));

			for (j = 0; j < backBalls; j++){

			if (j <= 6){	//Looping creating balls
			ctx.fillStyle = "black"; 
			ctx.beginPath();
			ctx.arc(cellMiddleHeight + (cellHeight * (i-8) - coordsX[j]),(cellWidth) - (cellWidth / 2 - coordsY[j]),7,0,2*Math.PI),true;
			ctx.closePath();
			ctx.fill();
		}
			//ctx.closePath();

			if (j < 500){ //this loop prints out now all the numbers, it will be modified only to print larger numbers later
				ctx.fillStyle = "red"; 
				//ctx.beginPath();
				ctx.fillText("" + backBalls,cellMiddleHeight + (cellHeight * (i- 8)),(cellWidth) - (cellWidth / 2));
				//ctx.closePath();
				//console.log("HAPPENED");
			}

		}

	}
}


function onCanvasClick(e) {
    var mCoordinate = getMouseLocation(e);
    var pit = getPitFromLocation(mCoordinate);
    var pit_index = processPitClick(pit);

    //only process moves from the current player 
    if (pit_index !== undefined)
    {
    	makeMove(pit_index);
        console.log(pit_index);	
    }
    // console.log(pit_index);

}
 
// Getting mouse x,y coordinate on a click event relative to the canvas
function getMouseLocation(e) {
 
    var mouseX = e.pageX - canvas.offsetLeft;
    var mouseY = e.pageY - canvas.offsetTop;
 
 	console.log("X coord: " + mouseX + " Y coord: " + mouseY);
    return { x: mouseX, y: mouseY };
}
 
// Get the pit corresponding to a mouse location
function getPitFromLocation(mCoordinate) {
    var pitCoordinate = { x: 0, y: 0 };
 
    if (mCoordinate.x < cellWidth) 
    {
    	pitCoordinate.x = 0;
    }
    else if (mCoordinate.x > cellWidth && mCoordinate.x < (cellWidth * 2)) 
    {
    	pitCoordinate.x = 1;
	}
    else if (mCoordinate.x > (cellWidth * 2) && mCoordinate.x < (cellWidth * 3)) 
	{
    	pitCoordinate.x = 2;
	}
	else if (mCoordinate.x > (cellWidth * 3) && mCoordinate.x < (cellWidth * 4)) 
	{
    	pitCoordinate.x = 3;
	}
	else if (mCoordinate.x > (cellWidth * 4) && mCoordinate.x < (cellWidth * 5)) 
	{
    	pitCoordinate.x = 4;
	}
	else if (mCoordinate.x > (cellWidth * 5) && mCoordinate.x < (cellWidth * 6)) 
	{
    	pitCoordinate.x = 5;
	}
	else if (mCoordinate.x > (cellWidth * 6) && mCoordinate.x < (cellWidth * 7)) 
	{
    	pitCoordinate.x = 6;
	}
	else if (mCoordinate.x > (cellWidth * 7) && mCoordinate.x < (cellWidth * 8)) 
	{
    	pitCoordinate.x = 7;
	}

if (mCoordinate.y < cellWidth) 
    {
    	pitCoordinate.y = 0;
    }
    else if (mCoordinate.y > cellWidth && mCoordinate.y < (cellWidth * 2)) 
    {
    	pitCoordinate.y = 1;
	}
    else if (mCoordinate.y > (cellWidth * 2) && mCoordinate.y < (cellWidth * 3)) 
	{
    	pitCoordinate.y = 2;
	}
	else if (mCoordinate.y > (cellWidth * 3) && mCoordinate.y < (cellWidth * 4)) 
	{
    	pitCoordinate.y = 3;
	}

 	console.log("Pit coord: " + pitCoordinate.x + "," + pitCoordinate.y);
    return pitCoordinate;
}

//returns the input conditions for a move, that is
//a tuple { pit_index: i, direction: dir }
// for now we only return the index and always move in the positive directoin
function processPitClick(pit)
{	
	//lazily change the player when testing
	// currentPlayer = 1;

	var pit_index;
	var i;

	//get the starting pit
	if (currentPlayer === 1)
	{
		if (pit.y === 2)
		{
			// console.log("We're on the front row for player1");

			//the starting pit on the front row is just the x coordinate of the pit
			pit_index = pit.x;
		}
		if (pit.y === 3)
		{
			// console.log("We're on the back row for player1");

			//
			pit_index = 15 - pit.x;
		}
	}
	else
	{
		if (pit.y === 0)
		{
			// console.log("We're on the back row for player2");

			pit_index = 15 - pit.x;
		}
		if (pit.y === 1)
		{
			// console.log("We're on the front row for player2");

			//the starting pit on the front row is just the x coordinate of the pit
			pit_index = pit.x;

		}
	}

	return pit_index;
}

function makeMove(pit_i)
{
	var endPitEmpty = false;
	var startPit;
	var endPit

	//get the pit from which to start
	if (currentPlayer === 1)
	{
		startPit = player1Board[pit_i];
	}
	else
	{
		startPit = player2Board[pit_i];
	}

	//keep going until the move ends in an empty pit
	while (!endPitEmpty)
	{
		//first, check if the pit this part of the move ends on
		//is empty or not

		if (currentPlayer === 1)
		{
			endPit = player1Board[((pit_i + startPit.length)%16)];
		}
		else
		{
			endPit = player2Board[((pit_i + startPit.length)%16)];
		}

		if (endPit.length === 0)
		{
			endPitEmpty = true;
		}

		//move the balls from the start pit into each of the next
		//pits, up to end pit
		while (startPit.length > 0)
		{
			pit_i++;

			if (pit_i === 16)
			{
				pit_i = 0;
			}

			if (currentPlayer === 1)
			{
				player1Board[pit_i].push(startPit.pop());
			}
			else 
			{
				player2Board[pit_i].push(startPit.pop());	
			}

			drawBalls();
			// setTimeout(drawBalls, 1000);
			
		}

		//only continue the move if the previous part of the move didn't end
		// in an empty pit
		if(!endPitEmpty)
		{
			//get the pit from which to continue
			if (currentPlayer === 1)
			{
				startPit = player1Board[pit_i];
			}
			else
			{
				startPit = player2Board[pit_i];
			}

			//steal from the other player if their pit wasn't empty
			if (pit_i < 8)
			{
				if (currentPlayer ===1) 
				{
					while (player2Board[pit_i].length > 0)
					{
						player1Board[pit_i].push(player2Board[pit_i].pop());
						// setTimeout(drawBalls(), 1500);
					}
				}
				else
				{
					while (player1Board[pit_i].length > 0)
					{
						player2Board[pit_i].push(player1Board[pit_i].pop());
						// setTimeout(drawBalls(), 1500);
					}
				}
			}
		}

		// for (i = pit_i + 1; i = pit_ i + startPit.length; i++)
		// {
		// 	if (i === 16)
		// 	{
		// 		i = 0;
		// 	}

		// 	if (currentPlayer === 1)
		// 	{
		// 		player1Board[i]
		// 	}
		// }
		
	}
	if (currentPlayer ===1)
	{
		currentPlayer = 2;
	}
	else
	{
		currentPlayer = 1;
	}
}

/*


			startingPit = player1Board[pit.x];

not what I want to do now, check out the sheet of paper 

var player1Board = new Array(16);
var player2Board - new Array(!6);

*/

