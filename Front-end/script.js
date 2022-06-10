const textarea = document.getElementById('input_text');
const LineNumber = document.getElementById('counting');
const content = document.getElementById('content');
const dropdown = document.getElementById("drop-down")
const btn = document.getElementById("btn")
const animation = document.getElementById("center-body")


var firstElement = "   "
var listDropDowon = []
instructions = [
    // memory reference
    'AND',
    'ADD',
    'LDA',
    'STA',
    'BUN',
    'BSA',
    'ISZ',
    "ORG",
    "I",

    // register reference
    'CLA',
    'CLE',
    'CMA',
    'CME',
    'CIR',
    'CIL',
    'INC',
    'SPA',
    'SNA',
    'SZA',
    'SZE',
    'HLT',

    // I/O reference
    'INP',
    'OUT',
    'SKI',
    'SKO',
    'ION',
    'IOF',
]
textarea.addEventListener("input", (e) =>{

    var line = coutingLine(textarea)
    LineNumber.innerHTML = ""
    for(var i = 1; i <= line + 1; i++){
            LineNumber.innerHTML += `<span>${i}</span>`
        }
        autoCompelet(e.pageX, e.pageY)
    console.log(firstElement)

})
textarea.addEventListener('keydown', (e) => {
    console.log(textarea.selectionStart, textarea.selectionEnd)

    if (e.key == "Tab") {
        e.preventDefault()
        GetValue(firstElement)
        firstElement = "   "
    }  
});

function ShowAnimation(){
    console.log('enter')
    setTimeout(() => {
        animation.style.visibility = "visible"
    }, 100)
    setTimeout(() => {
        animation.style.visibility = "hidden"
    }, 3000)
    body.style.opacity = "1"
    
}
function coutingLine(textarea){
        var line = 0
        var text = textarea.value
        for(var i = 0; i < text.length; i++){
            if(text[i] == '\n'){
                line++
            }
        }
    return line
}
function GetValue(value){
    
    console.log(value)
    if (value === undefined)
        value = "   "

    var text = textarea.value.slice(0, textarea.selectionEnd);
    var textArray = text.split(/[\s,]+/);
    var textArrayLength = textArray.length;
    var textArrayLast = textArray[textArrayLength - 1];

    if (value != "   ")
            textarea.setRangeText(value.trim(), textarea.selectionStart - textArrayLast.length , textarea.selectionEnd, "end");
    else
        textarea.setRangeText(value, textarea.selectionStart , textarea.selectionStart, "end");
    dropdown.innerHTML  = ""
    dropdown.style.visibility = "hidden"
    firstElement = "   "
}
function SizeLineChar(textarea){

    var text = textarea.value;
    var textArray = text.split("\n");
    var textArrayLength = textArray.length;
    var textArrayLast = textArray[textArrayLength - 1];
    return textArrayLast.length

}

function autoCompelet(cursorX, cursorY){

    dropdown.style.visibility = 'hidden'
    var list = []
    var text = textarea.value.slice(0, textarea.selectionEnd);
    var textArray = text.split(/[\s,]+/);
    var textArrayLength = textArray.length;
    var textArrayLast = textArray[textArrayLength - 1];
    textArrayLast = textArrayLast.replace(/\n/g, "");
    textArrayLast = textArrayLast.toUpperCase();

    for(var i = 0; i < instructions.length; i++) {
        dropdown.innerHTML ="" 
        if(textArrayLast == instructions[i].substr(0, textArrayLast.length) && textArrayLast != "") {
            list.push(instructions[i])        
        }
    }
    
    firstElement = list[0]
    listDropDowon = list
    if(list.length > 0) {
        dropdown.style.visibility = "visible"
        for(var i = 0; i < list.length; i++) {
            dropdown.innerHTML += `<div class = "li" onclick ="GetValue('${list[i]}')">${list[i]}</div>`;
        }
    }else
        dropdown.style.visibility = "hidden"
}