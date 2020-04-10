/*document.addEventListener('click', function(event) {
        var isClickInside = document.getElementById('top-nav').contains(event.target);
        if (isClickInside) {
	  if(document.getElementById('lower-nav').style.display=='grid'){
                document.getElementById('lower-nav').style.display='none';
		document.getElementById('top-arrow-one').classList.remove('down-arrow');
		document.getElementById('top-arrow-two').classList.remove('down-arrow');
            }
            else{ 
                document.getElementById('lower-nav').style.display='grid';
		document.getElementById('top-arrow-one').classList.add('down-arrow');
		document.getElementById('top-arrow-two').classList.add('down-arrow');
	    };
        }
        else {
	  if(document.getElementById('lower-nav').style.display=='grid'){
	    document.getElementById('lower-nav').style.display='none';
	    document.getElementById('top-arrow-one').classList.remove('down-arrow');
	    document.getElementById('top-arrow-two').classList.remove('down-arrow');
	  };
	};
        });
*/
function draw(){
var useF = document.getElementById("cvs");
	if (useF.getContext){
	  var ctx = useF.getContext("2d");
	  ctx.fill();
	  for(var i=20; i>0;i--){
	    var rectum = new Path2D();
	    ctx.fillStyle= randomColor();
	    
	    rectum.rect(5, 5, Math.PI ** (i), i*10);
	    //ctx.stroke(rectum);
	    ctx.fill();
	  }
	  //ctx.beginPath();
	  //ctx.moveTo(10,5);
	  //ctx.lineTo(10,90);
	  //ctx.lineTo(290,90);
	  //ctx.lineTo(290,5);
	  //ctx.fillStyle = "rgba(0,0,0,1)";
	  //ctx.fill()
	  //ctx.rect(50,50,50,50);
	  ///ctx.moveTo(10,5);
	  //ctx.fillStyle = "rgba(200,100,0,1)";
	  //ctx.fill();
	}
}

function gradColor(i,j) {
	var red = Math.floor(255-32.5*i);
	var blue = Math.floor(255-12.5*j);
	var green = 0;
	var color = "rgba(" + red + "," + green + "," + blue + "," + 1 + ")";
	return color;
}

function randomColor(){
  var red = Math.floor(Math.random()*255);
  var green = Math.floor(Math.random()*255);
  var blue = Math.floor(Math.random()*255);
  return "rgb(" + red + "," + green + "," + blue + ")";
}

function random(x){
  var rando = Math.random()*x;
  return rando;
}

