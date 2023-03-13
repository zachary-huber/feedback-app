// const e = require("cors");

// log that the file is loaded
console.log("form.js loaded");

var inputContainers = 0;
var inputLabels = 0;
var inputs = 0;
var hue = 0;
var newColor;

var formJSON;

function addElement() {
    newColor = generateRandomHSV(hue);

    // create a new div element
    var newDivID = "inputContainer" + inputContainers;
    var newDiv = document.createElement("div");
    newDiv.setAttribute("class", "inputContainer");
    newDiv.setAttribute("id", newDivID); // set id here
    console.log(newDivID);
    // document.getElementById(newDivID).getParent().removeChild(newDivID);

    // create a new button element - for delete button
    var newDeleteButton = document.createElement("button");
    newDeleteButton.setAttribute("type", "button");
    newDeleteButton.setAttribute("id", "button" + inputContainers); // set id here
    newDeleteButton.setAttribute("onclick", "deleteElement(" + newDivID + ")");
    newDeleteButton.setAttribute("class", "deleteButton");
    newDeleteButton.innerHTML = "X";


    // create a new input element - for input name
    var newInput = document.createElement("input");
    newInput.setAttribute("type", "text");
    newInput.setAttribute("id", "input" + inputs); // set id here
    // newInput.setAttribute("value", "input_" + inputs)
    newInput.setAttribute("placeholder", "Enter your inqury here...");
    newInput.setAttribute("class", "formElements");


    // create a new select element - for input type
    var selectID = "select" + inputs;
    var newSelect = document.createElement("select");
    newSelect.setAttribute("id", selectID); // set id here
    newSelect.setAttribute("class", "formElements");
    newSelect.setAttribute("onchange", "checkSelect("+ selectID +")");


    // create a new option element - for input type
    var options = ['text-field', 'true-false', 'attitude-scale'];
    for (var i = 0; i < options.length; i++) {
        var opt = options[i];
        var el = document.createElement("option");
        el.textContent = opt;
        el.value = opt;
        newSelect.appendChild(el);
    }


    // add the newly created element and its content into the DOM
    document.getElementById("form-elements").appendChild(newDiv);
    document.getElementById("inputContainer" + inputContainers).appendChild(newDeleteButton);
    document.getElementById("inputContainer" + inputContainers).appendChild(newSelect);
    document.getElementById("inputContainer" + inputContainers).appendChild(newInput);
    
    // increment the counters
    inputContainers++;
    inputLabels++;
    inputs++;

    return newDiv;
}




function removeParentElement(IDtoBeRemoved) {
    var element = document.getElementById(IDtoBeRemoved);
    element.parentNode.removeChild(element);
}


function saveForm(){
    var form = document.getElementById("form");
    var formHTML = form.innerHTML;
    localStorage.setItem("form", formHTML);
}


function loadForm(){
    var formHTML = localStorage.getItem("form");
    document.getElementById("form").innerHTML = formHTML;
}


function generateRandomHSV(hue) {
    var s = 100;
    var v = 85;
    hue += 200;
    h = hue;
    console.log(hue);
    return "hsl(" + h + ", " + s + "%, " + v + "%)";
}


function checkSelect(someID){
    var id = someID.id;
    var value = someID.value;
    // console.log(id);
    // console.log(value);
    switch (value) {
        case "text-field":
            console.log("text-field");
            someID.setAttribute("background", "rgba(22, 84, 218, 0.3)");
            break;
        case "true-false":
            console.log("true-false");
            someID.setAttribute("background", "red");
            break;
        case "attitude-scale":
            console.log("attitude-scale");
            break;

    default:
        console.log("default");
    }
}

function saveForm(){
    var formStructure = [];
    var formElements = document.getElementById("form-elements");
    var formTitle = document.getElementById("formTitle").innerHTML;
    formStructure.push({
        formTitle: formTitle
    });

    // for every child of form-elements, get select value and input value
    for (var i = 0; i < formElements.children.length; i++) {
        var child = formElements.children[i];
        var select = child.children[1];
        var input = child.children[2];
        console.log(select.value);
        console.log(input.value);


        // append select value and input value to formStructure array as an object
        formStructure.push({
            inputID: child.getAttribute("id"),
            fieldType: select.value,
            fieldNameQuestion: input.value
        });
    }
    console.log(formStructure);

    document.getElementById("formJSON").innerHTML = "Form JSON: <br>" + JSON.stringify(formStructure);
    return formStructure;
}

function createInputElement(type){
    var newInput = document.createElement("input");
    newInput.setAttribute("type", type);
    newInput.setAttribute("id", "input" + inputs); // set id here
    newInput.setAttribute("class", "formElements");
    return newInput;
}


function deleteElement(someID){
    someID.remove();
}

function loadFormEditor(formJSON){
    formTitle = formJSON[0].formTitle;
    document.getElementById("formTitle").innerHTML = formTitle;
    for (var i = 1; i < formJSON.length; i++) {
        var newDiv = addElement();
        var newSelect = newDiv.children[1];
        var newInput = newDiv.children[2];
        newSelect.value = formJSON[i].fieldType;
        newInput.value = formJSON[i].fieldNameQuestion;
    }
}

var responseElements = 0;
var responseInputs = 0;
var responseHeadings = 0;



