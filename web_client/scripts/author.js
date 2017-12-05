// Abby Gervase, Grace Milton and Roann Yanes
// author.js

var cookie = document.cookie.split(';');
var aid = cookie[1].split('=')[1].split(',')[0];
var author = cookie[1].split('=')[1].split(',')[1];

var pReq = new XMLHttpRequest();
var bid = "32"
var uid = "5"
var bookURL = "http://student04.cse.nd.edu:51082/books/";
var ratingURL = "http://student04.cse.nd.edu:51082/ratings/";
var recommendURL = "http://student04.cse.nd.edu:51082/recommendations/";
var authorURL = "http://student04.cse.nd.edu:51082/authors/";
var yearURL = "http://student04.cse.nd.edu:51082/years/";
var genreURL = "http://student04.cse.nd.edu:51082/genres/";

console.log(cookie);
Label.prototype = new Item();
Link.prototype = new Item();
Button.prototype = new Item();
Image.prototype = new Item();
Dropdown.prototype = new Item();
Break.prototype = new Item();

var pageTitle = new Label();
pageTitle.createLabel("More From "+author,"ratePageTitle", "h1");
pageTitle.addToDocument();

var pageSubtitle = new Label();
pageSubtitle.createLabel("Click the title to go to the Goodreads\u2122 page for each book.","ratePageSubtitle","h2");
pageSubtitle.addToDocument();

var getMain = new Button();
getMain.createButton("Go To Home Page", "mainButton");
getMain.addToDocument();
getMain.addClickEventHandler(goToPage, "index.html");

var recommendationButton = new Button();
recommendationButton.createButton("Go To Recommendations", "recommendButton");
recommendationButton.addToDocument();
recommendationButton.addClickEventHandler(goToPage, "recommend.html");

var break1 = new Break();
break1.addToDocument();

function goToPage(url){
    location.href = url;
}

var qReq = new XMLHttpRequest();
qReq.open("GET", authorURL+aid, true);
qReq.onload = function(e){
    data = JSON.parse(qReq.responseText);
    bids = data["books"];
    console.log(bids);
    for (i=0; i<bids.length; i++){
        changeBookInfo(i, bids[i]);
    }
}
qReq.onerror = function(e){
    console.error(qReq.statusText);
}
qReq.send(null);

function changeBookInfo(num, bid){
    var oReq = new XMLHttpRequest();
    oReq.open("GET", bookURL+bid, true);
    oReq.onload = function(e){
        bookreqdata = JSON.parse(oReq.responseText);
        var title = bookreqdata["title"];
        var authors = bookreqdata["authors"];
        var author_ids = bookreqdata["author_ids"];
        var tmpbreak1 = new Break();
        tmpbreak1.addToDocument();
        var tmpbreak2 = new Break();
        tmpbreak2.addToDocument();
        var linktmp = new Button();
        linktmp.createButton(title, "titleButton", "p");
        linktmp.addToDocument();
        linktmp.addClickEventHandler(goodreadsClick, bid);
    }
    oReq.onerror = function(e){
        console.error(oReq.statusText);
    }
    oReq.send(null);
}

function goodreadsClick(bid){
    location.href="https://www.goodreads.com/book/show/"+bid;
}
