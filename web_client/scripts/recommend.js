// Abby Gervase, Grace Milton and Roann Yanes
// recommend.js

var cookie = document.cookie.split(',');
var yearnum = cookie[2].split(';')[0];
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

var cookie = document.cookie;
console.log(cookie);
Label.prototype = new Item();
Link.prototype = new Item();
Button.prototype = new Item();
Image.prototype = new Item();
Dropdown.prototype = new Item();

var pageTitle = new Label();
pageTitle.createLabel("Read This Shit","ratePageTitle", "h1");
pageTitle.addToDocument();

var pageSubtitle = new Label();
pageSubtitle.createLabel("I don't wanna be heeerrre","ratePageSubtitle","h2");
pageSubtitle.addToDocument();

var getMain = new Button();
getMain.createButton("Go To Home Page", "getMain");
getMain.addToDocument();
getMain.addClickEventHandler(goToPage, "index.html");

var getRatings = new Button();
getRatings.createButton("Get Ratings", "getRatings");
getRatings.addToDocument();
getRatings.addClickEventHandler(goToPage, "rate.html");

var titleArray = new Array(booknum);
var authorArray = new Array(booknum);

/*
for (i=0; i<booknum; i++){
    var titletmp = new Label();
    var authortmp = new Link();
    titletmp.createLabel(String(i+1), "titleLabel"+String(i), "p");
    authortmp.createLabel(String(i+1), "authorLabel"+String(i), "author.html");
    titletmp.addToDocument();
    authortmp.addToDocument();
    titleArray[i] = titletmp;
    authorArray[i] = authortmp;
}

/*
var getMain2 = new Button();
getMain2.createButton("Go To Home Page", "getMain2");
getMain2.addToDocument();
getMain2.addClickEventHandler(goToPage, "index.html");

var getRatings2 = new Button();
getRatings2.createButton("Get Ratings", "getRatings2");
getRatings2.addToDocument();
getRatings2.addClickEventHandler(goToPage, "rate.html");
*/

function goToPage(url){
    location.href = url;
}

var qReq = new XMLHttpRequest();
qReq.open("GET", recommendURL+String(booknum), true);
qReq.onload = function(e){
    data = JSON.parse(qReq.responseText);
    bids = data["book_id"];
    for (i=0; i<booknum; i++){
        changeBookRec(i, bids[i]);
    }
}
qReq.onerror = function(e){
    console.error(qReq.statusText);
}
qReq.send(null);

function changeBookRec(num, bid){
    var oReq = new XMLHttpRequest();
    oReq.open("GET", bookURL+bid, true);
    oReq.onload = function(e){
        bookreqdata = JSON.parse(oReq.responseText);
        //console.log("MOVIE DATA NO FUNC: " + bookreqdata["title"]);
        var title = bookreqdata["title"];
        var authors = bookreqdata["authors"];
        var author_ids = bookreqdata["author_ids"];
        var titletmp = new Label();
        titletmp.createLabel((num+1)+". "+title, "titleLabel"+String(i), "p");
        titletmp.addToDocument();
        for (a=0; a<authors.length; a++){
            var tmpauth = new Button();
            //tmpauth.createLink(authors[a], String(author_ids[a])+"Link", "author.html");
            tmpauth.createButton(authors[a], String(author_ids[a])+"Link");
            tmpauth.addToDocument();
            tmpauth.addClickEventHandler(authorClick, author_ids[a]);
        }
    }
    oReq.onerror = function(e){
        console.error(oReq.statusText);
    }
    oReq.send(null);
    //console.log("IN CHANGE TEXT"+bookreqdata["title"]);
    //console.log("IN CHANGE TEXT"+ratingreqdata["rating"]);
}

function authorClick(aid){
    var cookie = document.cookie.split(';');
    /*
    for (var i = 0; i < cookie.length; i++) {
        var chip = cookie[i],
        entry = chip.split("="),
        name = entry[0];
        document.cookie = name + '=; expires=Thu, 01 Jan 1970 00:00:01 GMT;';
    }
    */
    document.cookie="aid="+aid;
    location.href = "author.html";
}

/*
var image = new Image();
image.createImage("http://student04.cse.nd.edu/skumar5/images/vxiIABQhiFlfODwamoevrzXvowU.jpg","image");
image.addToDocument();

var up = new Button();
up.createButton("Up", "up");
up.addToDocument();

var rating = new Label();
rating.createLabel(" ","rating");
rating.addToDocument();

args = [ bookTitle, rating, image ];

down.addClickEventHandler(rateFunc, 1.00);
up.addClickEventHandler(rateFunc, 5.00);

var bookreqdata;
var ratingreqdata;

function rateFunc(number){
    var data = {};
    data.book_id = bid;
    data.rating = number;
    var json = JSON.stringify(data);
    console.log(json);
    var put_xhr = new XMLHttpRequest();
    put_xhr.open("PUT",recommendURL+uid, true);
    put_xhr.onerror = function(e){
        console.error(put_xhr.statusText);
    }
    put_xhr.send(json);

    var qReq = new XMLHttpRequest();
    qReq.open("GET", recommendURL+uid, true);
    qReq.onload = function(e){
        data = JSON.parse(qReq.responseText);
        bid = data["book_id"];
        var oReq = new XMLHttpRequest();
        oReq.open("GET", bookURL+bid, true);
        oReq.onload = function(e){
            bookreqdata = JSON.parse(oReq.responseText);
            console.log("MOVIE DATA VOTE FUNC: " + bookreqdata["title"]);
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
            console.log("RATING DATA VOTE FUNC: " + ratingreqdata["rating"]);
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
qReq.open("GET", recommendURL+uid, true);
qReq.onload = function(e){
    data = JSON.parse(qReq.responseText);
    bid = data["book_id"];
    var oReq = new XMLHttpRequest();
    oReq.open("GET", bookURL+bid, true);
    oReq.onload = function(e){
        bookreqdata = JSON.parse(oReq.responseText);
        console.log("MOVIE DATA NO FUNC: " + bookreqdata["title"]);
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
        console.log("RATING DATA NO FUNC: " + ratingreqdata["rating"]);
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
    console.log("IN CHANGE TEXT"+bookreqdata["title"]);
    console.log("IN CHANGE TEXT"+ratingreqdata["rating"]);
    args[0].setText(bookreqdata["title"]);
    args[1].setText(ratingreqdata["rating"]);
    args[2].setImage(imageURL+bookreqdata["img"]);
}
*/
