var modal = document.getElementById("addStudentModal");

var addButton = document.getElementById("addButton");

var closeBtn = document.getElementById("closeBtn");
var saveBtn = document.getElementById("saveData");
const btnPopup = document.querySelector('.btnLogin-popup');

addButton.onclick = function () {
    modal.style.display = "block";
};

closeBtn.onclick = function () {
    modal.style.display = "none";
};


saveBtn.onclick = function () {
 
    modal.style.display = "none";
};

window.onclick = function (event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
};
