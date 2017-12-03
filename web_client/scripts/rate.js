// Abby Gervase, Grace Milton and NOT Roann Yanes
// rate.js

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


Label.prototype = new Item();
Button.prototype = new Item();
Image.prototype = new Item();
Dropdown.prototype = new Item();

var pageTitle = new Label();
pageTitle.createLabel("Rate Some Goddamn Books","ratePageTitle", "h1");
pageTitle.addToDocument();

var pageSubtitle = new Label();
pageSubtitle.createLabel("Roann actually did contribute she was just being a butt","ratePageSubtitle","h2");
pageSubtitle.addToDocument();

var rateThisBook = new Label();
rateThisBook.createLabel("Rate this Book","rateThisBook", "p");
rateThisBook.addToDocument();

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
bookImage.createImage(" ");
bookImage.addToDocument();

args = [bookTitle, bookAuthor, bookRating, bookImage]

// Vote Buttons

var one = new Button();
one.createButton("1", "one");
one.addToDocument();
one.addClickEventHandler(rateFunc, 1.00);

var two = new Button();
two.createButton("2", "two");
two.addToDocument();
two.addClickEventHandler(rateFunc, 2.00);

var three = new Button();
three.createButton("3", "three");
three.addToDocument();
three.addClickEventHandler(rateFunc, 3.00);

var four = new Button();
four.createButton("4", "four");
four.addToDocument();
four.addClickEventHandler(rateFunc, 4.00);

var five = new Button();
five.createButton("5", "five");
five.addToDocument();
five.addClickEventHandler(rateFunc, 5.00);

var getRecommendations = new Button();
getRecommendations.createButton("Get Recommendations", "getRecommendations");
getRecommendations.addToDocument();
getRecommendations.addClickEventHandler(goToPage, "recommend.html");

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
    qReq.open("GET", recommendURL+"1", true);
    qReq.onload = function(e){
        data = JSON.parse(qReq.responseText);
        console.log("Gotten from recommendations:",data)
        bid = data["book_id"][0];
        var oReq = new XMLHttpRequest();
        oReq.open("GET", bookURL+bid, true);
        oReq.onload = function(e){
            bookreqdata = JSON.parse(oReq.responseText);
            //console.log("MOVIE DATA VOTE FUNC: " + bookreqdata["title"]);
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
            //console.log("RATING DATA VOTE FUNC: " + ratingreqdata["rating"]);
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
qReq.open("GET", recommendURL+"1", true);
qReq.onload = function(e){
    data = JSON.parse(qReq.responseText);
    bid = data["book_id"][0];
    var oReq = new XMLHttpRequest();
    oReq.open("GET", bookURL+bid, true);
    oReq.onload = function(e){
        bookreqdata = JSON.parse(oReq.responseText);
        //console.log("MOVIE DATA NO FUNC: " + bookreqdata["title"]);
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
        //console.log("RATING DATA NO FUNC: " + ratingreqdata["rating"]);
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
    //console.log("IN CHANGE TEXT"+bookreqdata["title"]);
    //console.log("IN CHANGE TEXT"+ratingreqdata["rating"]);
    args[0].setText(bookreqdata["title"]);
    args[1].setText(bookreqdata["authors"]);
    args[2].setText(ratingreqdata["rating"]);
    args[3].setImage(bookreqdata["img"]);
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
