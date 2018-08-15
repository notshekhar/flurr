
function getHttp(url){
  let request = new XMLHttpRequest();
  request.open("GET", url);
  let text;
  request.onloadstart = function(){
    console.log("loading");
  }
  request.upload.onloadend = function(){
    // console.log(data);
    console.log("end loading bar");
    let text = request.responseText;
    console.log(text);
    console.log(request.statusText);
    console.log(request.status);
  }
  request.send();
}

function postHttp(url, data){
  let request = new XMLHttpRequest();
  request.open("POST", url);
  request.onloadstart = function(){
    console.log("loading");
  }
  request.onloadend = function(){
    console.log("endloading", request.responseText, request.status);
    console.log(request);
  }
  let d = new FormData();
  let keys = Object.keys(data);
  for(let i=0; i<keys.length; i++){
    d.append(keys[i], data[keys[i]]);
  }
  request.send(d);
}


function getMouce(){
  let pointx = [];
  let pointy = [];

  document.addEventListener("mousemove", function(e){
    x = e.clientX;
    y = e.clientY;
    pointx.push(x);
    pointy.push(y);
    // console.log({"x": x, "y": y});
    // data = {"x": x, "y": y};
  });
  return {"x": pointx[pointx.length-1], "y": pointy[pointy.length-1]};

}

function downloadJSON(a, data){
  let datStr = "data:text/json;charset=utf-8," + encodeURIComponent(JSON.stringify(data));
  let downloadNode = document.createElement("a");
  downloadNode.setAttribute("href", datStr);
  downloadNode.setAttribute("download", a + ".json");
  downloadNode.click();
  downloadNode.remove();
}

function firebaseStorage(path, filename){
  var storageRef = firebase.storage().ref('/stantschool/' + filename);
  var uploadTask = storageRef.put(path);
}
function firebaseDatabase(ref, data){
  let database = firebase.database();
  let dref = database.ref(ref);

  dref.push(data);
  // {"post id": 2}
}
function firebaseDatabaseRead(ref){
  let database = firebase.database();
  let dref = database.ref(ref);
  let data = [];
  dref.on("value", function(snap){
    let value = snap.val();
    let keys = Object.keys(value);
    for(let i = 0; i<keys.length; i++){

      console.log(value[keys[i]]);
      data.push(value[keys[i]]);

    }

  });

  return data
}

function loadPixels(img){
  let c=document.createElement("canvas");
  c.width = img.width;
  c.height = img.height;
  let ctx=c.getContext("2d");
  ctx.drawImage(img,0,0);
  let imgData=ctx.getImageData(0,0,c.width,c.height).data;
  return imgData;
}
function rgba(arr){
  let r=[];
  let g=[];
  let b =[];
  let a = [];

  for (let i = 0; i < arr.length; i+=4) {
    r.push(arr[i]);
    g.push(arr[i+1]);
    b.push(arr[i+2]);
    a.push(arr[i+3]);
  }
  return {"red": r, "green": g, "blue": b, "alpha": a};
}
function cto(pixels){
  let p=[];
  for (let i = 0; i < pixels.length; i++) {
    p.push(pixels[i]/255);
  }
  return p;
}
// function imagetourl(url){
//   let img = new Image();
//   img.src = url;
//   img.onload = function(){
//   }
// }
