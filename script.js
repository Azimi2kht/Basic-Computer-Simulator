const textarea = document.getElementById('input_text');
const LineNumber = document.getElementById('counting');
const content = document.getElementById('content');
const dropdown = document.getElementById("drop-down")
const btn = document.getElementById("btn")
const animation = document.getElementById("center-body")
var firstElement = ""
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
    

})
textarea.addEventListener('keydown', (e) => {
    if (e.key == "Tab") {
        // if (firstElement.length !=  0){
        //     GetValue(firstElement)
        //     firstElement = "    "
        // }
        e.preventDefault()
        textarea.value = textarea.value.slice(0, textarea.selectionStart) + "   " + textarea.value.slice(textarea.selectionStart, textarea.value.length);
    }  
});
function ShowAnimation(){
    setTimeout(() => {
        animation.style.visibility = "visible"
    }, 10)
    setTimeout(() => {
        animation.style.visibility = "hidden"
    }, 2000)
    
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
    
    var text = textarea.value;
    var textArray = text.split(/[\s,]+/);
    var textArrayLength = textArray.length;
    var textArrayLast = textArray[textArrayLength - 1];
    textarea.value  = text.slice(0, text.length - textArrayLast.length ) + value;
    dropdown.innerHTML  = ""
    textarea.setRangeText('', textarea.selectionStart, textarea.selectionEnd, "end")
    dropdown.style.visibility = "hidden"


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
    var text = textarea.value;
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
            dropdown.innerHTML += `<div class = "li" onclick ="GetValue('${list[i]}')">${list[i]}</div>`
        }
    }else
        dropdown.style.visibility = "hidden"
    dropdown.style.top = (textarea.selectionStart + 250 + coutingLine(textarea) * 22).toString()  + "px"
    dropdown.style.left = (textarea.selectionStart + 20 + SizeLineChar(textarea) * 10.3).toString() + "px"
}