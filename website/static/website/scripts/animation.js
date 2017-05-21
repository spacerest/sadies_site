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
  
function corner(){
  var corn = [];
  for (var i = 0; i < 3; i++){
	  corn[i]=Math.floor(random(4)+1);
          while (corn[i]===corn[i-1]||corn[i]===corn[i-2]){
      corne = Math.floor(random(4))+1;
      corn[i] = corne;
    }
  }
        return corn;
}

function coordinates(){
  var xc = [];
  var yc = [];
  var corn = corner();
  for (var i in corn){
    if (corn[i]%2===1){
      xc[i] = Math.ceil(random(6));
    } else {
      xc[i] = Math.floor(random(6)+30);
    }
  }
  for (var j in corn){
    if (corn[j]<3){
      yc[j] = Math.ceil(random(6));
    } else {
      yc[j] = Math.floor(random(6)+30);
    }
  }
  var xcObj = {
    xc1 : xc[0],
    xc2 : xc[1],
    xc3 : xc[2]
  }
  var ycObj = {
    yc1 : yc[0],
    yc2 : yc[1],
    yc3 : yc[2]
  };
  var coordObj = [xcObj,ycObj];
  return coordObj;
}

function triDesign(){
  var tritop = document.getElementById("tri-top");
  var tribottom = document.getElementById("tri-bottom");
  topAndBottom(tritop);
  topAndBottom(tribottom);
}

function topAndBottom(t){
  if (t.getContext){
  var ctx = t.getContext("2d");
  var rounds = 0; 
  
  for (var r = -100; r < 5000; r+=36){
    rounds += 1;  
    ctx.fillStyle = randomColor();
    ctx.strokeStyle = randomColor();
    /*ctx.beginPath();
    ctx.moveTo(r,0);
    ctx.lineTo(r,36);
    ctx.stroke();*/
  
    var coordObj = coordinates();
    var xcObj = coordObj[0];
    var ycObj = coordObj[1];

    ctx.beginPath();
    ctx.moveTo(xcObj.xc1 + (rounds-1)*36,ycObj.yc1);
    ctx.lineTo(xcObj.xc2 + (rounds-1)*36,ycObj.yc2);
    ctx.lineTo(xcObj.xc3 + (rounds-1)*36,ycObj.yc3);
    ctx.closePath();
    ctx.fill();
  

    } 
}}

