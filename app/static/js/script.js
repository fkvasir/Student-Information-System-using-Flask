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
        fetch('/course/delete/' + courseCode, {
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





function showStudentProfile(studentID) {
    console.log("Student ID:", studentID);
    window.location.href = '/students/profile/' + studentID;
  }
  
