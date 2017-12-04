// Abby Gervase, Grace Milton and Roann Yanes
// author.js

// parses through the cookie to get the dropdown selections
var cookie = document.cookie.split(';');
var aid = cookie[1].split('=')[1].split(',')[0];
var author = cookie[1].split('=')[1].split(',')[1];

var pReq = new XMLHttpRequest();
var bookURL = "http://student04.cse.nd.edu:51082/books/";
var ratingURL = "http://student04.cse.nd.edu:51082/ratings/";
var recommendURL = "http://student04.cse.nd.edu:51082/recommendations/";
var authorURL = "http://student04.cse.nd.edu:51082/authors/";
var yearURL = "http://student04.cse.nd.edu:51082/years/";
var genreURL = "http://student04.cse.nd.edu:51082/genres/";

// instantiation of items that are used on the author.html page
Label.prototype = new Item();
Link.prototype = new Item();
Button.prototype = new Item();
Image.prototype = new Item();
Dropdown.prototype = new Item();

// adds the title of the page to the author.html
var pageTitle = new Label();
pageTitle.createLabel("More From This Author","ratePageTitle", "h1");
pageTitle.addToDocument();

// adds name of author to the page
var pageSubtitle = new Label();
pageSubtitle.createLabel(author,"ratePageSubtitle","h2");
pageSubtitle.addToDocument();

// button to return to Home page (index.html)
var getMain = new Button();
getMain.createButton("Go To Home Page", "mainButton");
getMain.addToDocument();
getMain.addClickEventHandler(goToPage, "index.html");

// button to return to recommend.html
var recommendationButton = new Button();
recommendationButton.createButton("Go To Recommendations", "recommendButton");
recommendationButton.addToDocument();
recommendationButton.addClickEventHandler(goToPage, "recommend.html");

// sends user to new page on button click
function goToPage(url){
    location.href = url;
}

// retrieves the books by the author from book database
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

// error handling
qReq.onerror = function(e){
    console.error(qReq.statusText);
}
qReq.send(null);

// retrieves all of the books written by a particular author and displays them on the author.html page to the user
function changeBookInfo(num, bid){
    var oReq = new XMLHttpRequest();
    oReq.open("GET", bookURL+bid, true);
    oReq.onload = function(e){
        bookreqdata = JSON.parse(oReq.responseText);
        var title = bookreqdata["title"];
        var authors = bookreqdata["authors"];
        var author_ids = bookreqdata["author_ids"];
        var titletmp = new Label();
        titletmp.createLabel(title, "titleLabel"+String(i), "p");
        titletmp.addToDocument();
    }
    oReq.onerror = function(e){
        console.error(oReq.statusText);
    }
    oReq.send(null);
}
