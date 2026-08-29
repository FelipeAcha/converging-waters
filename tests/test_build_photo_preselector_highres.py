import base64, gzip, io, tempfile, unittest
from pathlib import Path
from PIL import Image

from scripts import build_photo_preselector_highres as builder


class HighResBuildTest(unittest.TestCase):
    def test_replaces_only_image_src_and_writes_highres_local_asset(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td) / 'review'; root.mkdir(); (root/'payload2').mkdir()
            low = '<section class="need" id="HUB-01" data-required="1"><article class="candidate"><div class="media"><img alt="x" src="data:image/webp;base64,AAAA"></div><div class="body"><code>HUB-01-A</code><h3>Same title</h3><input type="checkbox" data-code="HUB-01-A"></div></article></section>'
            gz = gzip.compress(low.encode(), mtime=0)
            (root/'payload2'/'000.txt').write_text(base64.b64encode(gz).decode())
            import hashlib
            (root/'index.html').write_text(f"<script>const PARTS=['payload2/000.txt'],EXPECTED='{hashlib.sha256(gz).hexdigest()}';</script>")

            im = Image.new('RGB',(1200,900),(1,2,3)); buf=io.BytesIO(); im.save(buf,'JPEG',quality=95)
            src = base64.b64encode(buf.getvalue()).decode()
            source = Path(td)/'source.html'
            source.write_text(f'<main><section class="need"><article class="candidate"><div class="media"><img alt="x" src="data:image/jpeg;base64,{src}"></div><div class="body"><code>HUB-01-A</code><h3>Different canonical title</h3></div></article></section></main>')

            report = builder.build(root, source, max_edge=1600, min_edge=800, chunk_count=1, session=None)
            out = gzip.decompress(base64.b64decode((root/'payload2'/'000.txt').read_text())).decode()
            self.assertEqual(report['counts']['assets'], 1)
            self.assertGreaterEqual(report['assets'][0]['long_edge'], 1200)
            self.assertIn('<h3>Same title</h3>', out)
            self.assertNotIn('Different canonical title', out)
            self.assertIn('assets/HUB-01-A.webp', out)


if __name__ == '__main__':
    unittest.main()
