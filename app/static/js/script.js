
// DELETE -- STUDENTS
document.addEventListener('DOMContentLoaded', function() {
  var deleteButtons = document.querySelectorAll('.custom-studentdelete-button');

  deleteButtons.forEach(function(button) {
      button.addEventListener('click', function() {
          var studentID = this.getAttribute('data-student-id');

          var confirmation = window.confirm('\nAre you sure you want to delete ' + studentID + '?');

          if (confirmation) {

            deleteStudent(studentID);
          } else {
          }
      });
  });
  function deleteStudent(studentID) {
      fetch('/students/delete/' + studentID, {
          method: 'DELETE',
          headers: {
              "X-CSRFToken": document.querySelector("meta[name='csrf_token']").content,
          }
      })
      .then(response => response.json())
      .then(data => {
          if (data.status === 'success') {
              alert('Student deleted successfully!');
              window.location.reload();
          } else {
              alert('Error deleting student: ' + data.message);
          }
      })
      .catch(error => {
          console.error('Error:', error);
          alert('An error occurred while deleting the student. Check the console for details.');
      });
  }
});

// DELETE -- COURSE
document.addEventListener('DOMContentLoaded', function() {
    var deleteButtons = document.querySelectorAll('.custom-coursedelete-button');
  
    deleteButtons.forEach(function(button) {
        button.addEventListener('click', function() {
            var courseCode = this.getAttribute('data-course-code');
  
            var confirmation = window.confirm('\nDeleting this course will delete some students that are enrolled in this course.\n\n\nAre you sure you want to delete ' + courseCode + '?');
  
            if (confirmation) {
  
              deleteCourse(courseCode);
            } else {
            }
        });
    });
    function deleteCourse(courseCode) {
        fetch('/courses/delete/' + courseCode, {
            method: 'DELETE',
            headers: {
                "X-CSRFToken": document.querySelector("meta[name='csrf_token']").content,
            }
        })
        .then(response => response.json())
        .then(data => {
            if (data.status === 'success') {
                alert('Course deleted successfully!');
                window.location.reload();
            } else {
                alert('Error deleting course: ' + data.message);
            }
        })
        .catch(error => {
            console.error('Error:', error);
            alert('An error occurred while deleting the course. Check the console for details.');
        });
    }
});

// DELETE -- COLLEGE
document.addEventListener('DOMContentLoaded', function() {
    var deleteButtons = document.querySelectorAll('.custom-collegedelete-button');
  
    deleteButtons.forEach(function(button) {
        button.addEventListener('click', function() {
            var collegeCode = this.getAttribute('data-college-code');
  
            var confirmation = window.confirm('\nDeleting this college will cause some courses and students in this college to be also deleted.\n\n\n Are you sure you want to delete ' + collegeCode + '?');
  
            if (confirmation) {
  
              deleteCollege(collegeCode);
            } else {
            }
        });
    });
    function deleteCollege(collegeCode) {
        fetch('/colleges/delete/' + collegeCode, {
            method: 'DELETE',
            headers: {
                "X-CSRFToken": document.querySelector("meta[name='csrf_token']").content,
            }
        })
        .then(response => response.json())
        .then(data => {
            if (data.status === 'success') {
                alert('College deleted successfully!');
                window.location.reload();
            } else {
                alert('Error deleting college: ' + data.message);
            }
        })
        .catch(error => {
            console.error('Error:', error);
            alert('An error occurred while deleting the college. Check the console for details.');
        });
    }
});




// SHOW STUDENT PROFILE
function showStudentProfile(studentID) {
    console.log("Student ID:", studentID);
    window.location.href = '/students/profile/' + studentID;
  }
  





