// Abby Gervase, Grace Milton and Roann Yanes
// rate.js

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

// instantiation of items that are used on the rate.html page
Label.prototype = new Item();
Button.prototype = new Item();
Image.prototype = new Item();
Dropdown.prototype = new Item();
Break.prototype = new Item();

// adds the title of the page to the rate.html
var pageTitle = new Label();
pageTitle.createLabel("Rate. Some. Books.","ratePageTitle", "h1");
pageTitle.addToDocument();

// informs the user what to do on the page
var pageSubtitle = new Label();
pageSubtitle.createLabel("Choose 1 to 5 stars.","ratePageSubtitle","h2");
pageSubtitle.addToDocument();

// adds the title of the book to the page
var bookTitle = new Label();
bookTitle.createLabel("Book Title","bookTitle", "p");
bookTitle.addToDocument();

// adds the author of the book to the page
var bookAuthor = new Label();
bookAuthor.createLabel("Book Author","bookAuthor", "p");
bookAuthor.addToDocument();

// adds the book's rating to the page
var bookRating = new Label();
bookRating.createLabel("Book Rating","bookRating", "p");
bookRating.addToDocument();

// adds the image of the book to the page
var bookImage = new Image();
bookImage.createImage(" ", "bookImage");
bookImage.addToDocument();

// stores the book information
args = [bookTitle, bookAuthor, bookRating, bookImage]

// Vote Buttons
var break1 = new Break();
break1.addToDocument();

var break2 = new Break();
break2.addToDocument();

// one star
var one = new Button();
one.createButton("\u2605", "one");
one.addToDocument();
one.addClickEventHandler(rateFunc, 1.00);

// two stars
var two = new Button();
two.createButton('\u2605\u2605', "two");
two.addToDocument();
two.addClickEventHandler(rateFunc, 2.00);

// three stars
var three = new Button();
three.createButton("\u2605\u2605\u2605", "three");
three.addToDocument();
three.addClickEventHandler(rateFunc, 3.00);

// four stars
var four = new Button();
four.createButton("\u2605\u2605\u2605\u2605", "four");
four.addToDocument();
four.addClickEventHandler(rateFunc, 4.00);

// five stars
var five = new Button();
five.createButton("\u2605\u2605\u2605\u2605\u2605", "five");
five.addToDocument();
five.addClickEventHandler(rateFunc, 5.00);

// adds "new line character"
var break3 = new Break();
break3.addToDocument();

var break4 = new Break();
break4.addToDocument();

// button to return to recommend.html
var getRecommendations = new Button();
getRecommendations.createButton("Get Recommendations", "recommendButton");
getRecommendations.addToDocument();
getRecommendations.addClickEventHandler(goToPage, "recommend.html");

// button to return to Home page (index.html)
var goHome = new Button();
goHome.createButton("Go Home", "mainButton");
goHome.addToDocument();
goHome.addClickEventHandler(goToPage, "index.html");

// sends user to new page on button click
function goToPage(url){
    location.href = url;
}

// sends the user's rating to the server as a POST
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
    
    // retrieves a new book for the user to rate
    var qReq = new XMLHttpRequest();
    qReq.open("GET", recommendURL+"1"+"/"+early+"/"+late+"/"+genrenum, true);
    qReq.onload = function(e){
        data = JSON.parse(qReq.responseText);
        bid = data["book_id"][0];
        var oReq = new XMLHttpRequest();
        // retrieves book information
        oReq.open("GET", bookURL+bid, true);
        oReq.onload = function(e){
            bookreqdata = JSON.parse(oReq.responseText);
            changeText(args);
        }
        // error handling
        oReq.onerror = function(e){
            console.error(oReq.statusText);
        }
        // error handling
        oReq.send(null);
        var pReq = new XMLHttpRequest();
        // retrieves book's rating
        pReq.open("GET", ratingURL+bid, true);
        pReq.onload = function(e){
            ratingreqdata = JSON.parse(pReq.responseText);
            changeText(args);
        }
        // error handling
        pReq.onerror = function(e){
            console.error(pReq.statusText);
        }
        pReq.send(null);
    }
    // error handling
    qReq.onerror = function(e){
        console.error(qReq.statusText);
    }
    qReq.send(null);
}

var qReq = new XMLHttpRequest();
// checks recommendation url
qReq.open("GET", recommendURL+"1"+"/"+early+"/"+late+"/"+genrenum, true);
qReq.onload = function(e){
    data = JSON.parse(qReq.responseText);
    bid = data["book_id"][0];
    var oReq = new XMLHttpRequest();
    // retrieves book information
    oReq.open("GET", bookURL+bid, true);
    oReq.onload = function(e){
        bookreqdata = JSON.parse(oReq.responseText);
        changeText(args);
    }
    // error handling
    oReq.onerror = function(e){
        console.error(oReq.statusText);
    }
    oReq.send(null);
    // retrieves rating information
    var pReq = new XMLHttpRequest();
    pReq.open("GET", ratingURL+bid, true);
    pReq.onload = function(e){
        ratingreqdata = JSON.parse(pReq.responseText);
        changeText(args);
    }
    // error handling
    pReq.onerror = function(e){
        console.error(pReq.statusText);
    }
    pReq.send(null);
}
// error handling
qReq.onerror = function(e){
    console.error(qReq.statusText);
}
qReq.send(null);

// changes the text displayed to the user to display the correct book information after rating a book
function changeText(args){
    console.log(bookreqdata["result"]+"error"+bookreqdata["result"]=="error")
    if(bookreqdata["result"] != "error"){
        args[0].setText(bookreqdata["title"]);
        args[1].setText(bookreqdata["authors"]);
        args[2].setText(ratingreqdata["rating"]);
        args[3].setImage(bookreqdata["img"]);
    }
    // informs user that there are no more books to rate
    else{
        args[0].setText("No more results for these parameters.");
        args[1].setText("Please return to home and search again!");
        args[2].setText(" ");
        args[3].setImage(" ");
    }
}

