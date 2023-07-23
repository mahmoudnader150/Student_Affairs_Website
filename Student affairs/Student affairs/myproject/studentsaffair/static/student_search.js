goButton = document.getElementById("go_button");
studentSearchBar = document.getElementById("student_search_bar");

goButton.onclick = function () {
  const search = studentSearchBar.value;
  studentRows = document.getElementsByClassName("student-table-row");
  for (let i = 0; i < studentRows.length; i++) {
    if (
      studentRows[i]
        .getElementsByClassName("student-table-row__name")[0]
        .innerHTML.trim() == search
    ) {
      studentRows[i].style.display = "";
    } else {
      studentRows[i].style.display = "none";
    }
  }
};