function addResponseElement(inputType, questionHeading){
    // create response element div
    var newDiv = document.createElement("div");
    newDiv.setAttribute("id", "responseElement" + responseElements);
    newDiv.setAttribute("class", "responseElement");
    document.getElementById("form-elements").appendChild(newDiv);

    // create response heading
    var newHeading = document.createElement("h3");
    newHeading.setAttribute("id", "responseHeading" + responseHeadings);
    newHeading.setAttribute("class", "responseHeading");
    newHeading.innerHTML = questionHeading;
    newDiv.appendChild(newHeading);

    switch (inputType) {
        case "text-field":
            // create response input
            var newInput = document.createElement("input");
            newInput.setAttribute("type", "text");
            newInput.setAttribute("name", "question");
            newInput.setAttribute("id", "responseInput" + responseInputs);
            newInput.setAttribute("class", "responseInput");
            newInput.setAttribute("placeholder", "Enter your answer here");
            newDiv.appendChild(newInput);
            break;
        case "true-false":
            var newInput = createInputElement("radio");
            newInput.setAttribute("name", "true-false" + responseInputs);
            newInput.setAttribute("value", "true");
            newInput.setAttribute("checked", "checked");
            newDiv.appendChild(newInput);
            var newLabel = document.createElement("label");
            newLabel.setAttribute("for", "true");
            newLabel.innerHTML = "True";
            newDiv.appendChild(newLabel);
            var newInput = createInputElement("radio");
            newInput.setAttribute("name", "true-false" + responseInputs);
            newInput.setAttribute("value", "false");
            newDiv.appendChild(newInput);
            var newLabel = document.createElement("label");
            newLabel.setAttribute("for", "false");
            newLabel.innerHTML = "False";
            newDiv.appendChild(newLabel);
            break;
        case "attitude-scale":
            var newInput = createInputElement("radio");
            newInput.setAttribute("name", "attitude-scale" + responseInputs);
            newInput.setAttribute("value", "1");
            newInput.setAttribute("checked", "checked");
            newDiv.appendChild(newInput);
            var newLabel = document.createElement("label");
            newLabel.setAttribute("for", "1");
            newLabel.innerHTML = "1 = Disagree";
            newDiv.appendChild(newLabel);
            var newInput = createInputElement("radio");
            newInput.setAttribute("name", "attitude-scale" + responseInputs);
            newInput.setAttribute("value", "2");
            newDiv.appendChild(newInput);
            var newLabel = document.createElement("label");
            newLabel.setAttribute("for", "2");
            newLabel.innerHTML = "2 = Neutral";
            newDiv.appendChild(newLabel);
            var newInput = createInputElement("radio");
            newInput.setAttribute("name", "attitude-scale" + responseInputs);
            newInput.setAttribute("value", "3");
            newDiv.appendChild(newInput);
            var newLabel = document.createElement("label");
            newLabel.setAttribute("for", "3");
            newLabel.innerHTML = "3 = Agree";
            newDiv.appendChild(newLabel);
            break;
            default:
                console.log("default");
    }
    

    responseHeadings++;
    responseInputs++;
    responseElements++;

    return newDiv;
}

function loadFormUser(formJSON){
    formTitle = formJSON[0].formTitle;
    document.getElementById("formTitle").innerHTML = formTitle;
    for (var i = 1; i < formJSON.length; i++) {
        var newResponseInput = formJSON[i].fieldType;
        var newResponseQuestionHeading = formJSON[i].fieldNameQuestion;
        if(newResponseQuestionHeading == ""){
            newResponseQuestionHeading = i + ". ";
        }
        else {
            newResponseQuestionHeading = i + ". " + newResponseQuestionHeading;
        }
        var ResponseInput = addResponseElement(newResponseInput, newResponseQuestionHeading);
    }
}


function submitResponses(){
    var responseElements = document.getElementsByClassName("responseElement");
    var responseJSON = [];
    for (var i = 0; i < responseElements.length; i++) {
        var child = responseElements[i];
        var responseHeading = child.children[0].innerHTML;
        var responseInput = child.children[1];
        var responseValue = responseInput.value;
        if(responseInput.type == "radio"){
            responseValue = responseInput.checked;
        }
        responseJSON.push({
            responseHeading: responseHeading,
            responseValue: responseValue
        });
    }
    console.log(responseJSON);
    document.getElementById("responseJSON").innerHTML = "Response JSON: <br>" + JSON.stringify(responseJSON);
    return responseJSON;
}

function sendData() {
    var formEditorJSON = saveForm();
    $.ajax({
        url: '/myview/',
        type: 'POST',
        data: {'formEditorJSON': formEditorJSON},
        success: function(response) {
            // Handle the response from the server
        },
        error: function(response) {
            // Handle the error
        }
    });
}

testJSON = [{"formTitle":"Form1Test"},{"inputID":"inputContainer0","fieldType":"text-field","fieldNameQuestion":"text field test"},{"inputID":"inputContainer1","fieldType":"attitude-scale","fieldNameQuestion":"Did you have a good day?"},{"inputID":"inputContainer2","fieldType":"true-false","fieldNameQuestion":"true false"},{"inputID":"inputContainer3","fieldType":"text-field","fieldNameQuestion":""}]
testJSON = [{"formTitle":"-Name your form here!-"},{"inputID":"inputContainer0","fieldType":"text-field","fieldNameQuestion":"asdasda"},{"inputID":"inputContainer1","fieldType":"attitude-scale","fieldNameQuestion":"weee"},{"inputID":"inputContainer2","fieldType":"text-field","fieldNameQuestion":"tttt"},{"inputID":"inputContainer3","fieldType":"true-false","fieldNameQuestion":"aaaa"},{"inputID":"inputContainer4","fieldType":"text-field","fieldNameQuestion":"aaaa"}]


// addResponseField();
// loadFormEditor(testJSON);
loadFormUser(testJSON);