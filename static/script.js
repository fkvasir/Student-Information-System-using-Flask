// Get the modal element
var modal = document.getElementById("addStudentModal");

// Get the button that opens the modal
var addButton = document.getElementById("addButton");

// Get the button elements inside the modal
var closeBtn = document.getElementById("closeAddModal");
var saveBtn = document.getElementById("saveData");

// When the user clicks the "Add" button, open the modal
addButton.onclick = function () {
    modal.style.display = "block";
};

// When the user clicks the close button, close the modal
closeBtn.onclick = function () {
    modal.style.display = "none";
};

// When the user clicks the save button, save data and close the modal
saveBtn.onclick = function () {
    // Handle saving data
    // Example: You can use an AJAX request to save data to the server

    // Close the modal
    modal.style.display = "none";
};

// When the user clicks anywhere outside the modal, close it
window.onclick = function (event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
};
