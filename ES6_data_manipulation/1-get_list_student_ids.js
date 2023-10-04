// 1-get_list_student_ids.js

export default function getListSudentIds(lastTask) {
  if (!Array.isArray(lastTask)) {
    return [];
  }

  const ids = lastTask.map((student) => student.id);

  return ids;
}
