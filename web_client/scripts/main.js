// Abbgy Gervase
// main.js

var pReq = new XMLHttpRequest();
var mid = "32"
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
pageTitle.createLabel("Book At Me Now","pageTitle", "h1");
pageTitle.addToDocument();

var pageSubtitle = new Label();
pageSubtitle.createLabel("A service that recommends books, hopefully","pageSubtitle","h2");
pageSubtitle.addToDocument();

var bookOpts = {
    1 : "1",
    5 : "5",
    10 : "10",
    15 : "15",
    20 : "20",
    30 : "30",
    40 : "40",
    50 : "50"
};

var yearOpts = {
    0 : "Select Option",
    1 : "B.C.",
    2 : "0-1000",
    3 : "1001-1500",
    4 : "1501-1600",
    5 : "1601-1700",
    6 : "1701-1800",
    7 : "1801-1850",
    8 : "1851-1900",
    9 : "1901-1910",
    10 : "1911-1920",
    11 : "1921-1930",
    12 : "1931-1940",
    13 : "1941-1950",
    14 : "1951-1960",
    15 : "1961-1970",
    16 : "1971-1980",
    17 : "1981-1990",
    18 : "1991-2000",
    19 : "2001-2010",
    20 : "2011-2017",
    21 : "2017"
};

var genreOpts = {
    0 :     "Select Option",
    1452 :  "Action/Adventure",
    4594 :  "Biographies",
    6857 :  "Children",
    7725 :  "Comedy",
    7778 :  "Comics",
    9886 :  "Drama",
    10059 : "Dystopia",
    11305 : "Fantasy",
    11743 : "Fiction",
    14552 : "History",
    14821 : "Horror",
    17933 : "Lesbians",
    20939 : "Mystery",
    21024 : "Mythology",
    21773 : "Nonfiction",
    23831 : "Poetry",
    25647 : "Religious",
    26138 : "Romance",
    26837 : "Science Fiction",
    27199 : "Series",
    30358 : "Thriller",
    33114 : "Young Adult"
}


var numBooksLabel = new Label();
pageTitle.createLabel("How many books do you want to look at?  ","numBooksLabel", "p");
pageTitle.addToDocument();

var numBooks = new Dropdown();
numBooks.createDropdown(bookOpts, "numBooks", 1);
numBooks.addToDocument();

var genreDropLabel = new Label();
genreDropLabel.createLabel("(Optional) What genre do you want to look at?","genreDropLabel", "p");
genreDropLabel.addToDocument();

var genreDrop = new Dropdown();
genreDrop.createDropdown(genreOpts, "genreDrop", 0);
genreDrop.addToDocument();

var yearDropLabel = new Label();
yearDropLabel.createLabel("(Optional) What year range do you want to look at?","yearDropLabel", "p");
yearDropLabel.addToDocument();

var yearDrop = new Dropdown();
yearDrop.createDropdown(yearOpts, "yearDrop", 0);
yearDrop.addToDocument();

var rateButton = new Button();
rateButton.createButton("Rate Books", "rateButton");
rateButton.addToDocument();
rateButton.addClickEventHandler(goToPage, "rate.html");

var recommendButton = new Button();
recommendButton.createButton("Get Recommended Books", "recommendButton");
recommendButton.addToDocument();
recommendButton.addClickEventHandler(goToPage, "recommend.html");

function goToPage(url){
    var cookie = document.cookie.split(';');
    for (var i = 0; i < cookie.length; i++) {
        var chip = cookie[i],
        entry = chip.split("="),
        name = entry[0];
        document.cookie = name + '=; expires=Thu, 01 Jan 1970 00:00:01 GMT;';
    }
    var booknum = String(numBooks.getSelected());
    var genrenum = String(genreDrop.getSelected());
    var yearnum = String(yearDrop.getSelected());
    document.cookie=booknum+","+genrenum+","+yearnum;
    location.href = url;    
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

down.addClickEventHandler(voteFunc, 1.00);
up.addClickEventHandler(voteFunc, 5.00);

var bookreqdata;
var ratingreqdata;

function voteFunc(number){
    var data = {};
    data.book_id = mid;
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
        mid = data["book_id"];
        var oReq = new XMLHttpRequest();
        oReq.open("GET", bookURL+mid, true);
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
        pReq.open("GET", ratingURL+mid, true);
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
    mid = data["book_id"];
    var oReq = new XMLHttpRequest();
    oReq.open("GET", bookURL+mid, true);
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
    pReq.open("GET", ratingURL+mid, true);
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
