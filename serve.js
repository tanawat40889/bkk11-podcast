// static server + HTTP Range (ให้เลื่อนเวลาเสียงได้)
const http = require('http'), fs = require('fs'), path = require('path');
const root = __dirname, port = +process.argv[2] || 8765;
const types = { '.html': 'text/html; charset=utf-8', '.js': 'text/javascript; charset=utf-8', '.css': 'text/css', '.json': 'application/json', '.mp3': 'audio/mpeg', '.png': 'image/png', '.svg': 'image/svg+xml' };
const srv = http.createServer((req, res) => {
  let p = path.join(root, decodeURIComponent(req.url.split('?')[0]));
  if (!p.startsWith(root)) return res.writeHead(403).end();
  if (p.endsWith(path.sep)) p += 'index.html';
  fs.stat(p, (err, st) => {
    if (err || !st.isFile()) return res.writeHead(404).end('not found');
    const h = { 'Content-Type': types[path.extname(p)] || 'application/octet-stream', 'Accept-Ranges': 'bytes' };
    const m = /bytes=(\d*)-(\d*)/.exec(req.headers.range || '');
    if (m) {
      const s = m[1] ? +m[1] : st.size - +m[2], e = m[1] && m[2] ? Math.min(+m[2], st.size - 1) : st.size - 1;
      if (s > e || s >= st.size) return res.writeHead(416, { 'Content-Range': `bytes */${st.size}` }).end();
      res.writeHead(206, { ...h, 'Content-Range': `bytes ${s}-${e}/${st.size}`, 'Content-Length': e - s + 1 });
      return fs.createReadStream(p, { start: s, end: e }).pipe(res);
    }
    res.writeHead(200, { ...h, 'Content-Length': st.size });
    req.method === 'HEAD' ? res.end() : fs.createReadStream(p).pipe(res);
  });
});
// ถ้าพอร์ตถูกใช้อยู่ ขยับไปพอร์ตถัดไป
srv.on('error', e => { if (e.code !== 'EADDRINUSE') throw e; srv.listen(srv.port = srv.port + 1) });
srv.once('listening', () => console.log(`http://localhost:${srv.address().port}`));
srv.listen(srv.port = port);
