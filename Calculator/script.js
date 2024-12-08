function execute(key){
    // clear the label
    if (key == "AC"){
        document.getElementById("text").value = 0;
    }
    // evaluation is = is pressed
    else if (key == "="){
        document.getElementById("text").value = eval(document.getElementById("text").value)
    }
    // let's put everything on the label
    else{
        if (document.getElementById("text").value != 0){
            document.getElementById("text").value += key;
        }
        else{
            document.getElementById("text").value = key;
        }
    }
}