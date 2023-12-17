function initializePage(){   
    const addModal = document.getElementById("addModal");
    const editModal = document.getElementById("editModal"); 
    const addButton = document.getElementById("addButton");
    const editButton = document.querySelectorAll(".custom-edit-button");
    const deleteButton = document.querySelectorAll(".custom-delete-button");
    var closeBtn = document.getElementById("closeBtn");
    var saveBtnStudent = document.getElementById("saveBtnStudent");
    var saveBtnCollege = document.getElementById("saveBtnCollege");
    var saveBtnCourse = document.getElementById("saveBtnCourse");
    var saveBtnEdit = document.getElementByID("saveBtnEdit")
    var addStudentForm = document.getElementById("addStudentForm");
    var addCourseForm = document.getElementById("addCourseForm");
    var addCollegeForm = document.getElementById("addCollegeForm");

   
    function addURL(section) {
        history.pushState({}, '', `/${section}/add`);
    }
    function updateURL(section) {
        history.pushState({}, '', `/${section}/edit`);
    }


    addModal.style.display = "none";
    editModal.style.display = "none";

    addButton.addEventListener("click", () => {
        addModal.style.display = "block";
        centerModal();

        const activeForm = document.querySelector(".active-form");
        if (activeForm) {
            const section = activeForm.getAttribute("data-section");
            if (section) {
                addURL(section);
            }
        }
    });
    editButton.addEventListener("click", () => {
        hideEditModal(); // Hide the edit modal
        centerModal();
    
        const activeForm = document.querySelector(".active-form");
        if (activeForm) {
            const section = activeForm.getAttribute("data-section");
            if (section) {
                updateURL(section);
            }
        }
    });
    

    
    closeBtn.addEventListener("click", () => {
        addModal.style.display = "none";
    });

    // Student : ADD
    saveBtnStudent.addEventListener("click", (event) => {
        event.preventDefault(); // Prevent the default form submission
    
        // Get input values
        const studentID = document.getElementById("studentID").value;
        const studentFname = document.getElementById("studentFname").value;
        const studentLname = document.getElementById("studentLname").value;
        const course = document.getElementById("course").value;
        const year = document.getElementById("year").value;
        const gender = document.getElementById("gender").value;
    
        const formData = {
            studentID: studentID,
            studentFname: studentFname,
            studentLname: studentLname,
            course: course,
            year: year,
            gender: gender,
        };
    
        // Send the data to the server
        fetch("/students/add", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(formData),
        })
        .then((response) => response.json())
        .then((data) => {
            if (data.success) {
                alert("Student added successfully");
                // Optionally, close the modal or clear the form fields
                addStudentForm.reset();
            } else {
                alert("Failed to add student. Please check your input.");
            }
        })
        .catch((error) => {
            console.error("Error:", error);
            alert("An error occurred. Please check the console for details.");
        });        
    });
    // Save Button (College)
    saveBtnCollege.addEventListener("click", (event) => {
        event.preventDefault();
        
        const collegeCode = document.getElementById("collegeCode").value;
        const collegeName = document.getElementById("collegeName").value;

        const formData = {
            collegeCode: collegeCode,
            collegeName: collegeName,
        };

        fetch("/colleges/add", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(formData),
        })
        .then((response) => response.json())
        .then((data) => {
            if (data.success) {
                alert("College added successfully");
                addCollegeForm.reset();
            } else {
                alert("Failed to add college. Please check your input.");
            }
        })
        .catch((error) => {
            console.error("Error:", error);
            alert("An error occurred. Please check the console for details.");
        });
    });
    // Course : ADD
    saveBtnCourse.addEventListener("click", (event) => {
        event.preventDefault(); // Prevent the default form submission
    
        // Get input values
        const courseCode = document.getElementById("courseCode").value;
        const courseName = document.getElementById("courseName").value;
        const college = document.getElementById("college").value;
    
        const formData = {
            courseCode: courseCode,
            courseName: courseName,
            college: college,
        };
    
        // Send the data to the server
        fetch("/courses/add", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(formData),
        })
        .then((response) => response.json())
        .then((data) => {
            if (data.success) {
                alert("Course added successfully");
                // Optionally, close the modal or clear the form fields
                addCourseForm.reset();
            } else {
                alert("Failed to add course. Please check your input.");
            }
        })
        .catch((error) => {
            console.error("Error:", error);
            alert("An error occurred. Please check the console for details.");
        });
    });

    // Add a click event listener to each "Edit" button
    editButton.forEach((editButton) => {
        editButton.addEventListener("click", (event) => {
            const studentID = editButton.getAttribute("data-student-id");
            const studentFname = editButton.getAttribute("data-fname");
            const studentLname = editButton.getAttribute("data-lname");
            const course = editButton.getAttribute("data-course");
            const year = editButton.getAttribute("data-year");
            const gender = editButton.getAttribute("data-gender");
    
            // Pre-fill the edit modal form fields with the data
            document.getElementById("editStudentID").value = studentID;
            document.getElementById("editStudentFname").value = studentFname;
            document.getElementById("editStudentLname").value = studentLname;
            document.getElementById("editcourse").value = course;
            document.getElementById("edityear").value = year;
            document.getElementById("editgender").value = gender;
    
            // Display the edit modal
            editModal.style.display = "block";
            centerModal();
        });
    });
    // Event listener for the "Save" button in the edit modal
    document.getElementById("saveBtnEdit").addEventListener("click", (event) => {
        event.preventDefault();
        
        // Get edited data from the edit modal fields
        const studentID = document.getElementById("editStudentID").value;
        const studentFname = document.getElementById("editStudentFname").value;
        const studentLname = document.getElementById("editStudentLname").value;
        const course = document.getElementById("editcourse").value;
        const year = document.getElementById("edityear").value;
        const gender = document.getElementById("editgender").value;

        // Send the edited data to the server for updating
        const formData = {
            studentID: studentID,
            studentFname: studentFname,
            studentLname: studentLname,
            course: course,
            year: year,
            gender: gender,
        };

        fetch("/students/edit", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(formData),
        })
        .then((response) => response.json())
        .then((data) => {
            if (data.success) {
                alert("Student updated successfully");
                // Optionally, close the modal or clear the form fields
                editModal.reset();
                editModal.style.display = "none";
            } else {
                alert("Failed to update student. Please check your input.");
            }
        })
        .catch((error) => {
            console.error("Error:", error);
            alert("An error occurred. Please check the console for details.");
        });
    });

    // Add a click event listener to each "Delete" button

    deleteButton.forEach((deleteButton) => {
        deleteButton.addEventListener("click", () => {
            const studentID = deleteButton.getAttribute("data-student-id");

            // Confirm the deletion
            if (confirm("Are you sure you want to delete this student?")) {
                // Send a DELETE request to your server to delete the student record
                fetch(`/students/delete/${studentID}`, {
                    method: "DELETE",
                })
                    .then((response) => response.json())
                    .then((data) => {
                        if (data.success) {
                            // If the record is successfully deleted, remove it from the UI
                            const row = deleteButton.parentElement.parentElement;
                            row.remove();
                            alert("Student deleted successfully");
                        } else {
                            alert("Failed to delete student. Please try again.");
                        }
                    })
                    .catch((error) => {
                        console.error("Error:", error);
                        alert("An error occurred while deleting the student.");
                    });
            }
        });
    });



    window.onclick = function (event) {
        if (event.target == addModal) {
            addModal.style.display = "none";
        }
    };
    function centerModal() {
        var modalContent = document.querySelector(".modal-content");
        var windowHeight = window.innerHeight;
        var topMargin = (windowHeight - modalContent.clientHeight) / 2;
        modalContent.style.marginTop = topMargin + "px";
    }
    // Call centerModal on window resize to keep the modal centered
    window.onresize = function () {
        if (addModal.style.display === "block") {
            centerModal();
        }
    };


    // Function to hide the edit modal
    function hideEditModal() {
        editModal.style.display = "none";
    }

    // Add an event listener to the "Close" button in the edit modal
    document.getElementById("closeEditModal").addEventListener("click", () => {
        editModal.style.display = "none";
    });
    // Function to hide the add modal
    function hideAddModal() {
        addModal.style.display = "none";
    }

    // Add an event listener to the "Close" button in the add modal
    document.getElementById("closeBtn").addEventListener("click", hideAddModal);

}

// Call the initialization function when the page loads
window.addEventListener('load', initializePage);
