// Abby Gervase, Grace Milton and NOT Roann Yanes
// rate.js

var cookie = document.cookie.split(',');
var late = cookie[3].split(';')[0];
var early = cookie[2];
var genrenum = cookie[1];
var booknum = cookie[0];

var pReq = new XMLHttpRequest();
var bid = "32"
var uid = "5"
var bookURL = "http://student04.cse.nd.edu:51082/books/";
var ratingURL = "http://student04.cse.nd.edu:51082/ratings/";
var recommendURL = "http://student04.cse.nd.edu:51082/recommendations/";
var authorURL = "http://student04.cse.nd.edu:51082/authors/";
var yearURL = "http://student04.cse.nd.edu:51082/years/";
var genreURL = "http://student04.cse.nd.edu:51082/genres/";


Label.prototype = new Item();
Button.prototype = new Item();
Image.prototype = new Item();
Dropdown.prototype = new Item();
Break.prototype = new Item();

var pageTitle = new Label();
pageTitle.createLabel("Rate. Some. Books.","ratePageTitle", "h1");
pageTitle.addToDocument();

var pageSubtitle = new Label();
pageSubtitle.createLabel("Choose 1 to 5 stars.","ratePageSubtitle","h2");
pageSubtitle.addToDocument();


var bookTitle = new Label();
bookTitle.createLabel("Book Title","bookTitle", "p");
bookTitle.addToDocument();

var bookAuthor = new Label();
bookAuthor.createLabel("Book Author","bookAuthor", "p");
bookAuthor.addToDocument();

var bookRating = new Label();
bookRating.createLabel("Book Rating","bookRating", "p");
bookRating.addToDocument();

var bookImage = new Image();
bookImage.createImage(" ", "bookImage");
bookImage.addToDocument();

args = [bookTitle, bookAuthor, bookRating, bookImage]

// Vote Buttons
var break1 = new Break();
break1.addToDocument();

var break2 = new Break();
break2.addToDocument();

var one = new Button();
one.createButton("\u2605", "one");
one.addToDocument();
one.addClickEventHandler(rateFunc, 1.00);

var two = new Button();
two.createButton('\u2605\u2605', "two");
two.addToDocument();
two.addClickEventHandler(rateFunc, 2.00);

var three = new Button();
three.createButton("\u2605\u2605\u2605", "three");
three.addToDocument();
three.addClickEventHandler(rateFunc, 3.00);

var four = new Button();
four.createButton("\u2605\u2605\u2605\u2605", "four");
four.addToDocument();
four.addClickEventHandler(rateFunc, 4.00);

var five = new Button();
five.createButton("\u2605\u2605\u2605\u2605\u2605", "five");
five.addToDocument();
five.addClickEventHandler(rateFunc, 5.00);

var break3 = new Break();
break3.addToDocument();

var break4 = new Break();
break4.addToDocument();

var getRecommendations = new Button();
getRecommendations.createButton("Get Recommendations", "recommendButton");
getRecommendations.addToDocument();
getRecommendations.addClickEventHandler(goToPage, "recommend.html");

var goHome = new Button();
goHome.createButton("Go Home", "mainButton");
goHome.addToDocument();
goHome.addClickEventHandler(goToPage, "index.html");

function goToPage(url){
    location.href = url;
}

function rateFunc(number){
    var data = {};
    data.id = bid;
    data.rating = number;
    console.log(data)
    var json = JSON.stringify(data);
    console.log(json);
    var put_xhr = new XMLHttpRequest();
    put_xhr.open("POST",recommendURL, true);
    put_xhr.onerror = function(e){
        console.error(put_xhr.statusText);
    }
    put_xhr.send(json);

    var qReq = new XMLHttpRequest();
    qReq.open("GET", recommendURL+"1"+"/"+early+"/"+late+"/"+genrenum, true);
    qReq.onload = function(e){
        data = JSON.parse(qReq.responseText);
        console.log("Gotten from recommendations:",data)
        bid = data["book_id"][0];
        var oReq = new XMLHttpRequest();
        oReq.open("GET", bookURL+bid, true);
        oReq.onload = function(e){
            bookreqdata = JSON.parse(oReq.responseText);
            changeText(args);
        }
        oReq.onerror = function(e){
            console.error(oReq.statusText);
        }
        oReq.send(null);
        var pReq = new XMLHttpRequest();
        pReq.open("GET", ratingURL+bid, true);
        pReq.onload = function(e){
            ratingreqdata = JSON.parse(pReq.responseText);
            changeText(args);
        }
        pReq.onerror = function(e){
            console.error(pReq.statusText);
        }
        pReq.send(null);
    }
    qReq.onerror = function(e){
        console.error(qReq.statusText);
    }
    qReq.send(null);
}

var qReq = new XMLHttpRequest();
qReq.open("GET", recommendURL+"1"+"/"+early+"/"+late+"/"+genrenum, true);
qReq.onload = function(e){
    data = JSON.parse(qReq.responseText);
    bid = data["book_id"][0];
    var oReq = new XMLHttpRequest();
    oReq.open("GET", bookURL+bid, true);
    oReq.onload = function(e){
        bookreqdata = JSON.parse(oReq.responseText);
        changeText(args);
    }
    oReq.onerror = function(e){
        console.error(oReq.statusText);
    }
    oReq.send(null);
    var pReq = new XMLHttpRequest();
    pReq.open("GET", ratingURL+bid, true);
    pReq.onload = function(e){
        ratingreqdata = JSON.parse(pReq.responseText);
        changeText(args);
    }
    pReq.onerror = function(e){
        console.error(pReq.statusText);
    }
    pReq.send(null);
}
qReq.onerror = function(e){
    console.error(qReq.statusText);
}
qReq.send(null);

function changeText(args){
    console.log(bookreqdata["result"]+"error"+bookreqdata["result"]=="error")
    if(bookreqdata["result"] != "error"){
        args[0].setText(bookreqdata["title"]);
        args[1].setText(bookreqdata["authors"]);
        args[2].setText(ratingreqdata["rating"]);
        args[3].setImage(bookreqdata["img"]);
    }
    else{
        args[0].setText("No more results for these parameters.");
        args[1].setText("Please return to home and search again!");
        args[2].setText(" ");
        args[3].setImage(" ");
    }
}

