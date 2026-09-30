// t = วินาทีที่คำถามเด้ง, a = index ของตัวเลือกที่ถูก, dur = ความยาว (วินาที), color = สีปก
window.PODCAST = {
  title: "ติวธรรมะ BKK11",
  parts: [
    {
      id: "part1", name: "Part 1", color: "#7c5cff",
      episodes: [
        { id: "p1e1", name: "Episode 1", src: "audio/part1/ep1.m4a", dur: 733, questions: [] },
        { id: "p1e2", name: "Episode 2", src: "audio/part1/ep2.m4a", dur: 1359, questions: [] },
        { id: "p1e3", name: "Episode 3", src: "audio/part1/ep3.m4a", dur: 1118, questions: [] }
      ]
    },
    { id: "part2", name: "Part 2", color: "#e0567a", episodes: [] },
    { id: "part3", name: "Part 3", color: "#16a08a", episodes: [] }
  ]
};
