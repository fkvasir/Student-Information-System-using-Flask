document.addEventListener('DOMContentLoaded', function() {
  var deleteButtons = document.querySelectorAll('.custom-studentdelete-button');

  deleteButtons.forEach(function(button) {
      button.addEventListener('click', function() {
          var studentID = this.getAttribute('data-student-id');

          var confirmation = window.confirm('Are you sure you want to delete ' + studentID + '?');

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

document.addEventListener('DOMContentLoaded', function() {
    var deleteButtons = document.querySelectorAll('.custom-coursedelete-button');
  
    deleteButtons.forEach(function(button) {
        button.addEventListener('click', function() {
            var courseCode = this.getAttribute('data-course-code');
  
            var confirmation = window.confirm('Are you sure you want to delete ' + courseCode + '?');
  
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
document.addEventListener('DOMContentLoaded', function() {
    var deleteButtons = document.querySelectorAll('.custom-collegedelete-button');
  
    deleteButtons.forEach(function(button) {
        button.addEventListener('click', function() {
            var collegeCode = this.getAttribute('data-college-code');
  
            var confirmation = window.confirm('Are you sure you want to delete ' + collegeCode + '?');
  
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





function showStudentProfile(studentID) {
    console.log("Student ID:", studentID);
    window.location.href = '/students/profile/' + studentID;
  }
  





  
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
            var csrfToken = document.querySelector("meta[name='csrf_token']").content;
            
            var formData = new FormData();
            formData.append('studentID', studentID);
            formData.append('studentLname', studentLname);
            formData.append('studentFname', studentFname);
            formData.append('course', course);
            formData.append('year', year);
            formData.append('gender', gender);

            fetch('/students/add', {
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

 