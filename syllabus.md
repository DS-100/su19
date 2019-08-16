---
layout: page
title: "Syllabus"
page_class: content-wide
---

The materials for each lecture are linked in the table below. Alternatively,
you can browse:

- [The Google Drive folder containing all lecture slides.](https://drive.google.com/drive/folders/155HsAyFuOFiyY8F3xDiEPTzZshlk8SiG)
- [The YouTube playlist of all recorded screencasts.](https://www.youtube.com/playlist?list=PLPHXc20GewP8J56CisONS_mFZWZAfa7jR)

<div class="table-responsive">
  <table class="syllabus table" id="syllabus_table">
    <colgroup>
      <col width="65px">
      <col width="78px">
      <col width="100px">
      <col width="">
    </colgroup>
    <thead>
      <tr class="syllabus__header">
        <th> Week </th>
        <th> Lecture </th>
        <th> Date </th>
        <th> Topic </th>
        <th> Lab </th>
        <th> Discussion </th>
        <th> Homework </th>
      </tr>
    </thead>
    <tbody>

    <!--
    The actual lecture rows. To add a lecture, edit _data/lectures.yml.
    -->

    {% include syllabus_entries.html %}


    </tbody>

  </table>
</div>

<!--
Script to highlight the current lecture.
Commented out since the course is over now.
-->

<!-- <script type="text/javascript">
const current_date = new Date();
const lectures = document.getElementsByClassName('lecture');

for (var i = 0; i < lectures.length; i++ ) {
  let lecture = lectures[i];
  const { lectureWeek, lectureDate } = lecture.dataset;
  const lec_date = new Date(lectureDate + ' 23:59:59');

  // We need to find the first occurance of lecture that pass today's date
  if (current_date <= lec_date) {
    lecture.className += ' lecture--current';

    // Need to look up the week element since it might be in the row above
    const weekEl = document.getElementById(`lecture-week-${lectureWeek}`);
    weekEl.className += ' lecture__week--current';

    // We will show the description for lectures in the coming week
    const descEls = document.getElementsByClassName(`description-week-${lectureWeek}`);
    for (var j = 0; j < descEls.length; j++) {
      descEl = descEls[j];
      descEl.hidden = null;
    }

    break;
  }

  window.location.hash = `lecture-week-${lectureWeek}`;
}
</script> -->
