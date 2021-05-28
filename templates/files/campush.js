

function campush() {
    alert("Sudmit")
    window.history.go(-1)
    myFunction()


}
function myFunction() {
    var x = document.getElementById("snackbar");
    x.className = "show";
    setTimeout(function () { x.className = x.className.replace("show", ""); }, 3000);
}