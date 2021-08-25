function selector(){
    let code = document.getElementById("code");
    let key = document.getElementById("key");
    let code_block = document.getElementById("code_block");
    let key_block = document.getElementById("key_block");

    if (key.checked){
        key_block.style.display = "block";
        code_block.style.display = "none";
    }
    else {
        key_block.style.display = "none";
        code_block.style.display = "block";
    }
}