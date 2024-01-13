function OpenNav() {
    document.getElementById("side-nav").style.width = "300px";
}

function CloseNav() {
    document.getElementById("side-nav").style.width = "0px";
}



function LightMode() {
    document.getElementById("body").style.backgroundColor = "#0F112C";
    document.getElementById("top-nav").style.backgroundColor = "#0F112C";

    var form = document.getElementById("form");

    if (form) {
        form.style.color = "black";
        form.style.backgroundColor = "#white";
    }

    var sunElement = document.getElementById("sun");
    var moonElement = document.getElementById("moon");

    if (sunElement && moonElement) {
        sunElement.style.display = "none";
        moonElement.style.display = "block";
    }





    document.getElementById("side-nav-top").style.backgroundColor = "#eeeeff";
    document.getElementById("side-nav").style.backgroundColor = "white";

    var label = document.getElementsByClassName("label");

    for (var i = 0; i < label.length; i++) {
    label[i].style.color = "black";}

    var input_box  = document.getElementsByClassName("input-box");

    for (var i = 0; i < input_box .length; i++) {
    input_box[i].style.color = "black";}

    var elements = document.getElementsByClassName("side-nav-link");

    for (var i = 0; i < elements.length; i++) {
    elements[i].style.color = "black";}

    var faq_cons = document.getElementsByClassName("faq-con");

    for (var i = 0; i < faq_cons.length; i++) {
        faq_cons[i].style.backgroundColor = "white";   
    }

    var faq_question = document.getElementsByClassName("faq-question");

    for (var i = 0; i < faq_question.length; i++) {
        faq_question[i].style.color = "black";   
    }

    var faq_answer = document.getElementsByClassName("faq-answer");

    for (var i = 0; i < faq_answer.length; i++) {
        faq_answer[i].style.backgroundColor = "#0d0f34";   
    }

    

}
  
function DarkMode() {
    document.getElementById("body").style.backgroundColor = "black";
    document.getElementById("top-nav").style.backgroundColor = "black";
    document.getElementById("side-nav-top").style.backgroundColor = "black";
    document.getElementById("side-nav").style.backgroundColor = "#0b1118";

    var form = document.getElementById("form");

    if (form) {
        form.style.color = "white";
        form.style.backgroundColor = "#0b1118";
    }

    var sunElement = document.getElementById("sun");
    var moonElement = document.getElementById("moon");

    if (sunElement && moonElement) {
        sunElement.style.display = "block";
        moonElement.style.display = "none";
    }


    var elements = document.getElementsByClassName("side-nav-link");

    for (var i = 0; i < elements.length; i++) {
    elements[i].style.color = "white";}

    var faq_cons = document.getElementsByClassName("faq-con");

    for (var i = 0; i < faq_cons.length; i++) {
        faq_cons[i].style.backgroundColor = "#0b1118";   
    }


    var faq_question = document.getElementsByClassName("faq-question");

    for (var i = 0; i < faq_question.length; i++) {
        faq_question[i].style.color = "white";   
    }

    var faq_answer = document.getElementsByClassName("faq-answer");

    for (var i = 0; i < faq_answer.length; i++) {
        faq_answer[i].style.backgroundColor = "black";   
    }

    var label = document.getElementsByClassName("label");

    for (var i = 0; i < label.length; i++) {
    label[i].style.color = "white";}

    var input_box = document.getElementsByClassName("input-box");

    for (var i = 0; i < input_box .length; i++) {
    input_box[i].style.color = "white";}

    

}


function toggleAnswer(answerId) {
    var answer = document.getElementById(answerId);
    answer.style.display = (answer.style.display === 'none' || answer.style.display === '') ? 'block' : 'none';
  }