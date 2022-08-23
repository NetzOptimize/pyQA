function myFunction() {
    alert("Hello! I am an alert box!");
}


const myTimeout = setTimeout(check, 3000);
const myTimeout2 = setTimeout(check2, 6000);




function check() {
    document.getElementById("demo").innerHTML = "<input type='checkbox'>";
}

function check2() {
    document.getElementById("demo2").innerHTML = "<input type='checkbox'>";
}

function myStopFunction() {
    clearTimeout(myTimeout);
}

function myFunction() {
    document.getElementById("dbclick ").innerHTML = "Double click works!";
}