// Roann Yanes, Abby Gervase, and Grace Milton
// paradigms.js

// function that adds a new Item to the document
function Item(){
    this.item = null;
    this.addToDocument = function(){
        document.body.appendChild(this.item);
    }
}

// function that adds a label for an item that is added to the document
function Label(){
    this.item = null;
    this.createLabel= function(text, id, type){
        this.id = id;
        var label = document.createElement(type);
        label.setAttribute("id",id);
        var textLabel = document.createTextNode(text);
        label.appendChild(textLabel);
        this.item = label;
    }
    this.setText = function(text){
        this.item.innerHTML = text;
    }
}

// function that creates a link to the document (used for button click)
function Link(){
    this.item = null;
    this.createLink= function(text, id, url){
        this.id = id
        var label = document.createElement("a");
        label.setAttribute("href",url);
        var textLabel = document.createTextNode(text);
        label.appendChild(textLabel);
        this.item = label;
    }
    this.setText = function(text){
        this.item.innerHTML = text;
    }
}

// function that adds a new image to the document body
function Image(){
    this.item = null;
    this.createImage= function(text, id){
        this.id = id;
        var label = document.createElement("img");
        label.setAttribute("id",id);
        label.setAttribute("src",text);
        this.item = label;
    }
    this.setImage = function(text){
        this.item.src = text;
    }
}

// function that adds a new button to the document body
function Button(){
    this.item = null;
    this.createButton = function(text, id){
        this.id = id;
        var label = document.createElement("button");
        label.setAttribute("id",id);
        var textLabel = document.createTextNode(text);
        label.appendChild(textLabel);
        this.item = label;
    }
    this.addClickEventHandler = function(handler, args){
        this.item.onmouseup = function(){ handler(args);};
    }
}

// function that allows a break to be added to the document body (new line character)
function Break(){
    this.item = null;
    var label = document.createElement("br");
    this.item = label;
}

// functions that allows a dropdown menu to be added to the document body
function Dropdown(){
    this.createDropdown = function(dict, id, selected){
        this.item = document.createElement("select");
        this.id = id;
        this.dict = dict;
        this.selected = selected;
        var html = '<select>';
        for (var key in dict){
            var value = key;
            var label = dict[key];
            html+="<option value='"+value+"'>"+label+"</option>";
        }
        html+='</select>';
        this.item.innerHTML = html;
    }
    this.getSelected = function(){
        this.selected = this.item.options[this.item.selectedIndex].value;
        return this.selected;
    }
}
