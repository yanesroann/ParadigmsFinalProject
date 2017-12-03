// Abby Gervase
// paradigms.js

function Item(){
    this.item = null;
    this.addToDocument = function(){
        document.body.appendChild(this.item);
    }
}

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

function Link(){
    this.item = null;
    this.createLink= function(text, id, url){
        this.id = id
        var label = document.createElement("a");
        //label.setAttribute("id",id);
        label.setAttribute("href",url);
        var textLabel = document.createTextNode(text);
        label.appendChild(textLabel);
        this.item = label;
    }
    this.setText = function(text){
        this.item.innerHTML = text;
    }
}

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

function Break(){
    this.item = null;
    var label = document.createElement("br");
    this.item = label;
}

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
