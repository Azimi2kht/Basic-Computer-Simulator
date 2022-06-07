const textarea = document.getElementById('input');
const countLine = document.getElementById("count");
const dropdown = document.getElementById("drop-down");
var LineNumber = 1;
instructions = [
    // memory reference
    'AND',
    'ADD',
    'LDA',
    'STA',
    'BUN',
    'BSA',
    'ISZ',

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
textarea.addEventListener('input', () => {
    
    var lines = 1
    const text = textarea.value;   
    for(var i = 0; i < text.length; i++) {
        if(text[i] == '\n') {
            lines++;
        }
    }
    countLine.innerText = "";
    for(var i = 1; i <= lines; i++)
        countLine.innerHTML += `<span>${i}</span>`;
    autoCompelet()
})
textarea.addEventListener('keydown', (e) => {
    if (e.key == "Tab") {
        e.preventDefault()
        textarea.setRangeText('  ', textarea.selectionStart, textarea.selectionEnd, "end")
    }
    
})

function autoCompelet(){
    var list = []
    var text = textarea.value;
    var textArray = text.split(" ");
    var textArrayLength = textArray.length;
    var textArrayLast = textArray[textArrayLength - 1];
    textArrayLast = textArrayLast.replace(/\n/g, "");
    textArrayLast = textArrayLast.toUpperCase();
    for(var i = 0; i < instructions.length; i++) {
        
        if(textArrayLast[0] == instructions[i][0]) {
            
            list.push(instructions[i])        
        }
    }
    if(list.length > 0) {
        dropdown.innerHTML ="" 
        for(var i = 0; i < list.length; i++) {
            dropdown.innerHTML += `<div class="li">${list[i]}</div>`

        }   
    }
}

