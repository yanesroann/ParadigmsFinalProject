// Abby Gervase, Grace Milton and Roann Yanes
// recommend.js

// parses through the cookie to get the dropdown selections
var cookie = document.cookie.split(',');
var late = cookie[3].split(';')[0];
var early = cookie[2];
var genrenum = cookie[1];
var booknum = cookie[0];

var pReq = new XMLHttpRequest();
var bookURL = "http://student04.cse.nd.edu:51082/books/";
var ratingURL = "http://student04.cse.nd.edu:51082/ratings/";
var recommendURL = "http://student04.cse.nd.edu:51082/recommendations/";
var authorURL = "http://student04.cse.nd.edu:51082/authors/";
var yearURL = "http://student04.cse.nd.edu:51082/years/";
var genreURL = "http://student04.cse.nd.edu:51082/genres/";

// instantiation of items that are used on the recommend.html page
var cookie = document.cookie;
console.log(cookie);
Label.prototype = new Item();
Link.prototype = new Item();
Button.prototype = new Item();
Image.prototype = new Item();
Dropdown.prototype = new Item();

// adds the title of the page to recommend.html
var pageTitle = new Label();
pageTitle.createLabel("Recommended 4 U","ratePageTitle", "h1");
pageTitle.addToDocument();

// informs the user what to do on the page
var pageSubtitle = new Label();
pageSubtitle.createLabel("Click the author's name to see more of their books.","ratePageSubtitle","h2");
pageSubtitle.addToDocument();

// button to return to Home page (index.html)
var getMain = new Button();
getMain.createButton("Go To Home Page", "mainButton");
getMain.addToDocument();
getMain.addClickEventHandler(goToPage, "index.html");

// button to return to rate.html
var getRatings = new Button();
getRatings.createButton("Get Ratings", "rateButton");
getRatings.addToDocument();
getRatings.addClickEventHandler(goToPage, "rate.html");

// sends user to new page on button click
function goToPage(url){
    location.href = url;
}

// checks recommendation url for books within user's specifications
var qReq = new XMLHttpRequest();
qReq.open("GET", recommendURL+booknum+"/"+early+"/"+late+"/"+genrenum, true);
qReq.onload = function(e){
    data = JSON.parse(qReq.responseText);
    var bids = [-1];
    bids = data["book_id"];
    // ensures that number of books requested is never larger than recommended amount
    // ensures that loop stops if there are no more books for specified parameters
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
    // informs user that there is no books within the parameters selected
    else{
        var noResults = new Label();
        noResults.createLabel("No results for these parameters, please try again!", "noResults", "p");
        noResults.addToDocument();
    }
}
// error handling
qReq.onerror = function(e){
    console.error(qReq.statusText);
}
qReq.send(null);

// changes the recommended books displyed to user based on specified parameters
function changeBookRec(num, bid){
    // retrieves book information
    var oReq = new XMLHttpRequest();
    oReq.open("GET", bookURL+bid, true);
    oReq.onload = function(e){
        // displays book information to the user
        bookreqdata = JSON.parse(oReq.responseText);
        var title = bookreqdata["title"];
        var authors = bookreqdata["authors"];
        var author_ids = bookreqdata["author_ids"];
        var titletmp = new Label();
        titletmp.createLabel(title, "titleLabel"+String(i), "p");
        titletmp.addToDocument();
        for (a=0; a<authors.length; a++){
            tmp_args = [author_ids[a], authors[a]];
            // creates a button to check out more books by a specific author (author.html)
            var tmpauth = new Button();
            tmpauth.createButton(authors[a], String(author_ids[a])+"Link");
            tmpauth.addToDocument();
            tmpauth.addClickEventHandler(authorClick, tmp_args);
        }
    }
    // error handling
    oReq.onerror = function(e){
        console.error(oReq.statusText);
    }
    oReq.send(null);
}

// stores author information in the cookies
function authorClick(args){
    var cookie = document.cookie.split(';');
    document.cookie="aid="+args[0]+","+args[1];
    location.href = "author.html";
}