// ADD -- COLLEGE
document.addEventListener('DOMContentLoaded', function() {
    var addCollegeButton = document.getElementById('addCollegeButton');
    
    if (addCollegeButton) {
            addCollegeButton.addEventListener('click', function() {
            var collegeCode = document.getElementById('collegeCode').value;
            var collegeName = document.getElementById('collegeName').value;
            var csrfToken = document.querySelector("meta[name='csrf_token']").content;
            
            var formData = new FormData();
            formData.append('collegeCode', collegeCode);
            formData.append('collegeName', collegeName);

            fetch('/colleges/add', {
                method: 'POST',
                body: formData,
                headers: {
                    "X-CSRFToken": csrfToken,
                },
            })
            .then(response => {
                // Log the full response for debugging
                console.log(response);
                return response.json();
            })
            .then(data => {
                console.log(data);  
                if (data.status === 'success') {
                    alert('College added successfully!');
                    window.location.href = "/colleges";
                } else {
                    alert('Error adding college: ' + data.message);
                }
            }) 
            .catch(error => {
                console.error('Error adding college:', error);
                alert('An error occurred while adding the college. Check the console for details.');
            });
        });
    }
});
// ADD -- COURSE
document.addEventListener('DOMContentLoaded', function() {
    var addCourseButton = document.getElementById('addCourseButton');
    
    if (addCourseButton) {
        addCourseButton.addEventListener('click', function() {
            var courseCode = document.getElementById('courseCode').value;
            var courseName = document.getElementById('courseName').value;
            var college = document.getElementById('college').value;
            var csrfToken = document.querySelector("meta[name='csrf_token']").content;
            
            var formData = new FormData();
            formData.append('courseCode', courseCode);
            formData.append('courseName', courseName);
            formData.append('college', college);

            fetch('/courses/add', {
                method: 'POST',
                body: formData,
                headers: {
                    "X-CSRFToken": csrfToken,
                },
            })
            .then(response => {

                console.log(response);
                return response.json();
            })
            .then(data => {
                console.log(data);  
                if (data.status === 'success') {
                    alert('Course added successfully!');
                    window.location.href = "/courses";
                } else {
                    alert('Error adding college: ' + data.message);
                }
            }) 
            .catch(error => {
                console.error('Error adding course:', error);
                alert('An error occurred while adding the course. Check the console for details.');
            });
        });
    }
});
// ADD -- STUDENT
document.addEventListener('DOMContentLoaded', function() {
    var addStudentButton = document.getElementById('addStudentButton');
    
    if (addStudentButton) {
        addStudentButton.addEventListener('click', function() {
            var studentID = document.getElementById('studentID').value;
            var studentLname = document.getElementById('studentLname').value;
            var studentFname = document.getElementById('studentFname').value;
            var course = document.getElementById('course').value;
            var year = document.getElementById('year').value;
            var gender = document.getElementById('gender').value;
            var profilePicture = document.getElementById('profile-picture').value;
            var csrfToken = document.querySelector("meta[name='csrf_token']").content;
            
            var formData = new FormData();
            formData.append('studentID', studentID);
            formData.append('studentLname', studentLname);
            formData.append('studentFname', studentFname);
            formData.append('course', course);
            formData.append('year', year);
            formData.append('gender', gender);
            formData.append('profile_picture', profilePicture); 

            fetch('/students/add', {
                method: 'POST',
                body: formData,
                headers: {
                    "X-CSRFToken": csrfToken,
                },
            })
            .then(response => response.json())
            .then(data => {
                if (data.status === 'success') {
                    alert('Student added successfully!');
                    window.location.href = "/students";
                } else {
                    alert('Error adding student: ' + data.message);
                }
            }) 
            .catch(error => {
                console.error('Error adding course:', error);
                alert('An error occurred while adding the student. Check the console for details.');
            });
        });
    }
});







// EDIT -- Colleges
document.addEventListener('DOMContentLoaded', function() {
    var csrfToken = document.head.querySelector('meta[name="csrf_token"]').content;

    var editCollegeButtons = document.querySelectorAll('.custom-edit-button');
    var editCollegeModal = document.getElementById('editCollegeModal');
    var closeEditCollegeModalButton = document.getElementById('closeEditCollegeModal');
    var editForm = document.getElementById('editForm');
    var editCollegeCodeInput = document.getElementById('editCollegeCode');
    var editCollegeNameInput = document.getElementById('editCollegeName');

    editCollegeButtons.forEach(function(button) {
        button.addEventListener('click', function() {
            console.log('Edit button clicked');
            var collegeCode = this.getAttribute('data-college-code');
            var collegeName = this.getAttribute('data-college-name');

            editCollegeCodeInput.value = collegeCode;
            editCollegeNameInput.value = collegeName;

            editCollegeModal.style.display = 'flex';
        });
    });

    closeEditCollegeModalButton.addEventListener('click', function() {
        editCollegeModal.style.display = 'none';
    });

    window.addEventListener('click', function(event) {
        if (event.target === editCollegeModal) {
            editCollegeModal.style.display = 'none';
        }
    });

    editForm.addEventListener('submit', function(event) {
        event.preventDefault();
    
        var collegeCodeValue = editCollegeCodeInput.value; 
        var collegeNameValue = editCollegeNameInput.value;
    
        fetch('/colleges/update', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrfToken,
            },
            body: JSON.stringify({
                editCollegeCode: collegeCodeValue,
                editCollegeName: collegeNameValue
            }),
        })
        .then(response => response.json())
        .then(data => {
            if (data.message) {
                console.log('Success:', data.message);
                alert('Colleges updated successfully');
                
                window.location.href = '/colleges';
            } else if (data.error) {
                console.error('Error:', data.error);
            }
        })
        .catch(error => {
            console.error('Error:', error);
        })
        .finally(() => {
            editCollegeModal.style.display = 'none';
        });
    });
});


