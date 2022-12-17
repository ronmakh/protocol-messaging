var XMLHttpRequest = require("xmlhttprequest").XMLHttpRequest;

function httpGet(theUrl) {
  let xmlHttpReq = new XMLHttpRequest();
  xmlHttpReq.open("GET", theUrl, false); 
  xmlHttpReq.send(null);
  return xmlHttpReq.responseText;
}
var i = 1
while (i ==1) {
  console.log(httpGet('http://localhost:8080'));
}
