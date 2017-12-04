// Abbgy Gervase, Roann Yanes, and Grace Milton
// main.js

var pReq = new XMLHttpRequest();
var bookURL = "http://student04.cse.nd.edu:51082/books/";
var ratingURL = "http://student04.cse.nd.edu:51082/ratings/";
var recommendURL = "http://student04.cse.nd.edu:51082/recommendations/";
var authorURL = "http://student04.cse.nd.edu:51082/authors/";
var yearURL = "http://student04.cse.nd.edu:51082/years/";
var genreURL = "http://student04.cse.nd.edu:51082/genres/";

// instantiation of items that are used on the index.html page
Label.prototype = new Item();
Button.prototype = new Item();
Image.prototype = new Item();
Dropdown.prototype = new Item();
Break.prototype = new Item();

// adds the title of the webservice to the index.html
var pageTitle = new Label();
pageTitle.createLabel("Book At Me Now","pageTitle", "h1");
pageTitle.addToDocument();

// adds our tag line to the index.html page
var pageSubtitle = new Label();
pageSubtitle.createLabel("\"The best book recommendation service I've ever seen.\"  \u2012 Barack Obama","pageSubtitle","h2");
pageSubtitle.addToDocument();

// dictionary of options for dropdown menu
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

// dictionary of year options for dropdown menu
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

// dictionary of genre options for dropdown menu
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

// asks the user how many books they want displayed to them
var numBooksLabel = new Label();
pageTitle.createLabel("How many book recommendations do you want?  ","numBooksLabel", "p");
pageTitle.addToDocument();

// adds number of books dropdown menu
var numBooks = new Dropdown();
numBooks.createDropdown(bookOpts, "numBooks", 1);
numBooks.addToDocument();

// asks the user what genre
var genreDropLabel = new Label();
genreDropLabel.createLabel("(Optional) What genre do you want to look at?","genreDropLabel", "p");
genreDropLabel.addToDocument();

// adds genre dropdown menu
var genreDrop = new Dropdown();
genreDrop.createDropdown(genreOpts, "genreDrop", 0);
genreDrop.addToDocument();

// asks the user what year they want books from
var yearDropLabel = new Label();
yearDropLabel.createLabel("(Optional) What year range do you want to look at?","yearDropLabel", "p");
yearDropLabel.addToDocument();

// adds year dropdown menu
var yearDrop = new Dropdown();
yearDrop.createDropdown(yearOpts, "yearDrop", 0);
yearDrop.addToDocument();

// adds break (new line)
var break1 = new Break();
break1.addToDocument();

// adds break (new line)
var break2 = new Break();
break2.addToDocument();

// adds a button that takes the user to the rate page
var rateButton = new Button();
rateButton.createButton("Rate Books", "rateButton");
rateButton.addToDocument();
rateButton.addClickEventHandler(goToPage, "rate.html");

// adds a button that takes the user to the reccomend page
var recommendButton = new Button();
recommendButton.createButton("Get Recommended Books", "recommendButton");
recommendButton.addToDocument();
recommendButton.addClickEventHandler(goToPage, "recommend.html");

// function to see what user selected from the home page and take user to a different page on button click
function goToPage(url){
    // retrieves selected from the cookies
    var cookie = document.cookie.split(';');
    for (var i = 0; i < cookie.length; i++) {
        var chip = cookie[i],
        entry = chip.split("="),
        name = entry[0];
        document.cookie = name + '=; expires=Thu, 01 Jan 1970 00:00:01 GMT;';
    }
    // retrieves the option selected by the user from the dropdown menu
    var booknum = String(numBooks.getSelected());
    var genrenum = String(genreDrop.getSelected());
    if (genrenum==0){ genrenum=30574;}
    var yearnum = yearDrop.getSelected();
    var early, late, years;
    // splits the year to retrieve the books from the book database within the range
    if(yearnum>1){
        var years = yearOpts[yearnum].split('-');
        var early = years[0];
        var late = years[1];
    }
    // if the user does not select a year range
    else if (yearnum==1){
        early = -5000;
        late = -1;
    }
    else{
        early = -5000;
        late = 2017;
    }
    // sets the user's choice in the cookies
    document.cookie=booknum+","+genrenum+","+early+","+late;
    location.href = url;    
}