// EDIT -- Courses
document.addEventListener('DOMContentLoaded', function() {
    var csrfToken = document.head.querySelector('meta[name="csrf_token"]').content;

    var editButtons = document.querySelectorAll('.custom-edit-button');
    var editModal = document.getElementById('editCourseModal');
    var closeEditCourseModalButton = document.getElementById('closeEditCourseModal');
    var editForm = document.getElementById('editForm');
    var editCourseCodeInput = document.getElementById('editCourseCode');
    var editCourseNameInput = document.getElementById('editCourseName');
    var editCollegeInput = document.getElementById('editCollege');


    editButtons.forEach(function(button) {
        button.addEventListener('click', function() {
            console.log('Edit button clicked');
            var courseCode = this.getAttribute('data-course-code');
            var courseName = this.getAttribute('data-course-name');
            var college = this.parentElement.parentElement.children[2].innerText;

            editCourseCodeInput.value = courseCode;
            editCourseNameInput.value = courseName;
            editCollegeInput.value = college;

            editModal.style.display = 'flex';
        });
    });

    closeEditCourseModalButton.addEventListener('click', function() {
        editModal.style.display = 'none';
    });

    window.addEventListener('click', function(event) {
        if (event.target === editModal) {
            editModal.style.display = 'none';
        }
    });

    editForm.addEventListener('submit', function(event) {
        event.preventDefault();

        var courseCodeValue = editCourseCodeInput.value;
        var courseNameValue = editCourseNameInput.value;
        var collegeValue = editCollegeInput.value;

        fetch('/courses/update', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrfToken,
            },
            body: JSON.stringify({
                editCourseCode: courseCodeValue, // Include courseCode
                editCourseName: courseNameValue,
                editCollege: collegeValue,
            }),
        })
        .then(response => response.json())
        .then(data => {
            if (data.message) {
                console.log('Success:', data.message);
                alert('Course updated successfully');
            } else if (data.error) {
                console.error('Error:', data.error);
            }
        })
        .catch(error => {
            console.error('Error:', error);
        })
        .finally(() => {
            editModal.style.display = 'none';
            window.location.reload(); 
        });
    });
    fetch('/colleges/get_college')
    .then(response => response.json())
    .then(courses => {
        const courseDropdown = document.getElementById('editCollege');
        courses.forEach(course => {
            const option = document.createElement('option');
            option.value = course.collegeCode;
            option.text = `${course.collegeCode} - ${course.collegeName}`;
            courseDropdown.add(option);
        });
    })
});

// EDIT -- Students
document.addEventListener('DOMContentLoaded', function() {
    var csrfToken = document.head.querySelector('meta[name="csrf_token"]').content;

    var editButtons = document.querySelectorAll('.custom-edit-button');
    var editModal = document.getElementById('editStudentModal');
    var closeEditStudentModalButton = document.getElementById('closeEditStudentModal');
    var editForm = document.getElementById('editForm');
    var editStudentIdInput = document.getElementById('editStudentId');
    var editStudentFNameInput = document.getElementById('editStudentFName');
    var editStudentLNameInput = document.getElementById('editStudentLName');
    var editCourseInput = document.getElementById('editCourse');
    var editYearInput = document.getElementById('editYear');
    var editGenderInput = document.getElementById('editGender');

    editButtons.forEach(function(button) {
        button.addEventListener('click', function() {
            console.log('Edit button clicked');
            var studentId = this.getAttribute('data-student-id');
            var studentFName = this.getAttribute('data-fname');
            var studentLName = this.getAttribute('data-lname');
            var course = this.getAttribute('data-course');
            var year = this.getAttribute('data-year');
            var gender = this.getAttribute('data-gender');

            editStudentIdInput.value = studentId;
            editStudentFNameInput.value = studentFName;
            editStudentLNameInput.value = studentLName;
            editCourseInput.value = course;
            editYearInput.value = year;
            editGenderInput.value = gender;

            editModal.style.display = 'flex';
        });
    });

    closeEditStudentModalButton.addEventListener('click', function() {
        editModal.style.display = 'none';
    });

    window.addEventListener('click', function(event) {
        if (event.target === editModal) {
            editModal.style.display = 'none';
        }
    });

    editForm.addEventListener('submit', function(event) {
        event.preventDefault();

        var studentIdValue = editStudentIdInput.value;
        var studentFNameValue = editStudentFNameInput.value;
        var studentLNameValue = editStudentLNameInput.value;
        var courseValue = editCourseInput.value;
        var yearValue = editYearInput.value;
        var genderValue = editGenderInput.value;

        fetch('/students/update', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrfToken,
            },
            body: JSON.stringify({
                editStudentId: studentIdValue,
                editStudentFName: studentFNameValue,
                editStudentLName: studentLNameValue,
                editCourse: courseValue,
                editYear: yearValue,
                editGender: genderValue,
            }),
        })
        .then(response => response.json())
        .then(data => {
            if (data.message) {
                console.log('Success:', data.message);
                alert('Student updated successfully');
            } else if (data.error) {
                console.error('Error:', data.error);
            }
        })
        .catch(error => {
            console.error('Error:', error);
        })
        .finally(() => {
            editModal.style.display = 'none';
            window.location.reload(); 
        });
    });
    fetch('/courses/get_courses')
    .then(response => response.json())
    .then(courses => {
        const courseDropdown = document.getElementById('editCourse');
        courses.forEach(course => {
            const option = document.createElement('option');
            option.value = course.courseCode;
            option.text = `${course.courseCode} - ${course.courseName}`;
            courseDropdown.add(option);
        });
    })
    .catch(error => {
        console.error('Error fetching courses:', error);
    });
});

