# ถอดเสียงเป็น JSON [{s,e,t}] ด้วย faster-whisper: python tools/transcribe.py audio/part1/ep1.m4a ...
import sys, json, os, time
from faster_whisper import WhisperModel
m = WhisperModel("large-v3", device="cpu", compute_type="int8", cpu_threads=8)
for f in sys.argv[1:]:
    out = os.path.join("transcripts", os.path.basename(os.path.dirname(f)) + "-" + os.path.splitext(os.path.basename(f))[0] + ".json")
    if os.path.exists(out): continue
    t0, r = time.time(), []
    segs, info = m.transcribe(f, language="th", vad_filter=True, beam_size=1, condition_on_previous_text=False)
    for x in segs:
        r.append({"s": round(x.start, 1), "e": round(x.end, 1), "t": x.text.strip()})
        print(f"{out} {x.end/info.duration*100:5.1f}% [{round(time.time()-t0)}s] {x.text.strip()[:40]}", flush=True)
        json.dump(r, open(out + ".part", "w"), ensure_ascii=False)
    json.dump(r, open(out, "w"), ensure_ascii=False, indent=0)
    os.remove(out + ".part")
    print("DONE", out, len(r), "segs", round(time.time() - t0), "s", flush=True)
