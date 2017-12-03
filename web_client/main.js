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
Break.prototype = new Item();

var pageTitle = new Label();
pageTitle.createLabel("Book At Me Now","pageTitle", "h1");
pageTitle.addToDocument();

var pageSubtitle = new Label();
pageSubtitle.createLabel("\"The best book recommendation service I've ever seen.\"  \u2012 Obama","pageSubtitle","h2");
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
    0 : "Select Option",
    1542 :  "Action/Adventure",
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
pageTitle.createLabel("How many book recommendations do you want?  ","numBooksLabel", "p");
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

var break1 = new Break();
break1.addToDocument();

var break2 = new Break();
break2.addToDocument();

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
    if (genrenum==0){ genrenum=30574;}
    var yearnum = yearDrop.getSelected();
    var early, late, years;
    if(yearnum>1){
        var years = yearOpts[yearnum].split('-');
        var early = years[0];
        var late = years[1];
    }
    else if (yearnum==1){
        early = -5000;
        late = -1;
    }
    else{
        early = -5000;
        late = 2017;
    }
    document.cookie=booknum+","+genrenum+","+early+","+late;
    location.href = url;    
}

