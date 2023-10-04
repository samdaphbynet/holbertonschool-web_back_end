// 2-get_students_by_loc.js

export default function getStudentByLocation(students, city) {
  const filteredStudent = students.filter((student) => student.location === city);

  return filteredStudent;
}
