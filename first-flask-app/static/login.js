let loginButton = document.getElementById("loginBtn");
 
let verifyCreds = function() {
    console.log("Hi")
    let userName = document.getElementById("usernameInput").value;
    let passWord = document.getElementById("passwordInput").value;
    window.location.replace("/todo")
}
loginButton.addEventListener("click", verifyCreds);