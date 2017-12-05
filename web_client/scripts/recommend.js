// Abby Gervase, Grace Milton and Roann Yanes
// recommend.js

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

var cookie = document.cookie;
console.log(cookie);
Label.prototype = new Item();
Link.prototype = new Item();
Button.prototype = new Item();
Image.prototype = new Item();
Dropdown.prototype = new Item();

var pageTitle = new Label();
pageTitle.createLabel("Recommended 4 U","ratePageTitle", "h1");
pageTitle.addToDocument();

var pageSubtitle = new Label();
pageSubtitle.createLabel("Click the author's name to see more of their books.","ratePageSubtitle","h2");
pageSubtitle.addToDocument();

var getMain = new Button();
getMain.createButton("Go To Home Page", "mainButton");
getMain.addToDocument();
getMain.addClickEventHandler(goToPage, "index.html");

var getRatings = new Button();
getRatings.createButton("Get Ratings", "rateButton");
getRatings.addToDocument();
getRatings.addClickEventHandler(goToPage, "rate.html");

function goToPage(url){
    location.href = url;
}

var qReq = new XMLHttpRequest();
qReq.open("GET", recommendURL+booknum+"/"+early+"/"+late+"/"+genrenum, true);
qReq.onload = function(e){
    data = JSON.parse(qReq.responseText);
    var bids = [-1];
    bids = data["book_id"];
    if(bids[0] != -1){
        if(bids.length<booknum){
            looplimit = bids.length;
        }
        else{
            looplimit = booknum;
        }
        for (i=0; i<looplimit; i++){
            changeBookRec(i, bids[i]);
        }
    }
    else{
        var noResults = new Label();
        noResults.createLabel("No results for these parameters, please try again!", "noResults", "p");
        noResults.addToDocument();
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
        var title = bookreqdata["title"];
        var authors = bookreqdata["authors"];
        var author_ids = bookreqdata["author_ids"];
        var titletmp = new Label();
        titletmp.createLabel(title, "titleLabel"+String(i), "p");
        titletmp.addToDocument();
        for (a=0; a<authors.length; a++){
            tmp_args = [author_ids[a], authors[a]]
            var tmpauth = new Button();
            tmpauth.createButton(authors[a], String(author_ids[a])+"Link");
            tmpauth.addToDocument();
            tmpauth.addClickEventHandler(authorClick, tmp_args);
        }
    }
    oReq.onerror = function(e){
        console.error(oReq.statusText);
    }
    oReq.send(null);
}

function authorClick(args){
    var cookie = document.cookie.split(';');
    document.cookie="aid="+args[0]+","+args[1];
    location.href = "author.html";
}
